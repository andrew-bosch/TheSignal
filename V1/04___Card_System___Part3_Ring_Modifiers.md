### STD.MOD.1 — OVERTURE
[↑ Standard](#standard)

#### Design Rationale

Overture is the bridge between STD.CA.9's anonymous funding gesture and formal alliance. When STD.CA.9 Fund succeeds, ARBITER delivers Overture (as a modifier card) to the acting faction. In a subsequent Month or Quarter, the faction assigns Overture to any of their Public Acts at Phase B. When that PA resolves at Beat 4 — regardless of outcome — ARBITER delivers a blank AccordForm to the acting faction. The faction drafts the terms and places the completed form in the Accord Placement Area during Beat 4 resolution or Debrief. The target faction then accepts, negotiates, or declines at Debrief. Mechanically: a free Issued ModReactCard that attaches one Accord initiation to any PA slot — ARBITER-delivered as a consequence of STD.CA.9's success, not drawn from the Modifier deck. Firing mechanism is trigger-based rather than beat-tied: the card watches for its own assigned host PA to resolve, rather than being bundled at Covert Dispatch — see the python block below and the Trigger vocab outstanding issue.

**Timing constraint:** Overture cannot be used in the Month it is received. STD.CA.9 resolves at Beat 3; the host PA must be declared at Phase B (before Beat 3). Overture is held to Month 2, Month 3, or a subsequent Quarter. Tradeable per Art 03 §11.5.

**Host PA restriction:** Cannot be assigned to STD.PA.8 Table an Accord or GUI.PA.2 Infrastructure Bond — both already deliver a blank AccordForm at Beat 4; stacking Overture would duplicate the Accord initiation on the same PA.

**Outcome addition mechanic:** Fires as an additional Automatic outcome when the host PA resolves at Beat 4, regardless of the host PA's success or failure. See §11.7.

#### Card Story
A quiet envelope arrives with no return address — just a blank form and the unmistakable understanding that someone, somewhere, is finally ready to talk.

#### Design Checklist (Art 04 §5 ModReactCard Design Checklist)

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Modifier card attaching Accord initiation as PA outcome addition. Alliance-opening mechanic — earned through STD.CA.9; formalized through PA attachment. | Art 04 §11.1; Art 06 §9.4 |
| Voice fit | ⚠ | `perspectives={}` is empty (deferred to D-04-08); `narrative` line is populated and reads in the correct diplomatic register. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction = All` — no alignment penalty for using Overture; doctrine weight carried by STD.CA.9. | Art 04 §6.5 |
| Card type fit | ✓ | Issued `ModReactCard` — ARBITER-delivered from STD.CA.9, not deck-drawn; fires when its assigned host PA resolves. Does not enter Resolution Grid as independent action. | Art 04 §6.1, §11.1, §11.4 |
| Taxonomy fit | ⚠ | `layer/function/subject=None` — not grounded against precedent (see Outstanding Issues: Taxonomy assignment). | Art 04b §4; ref_taxonomy.md §5.2 |
| Balance | ✓ | `cost = None` — reward from STD.CA.9 success (2 Capital + roll risk already paid); assignment free. Accord Portrait implications governed by Art 06 §9.9. | Art 02 §8; Art 06 §9.9 |
| Effect duration | ✓ | Immediate — AccordForm delivery is instantaneous. Resulting Accord's duration governed by Art 06 §9.3–§9.7 independently. | Art 04 §5 P19 |
| Persistence | ✓ | `persistence = Immediate` — no lingering game-state marker from Overture itself once the AccordForm is delivered; the resulting Accord's own persistence is a separate downstream concern (Art 06 §9.3–§9.7). | Art 04 §6.2 |
| Trigger validity | ⚠ | Fires when its assigned host PA resolves (Beat 4) — trigger form `public_act.resolved(pa=X)` is new, not yet in confirmed TriggerExpr vocabulary (§6.3). Same category of gap as GD-01's district-scoped trigger (04-n27). | Art 04 §6.3; §11.1 |
| Portrait validity | ✓ | `portrait={}` — correctly typed (schema declares `portrait: dict[Faction, PortraitEntry]`, not Optional; empty dict is the right "no entry" representation, not `None`). No portrait entry for Overture's own assignment; Portrait implications for the resulting Accord governed separately by Art 06 §9.9. | Art 04 §6.1–§6.2; Art 06 §9.9 |
| Supported by zones | ✓ (N/A) | `target_district=None` — Overture isn't a territory-scoped effect. | Art 01 §6–§7 |
| Supported by components | ✓ | AccordForm (Art 06 §9.2). No new components. | Art 06 §9.2 |
| Supported by game procedure | ✓ | Assignment at Phase B; blank form delivered at Beat 4; faction drafts and places in Accord Placement Area at their discretion (no timing constraint; queued for next Debrief if placed outside Debrief window). Execution at Debrief per Art 06 §9.4. Delivery from ARBITER tableau: procedure in STD.CA.9 `arbiter_note`; deliver-from-tableau is consistent with existing ARBITER delivery subroutines, no novel behavior; Art 07 subroutine pass still needed to formalize. | Art 03 Phase B; Art 06 §9.4; STD.CA.9 |
| Data schema validation | ⚠ | Required scaffolding fields present on sibling card GD-01 (`resolution_type`, `outcome_type`, `boost`, `ps_framing`, `declared_params`) now present, matching GD-01 precedent; `value_rating` resolved to N/A. Trigger form still unconfirmed against §6.3 (see Trigger validity). | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Grounded envelope-delivery scene; no mechanic restatement. | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — free assignment; the real cost was already paid via STD.CA.9's own resource tier. Mono/cross-resource distinction doesn't apply to a zero-cost effect. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on how often STD.CA.9 succeeds and the faction chooses to assign the resulting Overture — a fairly rare, player-gated combination; best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other card shares this trigger shape (bound to one specific `assigned_pa` instance), so collision risk with other React cards is low. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic outcome-addition with no execution-quality dimension — `Automatic` is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | A faction could plausibly hold multiple Overture copies (from multiple STD.CA.9 successes) and assign each to a different PA independently — not explicitly documented; same open-question category as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not ring-scoped; `faction=All` and Issued acquisition, no ring gating applies. |  |

#### Outstanding Issues

- **Taxonomy assignment:** `layer/function/subject=None` — the comparison used to justify this was incorrect (compared against GD-01, which does carry real taxonomy: Territory/Add/StructureBlock). Open — candidate if assigned: Information/Add/AccordAgreement (a confirmed registered subject per ref_taxonomy.md §5.2), paralleling how SYN.CA.11 Redline and SYN.MOD.1 carry real Accord-manipulation taxonomy.
- **Perspectives:** TBD — deferred to modifier card voice pass (D-04-08)
- **Card ID:** TBD — pending 04-n1 numbering pass
- **Value rating:** N/A. ModReactCard carries `value_rating` in general, but it's a deck-drawn/Splay-scoring field; Overture's Issued acquisition means it's never drawn or scored, so the field doesn't apply. Set to `value_rating = None` in the spec below.
- **STD.CA.9 balance reassessment:** Flag for after §11 redesign confirms Overture's modifier value
- **ARBITER delivery formalization:** Overture delivery (STD.CA.9 → Beat 3 → acting faction hand) pending Art 07 ARBITER subroutine pass; STD.CA.9 `arbiter_note` covers interim reference
- **Trigger vocab — `public_act.resolved(pa=X)`:** New PA-resolution trigger form, not yet in confirmed TriggerExpr vocabulary (§6.3). Needs the same kind of extension as GD-01's district-scoped `structure_block.placed` (04-n27). Also needs an Art 03 procedure describing how a card "attaches" to a specific PA at Phase B and how ARBITER/the table tracks that binding through to Beat 4.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (Taxonomy, Perspectives, ID, trigger vocab) | |

```python
Overture = Card(
    id      = "STD.MOD.1",  version = "v1.3",
    name    = "Overture",
    tagline = "Extend a formal invitation to negotiate — attached to any public act you declare.",
    type    = ModReactCard,  faction = All,

    layer   = None,  function = None,  subject = None,  # per-card choice — Overture isn't an action-taxonomy category

    beat            = None,
    resolution      = Automatic,
    resolution_type = Transactional,
    outcome_type    = None,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    ring_constraint = None,  ring_origin = None,
    value_rating    = None,  # N/A — Issued acquisition, never deck-drawn/Splay-scored
    trigger         = public_act.resolved(pa=overture.assigned_pa),  # NEW trigger form — pending §6.3 vocab extension
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,  # named on AccordForm when drafted — not declared at card assignment
    target_object   = AccordForm,
    declared_params = None,  # Overture uses the informal assigned_pa fill-in field directly, same pattern as GD-01's deed.district; no formal declared_params dict needed

    target_taxonomy=None,
    affinity    = None,
    restriction = overture.assigned_pa.type not in [STD.PA.8, GUI.PA.2],  # avoids duplicate AccordForm on same PA
    cost        = None,  # earned as STD.CA.9 success reward; free to assign
    boost       = None,

    acquisition      = Issued,
    generating_card  = "STD.CA.9",

    # Fires when the assigned host PA resolves (any outcome: success or fail)
    success = arbiter.deliver(faction(acting), AccordForm(blank)),
    successcrit = None,  fail = None,  failcrit = None,
    # Faction fills form per Art 06 §9.3; places in Accord Placement Area during Beat 4 or Debrief.
    # Art 06 §9.4 formation procedure applies from placement forward.

    portrait = {},  # no entry; Art 06 §9.9 governs Portrait for resulting Accord
    ps_framing = None,

    narrative    = "The terms don't matter yet. What matters is that the door is open.",
    perspectives = {},  # modifier card voice pass deferred to D-04-08
    design_note  = "Outcome addition modifier: attaches Accord initiation as additional Beat 4 outcome on any PA. "
                   "Fires on any host PA outcome — success or fail. Earned from STD.CA.9 success; free to assign. "
                   "Cannot assign to STD.PA.8 or GUI.PA.2 (duplicate AccordForm). "
                   "Must be held to a subsequent Month: Overture delivered at Beat 3 via STD.CA.9; host PA declared at Phase B before Beat 3. "
                   "Target faction not declared at Phase B — named on AccordForm when drafted. "
                   "assigned_pa is set when the faction attaches this card to a PA at Phase B — mirrors GD-01's fill-in-field pattern (deed.district), just faction-written instead of ARBITER-written.",
    arbiter_note = "On host PA resolution at Beat 4: deliver one blank AccordForm from ARBITER tableau supply to acting faction. "
                   "Faction drafts and places in Accord Placement Area at their discretion — no timing constraint. "
                   "Proceed per Art 06 §9.4.",
)
```

---

### STD.MOD.2 — SENIOR LIAISON

#### Design Rationale
First Ring Modifier content in the game — 04-29/09-06 pattern-setter, establishing the stub format for the Ring Modifier set. Voice sourced from Art 00 §6.7 Ring Character: Core's defining anxiety is proximity, not force, so Ring 1 content leans on institutional access and standing rather than the Directorate's already-shipped literal-force doctrine (DIR.MOD.10–13) — same city, deliberately different lever, available to whichever faction holds the card. Each ring ships two complete 4-card sets — Portable (`ring_constraint=None`) and Ring-Locked (`ring_constraint=`ring) — per 04-n161. This is the Portable set's weaker Boost tier (+1): a favor that travels with whoever's holding it, not the Core itself.

#### Card Story
A liaison who owes you something makes a call on your behalf — reinforcing whichever side the playing faction has named, and nobody in the room needs to know where the call came from.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A personal favor called in is a grounded expression of Ring 1/Core's institutional-access character (Art 00 §6.7), distinct from any faction's literal-force doctrine. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`, no perspectives required (Standard card); narrative/tagline read in Core's institutional-proximity register. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent — no faction relationship in play (Standard card, no faction doctrine to serve). | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Asset-category naming slot for Ring 1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; no cost step exists for this subclass; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=1` correctly set for a Portable asset (favor travels with holder, sourced from Core). | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.2 = Card(
    id      = "STD.MOD.2",  card_id = "STD.MOD.2",  version = "v0.1",
    name    = "Senior Liaison",
    tagline = "A Core insider willing to make a call on your behalf — the reason doesn't have to travel with the favor.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the favor travels with the holder, not the Core (closes 04-n161 alongside STD.MOD.6's Locked counterpart)
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A liaison who owes you something makes a call. Nobody in the room needs to know where the call came from.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.3 — SIGNED-OUT INSTRUMENTATION

#### Design Rationale
Portable set, Equipment category — rounds out the Boost pair before the Hinder pair. Precision gear drawn from Chorus Research's stores, carried out rather than left behind. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.2.

#### Card Story
The requisition slip says routine maintenance. The gear is somewhere else entirely by the time anyone checks — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Precision equipment quietly diverted for use elsewhere fits Core's institutional-access character — the leverage is proximity to Chorus Research's stores. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; institutional-requisition register, distinct from STD.MOD.2's personal-favor framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Equipment-category naming slot for Ring 1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=1` correctly set for a Portable asset. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.3 = Card(
    id      = "STD.MOD.3",  card_id = "STD.MOD.3",  version = "v0.1",
    name    = "Signed-Out Instrumentation",
    tagline = "Precision gear signed out of storage on short notice — nobody's flagged it missing yet.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — the equipment leaves the building
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The requisition slip says routine maintenance. The gear is somewhere else entirely by the time anyone checks.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.4 — CLEARANCE REVIEW

#### Design Rationale
Portable set, weaker Hinder tier (−1). The disruption is a mark against a person, not a place — it follows the target wherever they go. Same no-cost/playtest-flagged (04-n94) terms as the rest of the Ring 1 set.

#### Card Story
A name enters an audit list. Nobody says why the review opened. Nobody has to — the named faction's position slows down until it clears.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | An administrative audit as leverage fits Core's institutional-access character — bureaucratic friction, not force. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; institutional-audit register, consistent with Core voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category Hinder slot for Ring 1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=1` correctly set — the review follows the target, not a district. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.4 = Card(
    id      = "STD.MOD.4",  card_id = "STD.MOD.4",  version = "v0.1",
    name    = "Clearance Review",
    tagline = "A name enters an audit list. Everything that name is attached to slows down until the review clears.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the review follows the target, not the district
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Nobody says why the review opened. Nobody has to. The pause is the point.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.5 — ACCESS FROZEN

#### Design Rationale
Portable set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Portable pattern for Ring 1. Where Clearance Review is a slow-down, this is an outright suspension, and it holds wherever the target tries to use the access. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
The system returns the same message everywhere it's checked: access denied, pending review — the named faction's credentials stop working, everywhere, until further notice.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Outright credential suspension is the escalated form of Core's institutional-access character — still bureaucratic, not force. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same institutional register as STD.MOD.4, escalated to full suspension. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category escalated Hinder slot alongside STD.MOD.4. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=1` correctly set — the suspension travels with the target's credentials, not the Core. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.5 = Card(
    id      = "STD.MOD.5",  card_id = "STD.MOD.5",  version = "v0.1",
    name    = "Access Frozen",
    tagline = "The credentials still exist. They just stop working, everywhere, until further notice.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — the suspension travels with the target's credentials, not the Core
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The system returns the same message everywhere it's checked: access denied, pending review.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.6 — CITADEL CONTACT

#### Design Rationale
Ring-Locked set opens — Ring 1's other half of the 04-n161 test pair. Same Asset/Boost+1 slot as STD.MOD.2, but the pull genuinely doesn't leave the building: `ring_constraint=1` restricts play to Battlefield Strength for a Ring 1 district. Same no-cost/playtest-flagged (04-n94) terms as the Portable set.

#### Card Story
The contact is real, and so is the favor — reinforcing whichever side the playing faction has named, but neither the contact nor the favor leaves Government Citadel.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound institutional contact fits Core's institutional-access character; the Ring-Locked constraint is the narrative point, not a limitation to excuse. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same institutional register as the Portable set, framed around physical presence at Government Citadel. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Asset-category naming slot for Ring 1, paired with STD.MOD.2's Portable counterpart per 04-n161. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=1`/`ring_origin=1` correctly restrict play to a Ring 1 district contest, matching the narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card; `arbiter_note` correctly states the ring restriction. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.6 = Card(
    id      = "STD.MOD.6",  card_id = "STD.MOD.6",  version = "v0.1",
    name    = "Citadel Contact",
    tagline = "Pull that stops existing the moment you're not standing inside Government Citadel.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The contact is real, and so is the favor. Neither one leaves the building.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 1 district.",
)
```

---

### STD.MOD.7 — SANCTUM LEDGER ACCESS

#### Design Rationale
Ring-Locked set, Equipment category. A live feed into Financial Sanctum's own books — the access is the Sanctum's, not the holder's, so it doesn't travel. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.6.

#### Card Story
The numbers only mean anything inside the Sanctum's own walls — reinforcing whichever side the playing faction has named, but worthless the moment the feed leaves the building.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound data feed fits Core's institutional-access character; the ring restriction expresses the institution's own walls, not an arbitrary limit. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; institutional-data register, distinct from STD.MOD.6's personal-contact framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Equipment-category naming slot for Ring 1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=1`/`ring_origin=1` correctly restrict play to a Ring 1 district contest. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.7 = Card(
    id      = "STD.MOD.7",  card_id = "STD.MOD.7",  version = "v0.1",
    name    = "Sanctum Ledger Access",
    tagline = "A live feed into what Financial Sanctum is actually tracking — worthless the moment you're not on its network.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The numbers only mean anything inside the Sanctum's own walls. Outside them, it's just a feed with nothing to compare against.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 1 district.",
)
```

---

### STD.MOD.8 — CHECKPOINT DELAY

#### Design Rationale
Ring-Locked set, weaker Hinder tier (−1). The friction is physical — a specific checkpoint, not a general restriction — so it only bites where that checkpoint stands. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
The checkpoint has never once been called temporary. Tonight it's also slow, and nobody's explaining why — the named faction's position at that checkpoint suffers for it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A physical checkpoint slowdown fits Core's institutional-access character; location-bound friction, not force. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; institutional-friction register, consistent with Core voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category Hinder slot for Ring 1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=1`/`ring_origin=1` correctly restrict play to a Ring 1 district contest, matching the physical-checkpoint narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.8 = Card(
    id      = "STD.MOD.8",  card_id = "STD.MOD.8",  version = "v0.1",
    name    = "Checkpoint Delay",
    tagline = "Military Installation's own checkpoints slow a target's people down — right there, and nowhere else.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The checkpoint has never once been called temporary. Tonight it's also slow, and nobody's explaining why.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 1 district.",
)
```

---

### STD.MOD.9 — PERIMETER LOCKOUT

#### Design Rationale
Ring-Locked set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Ring-Locked pattern for Ring 1. Outright denial at a named perimeter, not a slowdown. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
No explanation posted. Just a perimeter that stopped opening for one name on the list — the named faction's access at that perimeter is denied outright.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Outright perimeter denial is the escalated form of Core's institutional-access character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same institutional register as STD.MOD.8, escalated to full denial. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category escalated Hinder slot alongside STD.MOD.8. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=1`/`ring_origin=1` correctly restrict play to a Ring 1 district contest, matching the named-perimeter narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.9 = Card(
    id      = "STD.MOD.9",  card_id = "STD.MOD.9",  version = "v0.1",
    name    = "Perimeter Lockout",
    tagline = "Military Installation denies a target's access outright — the restriction only exists at that perimeter.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "No explanation posted. Just a perimeter that stopped opening for one name on the list.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 1 district.",
)
```

---

### STD.MOD.10 — LINE SUPERVISOR

#### Design Rationale
Ring 2 (Mid) opens, Portable set. Voice per Art 00 §6.7: the Mid's defining anxiety is throughput, not force or construction — deliberately distinct from Guild's already-shipped material-commitment doctrine (GUI.MOD.11–14). This is operational leverage available to anyone with a stake in the Mid, not a faction specialty. Same no-cost/playtest-flagged (04-n94) terms as the rest of the subclass.

#### Card Story
The schedule says one thing. A shift supervisor makes it say another, quietly, before the shift starts — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A rerouted shift/schedule is a grounded expression of the Mid's operational-throughput character (Art 00 §6.7), deliberately distinct from Guild's material-commitment doctrine. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; operational-logistics register specific to the Mid, distinct from Core's institutional-access voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Asset-category naming slot for Ring 2. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=2` correctly set for a Portable asset (favor travels with holder, sourced from the Mid). | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.10 = Card(
    id      = "STD.MOD.10",  card_id = "STD.MOD.10",  version = "v0.1",
    name    = "Line Supervisor",
    tagline = "A shift supervisor reroutes a crew or a schedule on short notice — the favor travels wherever it's called in.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the favor travels with the holder, not the Mid (closes 04-n161 alongside STD.MOD.14's Locked counterpart)
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The schedule says one thing. The supervisor makes it say another, quietly, before the shift starts.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.11 — RELAY PRIORITY

#### Design Rationale
Portable set, Equipment category. A grid or data allocation override — small enough to carry, general enough to apply anywhere. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.10.

#### Card Story
For an hour, someone else's allocation is quietly someone else's problem — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A grid/data allocation override is a grounded expression of the Mid's operational-throughput character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; operational/infrastructure register, distinct from STD.MOD.10's personnel framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Equipment-category naming slot for Ring 2. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=2` correctly set for a Portable asset. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.11 = Card(
    id      = "STD.MOD.11",  card_id = "STD.MOD.11",  version = "v0.1",
    name    = "Relay Priority",
    tagline = "A brief allocation override, pulled from the grid and carried wherever it's needed.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — the override travels with the holder
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "For an hour, someone else's allocation is quietly someone else's problem.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.12 — REGULATORY HOLD

#### Design Rationale
Portable set, weaker Hinder tier (−1). Paperwork attached to a name, not a desk — it follows the target through the system. Same no-cost/playtest-flagged (04-n94) terms as the rest of the Ring 2 set.

#### Card Story
The form is correct. The form is always correct. It's still not moving — the named faction's position stalls wherever they refile it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Regulatory/paperwork friction fits the Mid's operational-throughput character — a chokepoint, not force. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; operational-bureaucracy register consistent with Mid voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category Hinder slot for Ring 2. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=2` correctly set — the hold follows the target's filing, not a fixed office. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.12 = Card(
    id      = "STD.MOD.12",  card_id = "STD.MOD.12",  version = "v0.1",
    name    = "Regulatory Hold",
    tagline = "A target's paperwork stalls in the system — and keeps stalling, wherever they refile it.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the hold follows the target's filing, not a fixed office
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The form is correct. The form is always correct. It's still not moving.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.13 — SUPPLY LINE FROZEN

#### Design Rationale
Portable set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Portable pattern for Ring 2. A shipment stalls wherever it was headed, not wherever it started. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Somewhere in transit, a manifest gets flagged. It doesn't matter where it started — the named faction's shipment never arrives, wherever it was actually going.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A stalled shipment/manifest is the escalated form of the Mid's operational-throughput character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same operational register as STD.MOD.12, escalated to full disruption. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category escalated Hinder slot alongside STD.MOD.12. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=2` correctly set — the disruption follows the shipment's destination, not the Mid. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.13 = Card(
    id      = "STD.MOD.13",  card_id = "STD.MOD.13",  version = "v0.1",
    name    = "Supply Line Frozen",
    tagline = "A shipment through the Mid quietly stalls — cutting the target off wherever it was actually going.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — the disruption follows the shipment's destination, not the Mid
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Somewhere in transit, a manifest gets flagged. It doesn't matter where it started. It matters that it never arrives.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.14 — POWER GRID CHIEF

#### Design Rationale
Ring-Locked set opens for Ring 2 — the 04-n161 test pair with STD.MOD.10. Weight that only exists on the floor of the Power Grid itself. Same no-cost/playtest-flagged (04-n94) terms as the Portable set.

#### Card Story
Outside the Grid, he's nobody in particular. Inside it, nothing moves without him knowing — reinforcing whichever side the playing faction has named, but only on the Power Grid's own floor.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound floor authority fits the Mid's operational-throughput character; the Ring-Locked constraint expresses the narrative directly. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same operational register as the Portable set, framed around physical presence at the Power Grid. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Asset-category naming slot for Ring 2, paired with STD.MOD.10's Portable counterpart per 04-n161. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=2`/`ring_origin=2` correctly restrict play to a Ring 2 district contest, matching the narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card; `arbiter_note` correctly states the ring restriction. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.14 = Card(
    id      = "STD.MOD.14",  card_id = "STD.MOD.14",  version = "v0.1",
    name    = "Power Grid Chief",
    tagline = "Commands real weight on the floor of the Power Grid. Nowhere else knows his name.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Outside the Grid, he's nobody in particular. Inside it, nothing moves without him knowing.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 2 district.",
)
```

---

### STD.MOD.15 — COMMUNICATIONS HUB OVERRIDE

#### Design Rationale
Ring-Locked set, Equipment category. A direct line into the relay system — it only works standing near a relay tower. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.14.

#### Card Story
The override rides the Hub's own relay hardware — reinforcing whichever side the playing faction has named, but it's just a dead handset anywhere without towers.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound relay override fits the Mid's operational-throughput character; the ring restriction expresses the hardware dependency directly. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; operational/infrastructure register, distinct from STD.MOD.14's personnel framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Equipment-category naming slot for Ring 2. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=2`/`ring_origin=2` correctly restrict play to a Ring 2 district contest. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.15 = Card(
    id      = "STD.MOD.15",  card_id = "STD.MOD.15",  version = "v0.1",
    name    = "Communications Hub Override",
    tagline = "A direct line into the relay system — useless the moment you're not standing near a tower.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The override rides the Hub's own relay hardware. Take it somewhere without towers and it's just a dead handset.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 2 district.",
)
```

---

### STD.MOD.16 — PERMIT OFFICE FREEZE

#### Design Rationale
Ring-Locked set, weaker Hinder tier (−1). The jam is specific to the Regulatory District's own queue — business filed anywhere else is unaffected. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
The clerk isn't stalling. The queue is just, tonight, exactly this long — the named faction's business at the Regulatory District suffers for it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound permit queue jam fits the Mid's operational-throughput character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; operational-bureaucracy register consistent with Mid voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category Hinder slot for Ring 2. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=2`/`ring_origin=2` correctly restrict play to a Ring 2 district contest, matching the location-bound narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.16 = Card(
    id      = "STD.MOD.16",  card_id = "STD.MOD.16",  version = "v0.1",
    name    = "Permit Office Freeze",
    tagline = "The Regulatory District's own queue jams for a target — only for business actually filed there.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The clerk isn't stalling. The queue is just, tonight, exactly this long.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 2 district.",
)
```

---

### STD.MOD.17 — CLEARINGHOUSE LOCKOUT

#### Design Rationale
Ring-Locked set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Ring-Locked pattern for Ring 2. Capital frozen exactly where it sits at Financial Clearinghouse. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
The transfer clears the Sanctum end fine. It just never quite finishes clearing this one — the named faction's capital sticks mid-transfer, frozen exactly where it sits.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A capital transfer frozen at a specific clearinghouse is the escalated form of the Mid's operational-throughput character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same operational register as STD.MOD.16, escalated to full lockout. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category escalated Hinder slot alongside STD.MOD.16. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=2`/`ring_origin=2` correctly restrict play to a Ring 2 district contest, matching the Clearinghouse-specific narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.17 = Card(
    id      = "STD.MOD.17",  card_id = "STD.MOD.17",  version = "v0.1",
    name    = "Clearinghouse Lockout",
    tagline = "A target's capital sticks mid-transfer at Financial Clearinghouse — frozen exactly where it sits.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The transfer clears the Sanctum end fine. It just never quite finishes clearing this one.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 2 district.",
)
```

---

### STD.MOD.18 — FAMILIAR FACE

#### Design Rationale
Ring 3 (Baryo) opens, Portable set. Voice per Art 00 §6.7: Baryo's defining anxiety is exposure, and its leverage is community and the gray economy — deliberately distinct from Network's already-shipped broadcast/public-attention doctrine (NET.MOD.15–18) and Ghost's intelligence doctrine (GHO.MOD.12–15). This is street-level social capital, not information or attention. Same no-cost/playtest-flagged (04-n94) terms as the rest of the subclass.

#### Card Story
A nod, a name dropped, and suddenly you're not a stranger anymore — the vouching travels as far as the person willing to give it, reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Street-level social vouching is a grounded expression of Baryo's community/gray-economy character (Art 00 §6.7), distinct from Network's broadcast doctrine and Ghost's intelligence doctrine. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; informal community-trust register specific to Baryo, distinct from Core/Mid's institutional/operational voices. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Asset-category naming slot for Ring 3. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=3` correctly set for a Portable asset (connection travels with holder, sourced from Baryo). | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.18 = Card(
    id      = "STD.MOD.18",  card_id = "STD.MOD.18",  version = "v0.1",
    name    = "Familiar Face",
    tagline = "Someone in the crowd knows you and vouches for you — the door opens wherever you actually need it to.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the connection travels with the holder, not Baryo (closes 04-n161 alongside STD.MOD.22's Locked counterpart)
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A nod, a name dropped, and suddenly you're not a stranger anymore. It travels as far as the person vouching for you is willing to go.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.19 — SCAVENGED RIG

#### Design Rationale
Portable set, Equipment category. Improvised tech, built for exactly this — being carried somewhere else. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.18.

#### Card Story
None of the parts match. All of them work — reinforcing whichever side the playing faction has named, wherever the rig gets carried.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Improvised, scavenged equipment fits Baryo's gray-economy character — resourcefulness, not institutional or broadcast leverage. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; improvised/gray-economy register, distinct from STD.MOD.18's social-vouching framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Equipment-category naming slot for Ring 3. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=3` correctly set for a Portable asset. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.19 = Card(
    id      = "STD.MOD.19",  card_id = "STD.MOD.19",  version = "v0.1",
    name    = "Scavenged Rig",
    tagline = "Improvised tech pulled together from whatever the Mid discarded last quarter — built to travel.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — improvised and portable by nature
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "None of the parts match. All of them work. That's the whole design philosophy.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.20 — VENDORS CLOSE RANKS

#### Design Rationale
Portable set, weaker Hinder tier (−1). The gray economy's judgment follows the target, not the block they were standing on. Same no-cost/playtest-flagged (04-n94) terms as the rest of the Ring 3 set.

#### Card Story
Nobody posted a notice. Everyone who needed to know already does — the named faction stops getting credit through the gray economy, no matter where they try next.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Informal reputational blacklisting fits Baryo's community/gray-economy character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; gray-economy/community register consistent with Baryo voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category Hinder slot for Ring 3. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=3` correctly set — the reputation follows the target, not a single block. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.20 = Card(
    id      = "STD.MOD.20",  card_id = "STD.MOD.20",  version = "v0.1",
    name    = "Vendors Close Ranks",
    tagline = "Word moves through the gray economy — a target stops getting credit, no matter where they try next.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the reputation follows the target, not a single block
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Nobody posted a notice. Everyone who needed to know already does.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.21 — BARYO TURNS ITS BACK

#### Design Rationale
Portable set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Portable pattern for Ring 3. The community's withdrawal is total and it follows the target, not the ring. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Doors that used to open don't. Nobody explains why. Nobody has to — the ring's informal networks stop cooperating with the named faction everywhere at once.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Total community withdrawal is the escalated form of Baryo's gray-economy/social-network character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same community register as STD.MOD.20, escalated to total withdrawal. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Portable Tactic-category escalated Hinder slot alongside STD.MOD.20. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=3` correctly set — the withdrawal follows the target's name, not a fixed block. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.21 = Card(
    id      = "STD.MOD.21",  card_id = "STD.MOD.21",  version = "v0.1",
    name    = "Baryo Turns Its Back",
    tagline = "The ring's informal networks stop cooperating with a target everywhere at once.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — the withdrawal follows the target's name, not a fixed block
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Doors that used to open don't. Nobody explains why. Nobody has to.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### STD.MOD.22 — STRIP REGULAR

#### Design Rationale
Ring-Locked set opens for Ring 3 — the 04-n161 test pair with STD.MOD.18. Standing that's real, and real only, on the Commercial Strip. Same no-cost/playtest-flagged (04-n94) terms as the Portable set.

#### Card Story
Ask about him three blocks over and you get a shrug. Ask on the Strip and everyone has an opinion — reinforcing whichever side the playing faction has named, but only there.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound community fixture fits Baryo's gray-economy/community character; the Ring-Locked constraint expresses the narrative directly. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same community register as the Portable set, framed around physical presence on the Commercial Strip. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Asset-category naming slot for Ring 3, paired with STD.MOD.18's Portable counterpart per 04-n161. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=3`/`ring_origin=3` correctly restrict play to a Ring 3 district contest, matching the narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card; `arbiter_note` correctly states the ring restriction. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.22 = Card(
    id      = "STD.MOD.22",  card_id = "STD.MOD.22",  version = "v0.1",
    name    = "Strip Regular",
    tagline = "A fixture of the Commercial Strip. Everybody there owes him a little something. Nobody past it does.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Ask about him three blocks over and you get a shrug. Ask on the Strip and everyone has an opinion.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 3 district.",
)
```

---

### STD.MOD.23 — MARKET STALL CACHE

#### Design Rationale
Ring-Locked set, Equipment category. Goods stockpiled in a specific stall — moving them defeats the point of having stockpiled them there. Same no-cost/playtest-flagged (04-n94) terms as STD.MOD.22.

#### Card Story
The cache has been building for years, one odd lot at a time — reinforcing whichever side the playing faction has named, but it was never going anywhere.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A location-bound stockpile fits Baryo's gray-economy character; the ring restriction expresses the physical stall directly. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; gray-economy/commerce register, distinct from STD.MOD.22's personal-standing framing. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Equipment-category naming slot for Ring 3. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=3`/`ring_origin=3` correctly restrict play to a Ring 3 district contest. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.23 = Card(
    id      = "STD.MOD.23",  card_id = "STD.MOD.23",  version = "v0.1",
    name    = "Market Stall Cache",
    tagline = "Goods and gear stockpiled in a Strip stall — useless anywhere but there.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The cache has been building for years, one odd lot at a time. It was never going anywhere.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 3 district.",
)
```

---

### STD.MOD.24 — HOUSING ARRANGEMENT CALLED IN

#### Design Rationale
Ring-Locked set, weaker Hinder tier (−1). The leverage belongs to a specific unofficial landlord over a specific arrangement — it doesn't extend past that reach. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
No one signed anything. That was always the arrangement's whole strength, and tonight it's a weakness instead — the named faction's stay in that arrangement's reach turns difficult.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Informal-landlord leverage bound to a specific arrangement fits Baryo's gray-economy character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; unofficial/informal-arrangement register consistent with Baryo voice. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category Hinder slot for Ring 3. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=3`/`ring_origin=3` correctly restrict play to a Ring 3 district contest, matching the arrangement's-reach narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.24 = Card(
    id      = "STD.MOD.24",  card_id = "STD.MOD.24",  version = "v0.1",
    name    = "Housing Arrangement Called In",
    tagline = "One of the ring's unofficial landlords makes a target's stay difficult — only within that arrangement's reach.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "No one signed anything. That was always the arrangement's whole strength, and tonight it's a weakness instead.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 3 district.",
)
```

---

### STD.MOD.25 — TRANSIT HUB SHUTOUT

#### Design Rationale
Ring-Locked set, escalated Hinder tier (−2) — completes the 2 Boost / 2 Hinder Ring-Locked pattern for Ring 3, and closes out the 24-card Ring Modifier stub pass. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Every shift finds a reason not to touch the load. By evening it's still sitting exactly where it was unloaded — the named faction's position at the Hub goes nowhere.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Coordinated labor non-cooperation at a named hub is the escalated form of Baryo's gray-economy/community character. | Art 00 §6.7; Art 04 §5a |
| Voice fit | ✓ | `faction=All`; same community register as STD.MOD.24, escalated to a full shutout. | Art 00 §6.7, §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/`subtype=Standard` correct; fills the Ring-Locked Tactic-category escalated Hinder slot alongside STD.MOD.24. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked whole-subclass pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (locked whole-subclass convention). | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=3`/`ring_origin=3` correctly restrict play to a Ring 3 district contest, matching the named-Hub narrative. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.25 = Card(
    id      = "STD.MOD.25",  card_id = "STD.MOD.25",  version = "v0.1",
    name    = "Transit Hub Shutout",
    tagline = "Transit labor stops moving anything for a target — right at the Hub, and nowhere the Hub doesn't reach.",
    type    = ModBattleCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Every shift finds a reason not to touch the load. By evening it's still sitting exactly where it was unloaded.",
    arbiter_note = "Playable by any faction, not just whoever drew it (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target. Usable only in Battlefield Strength for a Ring 3 district.",
)
```

---

### STD.MOD.26 — ZONING VARIANCE

#### Design Rationale
Minor tier of Ring 1's Portable `threshold_delta` quartet — a self-only +5 host-threshold ease bundled at Dispatch with any CA/PA the holder submits (self-only is schema-locked, §6.3/04-n170: 3 of 4 `ModActionExpr` variants carry no faction-target field). Portable (`ring_constraint=None`) fits the concept: "someone already cleared this elsewhere" doesn't require the holder to still be standing in Ring 1 to use it — `ring_origin=1` keeps the card's *source* Core-flavored (institutional access, Art 00 §6.7) even though its *use* travels. `cost=None` per the closed PM02 L256 convention (splay-display legibility), not a per-card gap.

#### Card Story
A zoning officer signs off on an exception before anyone downstream even has to file the objection — the paperwork simply never becomes a problem.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic ease-of-passage; matches Ring 1/Core "institutional access" ring character. Parasitic on host, no independent action. | Art 00 §6.7; Art 04 §11.1 |
| Voice fit | ✓ | `faction=All`, no perspectives required (Standard card). Tagline/narrative read in the neutral institutional register consistent with Core voice. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`; `doctrine_mod` correctly absent — no faction relationship in play. | Art 04 §6.2 |
| Card type fit | ✓ | ModActionCard, `subtype=Standard`; correctly excluded from taxonomy (`layer`/`function`/`subject=None`) per §11.1 — parasitic on host, not its own action category. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | `layer`/`function`/`subject` schema-locked None for all modifier subclasses — not an open taxonomy question here. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the locked 4-value `threshold_delta` ladder (+5/+10/+15/+20); `value_rating=1` correctly mirrors tier (L259). | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host at resolution, consumed on use — no standing effect. | Art 04 §5 P19 |
| Persistence | N/A | `persistence`/`persistence_condition`/`persistence_effect` schema-locked None for ModActionCard — no standing marker. | Art 04 §6.2 |
| Trigger validity | N/A | `trigger` schema-locked None for ModActionCard — bundled at Dispatch, not trigger-fired. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` genuinely assessed, not a TBD punt — a procedural ease-of-passage nudge carries no doctrinal weight and affects no faction's standing. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=1` are the zone-relevant fields, set correctly for a Portable asset. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components; physical modifier card only. | Art 02 |
| Supported by game procedure | ✓ | Dispatch-bundling procedure at Art 03 §9.1.1/§9.4.0.1 covers attachment; `arbiter_note` cites it correctly. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding, not previously applied to this corpus). All other §6.1/§6.2 fields present and correctly typed. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Card Story is a plain 1-sentence New Meridian event, not a mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | ModActionCard carries no `success`/`successcrit`/`fail`/`failcrit` of its own (schema-locked None) — determinacy belongs to the host action. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None` is the closed whole-subclass convention (PM02 L256); out of scope for the 04-n178 Floor Act rule (scoped to CovertOp/PublicAct/ModReact only). | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.26 = Card(
    id      = "STD.MOD.26",  card_id = "STD.MOD.26",  version = "v0.1",
    name    = "Zoning Variance",
    tagline = "A quiet exception clears the way before anyone downstream has to ask for one.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only — no faction param on this variant (§6.3). Tracked at PM05 04-n170; remove this comment once resolved.
    value_rating    = 1,
    ring_constraint = None,   # Portable set — the exception travels with whoever's holding it
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A quiet exception makes a Core placement or build action easier to clear — filed and approved before anyone thought to object.",
    arbiter_note = "Attach at Dispatch to any CA/PA in the holder's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### STD.MOD.27 — REDACTED FILE

#### Design Rationale
Second tier of Ring 1's Portable `threshold_delta` quartet (+10) — identical structure to STD.MOD.26, self-only host-threshold ease. Narrative distinct from Zoning Variance: information suppression rather than pre-clearance, still fitting Core's institutional-access register.

#### Card Story
A report reaches its audience with the inconvenient part blacked out — smoothing the acting faction's own submission.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional information-control ease; same Core register as STD.MOD.26. | Art 00 §6.7; Art 04 §11.1 |
| Voice fit | ✓ | `faction=All`, neutral institutional register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as STD.MOD.26. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier of the 4-value ladder; `value_rating=2` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis as STD.MOD.26. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.27 = Card(
    id      = "STD.MOD.27",  card_id = "STD.MOD.27",  version = "v0.1",
    name    = "Redacted File",
    tagline = "The report goes out with the inconvenient part blacked out.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A report reaches its audience with the inconvenient part blacked out — smoothing the acting faction's own submission.",
    arbiter_note = "Self-only, same basis as STD.MOD.26.",
)
```

---

### STD.MOD.28 — MAINTENANCE WINDOW

#### Design Rationale
Third tier of the Portable `threshold_delta` quartet (+15). Reframed from an earlier hostile-flavored seed concept ("Cordoned Block" — sealing a rival's district "for maintenance," raising their difficulty) per 04-n170: `threshold_delta` carries no faction parameter, so it can only ever ease the holder's own host action, never hinder a rival's. The reframe keeps the "maintenance closure" flavor but repoints the mechanical benefit to the acting faction's own operation in the cleared space.

#### Card Story
A district block is cordoned off "for maintenance" — which clears space for the acting faction's own operation there.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Core institutional register; reframe correctly resolves to self-only benefit. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ✓ | `faction=All`, neutral register — reframed narrative doesn't retain hostile framing. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as STD.MOD.26/27. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier of the 4-value ladder; `value_rating=3` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis as STD.MOD.26. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Reframed narrative reads as a clean self-only event, no hostile residue. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.28 = Card(
    id      = "STD.MOD.28",  card_id = "STD.MOD.28",  version = "v0.1",
    name    = "Maintenance Window",
    tagline = "The block is closed off \"for maintenance\" — which clears the way for something else entirely.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A district block cordoned off \"for maintenance\" clears space for the acting faction's own operation there.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170 (same basis as the faction-set threshold_delta reframes: DIR.MOD.15/16, GUI.MOD.17, GHO.MOD.18, NET.MOD.21, SYN.MOD.18).",
)
```

---

### STD.MOD.29 — CLASSIFIED BRIEFING

#### Design Rationale
Capstone tier of the Portable `threshold_delta` quartet (+20). Reframed from an earlier hostile-flavored seed concept ("Sealed Minutes" — classifying context before a rival can plan around it) per 04-n170, same self-only correction as STD.MOD.28. As the top tier, this card is the first in the set to carry an explicit playtest caveat (04-n157) — the +20 magnitude is the largest single `threshold_delta` value in the entire card system and hasn't been logged against actual play outcomes yet. **Outstanding issue:** narrative still reads slightly dual-purpose ("raising their difficulty" for a rival, "smooths the way" for the holder) despite the effect being schema-locked self-only — worth a light narrative tighten so the Card Story doesn't imply a hindrance the mechanic can't deliver.

#### Card Story
Key context is classified before a rival can plan around it — and for the faction holding the briefing, the same classification smooths their own way through.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Core institutional register as the rest of the tier. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ⚠ | Narrative/`narrative` field still frames a rival's difficulty rising, but the mechanic (`threshold_delta`) only ever eases the holder's own host — narrative implies a hindrance the card can't deliver. Minor tighten recommended, not blocking. | Art 00 §9; PM05 04-n170 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as rest of tier. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` correctly mirrors tier (L259), but +20 is unvalidated against actual play (04-n157 playtest flag — largest single `threshold_delta` value in the system). | PM02 L258, L259; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis as rest of tier. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ⚠ | Story is plain and in-world, but see Voice fit — implies dual-purpose effect the schema doesn't support. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (narrative tighten, +20 playtest flag) |  |

```python
STD.MOD.29 = Card(
    id      = "STD.MOD.29",  card_id = "STD.MOD.29",  version = "v0.1",
    name    = "Classified Briefing",
    tagline = "The key context is classified in the acting faction's favor before anyone else can plan around it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Key context is classified before a rival can plan around it, raising their difficulty — but for the holder, the same classification smooths the way.",
    arbiter_note = "Capstone tier, reframed per 04-n170 — log actual play outcomes before treating +20 as balanced (04-n157, same playtest caveat as the rest of this set). Narrative reads dual-purpose despite the self-only mechanic — see Outstanding Issues.",
)
```

---

### STD.MOD.30 — INSTITUTIONAL BACKING

#### Design Rationale
Common tier (n=1) of the Portable `success_multiplier` pair — fires the host's success effect an additional time when the host succeeds. Self-only (no faction-target field on this `ModActionExpr` variant either), consistent with the tier's Core "institutional access" framing: an unseen endorsement, not a visible act.

#### Card Story
An unseen endorsement from within the Core amplifies a successful action's effect.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Amplification-via-quiet-endorsement fits Core register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as threshold_delta tier. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier of the 2-value `success_multiplier` pair; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.30 = Card(
    id      = "STD.MOD.30",  card_id = "STD.MOD.30",  version = "v0.1",
    name    = "Institutional Backing",
    tagline = "An unseen endorsement from within the Core, and the outcome lands harder for it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An unseen endorsement from within the Core amplifies a successful action's effect.",
    arbiter_note = "Self-only, amplifies the holder's own host action.",
)
```

---

### STD.MOD.31 — CEREMONIAL GROUNDBREAKING

#### Design Rationale
Capstone tier (n=2) of the Portable `success_multiplier` pair — doubling an already-uncommon effect type (only 2 cards/set use it), so this is the highest-leverage single card in the Portable set on a per-card basis. Carries the same unvalidated-playtest caveat as STD.MOD.29's +20 threshold_delta.

#### Card Story
Official recognition of a successful placement makes its result carry further than usual.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ceremony-as-amplifier fits Core institutional register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as tier. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, but n=2 success_multiplier is unvalidated against play — doubling an outcome is a stronger lever than any single `threshold_delta`/`ps_shift` tier in the set. | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (n=2 playtest flag) |  |

```python
STD.MOD.31 = Card(
    id      = "STD.MOD.31",  card_id = "STD.MOD.31",  version = "v0.1",
    name    = "Ceremonial Groundbreaking",
    tagline = "Official recognition turns a routine placement into something that carries.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Official recognition of a successful placement makes its result carry further than usual.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### STD.MOD.32 — OFF THE RECORD

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` 2×2 matrix — the only `ModActionExpr` variant carrying a faction parameter (`acting`/`target`/named). This half resolves to the acting faction and needs no host-declared target, so — unlike the target-hinder half (STD.MOD.34/35) — it carries no submission-validity dependency.

#### Card Story
An exchange is agreed by everyone present to have never happened — insulating the acting faction from the standing cost it would otherwise carry.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Discretion-as-PS-insulation fits Core institutional register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no separate `target_faction`/`doctrine_mod` question; resolves to whoever submitted the host. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as rest of set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 `ps_shift` matrix; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — PS shift is the card's whole effect, no separate Portrait signal implied. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | `faction="acting"` resolves cleanly to the submitter — no target-dependency gap (contrast STD.MOD.34/35). | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.32 = Card(
    id      = "STD.MOD.32",  card_id = "STD.MOD.32",  version = "v0.1",
    name    = "Off the Record",
    tagline = "An exchange, agreed by everyone present to have never happened.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An exchange is agreed to never have happened — insulating the acting faction from the standing cost it would otherwise carry.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### STD.MOD.33 — PUBLIC CITATION

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` 2×2 matrix — same self-resolution basis as STD.MOD.32, doubled magnitude.

#### Card Story
A formal citation boosts standing through institutional channels rather than the public eye.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.32. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 `ps_shift` matrix; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.33 = Card(
    id      = "STD.MOD.33",  card_id = "STD.MOD.33",  version = "v0.1",
    name    = "Public Citation",
    tagline = "A formal citation, delivered through institutional channels rather than the public eye.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A formal citation boosts standing through institutional channels rather than the public eye.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### STD.MOD.34 — WORD TO THE WISE

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` 2×2 matrix. `faction="target"` resolves against whichever faction the host CA/PA it's packet-paired with declares as `target_faction` (§6.1) — the modifier has no target of its own; it's definitionally the host's target.

#### Card Story
A quiet, informal heads-up to the right official costs a named faction a small, deniable amount of standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Discreet-tip-as-hindrance fits Core institutional register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` — resolves to whichever faction the host names; no `doctrine_mod` needed since this card doesn't itself declare the target. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 `ps_shift` matrix; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.34 = Card(
    id      = "STD.MOD.34",  card_id = "STD.MOD.34",  version = "v0.1",
    name    = "Word to the Wise",
    tagline = "A quiet, informal heads-up to exactly the right official.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A quiet, informal heads-up to the right official costs a named faction a small, deniable amount of standing.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA it's packet-paired with names as its target_faction (§6.1) — the modifier's target IS the host action, not an independently-declared field.",
)
```

---

### STD.MOD.35 — NAMED IN THE REVIEW

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` 2×2 matrix. Same target-resolution behavior as STD.MOD.34 (resolves via host pairing, not an independent field), doubled magnitude.

#### Card Story
An audit's findings reach exactly the audience that costs a rival the most standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.34. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 `ps_shift` matrix; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.35 = Card(
    id      = "STD.MOD.35",  card_id = "STD.MOD.35",  version = "v0.1",
    name    = "Named in the Review",
    tagline = "An audit's findings reach exactly the audience that costs the most.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An audit's findings reach exactly the audience that costs a rival the most standing.",
    arbiter_note = "Same target-resolution behavior as STD.MOD.34, major tier.",
)
```

---

### STD.MOD.36 — FEE WAIVED

#### Design Rationale
Common tier (n=1) of the Portable `cost_reduction` pair — PA-only per §6.3 (CA cost is already committed at Dispatch before Beat 0, so a cost reduction has nothing left to apply to; only PAs, declared at §9.2, have a cost step this can discount). `arbiter_note` correctly flags the PA-only restriction and the different attachment point (§9.2, not §9.1.1).

#### Card Story
A routine institutional charge is quietly set aside for the acting faction only.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Fee-waiver fits Core institutional register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set; correctly PA-restricted per `cost_reduction`'s §6.3 definition. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier of the 2-value `cost_reduction` pair; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Correctly attaches at §9.2 Public Declaration (not §9.1.1 Dispatch, since PA cost isn't committed until declaration) — `arbiter_note` cites the right procedure. | Art 03 §9.2 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.36 = Card(
    id      = "STD.MOD.36",  card_id = "STD.MOD.36",  version = "v0.1",
    name    = "Fee Waived",
    tagline = "A routine institutional charge, quietly set aside for one submission only.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A routine institutional charge is quietly set aside for the acting faction only.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.37 — EMERGENCY ALLOCATION

#### Design Rationale
Capstone tier (n=2) of the Portable `cost_reduction` pair, PA-only per §6.3. Closes the Ring 1 Portable set (STD.MOD.26–37, 12 cards). Same unvalidated-magnitude caveat as the other two capstones in this set (STD.MOD.29, STD.MOD.31) — a 2-unit cost reduction hasn't been checked against any specific PA's actual cost to confirm it isn't a near-total discount on cheap PAs.

#### Card Story
Funds normally locked behind approval move immediately, discounting an urgent action's cost.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Emergency-allocation framing fits Core institutional register. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, same basis as STD.MOD.36. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, but a flat 2-unit `cost_reduction` isn't proportional to PA cost — could zero out or exceed a cheap PA's cost entirely. Unvalidated (04-n157). | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=1` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Attaches at §9.2 Public Declaration, same as STD.MOD.36. | Art 03 §9.2 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (flat-vs-proportional cost_reduction magnitude, 04-n157) |  |

```python
STD.MOD.37 = Card(
    id      = "STD.MOD.37",  card_id = "STD.MOD.37",  version = "v0.1",
    name    = "Emergency Allocation",
    tagline = "Funds normally locked behind approval move immediately, no questions asked.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — closes Ring 1's Portable 12-card set
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Funds normally locked behind approval move immediately, discounting an urgent action's cost.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 1's Portable set (STD.MOD.26–37); Ring-Locked set follows (STD.MOD.38–49).",
)
```

---

### STD.MOD.38 — RECOGNIZED ON SIGHT

#### Design Rationale
Ring-Locked set opens for Ring 1 — the other half of the 04-n161 Portable/Ring-Locked pair, same slot as STD.MOD.26 but `ring_constraint=1` restricts it to hosts targeting a Ring 1 district. Invented fresh (not seed-drawn) — the Portable set already used all 4 seed-pool threshold_delta concepts for Core.

#### Card Story
The recognition is real, but it's tied to this specific checkpoint — it doesn't travel with the holder anywhere else.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-anchored recognition fits Ring-Locked framing; distinct concept from Portable's STD.MOD.26 (not a reskin). | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as Portable set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 4-value ladder; `value_rating=1` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts — deployment restriction is itself the zone-relevant field. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Dispatch-bundling procedure covers attachment; ring-match validation is the same established mechanic as Ring-Locked ModBattleCard precedent. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event; correctly conveys the location-anchored constraint. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.38 = Card(
    id      = "STD.MOD.38",  card_id = "STD.MOD.38",  version = "v0.1",
    name    = "Recognized on Sight",
    tagline = "The guards at this specific gate wave you through without checking the manifest.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),
    value_rating    = 1,
    ring_constraint = 1,      # Ring-Locked set — usable only with ops targeting a Ring 1 district (closes 04-n161 alongside STD.MOD.26's Portable counterpart)
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The recognition is real, but it's tied to this specific checkpoint — it doesn't travel with the holder anywhere else.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.39 — STANDING REQUEST

#### Design Rationale
Mid tier (+10) of the Ring-Locked `threshold_delta` quartet. Same structure as STD.MOD.38, different flavor (pre-filed paperwork vs. checkpoint recognition).

#### Card Story
A standing relationship with the archive staff eases a paperwork-dependent action — but only within their reach.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Ring-Locked institutional-access basis as STD.MOD.38. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis as STD.MOD.38. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.39 = Card(
    id      = "STD.MOD.39",  card_id = "STD.MOD.39",  version = "v0.1",
    name    = "Standing Request",
    tagline = "The paperwork was pre-filed with the archive staff weeks ago.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A standing relationship with the archive staff eases a paperwork-dependent action — but only within their reach.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.40 — BACK-CHANNEL WORD

#### Design Rationale
Third tier (+15) of the Ring-Locked `threshold_delta` quartet. Same structure as STD.MOD.38/39, unlike the Portable set's equivalent tier (STD.MOD.28) this one was never a hostile-flavored reframe — invented fresh, so carries no 04-n170 provenance note.

#### Card Story
A direct line into the administrative wing eases the operation — but the line only reaches this far.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Ring-Locked basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register — clean self-only framing throughout (no dual-purpose residue, contrast STD.MOD.29). | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.40 = Card(
    id      = "STD.MOD.40",  card_id = "STD.MOD.40",  version = "v0.1",
    name    = "Back-Channel Word",
    tagline = "A direct line into the administrative wing, open only from inside the building.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A direct line into the administrative wing eases the operation — but the line only reaches this far.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.41 — FULL CLEARANCE

#### Design Rationale
Capstone tier (+20) of the Ring-Locked `threshold_delta` quartet. Unlike Portable's capstone (STD.MOD.29), narrative here is clean self-only throughout — "so long as the work stays here" correctly reinforces the ring restriction rather than implying a rival-facing effect.

#### Card Story
Full clearance from within the Core itself — nothing left to process through ordinary channels, so long as the work stays here.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Ring-Locked basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative — no dual-purpose framing (contrast STD.MOD.29). | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, but +20 unvalidated against play (04-n157) — same caveat as STD.MOD.29, though ring-locking here somewhat narrows the practical impact vs. the Portable capstone. | PM02 L258, L259, L261; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.41 = Card(
    id      = "STD.MOD.41",  card_id = "STD.MOD.41",  version = "v0.1",
    name    = "Full Clearance",
    tagline = "Nothing left to process through ordinary channels — the clearance is already signed.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Full clearance from within the Core itself — nothing left to process through ordinary channels, so long as the work stays here.",
    arbiter_note = "Capstone tier, usable only with an operation targeting a Ring 1 district — log actual play outcomes before treating +20 as balanced (04-n157).",
)
```

---

### STD.MOD.42 — SHIFT CHANGE TIMING

#### Design Rationale
Common tier (n=1) of the Ring-Locked `success_multiplier` pair — location-anchored knowledge rather than Portable's unseen institutional endorsement (STD.MOD.30), same mechanic.

#### Card Story
Knowing exactly how this specific checkpoint runs its shift changes lets a successful action land further than expected.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-specific knowledge fits Ring-Locked framing. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier of the 2-value pair; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.42 = Card(
    id      = "STD.MOD.42",  card_id = "STD.MOD.42",  version = "v0.1",
    name    = "Shift Change Timing",
    tagline = "Knowing exactly when the checkpoint staff rotate changes what a result is worth.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Knowing exactly how this specific checkpoint runs its shift changes lets a successful action land further than expected.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.43 — FULL INSTITUTIONAL WEIGHT

#### Design Rationale
Capstone tier (n=2) of the Ring-Locked `success_multiplier` pair — same unvalidated-magnitude caveat as Portable's equivalent (STD.MOD.31), narrative correctly reinforces the ring restriction ("only inside its own reach").

#### Card Story
When the institution itself backs an outcome, it carries much further than a routine result would — but only inside its own reach.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Ring-Locked basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, but n=2 success_multiplier unvalidated (same caveat as STD.MOD.31). | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.43 = Card(
    id      = "STD.MOD.43",  card_id = "STD.MOD.43",  version = "v0.1",
    name    = "Full Institutional Weight",
    tagline = "When the Core itself backs an outcome, it carries much further than a routine result would.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "When the institution itself backs an outcome, it carries much further than a routine result would — but only inside its own reach.",
    arbiter_note = "Rare/capstone tier, usable only with an operation targeting a Ring 1 district — log actual play outcomes before treating n=2 as balanced (04-n157).",
)
```

---

### STD.MOD.44 — NOTED FAVORABLY

#### Design Rationale
Self-boost minor tier (+1) of the Ring-Locked `ps_shift` 2×2 matrix. `faction="acting"` needs no host-declared target, so — same as Portable's STD.MOD.32 — carries no submission-validity dependency.

#### Card Story
A quiet, favorable notation enters the institution's own record — a small, deliberate boost to standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Ring-Locked basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 matrix; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.44 = Card(
    id      = "STD.MOD.44",  card_id = "STD.MOD.44",  version = "v0.1",
    name    = "Noted Favorably",
    tagline = "A quiet, favorable notation enters the record — this record specifically.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A quiet, favorable notation enters the institution's own record — a small, deliberate boost to standing.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction. Usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.45 — FORMAL RECOGNITION

#### Design Rationale
Self-boost major tier (+2) of the Ring-Locked `ps_shift` matrix — same self-resolution basis as STD.MOD.44, doubled magnitude.

#### Card Story
Formal recognition from within the institution itself is a significant, visible boost — earned specifically here.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.44. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 matrix; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.45 = Card(
    id      = "STD.MOD.45",  card_id = "STD.MOD.45",  version = "v0.1",
    name    = "Formal Recognition",
    tagline = "Recognition from within the institution itself — visible, and hard to dismiss.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Formal recognition from within the institution itself is a significant, visible boost — earned specifically here.",
    arbiter_note = "Self-boost, major tier, resolves to the acting faction — usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.46 — QUIETLY FLAGGED

#### Design Rationale
Target-hinder minor tier (−1) of the Ring-Locked `ps_shift` matrix — same target-resolution behavior as STD.MOD.34 (resolves via host pairing, not an independent field), location-anchored flavor.

#### Card Story
A named faction's presence is quietly flagged at this specific checkpoint — small, but on the record.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.34, location-anchored. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 matrix; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.46 = Card(
    id      = "STD.MOD.46",  card_id = "STD.MOD.46",  version = "v0.1",
    name    = "Quietly Flagged",
    tagline = "A named faction's presence gets a small, quiet notation at this specific checkpoint.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A named faction's presence is quietly flagged at this specific checkpoint — small, but on the record.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.47 — DENIED ACCESS

#### Design Rationale
Target-hinder major tier (−2) of the Ring-Locked `ps_shift` matrix. Same target-resolution behavior as STD.MOD.46 (resolves via host pairing, not an independent field), doubled magnitude.

#### Card Story
A rival is visibly and formally denied access to institutional records — a real, public cost to standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.46. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 matrix; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.47 = Card(
    id      = "STD.MOD.47",  card_id = "STD.MOD.47",  version = "v0.1",
    name    = "Denied Access",
    tagline = "A named faction is visibly and formally turned away — everyone in the building knows why.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A rival is visibly and formally denied access to institutional records — a real, public cost to standing.",
    arbiter_note = "Same target-resolution behavior as STD.MOD.46, major tier — usable only with an operation targeting a Ring 1 district.",
)
```

---

### STD.MOD.48 — REASSIGNED ON PAPER

#### Design Rationale
Common tier (n=1) of the Ring-Locked `cost_reduction` pair, PA-only per §6.3. Same procedural basis as Portable's STD.MOD.36; `arbiter_note` correctly notes both the PA-only restriction and the §9.2 attachment point.

#### Card Story
An administrative reshuffle absorbs part of an action's overhead — quietly, and only on this institution's books.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.36. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier of the 2-value pair; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Correctly attaches at §9.2, same as STD.MOD.36. | Art 03 §9.2 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.48 = Card(
    id      = "STD.MOD.48",  card_id = "STD.MOD.48",  version = "v0.1",
    name    = "Reassigned on Paper",
    tagline = "An administrative reshuffle quietly absorbs part of the overhead.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = 1,
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An administrative reshuffle absorbs part of an action's overhead — quietly, and only on this institution's books.",
    arbiter_note = "PA host only, usable only with a PA targeting a Ring 1 district. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.49 — JUMPED THE QUEUE

#### Design Rationale
Capstone tier (n=2) of the Ring-Locked `cost_reduction` pair. Same flat-vs-proportional caveat as Portable's STD.MOD.37. Closes Ring 1's 24-card Ring ModAction set (Portable STD.MOD.26–37 + Ring-Locked STD.MOD.38–49).

#### Card Story
A submission that skips the full review process skips the overhead that comes with it — but only through this specific channel.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.37. | Art 00 §6.7 |
| Voice fit | ✓ | `faction=All`, neutral register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, but flat 2-unit reduction not checked against any specific PA's actual cost — same unresolved question as STD.MOD.37. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=1` correctly restricts to Ring 1-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.49 = Card(
    id      = "STD.MOD.49",  card_id = "STD.MOD.49",  version = "v0.1",
    name    = "Jumped the Queue",
    tagline = "The submission skips the full review process — and skips the overhead that comes with it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = 1,      # Ring-Locked set — closes Ring 1's 24-card set (Portable + Ring-Locked)
    ring_origin     = 1,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A submission that skips the full review process skips the overhead that comes with it — but only through this specific channel.",
    arbiter_note = "Capstone cost_reduction tier, usable only with a PA targeting a Ring 1 district — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 1 (STD.MOD.26–49, 24 cards); Ring 2 (Mid) follows.",
)
```

---

### STD.MOD.50 — REZONED CORRIDOR

#### Design Rationale
Ring 2 (Mid) Portable set opens — same format as Ring 1 (STD.MOD.26), minor threshold_delta tier (+5). Voice per Art 00 §6.7: operational throughput and infrastructure chokepoints, distinct from Ring 1's institutional-access lean and Network's broadcast doctrine.

#### Card Story
An infrastructure corridor is reclassified, making a placement there easier to clear.

**Design checklist:** Same disposition as STD.MOD.26 (identical mechanic/tier, Mid flavor). Voice/narrative independently checked — clean self-only framing, correctly Mid-flavored (corridor rezoning, not Core paperwork).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Infrastructure-rezoning fits Mid's throughput/chokepoint register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative, no dual-purpose residue. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as STD.MOD.26. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.50 = Card(
    id      = "STD.MOD.50",  card_id = "STD.MOD.50",  version = "v0.1",
    name    = "Rezoned Corridor",
    tagline = "The corridor gets reclassified, and the placement clears without a fight.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only — no faction param on this variant (§6.3). Tracked at PM05 04-n170; remove this comment once resolved.
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An infrastructure corridor is reclassified, making a placement there easier to clear.",
    arbiter_note = "Attach at Dispatch to any CA/PA in the holder's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### STD.MOD.51 — RELAY INTERCEPT

#### Design Rationale
Mid tier (+10). Same structure as STD.MOD.50, self-only.

#### Card Story
A tapped communications relay lets the acting faction anticipate and ease their own move.

**Design checklist:** Same disposition as STD.MOD.50/26. Narrative independently checked — clean self-only.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Mid basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.51 = Card(
    id      = "STD.MOD.51",  card_id = "STD.MOD.51",  version = "v0.1",
    name    = "Relay Intercept",
    tagline = "A tapped relay means the move is already anticipated before it's made.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A tapped communications relay lets the acting faction anticipate and ease their own move.",
    arbiter_note = "Self-only, same basis as STD.MOD.50.",
)
```

---

### STD.MOD.52 — MANIFEST CORRECTION

#### Design Rationale
Third tier (+15). Reframed from "Manifest Discrepancy" (hostile) per 04-n170, same self-only correction as STD.MOD.28.

#### Card Story
The acting faction's own shipping manifest is quietly corrected in advance, smoothing a logistics-dependent action.

**Design checklist:** Same disposition as STD.MOD.28. Narrative independently checked — clean, correctly "own manifest" throughout, no dual-purpose residue (unlike STD.MOD.29's capstone).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Mid basis. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only reframe. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.52 = Card(
    id      = "STD.MOD.52",  card_id = "STD.MOD.52",  version = "v0.1",
    name    = "Manifest Correction",
    tagline = "The manifest gets quietly corrected before anyone downstream has to reconcile it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The acting faction's own shipping manifest is quietly corrected in advance, smoothing a logistics-dependent action.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as STD.MOD.28/29.",
)
```

---

### STD.MOD.53 — GRIEVANCE WITHDRAWN

#### Design Rationale
Capstone tier (+20). Reframed from "Union Grievance" (hostile) per 04-n170. Unlike Portable's Ring 1 capstone (STD.MOD.29), narrative here is clean throughout — "against the acting faction's own submission" correctly keeps the effect self-only, no dual-purpose residue.

#### Card Story
A formal labor complaint against the acting faction's own submission is quietly withdrawn before it can raise the bar.

**Design checklist:** Same disposition as STD.MOD.29 except narrative is clean (verified independently — no rival-facing implication).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Mid basis. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only — "own submission" correctly scopes the effect (contrast STD.MOD.29). | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, +20 unvalidated (04-n157). | PM02 L258, L259; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Clean self-only event, no schema/narrative mismatch. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (+20 playtest flag) |  |

```python
STD.MOD.53 = Card(
    id      = "STD.MOD.53",  card_id = "STD.MOD.53",  version = "v0.1",
    name    = "Grievance Withdrawn",
    tagline = "The complaint gets quietly withdrawn before it ever reaches a hearing.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A formal labor complaint against the acting faction's own submission is quietly withdrawn before it can raise the bar.",
    arbiter_note = "Capstone tier, reframed per 04-n170 — log actual play outcomes before treating +20 as balanced (04-n157).",
)
```

---

### STD.MOD.54 — CROSS-DOCKED EFFICIENTLY

#### Design Rationale
Common tier (n=1) of the `success_multiplier` pair. Same self-only basis as STD.MOD.30.

#### Card Story
Resources moved without ever formally stopping compound the action's benefit.

**Design checklist:** Same disposition as STD.MOD.30.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Logistics-throughput fits Mid register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.54 = Card(
    id      = "STD.MOD.54",  card_id = "STD.MOD.54",  version = "v0.1",
    name    = "Cross-Docked Efficiently",
    tagline = "Resources move through without ever formally stopping.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Resources moved without ever formally stopping compound the action's benefit.",
    arbiter_note = "Self-only, amplifies the holder's own host action.",
)
```

---

### STD.MOD.55 — CHAIN REACTION

#### Design Rationale
Capstone tier (n=2). Same unvalidated-magnitude caveat as STD.MOD.31.

#### Card Story
One system's output feeding directly into the next multiplies the outcome well past what was planned.

**Design checklist:** Same disposition as STD.MOD.31.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Mid basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated (same caveat as STD.MOD.31). | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.55 = Card(
    id      = "STD.MOD.55",  card_id = "STD.MOD.55",  version = "v0.1",
    name    = "Chain Reaction",
    tagline = "One system's output feeds directly into the next, and the outcome multiplies.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "One system's output feeding directly into the next multiplies the outcome well past what was planned.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### STD.MOD.56 — COMPLIANCE CERTIFICATE

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` matrix. Same self-resolution basis as STD.MOD.32 — no target dependency.

#### Card Story
A stamp of approval becomes a small, visible standing win.

**Design checklist:** Same disposition as STD.MOD.32.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Compliance-certification fits Mid register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.56 = Card(
    id      = "STD.MOD.56",  card_id = "STD.MOD.56",  version = "v0.1",
    name    = "Compliance Certificate",
    tagline = "A stamp of approval, small but visible.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A stamp of approval becomes a small, visible standing win.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### STD.MOD.57 — MODEL FACILITY

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same basis as STD.MOD.56, doubled magnitude.

#### Card Story
The acting faction's operation is cited publicly as a model of efficient operation — a real standing win.

**Design checklist:** Same disposition as STD.MOD.56.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.56. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.57 = Card(
    id      = "STD.MOD.57",  card_id = "STD.MOD.57",  version = "v0.1",
    name    = "Model Facility",
    tagline = "The operation gets cited publicly as an example of how it's supposed to run.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The acting faction's operation is cited publicly as a model of efficient operation — a real standing win.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### STD.MOD.58 — DELAY LOGGED

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.34 — resolves via host pairing, not an independent field.

#### Card Story
A minor procedural delay on a rival's shipment gets logged in the public record — small, but on the record.

**Design checklist:** Same disposition as STD.MOD.34.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Mid basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.58 = Card(
    id      = "STD.MOD.58",  card_id = "STD.MOD.58",  version = "v0.1",
    name    = "Delay Logged",
    tagline = "A minor procedural delay, logged where the public record can find it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A minor procedural delay on a rival's shipment gets logged in the public record — small, but on the record.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — the host it's packet-paired with at Dispatch.",
)
```

---

### STD.MOD.59 — SAFETY CITATION

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.58 (resolves via host pairing, not an independent field), doubled magnitude.

#### Card Story
A public safety violation becomes standing damage for whoever's named on the citation.

**Design checklist:** Same disposition as STD.MOD.58.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.58. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.59 = Card(
    id      = "STD.MOD.59",  card_id = "STD.MOD.59",  version = "v0.1",
    name    = "Safety Citation",
    tagline = "A public safety violation, and the paperwork has a name attached.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A public safety violation becomes standing damage for whoever's named on the citation.",
    arbiter_note = "Same target-resolution behavior as STD.MOD.58, major tier.",
)
```

---

### STD.MOD.60 — PRIORITY ROUTING

#### Design Rationale
Common tier (n=1) of the `cost_reduction` pair, PA-only per §6.3. Same procedural basis as STD.MOD.36.

#### Card Story
The acting faction's submission is rerouted to the front of a queue, skipping delay-related overhead.

**Design checklist:** Same disposition as STD.MOD.36.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.36. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.60 = Card(
    id      = "STD.MOD.60",  card_id = "STD.MOD.60",  version = "v0.1",
    name    = "Priority Routing",
    tagline = "The submission gets rerouted to the front of the queue.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The acting faction's submission is rerouted to the front of a queue, skipping delay-related overhead.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.61 — BULK RATE

#### Design Rationale
Capstone tier (n=2) of the `cost_reduction` pair. Same flat-vs-proportional caveat as STD.MOD.37. Closes Ring 2's Portable set (12 cards).

#### Card Story
A resource purchase clears at an institutional discount not normally available.

**Design checklist:** Same disposition as STD.MOD.37.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.37. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost — same unresolved question as STD.MOD.37. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=2` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.61 = Card(
    id      = "STD.MOD.61",  card_id = "STD.MOD.61",  version = "v0.1",
    name    = "Bulk Rate",
    tagline = "An institutional discount that isn't normally on offer.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — closes Ring 2's Portable 12-card set
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A resource purchase clears at an institutional discount not normally available.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 2's Portable set (STD.MOD.50–61); Ring-Locked set follows (STD.MOD.62–73).",
)
```

---

### STD.MOD.62 — DOCK FAMILIARITY

#### Design Rationale
Ring-Locked set opens for Ring 2 — invented fresh (Portable set used all 4 seed threshold_delta concepts). Same structure as STD.MOD.38, minor tier.

#### Card Story
Regular business at this specific freight dock eases a logistics-dependent action there — but only there.

**Design checklist:** Same disposition as STD.MOD.38.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-anchored logistics fits Ring-Locked Mid framing. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.62 = Card(
    id      = "STD.MOD.62",  card_id = "STD.MOD.62",  version = "v0.1",
    name    = "Dock Familiarity",
    tagline = "Regular business at this specific freight dock smooths the paperwork every time.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Regular business at this specific freight dock eases a logistics-dependent action there — but only there.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.63 — GRID RAPPORT

#### Design Rationale
Mid tier (+10). Same structure as STD.MOD.62/39.

#### Card Story
A standing relationship with substation staff eases an infrastructure-dependent action — within their lines only.

**Design checklist:** Same disposition as STD.MOD.39.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.63 = Card(
    id      = "STD.MOD.63",  card_id = "STD.MOD.63",  version = "v0.1",
    name    = "Grid Rapport",
    tagline = "A standing relationship with substation staff eases anything running through their lines.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A standing relationship with substation staff eases an infrastructure-dependent action — within their lines only.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.64 — LINE ACCESS

#### Design Rationale
Third tier (+15). Same structure as STD.MOD.63, never a hostile reframe (invented fresh, like STD.MOD.40).

#### Card Story
Priority access at a specific communications hub smooths a relay-dependent action — but only through that hub.

**Design checklist:** Same disposition as STD.MOD.40.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.64 = Card(
    id      = "STD.MOD.64",  card_id = "STD.MOD.64",  version = "v0.1",
    name    = "Line Access",
    tagline = "Priority access to a specific relay hub, open only from inside its footprint.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Priority access at a specific communications hub smooths a relay-dependent action — but only through that hub.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.65 — FULL PROCESSING RIGHTS

#### Design Rationale
Capstone tier (+20). Clean self-only narrative throughout, same as STD.MOD.41.

#### Card Story
Full standing at the district clearinghouse means paperwork simply moves, no matter the action — so long as it moves through here.

**Design checklist:** Same disposition as STD.MOD.41.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, +20 unvalidated (04-n157). | PM02 L258, L259, L261; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event, self-only clean. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (+20 playtest flag) |  |

```python
STD.MOD.65 = Card(
    id      = "STD.MOD.65",  card_id = "STD.MOD.65",  version = "v0.1",
    name    = "Full Processing Rights",
    tagline = "Full standing at the district clearinghouse — paperwork simply moves.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Full standing at the district clearinghouse means paperwork simply moves, no matter the action — so long as it moves through here.",
    arbiter_note = "Capstone tier, usable only with an operation targeting a Ring 2 district — log actual play outcomes before treating +20 as balanced (04-n157).",
)
```

---

### STD.MOD.66 — OVERTIME CREW

#### Design Rationale
Common tier (n=1) of the Ring-Locked `success_multiplier` pair. Same self-only basis as STD.MOD.54/42.

#### Card Story
An extra shift pushes a build further than scheduled, amplifying its result — a local crew, working local hours.

**Design checklist:** Same disposition as STD.MOD.42.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-specific labor fits Ring-Locked framing. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.66 = Card(
    id      = "STD.MOD.66",  card_id = "STD.MOD.66",  version = "v0.1",
    name    = "Overtime Crew",
    tagline = "An extra shift pushes the build further than scheduled.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An extra shift pushes a build further than scheduled, amplifying its result — a local crew, working local hours.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.67 — FULL UTILIZATION

#### Design Rationale
Capstone tier (n=2). Same unvalidated-magnitude caveat as STD.MOD.43.

#### Card Story
A facility running at capacity turns a routine action into an exceptional one — but only this facility, running this way.

**Design checklist:** Same disposition as STD.MOD.43.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated. | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.67 = Card(
    id      = "STD.MOD.67",  card_id = "STD.MOD.67",  version = "v0.1",
    name    = "Full Utilization",
    tagline = "A facility running at full capacity turns a routine action into an exceptional one.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A facility running at capacity turns a routine action into an exceptional one — but only this facility, running this way.",
    arbiter_note = "Rare/capstone tier, usable only with an operation targeting a Ring 2 district — log actual play outcomes before treating n=2 as balanced (04-n157).",
)
```

---

### STD.MOD.68 — FILED UNDER ROUTINE

#### Design Rationale
Self-boost minor tier (+1) of the Ring-Locked `ps_shift` matrix. Same self-resolution basis as STD.MOD.44.

#### Card Story
A genuinely significant action is buried among routine paperwork, muting any standing consequence either way — a small protective boost.

**Design checklist:** Same disposition as STD.MOD.44.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.68 = Card(
    id      = "STD.MOD.68",  card_id = "STD.MOD.68",  version = "v0.1",
    name    = "Filed Under Routine",
    tagline = "A genuinely significant action, buried among routine paperwork at this specific office.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A genuinely significant action is buried among routine paperwork, muting any standing consequence either way — a small protective boost.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction. Usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.69 — RELIABILITY COMMENDATION

#### Design Rationale
Self-boost major tier (+2) of the Ring-Locked `ps_shift` matrix — same basis as STD.MOD.68, doubled magnitude.

#### Card Story
A public commendation for keeping the Mid's infrastructure running is a real, visible standing win.

**Design checklist:** Same disposition as STD.MOD.68.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.68. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.69 = Card(
    id      = "STD.MOD.69",  card_id = "STD.MOD.69",  version = "v0.1",
    name    = "Reliability Commendation",
    tagline = "A public commendation for keeping this specific facility running without a hitch.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A public commendation for keeping the Mid's infrastructure running is a real, visible standing win.",
    arbiter_note = "Self-boost, major tier, resolves to the acting faction — usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.70 — OVERDRAWN ACCOUNT EXPOSED

#### Design Rationale
Target-hinder minor tier (−1) of the Ring-Locked `ps_shift` matrix. Same target-resolution behavior as STD.MOD.58/34 — resolves via host pairing, not an independent field.

#### Card Story
A rival's resource draw becomes public knowledge at this specific institution — a small cost to their standing.

**Design checklist:** Same disposition as STD.MOD.58.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.70 = Card(
    id      = "STD.MOD.70",  card_id = "STD.MOD.70",  version = "v0.1",
    name    = "Overdrawn Account Exposed",
    tagline = "A rival's resource draw becomes public knowledge, at this specific institution.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A rival's resource draw becomes public knowledge at this specific institution — a small cost to their standing.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.71 — PUBLIC SANCTION

#### Design Rationale
Target-hinder major tier (−2) of the Ring-Locked `ps_shift` matrix. Same target-resolution behavior as STD.MOD.70 (resolves via host pairing, not an independent field), doubled magnitude.

#### Card Story
A named rival is formally sanctioned at this institution — visible to every faction that does business through it.

**Design checklist:** Same disposition as STD.MOD.70.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.70. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.71 = Card(
    id      = "STD.MOD.71",  card_id = "STD.MOD.71",  version = "v0.1",
    name    = "Public Sanction",
    tagline = "A formal sanction, posted where every faction doing business here will see it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A named rival is formally sanctioned at this institution — visible to every faction that does business through it.",
    arbiter_note = "Same target-resolution behavior as STD.MOD.70, major tier — usable only with an operation targeting a Ring 2 district.",
)
```

---

### STD.MOD.72 — CONSIGNMENT HOLD RELEASED

#### Design Rationale
Common tier (n=1) of the Ring-Locked `cost_reduction` pair, PA-only per §6.3. Same procedural basis as STD.MOD.60/48.

#### Card Story
A shipment already in the system is released without the fee a fresh order would carry — this system specifically.

**Design checklist:** Same disposition as STD.MOD.48.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.48. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.72 = Card(
    id      = "STD.MOD.72",  card_id = "STD.MOD.72",  version = "v0.1",
    name    = "Consignment Hold Released",
    tagline = "A shipment already in the system clears without the fee a fresh order would carry.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = 2,
    ring_origin     = 2,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A shipment already in the system is released without the fee a fresh order would carry — this system specifically.",
    arbiter_note = "PA host only, usable only with a PA targeting a Ring 2 district. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.73 — STANDING UTILITY CONTRACT

#### Design Rationale
Capstone tier (n=2) of the Ring-Locked `cost_reduction` pair. Same flat-vs-proportional caveat as STD.MOD.61/49. Closes Ring 2's 24-card Ring ModAction set.

#### Card Story
An existing utility contract absorbs the overhead of a fresh submission — but only at this specific facility.

**Design checklist:** Same disposition as STD.MOD.49.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.49. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=2` correctly restricts to Ring 2-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.73 = Card(
    id      = "STD.MOD.73",  card_id = "STD.MOD.73",  version = "v0.1",
    name    = "Standing Utility Contract",
    tagline = "An existing service agreement makes this considerably cheaper to mount.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = 2,      # Ring-Locked set — closes Ring 2's 24-card set (Portable + Ring-Locked)
    ring_origin     = 2,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed
    cost            = None,

    portrait     = None,
    narrative    = "An existing service agreement lowers what this action costs to mount — through this specific utility, and no other.",
    arbiter_note = "Capstone cost_reduction tier, usable only with a PA targeting a Ring 2 district — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 2 (STD.MOD.50–73, 24 cards); Ring 3 (Baryo) follows.",
)
```

---

### STD.MOD.74 — SQUATTER'S CLAIM

#### Design Rationale
Ring 3 (Baryo) Portable set opens — same format as Rings 1–2, minor threshold_delta tier (+5). Voice per Art 00 §6.7: gray economy and community network, distinct from Ghost's epistemic doctrine and Rings 1–2's institutional/infrastructure lean.

#### Card Story
An informally occupied space becomes easier to formalize into a real presence claim.

**Design checklist:** Same disposition as STD.MOD.26/50 (identical mechanic/tier). Narrative independently checked — clean self-only, correctly Baryo-flavored (informal claim, not paperwork/reclassification).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Informal-economy claim-staking fits Baryo's gray-economy/community register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as STD.MOD.26. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.74 = Card(
    id      = "STD.MOD.74",  card_id = "STD.MOD.74",  version = "v0.1",
    name    = "Squatter's Claim",
    tagline = "An informally occupied space becomes a real claim, on paper, without a fight.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only — no faction param on this variant (§6.3). Tracked at PM05 04-n170; remove this comment once resolved.
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An informally occupied space becomes easier to formalize into a real presence claim.",
    arbiter_note = "Attach at Dispatch to any CA/PA in the holder's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### STD.MOD.75 — LANDLORD'S BLESSING

#### Design Rationale
Mid tier (+10). Same structure as STD.MOD.74, self-only.

#### Card Story
Backing from one of Baryo's unofficial housing authorities smooths a placement nobody easily challenges.

**Design checklist:** Same disposition as STD.MOD.74. Narrative independently checked — clean self-only.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Baryo basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.75 = Card(
    id      = "STD.MOD.75",  card_id = "STD.MOD.75",  version = "v0.1",
    name    = "Landlord's Blessing",
    tagline = "One of Baryo's unofficial housing authorities backs the placement, and nobody easily challenges it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Backing from one of Baryo's unofficial housing authorities smooths a placement nobody easily challenges.",
    arbiter_note = "Self-only, same basis as STD.MOD.74.",
)
```

---

### STD.MOD.76 — DOCK CONTACTS

#### Design Rationale
Third tier (+15). Reframed from "Word on the Docks" (hostile) per 04-n170, same self-only correction as STD.MOD.28/52.

#### Card Story
Advance word from contacts at the docks smooths the acting faction's own shipment-dependent operation.

**Design checklist:** Same disposition as STD.MOD.52. Narrative independently checked — clean, "acting faction's own" correctly scopes the effect.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Baryo basis. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only reframe. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.76 = Card(
    id      = "STD.MOD.76",  card_id = "STD.MOD.76",  version = "v0.1",
    name    = "Dock Contacts",
    tagline = "Advance word from the right people at the docks smooths the whole operation.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Advance word from contacts at the docks smooths the acting faction's own shipment-dependent operation.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as STD.MOD.28/29/52/53.",
)
```

---

### STD.MOD.77 — NEIGHBORHOOD BACKING

#### Design Rationale
Capstone tier (+20). Reframed from "Petition Drive" (hostile) per 04-n170. Clean self-only narrative throughout — "the acting faction's own submission" and "the neighborhood's already decided" correctly scope the effect, no dual-purpose residue.

#### Card Story
Visible grassroots support for the acting faction's own submission smooths its passage — the neighborhood's already decided.

**Design checklist:** Same disposition as STD.MOD.53/29 except narrative is clean (verified independently).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Baryo basis. | Art 00 §6.7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only, no dual-purpose framing (contrast STD.MOD.29). | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, +20 unvalidated (04-n157). | PM02 L258, L259, L261; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.77 = Card(
    id      = "STD.MOD.77",  card_id = "STD.MOD.77",  version = "v0.1",
    name    = "Neighborhood Backing",
    tagline = "Visible grassroots support smooths the way — nobody's raising a petition against this one.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Visible grassroots support for the acting faction's own submission smooths its passage — the neighborhood's already decided.",
    arbiter_note = "Capstone tier, reframed per 04-n170 — log actual play outcomes before treating +20 as balanced (04-n157).",
)
```

---

### STD.MOD.78 — COMMUNITY POOL

#### Design Rationale
Common tier (n=1) of the `success_multiplier` pair. Same self-only basis as STD.MOD.30/54.

#### Card Story
Several small contributions combine into an outcome larger than any single source could produce.

**Design checklist:** Same disposition as STD.MOD.30.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pooled-resource concept fits Baryo's community register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.78 = Card(
    id      = "STD.MOD.78",  card_id = "STD.MOD.78",  version = "v0.1",
    name    = "Community Pool",
    tagline = "Several small contributions combine into more than any one source could produce.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Several small contributions combine into an outcome larger than any single source could produce.",
    arbiter_note = "Self-only, amplifies the holder's own host action.",
)
```

---

### STD.MOD.79 — PACKED HOUSE

#### Design Rationale
Capstone tier (n=2). Same unvalidated-magnitude caveat as STD.MOD.31/55.

#### Card Story
An unusually large crowd amplifies whatever the action was counting on being seen.

**Design checklist:** Same disposition as STD.MOD.31.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Baryo basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated. | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.79 = Card(
    id      = "STD.MOD.79",  card_id = "STD.MOD.79",  version = "v0.1",
    name    = "Packed House",
    tagline = "An unusually large crowd amplifies whatever this was counting on being seen.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An unusually large crowd amplifies whatever the action was counting on being seen.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### STD.MOD.80 — STREET REPUTATION

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` matrix. Same self-resolution basis as STD.MOD.32/56 — no target dependency.

#### Card Story
Word of mouth shifts standing faster than any official channel — a small, organic boost.

**Design checklist:** Same disposition as STD.MOD.32.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Word-of-mouth fits Baryo's community register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.80 = Card(
    id      = "STD.MOD.80",  card_id = "STD.MOD.80",  version = "v0.1",
    name    = "Street Reputation",
    tagline = "Word of mouth moves faster than any official channel ever could.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Word of mouth shifts standing faster than any official channel — a small, organic boost.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### STD.MOD.81 — NEIGHBORHOOD VOUCHING

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same basis as STD.MOD.80, doubled magnitude.

#### Card Story
The neighborhood vouches for the acting faction publicly — a real and visible standing win.

**Design checklist:** Same disposition as STD.MOD.80.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.80. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.81 = Card(
    id      = "STD.MOD.81",  card_id = "STD.MOD.81",  version = "v0.1",
    name    = "Neighborhood Vouching",
    tagline = "The whole block vouches for it, publicly and without being asked twice.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "The neighborhood vouches for the acting faction publicly — a real and visible standing win.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### STD.MOD.82 — BUSKER'S TIP

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.34 — resolves via host pairing, not an independent field.

#### Card Story
A street performer's aside becomes the detail that costs a named faction a little standing.

**Design checklist:** Same disposition as STD.MOD.34.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same Baryo basis. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.82 = Card(
    id      = "STD.MOD.82",  card_id = "STD.MOD.82",  version = "v0.1",
    name    = "Busker's Tip",
    tagline = "A street performer's aside becomes the detail somebody has to answer for.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A street performer's aside becomes the detail that costs a named faction a little standing.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — the host it's packet-paired with at Dispatch.",
)
```

---

### STD.MOD.83 — OVERHEARD AT THE STRIP

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.82 (resolves via host pairing, not an independent field), doubled magnitude.

#### Card Story
A casual conversation becomes something a rival has to publicly answer for — the Strip doesn't forget what it hears.

**Design checklist:** Same disposition as STD.MOD.82.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.82. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.83 = Card(
    id      = "STD.MOD.83",  card_id = "STD.MOD.83",  version = "v0.1",
    name    = "Overheard at the Strip",
    tagline = "A casual conversation becomes something a rival has to publicly answer for.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A casual conversation becomes something a rival has to publicly answer for — the Strip doesn't forget what it hears.",
    arbiter_note = "Same target-resolution behavior as STD.MOD.82, major tier.",
)
```

---

### STD.MOD.84 — CREDIT WITH THE VENDOR

#### Design Rationale
Common tier (n=1) of the `cost_reduction` pair, PA-only per §6.3. Same procedural basis as STD.MOD.36/60.

#### Card Story
Informal credit lets an action proceed before payment technically clears.

**Design checklist:** Same disposition as STD.MOD.36.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Informal-credit economy fits Baryo register. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.84 = Card(
    id      = "STD.MOD.84",  card_id = "STD.MOD.84",  version = "v0.1",
    name    = "Credit with the Vendor",
    tagline = "Informal credit lets this proceed before payment technically clears.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Informal credit lets an action proceed before payment technically clears.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.85 — BARTER CHAIN

#### Design Rationale
Capstone tier (n=2) of the `cost_reduction` pair. Same flat-vs-proportional caveat as STD.MOD.37/61. Closes Ring 3's Portable set (12 cards).

#### Card Story
A resource moves through several informal trades before landing where it was always headed, cheaper than a direct purchase.

**Design checklist:** Same disposition as STD.MOD.37.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.37. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=3` correct for Portable. | Art 01 §6–§7 |
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

```python
STD.MOD.85 = Card(
    id      = "STD.MOD.85",  card_id = "STD.MOD.85",  version = "v0.1",
    name    = "Barter Chain",
    tagline = "The resource moves through several informal trades before landing exactly where it was always headed.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,   # Portable set — closes Ring 3's Portable 12-card set
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A resource moves through several informal trades before landing where it was always headed, cheaper than a direct purchase.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 3's Portable set (STD.MOD.74–85); Ring-Locked set follows (STD.MOD.86–97).",
)
```

---

### STD.MOD.86 — REGULAR CUSTOMER

#### Design Rationale
Ring-Locked set opens for Ring 3 — invented fresh (Portable set used all 4 seed threshold_delta concepts). Same structure as STD.MOD.38/62, minor tier.

#### Card Story
Being a known face at a specific market stall eases an economy-dependent action there — but only there.

**Design checklist:** Same disposition as STD.MOD.38/62.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-anchored market familiarity fits Ring-Locked Baryo framing. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.86 = Card(
    id      = "STD.MOD.86",  card_id = "STD.MOD.86",  version = "v0.1",
    name    = "Regular Customer",
    tagline = "Being a known face at this specific stall smooths business there, every time.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Being a known face at a specific market stall eases an economy-dependent action there — but only there.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.87 — ROUTE KNOWLEDGE

#### Design Rationale
Mid tier (+10). Same structure as STD.MOD.86/39/63.

#### Card Story
Knowing exactly how a specific transit point actually runs eases an operation passing through it — knowledge that doesn't travel elsewhere.

**Design checklist:** Same disposition as STD.MOD.39.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.87 = Card(
    id      = "STD.MOD.87",  card_id = "STD.MOD.87",  version = "v0.1",
    name    = "Route Knowledge",
    tagline = "Knowing exactly how this transit point actually runs eases anything passing through it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Knowing exactly how a specific transit point actually runs eases an operation passing through it — knowledge that doesn't travel elsewhere.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.88 — NEIGHBORHOOD STANDING

#### Design Rationale
Third tier (+15). Same structure as STD.MOD.87, never a hostile reframe (invented fresh).

#### Card Story
Established standing in a specific housing block smooths a placement there — standing that doesn't extend past the block.

**Design checklist:** Same disposition as STD.MOD.40/64.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.88 = Card(
    id      = "STD.MOD.88",  card_id = "STD.MOD.88",  version = "v0.1",
    name    = "Neighborhood Standing",
    tagline = "Established standing in this specific block smooths a placement nobody here would challenge.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Established standing in a specific housing block smooths a placement there — standing that doesn't extend past the block.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.89 — LOCAL FIXTURE

#### Design Rationale
Capstone tier (+20). Clean self-only narrative throughout, closes Ring 3's threshold_delta progression.

#### Card Story
Being a fixture at this specific spot means nothing about an operation there needs explaining or clearing — but the standing doesn't travel.

**Design checklist:** Same disposition as STD.MOD.41/65.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, +20 unvalidated (04-n157). | PM02 L258, L259, L261; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event, self-only clean. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (+20 playtest flag) |  |

```python
STD.MOD.89 = Card(
    id      = "STD.MOD.89",  card_id = "STD.MOD.89",  version = "v0.1",
    name    = "Local Fixture",
    tagline = "Being a fixture here means nothing about this operation needs explaining.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Being a fixture at this specific spot means nothing about an operation there needs explaining or clearing — but the standing doesn't travel.",
    arbiter_note = "Capstone tier, usable only with an operation targeting a Ring 3 district — log actual play outcomes before treating +20 as balanced (04-n157). Closes Ring 3's threshold_delta tier progression.",
)
```

---

### STD.MOD.90 — FESTIVAL GROUNDS

#### Design Rationale
Common tier (n=1) of the Ring-Locked `success_multiplier` pair. Same self-only basis as STD.MOD.78/54/42.

#### Card Story
A temporary permit becomes cover for something that lands bigger than expected — but only on these grounds.

**Design checklist:** Same disposition as STD.MOD.42/66.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Location-specific event cover fits Ring-Locked framing. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.90 = Card(
    id      = "STD.MOD.90",  card_id = "STD.MOD.90",  version = "v0.1",
    name    = "Festival Grounds",
    tagline = "A temporary permit becomes cover for something that lands bigger than expected.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A temporary permit becomes cover for something that lands bigger than expected — but only on these grounds.",
    arbiter_note = "Self-only; usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.91 — WORD SPREADS FAST

#### Design Rationale
Capstone tier (n=2). Same unvalidated-magnitude caveat as STD.MOD.79/43/67.

#### Card Story
Informal networks carry an outcome further than any official channel would — but only within this network's reach.

**Design checklist:** Same disposition as STD.MOD.43/67.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated. | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.91 = Card(
    id      = "STD.MOD.91",  card_id = "STD.MOD.91",  version = "v0.1",
    name    = "Word Spreads Fast",
    tagline = "Informal networks carry the outcome further than any official channel would.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Informal networks carry an outcome further than any official channel would — but only within this network's reach.",
    arbiter_note = "Rare/capstone tier, usable only with an operation targeting a Ring 3 district — log actual play outcomes before treating n=2 as balanced (04-n157).",
)
```

---

### STD.MOD.92 — QUIET WORD TO THE CROWD

#### Design Rationale
Self-boost minor tier (+1) of the Ring-Locked `ps_shift` matrix. Same self-resolution basis as STD.MOD.80/68/44.

#### Card Story
A rumor seeded in a local gathering changes how an outcome is read — protecting the acting faction's standing, quietly.

**Design checklist:** Same disposition as STD.MOD.44/68.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.92 = Card(
    id      = "STD.MOD.92",  card_id = "STD.MOD.92",  version = "v0.1",
    name    = "Quiet Word to the Crowd",
    tagline = "A rumor seeded in a gathering, shaping how the outcome gets read locally.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A rumor seeded in a local gathering changes how an outcome is read — protecting the acting faction's standing, quietly.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction. Usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.93 — BLOCK PARTY

#### Design Rationale
Self-boost major tier (+2) of the Ring-Locked `ps_shift` matrix — same basis as STD.MOD.92, doubled magnitude.

#### Card Story
A genuinely celebrated local event puts the acting faction's name in a good light, visibly and specifically here.

**Design checklist:** Same disposition as STD.MOD.92.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.92. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.93 = Card(
    id      = "STD.MOD.93",  card_id = "STD.MOD.93",  version = "v0.1",
    name    = "Block Party",
    tagline = "A genuinely celebrated local event, and the acting faction's name is all over it.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A genuinely celebrated local event puts the acting faction's name in a good light, visibly and specifically here.",
    arbiter_note = "Self-boost, major tier, resolves to the acting faction — usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.94 — QUIET WORD AGAINST THEM

#### Design Rationale
Target-hinder minor tier (−1) of the Ring-Locked `ps_shift` matrix. Same target-resolution behavior as STD.MOD.82/58/34 — resolves via host pairing, not an independent field.

#### Card Story
A passing comment at the market costs a named faction a little standing — nothing traceable, nothing worth a formal answer.

**Design checklist:** Same disposition as STD.MOD.82.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier; `value_rating=1` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.94 = Card(
    id      = "STD.MOD.94",  card_id = "STD.MOD.94",  version = "v0.1",
    name    = "Quiet Word Against Them",
    tagline = "A passing comment at the market costs a named faction a little standing, locally.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A passing comment at the market costs a named faction a little standing — nothing traceable, nothing worth a formal answer.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.95 — TURNED AWAY

#### Design Rationale
Target-hinder major tier (−2) of the Ring-Locked `ps_shift` matrix. Same target-resolution behavior as STD.MOD.94 (resolves via host pairing, not an independent field), doubled magnitude. Closes Ring 3's `ps_shift` matrix and, with it, all 12 target-hinder ModActionCards in the 72-card Ring corpus (2 per set × 6 sets); the remaining 10 (Ring: 12, Faction: 10) are in the 5 faction sets, not yet reached.

#### Card Story
A named faction is visibly turned away at this specific spot — a real, public cost to standing that the whole block sees.

**Design checklist:** Same disposition as STD.MOD.94.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.94. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier; `value_rating=2` mirrors tier. | PM02 L257, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

```python
STD.MOD.95 = Card(
    id      = "STD.MOD.95",  card_id = "STD.MOD.95",  version = "v0.1",
    name    = "Turned Away",
    tagline = "A named faction is visibly denied service, right where everyone can see it happen.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A named faction is visibly turned away at this specific spot — a real, public cost to standing that the whole block sees.",
    arbiter_note = "Same target-resolution constraint as STD.MOD.94, major tier — usable only with an operation targeting a Ring 3 district.",
)
```

---

### STD.MOD.96 — SCRAP VALUE

#### Design Rationale
Common tier (n=1) of the Ring-Locked `cost_reduction` pair, PA-only per §6.3. Same procedural basis as STD.MOD.84/72/60/48/36.

#### Card Story
Discarded materials from the Mid get reused at a fraction of fresh cost — but only through this specific yard.

**Design checklist:** Same disposition as STD.MOD.48/72.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259, L261 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.96 = Card(
    id      = "STD.MOD.96",  card_id = "STD.MOD.96",  version = "v0.1",
    name    = "Scrap Value",
    tagline = "Discarded materials get reused at a fraction of fresh cost.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = 3,
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Discarded materials from the Mid get reused at a fraction of fresh cost — but only through this specific yard.",
    arbiter_note = "PA host only, usable only with a PA targeting a Ring 3 district. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### STD.MOD.97 — FAVOR OWED

#### Design Rationale
Capstone tier (n=2) of the Ring-Locked `cost_reduction` pair. Same flat-vs-proportional caveat as STD.MOD.85/73/61/49. Closes Ring 3's 24-card set — and, with it, the full 72-card Ring ModActionCard corpus (STD.MOD.26–97).

#### Card Story
A debt called in from the informal economy waives part of what an action would otherwise cost — this economy specifically, no other.

**Design checklist:** Same disposition as STD.MOD.49/73.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as tier. | Art 00 §6.7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost — same unresolved question across all 6 cost_reduction capstones in the Ring set. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=3` correctly restricts to Ring 3-targeting hosts. | Art 01 §6–§7; Art 04 §6.2 |
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

```python
STD.MOD.97 = Card(
    id      = "STD.MOD.97",  card_id = "STD.MOD.97",  version = "v0.1",
    name    = "Favor Owed",
    tagline = "A debt from the informal economy, called in to cover part of the cost.",
    type    = ModActionCard,  subtype = Standard,  faction = All,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = 3,      # Ring-Locked set — closes Ring 3's 24-card set and the full 72-card Ring ModAction stub pass
    ring_origin     = 3,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A debt called in from the informal economy waives part of what an action would otherwise cost — this economy specifically, no other.",
    arbiter_note = "Capstone cost_reduction tier, usable only with a PA targeting a Ring 3 district — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Closes Ring 3 (STD.MOD.74–97, 24 cards) and the full Ring ModAction stub pass (72 cards, STD.MOD.26–97) — 09-06's ModActionCard leg now fully complete, faction-set and ring-set alike.",
)
```

---

### STD.MOD.98 — NOTIFIED OF ENCROACHMENT

#### Design Rationale
Ring 1 ModReactCard pattern-setter (04-53/09-06) — establishes that Ring Modifier ModReactCard content carries real trigger + Layer/Function/Subject the same way faction ModReactCards do, but is available to whoever holds the card rather than doctrinally locked. Mechanically mirrors DIR.MOD.7 Eminent Domain's flat single-chip yield, but fires off a rival's move instead of the holder's own action — a competitive echo, not an initiative. Deliberately the weakest tier (value_rating 1, single chip) — Ring ModReact power is meant to sit at or below faction-specific equivalents.

#### Card Story
A rival stakes a new claim in Core. Whoever's holding this card gets word fast enough to stake one too — not because they did anything, just because they were already watching that address.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Reactive claim-staking against a rival's move is a grounded competitive dynamic for a contested Ring; matches 04-53's "available to whoever holds it" intent. | Art 00 §7; 04-53 |
| Voice fit | ✓ | `narrative` reads in Core's institutional/proximity register. `perspectives=None` — live/per-card field for ModReactCard (§6.2), not blanket-None; whether faction-differentiated perspective text is warranted on identical-effect Standard cards is an open convention question, not a Voice fit failure. | Art 00 §6.7, §9 |
| Doctrine alignment | ✓ | No `target_faction` — card doesn't act against a named rival, so `doctrine_mod=None` is trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Standard/faction=All with real taxonomy — correctly classified per §6.1; available to any holder, distinct from Ghost's faction-locked presence-triggered cards. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Independently verified against `ref_taxonomy.md`: Presence token's listed Layer is Territory; Layer×Function validity matrix (§5.1) confirms Territory×Add is valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort, pre-Art 00c) | value_rating 1, single chip, cost=None — at/below faction-specific power by design. Magnitude playtest-flagged like the rest of the set (04-n94). | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — fully resolved at trigger, no multi-Quarter temporary. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Field absent from spec. §6.2 lists persistence as live/per-card for ModReactCard, not None — but whether Immediate should be an explicit line or an implicit default for fire-and-consume cards is an open schema question (`schema_cleanup_log.md` #2), not resolved here. | Art 04 §6.2 |
| Trigger validity | ✓ | `presence_chip.placed(faction=opponent, ring=1)` — confirmed TriggerExpr vocabulary (§6.3), publicly observable board event. | Art 04 §6.3 |
| Portrait validity | ✓ | Principle 11: Portrait fires when an action *strongly* aligns/opposes doctrine; grey areas produce none. This card's action (automatic, reactive, 1-chip, identical for every holder) is doctrinally neutral logistics for all five factions — no faction's doctrine is meaningfully expressed by holding or playing it. Justified absence documented uniformly across all five per the Standard-card portrait convention; distinct from DIR.MOD.9-style cards where the action is a deliberate, doctrinally-loaded choice. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district`; ring context (`ring_constraint=1`, `ring_origin=1`) consistent. | Art 01 §6–7 |
| Supported by components | ✓ | Presence chip is an existing component; `arbiter.place()` reuses the standard placement mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Trigger and response both reuse already-defined ARBITER chip-placement behavior — no novel procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Missing `persistence`/`resolution_type` — see Persistence row above; logged in `schema_cleanup_log.md`, not hand-fixed here to avoid a partial-fix inconsistency ahead of that decision. All other fields present and correctly typed. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story states a concrete event (rival's chip placement → holder's matching claim); mechanic follows directly, no retrofit. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch, no `game.choose_one()`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — no resource cost to evaluate. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Presence-chip placement in Ring 1 is a common recurring event; effect is modest (1 chip) — not overfire either. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 ModReact card shares this exact trigger; STD.MOD.100 uses the removal side, not a race. (Cross-file collision against faction Ghost cards not checked — out of this batch's scope.) |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary reaction — no execution-quality dimension to model via roll. |  |
| Stack behavior (ModReactCard) | ⚠ | Undocumented: does holding two copies double-fire on one rival placement? No restriction clause present. Genuinely open. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=1` matches trigger scope; frequency supports a ring-locked card remaining playable. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.98 = Card(
    id      = "STD.MOD.98",  card_id = "STD.MOD.98",  version = "v0.1",
    name    = "Notified of Encroachment",
    tagline = "A quiet call from someone who watches the building next door.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Core doesn't miss a new arrival. Word reaches the right desk before the ink dries.",
    perspectives = None,
    design_note  = "Ring ModReactCard pattern-setter (04-53 direction). A rival's presence placement in Core is met with an immediate matching reinforcement from whoever holds this card. Deliberately modest (single-unit, at or below faction-specific power) — mirrors DIR.MOD.7 Eminent Domain's flat presence-yield template.",
    arbiter_note = None,
)
```

---

### STD.MOD.99 — STRUCTURAL OBJECTION

#### Design Rationale
Territory reaction that punishes a rival's structure placement rather than rewarding the holder's own position — the first punitive-shaped card in the Ring 1 set (98/100 are purely additive). Removes one presence chip from the triggering faction in the same district as their new structure: a bureaucratic cost layered on the structure, not a reversal of the placement itself (GR 7.2b — committed states are final; this is a new mutation, distinct from an undo).

#### Card Story
A rival pours concrete in Core. The paperwork that follows costs them a foothold elsewhere in the same district — not the structure itself, just the ground around it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic retaliation for structure placement is a grounded competitive dynamic; matches 04-53's holder-agnostic intent. | Art 00 §7; 04-53 |
| Voice fit | ✓ | `narrative` reads in Core's institutional register. Same open `perspectives=None` convention question as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction=trigger.faction` IS set here (genuinely adversarial, unlike 98/100) — `doctrine_mod=None` is still correctly justified: `resolution=Automatic`/`threshold=None` means there's no roll for a threshold modifier to adjust; `doctrine_mod` only has meaning on d100 cards. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — Territory×Remove confirmed valid in the Layer×Function matrix (§5.1). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | value_rating 2 — pricing model reads this above STD.MOD.98/100's tier despite the shared single-chip-removal shape; magnitude-mirror convention superseded for this card, single-chip removal, cost=None. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=X, ring=Z)` matches confirmed §6.3 signature exactly. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.98, explicitly weighed against the adversarial angle here (this removes a rival's chip, unlike 98/100's pure self-benefit) — narrative frames it as procedural/bureaucratic, magnitude is minor (1 chip), no faction's doctrine is strongly expressed by holding or playing it. Uniform absence, all five factions. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event, mechanic follows directly. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Structure placement in Ring 1 is a recurring but less frequent event than presence-chip placement — moderate frequency, not underfire. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded binary reaction, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98 — undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.99 = Card(
    id      = "STD.MOD.99",  card_id = "STD.MOD.99",  version = "v0.1",
    name    = "Structural Objection",
    tagline = "A formal complaint, filed the same afternoon the concrete sets.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Remove,  subject = PresenceToken,

    trigger         = structure_block.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 2,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Core paperwork moves fast when it wants to. An objection on record costs someone their footing.",
    perspectives = None,
    design_note  = "Removes 1 presence chip from the triggering faction in the same district as their new structure — a bureaucratic cost, not a reversal of the structure placement itself (GR 7.2b compliant).",
    arbiter_note = None,
)
```

---

### STD.MOD.100 — ESCORT WITHDRAWN

#### Design Rationale
Mirror image of STD.MOD.98 — same additive Territory reaction, opposite trigger direction (a rival's chip removed rather than placed). Together the pair covers both directions of Core presence flux.

#### Card Story
The building doesn't stay empty long. Core fills what's vacated before the news spreads.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.98, mirrored direction. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — same verified pairing as STD.MOD.98. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same modest tier as STD.MOD.98. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.removed(faction=opponent, ring=1)` — §6.3's confirmed signature for `.removed()` is `presence_chip.removed(faction=X, district=Y)`, district only; no `ring=` parameter is documented for `.removed()` the way it is for `.placed()`. Reasonable to assume symmetry, but not yet confirmed as written — flagging as a vocabulary-gap alongside the other §6.3 items, not a blocker. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.98 (exact mirror, no target_faction). | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same recurring frequency as STD.MOD.98's placement side. |  |
| Firing window (ModReactCard) | ✓ | No collision with STD.MOD.98 (opposite trigger direction). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.98. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.100 = Card(
    id      = "STD.MOD.100",  card_id = "STD.MOD.100",  version = "v0.1",
    name    = "Escort Withdrawn",
    tagline = "Someone else's retreat is Core's opening.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.removed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "The building doesn't stay empty long. Core fills what's vacated before the news spreads.",
    perspectives = None,
    design_note  = "Fires on any presence removal in Core; narrative frames it as claiming a vacated district. ARBITER confirms narrative fit case-by-case — no distinct 'last chip' filter exists in confirmed TriggerExpr vocabulary (04-n171).",
    arbiter_note = None,
)
```

---

### STD.MOD.101 — OVERHEARD IN THE COMMISSARY

#### Design Rationale
Information reaction to a rival locking down Dominant status in Core — worked through 3 rejected trigger candidates before landing here: Beat 0 `resolution_grid.updated` (covert, not publicly observable — contradicts the whole premise of a ModReactCard trigger); `world_event.played` (gated by the undesigned Broadcast Card taxonomy, XA-54); `deployment_marker` events (Upkeep-anchored only, too rare for a standard React). `dominant_marker.placed(faction=opponent, ring=1)` is the confirmed landing point — Dominant Marker changes through ordinary CA/PA resolution across the Quarter, genuinely public, and not yet used elsewhere in this set. Reward is an Intel Token on the triggering faction rather than the originally-proposed "draw 1 modifier card" — corrected for circularity (a modifier card's reward shouldn't itself be another modifier card with no thematic tie to "overheard information").

#### Card Story
Everyone in the building hears when someone finally locks the room down. Whoever's holding this card gets the story before it's officially announced.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A rival achieving Dominant status in Core is major public news — an information reaction naturally follows. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction=trigger.faction` set, but `doctrine_mod=None` correctly justified — Automatic/no threshold, same basis as STD.MOD.99. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — Information×Add confirmed valid in the Layer×Function matrix (§5.1). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | value_rating 1 — pricing model reads the Intel Token payload below STD.MOD.99/111/123's tier. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `dominant_marker.placed(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ⚠ | Not the same grey-area shape as 98–100: this card converts a rival's *public, doctrinally significant* milestone (Dominant status) into a private intelligence gain for the holder. Unlike the earlier cards' reflexive chip logistics, "capitalizing on overheard institutional information" reads as more deliberate — plausibly Portrait-relevant for at least Ghost (doctrine: understanding precedes action) if Ghost holds it. Genuinely uncertain rather than a settled absence — flagging rather than defaulting. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Intel Token is an existing component; `arbiter.deliver()` reuses the standard delivery mechanism (mirrors GHO.MOD.2 Perimeter Sensors' template, per design_note). | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Persistence/resolution_type deferred (same as STD.MOD.98, still open — schema_cleanup_log #41). `faction(holder)` (used here as a Faction-object receiver passed positionally to `arbiter.deliver()`, mirroring Overture's established `faction(acting)` pattern) is now confirmed §6.3 MutationExpr vocabulary. | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Dominant status changes are infrequent relative to chip placement, but Dominant is a genuinely significant milestone each time — value_rating 2 reflects the lower frequency / higher stakes balance. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope; frequency (infrequent but real) supports remaining ring-locked. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.101 = Card(
    id      = "STD.MOD.101",  card_id = "STD.MOD.101",  version = "v0.1",
    name    = "Overheard in the Commissary",
    tagline = "Everyone in the building hears when someone finally locks the room down.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Information,  function = Add,  subject = IntelToken,

    trigger         = dominant_marker.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.deliver(faction(holder), IntelToken(faction=trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Dominance in Core isn't quiet. The commissary knows before the announcement is official.",
    perspectives = None,
    design_note  = "Mirrors GHO.MOD.2 Perimeter Sensors' Intel Token delivery template. Reward changed from an initial 'draw 1 modifier card' (circular — a modifier card's reward shouldn't itself be another modifier card, with no thematic tie to 'overheard information') — Intel Token on the triggering faction ties the reward to what the card is actually about.",
    arbiter_note = None,
)
```

---

### STD.MOD.102 — ACCESS LOG PULLED

#### Design Rationale
Information reaction: any Accord forming anywhere passes through institutional record-keeping Core has a hand in — deliberately not ring-scoped, since triggers don't need to be ring-scoped and Accords aren't a ring-dimensioned component to begin with. "Core flavor" comes from doctrine/theme (institutional paperwork), not a mechanical filter.

#### Card Story
An Accord anywhere in the city passes through institutional record-keeping. Core's clerks note who's tied to whom.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional paperwork tracking Accords anywhere in the city is a grounded Core-flavored premise even without ring-scoping the trigger itself. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Per 04-n173: `layer=Standing, function=Shift` — the effect (`faction(holder).standing.add(1)`) mutates the Standing track directly, and the matrix marks Standing×Add as invalid ("subsumed by Shift"). Unified with STD.MOD.107/108/109 (were `Standing/Add`, also corrected) rather than the reverse — same fix across all 12 cards in this shape. | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | value_rating 1, +1 PS, cost=None — modest, consistent with the set's floor tier. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.placed(faction=Any)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Grey-area basis as STD.MOD.98/99/100: passive institutional record-keeping, automatic, no adversarial target, modest single-point PS gain — no faction's doctrine is meaningfully expressed. | Art 04 §6.2 P11 |
| Supported by zones | ✓ (N/A) | `target_district=None` by design — Accords aren't zone-scoped. | Art 01 §6–7 |
| Supported by components | ✓ | Standing marker is an existing component. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Persistence/resolution_type deferred (same as STD.MOD.98, still open — schema_cleanup_log #41). `faction(holder)` (here used as a Faction-object receiver for `.standing.add()`, same pattern as STD.MOD.107–109) is now confirmed §6.3 MutationExpr vocabulary. | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Accord formation is a genuine city-wide event, moderate frequency, not ring-filtered so not underfire. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=1` set per convention, though the trigger itself isn't ring-scoped — accepted design. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.102 = Card(
    id      = "STD.MOD.102",  card_id = "STD.MOD.102",  version = "v0.1",
    name    = "Access Log Pulled",
    tagline = "A filed agreement is a public document, and Core reads its own paperwork.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = accord.placed(faction=Any),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "An Accord anywhere in the city passes through institutional record-keeping. Core's clerks note who's tied to whom.",
    perspectives = None,
    design_note  = "Not ring-scoped by design — Accords have no ring dimension, so 'Core flavor' comes from doctrine/theme (institutional paperwork), not a mechanical filter. Ring ModReact triggers don't require ring-scoping.",
    arbiter_note = None,
)
```

---

### STD.MOD.103 — FLAGGED FOR REVIEW

#### Design Rationale
Submission reaction: a rival's Public Act submission in Core draws bureaucratic obstruction. The effect is a negative threshold delta (a hindering effect, unlike the established ModActionCard "benefit" convention of a positive `threshold_delta`). Grounded in Art 03: flat threshold modifiers already accumulate on submitted actions before resolution via the existing BEC/BM-xx modifier pipeline (§9.4.1.1/§9.4.3.1.3), and M-11 Type B Countermeasure already imposes a flat threshold delta on operations targeting a faction. `arbiter.modify(target, threshold, delta)` is one more source feeding that same existing pipeline, not new ARBITER behavior.

#### Card Story
A submission lands on the wrong desk, and now it needs a second signature.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic obstruction of a rival's submission is a grounded Core-flavored premise. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction=trigger.faction` set, `doctrine_mod=None` justified — Automatic/no threshold-roll to adjust (same basis as STD.MOD.99). | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — Submission×Modify confirmed valid in the Layer×Function matrix. `function=Modify` also matches the actual mutation verb used (`arbiter.modify`) — internally consistent. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | value_rating 1 — pricing-model tier overrides the magnitude-mirror convention; −5 threshold (a real but moderate hindrance), cost=None. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate — the threshold penalty applies once, to one already-submitted PA. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `public_act.placed_on_frg(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ⚠ | Deliberately obstructing a rival's Public Act is a more pointed adversarial choice than STD.MOD.98–102's passive logistics — plausibly doctrine-relevant (e.g., Directorate's "control and restraint" doctrine might read obstruction favorably; Ghost's "understanding precedes action" might read it as premature interference). Flagging as genuinely open rather than defaulting to None. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | No new component — modifies an existing submitted card's threshold field. | Art 02 §6–8 |
| Supported by game procedure | ✓ | `arbiter.modify(target, threshold, delta)` isn't new ARBITER behavior — it feeds the existing threshold-modifier-accumulation pipeline already used by BM-xx tokens and M-11 Type B Countermeasure (Art 03 §9.4.1.1/§9.4.3.1.3). | Art 03 §9.4.1.1, §9.4.3.1.3 |
| Data schema validation | ⚠ (deferred) | Persistence/resolution_type deferred (same as STD.MOD.98, still open — schema_cleanup_log #41). `arbiter.modify(target, field, delta)` (procedurally grounded per the row above) is now confirmed §6.3 MutationExpr vocabulary. | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | PA submission in Ring 1 is a regular recurring event — not underfire; moderate power (−5) keeps it from being oppressive. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98 — does a second copy compound to −10? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.103 = Card(
    id      = "STD.MOD.103",  card_id = "STD.MOD.103",  version = "v0.1",
    name    = "Flagged for Review",
    tagline = "A submission lands on the wrong desk, and now it needs a second signature.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Submission,  function = Modify,  subject = PublicAct,

    trigger         = public_act.placed_on_frg(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = trigger.card,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.modify(trigger.card, threshold, delta=-5),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Core's review process exists to slow things down. It works exactly as designed, on whoever it's aimed at.",
    perspectives = None,
    design_note  = "Hinders the flagged PA (−5 threshold — makes success harder), not a self-benefit. `arbiter.modify(target, field, delta)` is a new mutation form, not yet in confirmed vocabulary; flagged for reconciliation (04-n171). Procedurally grounded in the existing BM-xx/M-11 threshold-modifier-accumulation pipeline (Art 03 §9.4.1.1/§9.4.3.1.3), not new ARBITER behavior.",
    arbiter_note = None,
)
```

---

### STD.MOD.104 — BUDGET REALLOCATED

#### Design Rationale
Economy reaction: a rival's structure placement in Core is skimmed for a cut — generalized to whatever resource is native to the triggering faction, not hardcoded. This is a Standard card, usable by any faction, so the resource type must key off the rival who caused the trigger, not a fixed type like Capacity.

#### Card Story
Every structure that goes up in Core passes through an office with its hand out.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Skimming a cut from new construction is a grounded institutional-graft premise. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction=trigger.faction` set, `doctrine_mod=None` justified — Automatic/no threshold-roll (same basis as STD.MOD.99). | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — Economy×Add confirmed valid in the Layer×Function matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | value_rating 1, +1 resource unit, cost=None — floor tier. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.99 (minor, automatic skim on a rival's move) — modest single-unit resource gain, no faction's doctrine strongly expressed. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Native resource tokens are existing components. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Persistence/resolution_type deferred (same as STD.MOD.98, still open — schema_cleanup_log #41). `NativeResource(faction)` (parameterizes the existing bare `NativeResource` subject symbol so a `faction=All` card can resolve the correct resource type at runtime, needed because — unlike faction-specific precedent, e.g. GUI.MOD.2/3/4's hardcoded Capacity — this card has no single fixed faction context) is now confirmed §6.3 MutationExpr vocabulary. | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same as STD.MOD.99's structure-placement frequency. |  |
| Firing window (ModReactCard) | ✓ | Shares its trigger event with STD.MOD.99 (both fire on `structure_block.placed`) — not a race, since both can independently apply to the same event (one removes a chip, one grants a resource); multiple cards firing on the same confirmed event is standard practice elsewhere in the set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.104 = Card(
    id      = "STD.MOD.104",  card_id = "STD.MOD.104",  version = "v0.1",
    name    = "Budget Reallocated",
    tagline = "New construction means new permits, and permits mean a cut for whoever processes them.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Every structure that goes up in Core passes through an office with its hand out.",
    perspectives = None,
    design_note  = "`NativeResource(faction)` parameterizes the existing bare `NativeResource` subject symbol (Art 04 §6.1 line ~1559 usage) to resolve dynamically per triggering faction — needed because this card, unlike faction-specific precedent (GUI.MOD.2/3/4's hardcoded Capacity), doesn't have a single fixed faction context. Flagged for reconciliation (04-n171).",
    arbiter_note = None,
)
```

---

### STD.MOD.105 — AUDIT TRAIL

#### Design Rationale
Economy reaction: a rival reaching Established status in Core triggers an audit — same `NativeResource(faction)` generalization as STD.MOD.104.

#### Card Story
Reaching Established status means an audit — and audits find things.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.104. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.104. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.104. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same floor tier as STD.MOD.104. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `established_marker.placed(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.104. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.104. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.104 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(faction)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Established status is a real but infrequent milestone — not overfire. |  |
| Firing window (ModReactCard) | ✓ | Shares its trigger event with GUI.MOD.9 Field Supervisor (per design_note) — not a race; multiple cards firing on the same confirmed event is standard practice elsewhere in the set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.105 = Card(
    id      = "STD.MOD.105",  card_id = "STD.MOD.105",  version = "v0.1",
    name    = "Audit Trail",
    tagline = "Reaching Established status means an audit — and audits find things.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = established_marker.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Core's institutions track every faction's climb. The audit itself has a price, paid to whoever runs it.",
    perspectives = None,
    design_note  = "Same NativeResource(faction) generalization as STD.MOD.104 (04-n171). Shares its trigger event with GUI.MOD.9 Field Supervisor's established_marker.placed precedent — multiple cards firing on the same confirmed event is standard practice (e.g. presence_chip.placed already triggers several Ghost cards independently).",
    arbiter_note = None,
)
```

---

### STD.MOD.106 — EMERGENCY RESERVE

#### Design Rationale
Economy reaction: self-triggered safety net when the holder's own presence in Core is squeezed — same `NativeResource` generalization as STD.MOD.104/105, but keyed to the holder's own faction rather than a rival's. Distinct from the Floor Act mechanic (PM02 VE-01) — this is a Core-specific, presence-loss-triggered reserve, not a general insufficient-resource safety net.

#### Card Story
A reserve fund, tapped the moment the ground gives out from under you.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A contingency reserve triggered by the holder's own setback is a grounded, self-serving premise distinct from the reactive-to-rival shape of 98–105. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` (self-triggered) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.104/105. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same floor tier as STD.MOD.104/105 — compensatory rather than punitive, appropriate for a self-triggered safety net. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.removed(faction=holder, ring=1)` — same `ring=` parameter gap on `.removed()` flagged at STD.MOD.100; also worth confirming `faction=holder` is valid as a bare trigger-match parameter the same way `faction=opponent` is used elsewhere (plausible, since it's the same symbol class, but not yet independently confirmed in a trigger-matching position specifically). | Art 04 §6.3 |
| Portrait validity | ✓ | Self-triggered contingency, automatic, modest single-unit resource gain — no adversarial target, no faction's doctrine strongly expressed by having a reserve fund. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.104. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.104 (persistence/resolution_type deferred, still open — schema_cleanup_log #41), plus the `ring=` parameter question above; `NativeResource(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Presence-chip loss is a recurring event for any faction under pressure — not underfire. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this exact `faction=holder` trigger scoping. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.106 = Card(
    id      = "STD.MOD.106",  card_id = "STD.MOD.106",  version = "v0.1",
    name    = "Emergency Reserve",
    tagline = "A reserve fund, tapped the moment the ground gives out from under you.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = presence_chip.removed(faction=holder, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(holder)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Losing a foothold in Core isn't the end — there's always a contingency line item for exactly this.",
    perspectives = None,
    design_note  = "Distinct from the existing Floor Act mechanic (PM02 VE-01) — this is a Core-specific, presence-loss-triggered reserve, not a general insufficient-resource safety net. NativeResource(holder) keys to the holder's own faction, not a rival's (04-n171).",
    arbiter_note = None,
)
```

---

### STD.MOD.107 — ON THE DOCKET

#### Design Rationale
Standing reaction: a rival's standing gain in Core draws a formal, procedural response — a straightforward capitalize-on-rival's-gain template. `faction(holder).standing.add(1)` stands on its own precedent within the Ring set, STD.MOD.102.

#### Card Story
Every gain gets a formal response, whether anyone asked for one or not.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal procedural response to a rival's standing gain is a grounded Core-flavored premise. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction=trigger.faction` set, `doctrine_mod=None` justified — Automatic/no threshold-roll (same basis as STD.MOD.99). | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Per 04-n173: `function=Add` → `function=Shift` — Standing×Add is invalid per the matrix ("subsumed by Shift"). Also unifies with STD.MOD.102/114/126 (were `Information/Add` for the identical effect, also corrected to `Standing/Shift`). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | value_rating 1, +1 PS, cost=None — floor tier. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.increased(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Grey-area basis as STD.MOD.98–100/104: passive procedural response, automatic, modest single-point PS gain. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.102. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Persistence/resolution_type deferred (same as STD.MOD.98, still open — schema_cleanup_log #41). `faction(holder)` (same basis as STD.MOD.102) is now confirmed §6.3 MutationExpr vocabulary. | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Standing shifts are a recurring event — not underfire. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.109 — not a race, since standing can't increase and decrease simultaneously for the same faction. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.107 = Card(
    id      = "STD.MOD.107",  card_id = "STD.MOD.107",  version = "v0.1",
    name    = "On the Docket",
    tagline = "Every gain gets a formal response, whether anyone asked for one or not.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.increased(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Standing shifts in Core get logged, cross-referenced, and answered — Core doesn't let a change go unremarked.",
    perspectives = None,
    design_note  = "Straightforward capitalize-on-rival's-gain template — `faction(holder).standing.add(1)` stands on its own precedent within the Ring set, STD.MOD.102.",
    arbiter_note = None,
)
```

---

### STD.MOD.108 — PRECEDENT CITED

#### Design Rationale
Standing reaction: a Core district turning Contested is treated as a procedural opening. Reframed from an earlier seed concept ("an Accord involving a Core-based faction forms") — Accords aren't ring-scoped, so a Core-specific version couldn't distinguish itself from the other rings' copies. Tension Marker placement is a genuinely ring-scoped, confirmed-vocabulary substitute with the same "formal/procedural response" character.

#### Card Story
Core keeps records of every dispute. A district turning contested opens the door to citing precedent from somewhere else.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A contested district as a procedural/legal opening is a grounded Core-flavored premise. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ (N/A) | No `target_faction` (tension marker isn't faction-scoped) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.107: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same floor tier as STD.MOD.107. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `tension_marker.placed` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.107. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — valid. | Art 01 §6–7 |
| Supported by components | ✓ | Tension Marker is an existing component. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Tension Marker placement is a recurring board event — not underfire. |  |
| Firing window (ModReactCard) | ✓ | No other Ring 1 card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.108 = Card(
    id      = "STD.MOD.108",  card_id = "STD.MOD.108",  version = "v0.1",
    name    = "Precedent Cited",
    tagline = "A contested district is a legal opening as much as a physical one.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = tension_marker.placed(ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Core keeps records of every dispute. A district turning contested opens the door to citing precedent from somewhere else.",
    perspectives = None,
    design_note  = "Reframed from an earlier seed concept (originally 'an Accord involving a Core-based faction forms') — Accords aren't ring-scoped, so a Core-specific version couldn't distinguish itself from the other rings' copies. Tension Marker placement is a genuinely ring-scoped, confirmed-vocabulary substitute with the same 'formal/procedural response' character.",
    arbiter_note = None,
)
```

---

### STD.MOD.109 — QUIET REPRIMAND

#### Design Rationale
Standing reaction: a rival's standing drop in Core is capitalized on. Mirrors STD.MOD.107's template, opposite trigger direction. Closes the 12-card Ring 1 (Core) ModReactCard set.

#### Card Story
A reprimand doesn't need to be loud to be effective. Core specializes in the quiet kind.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.107, mirrored direction. | Art 00 §7 |
| Voice fit | ✓ | Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.107. | Art 04 §6.5 |
| Card type fit | ✓ | Same classification basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.107/108: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same floor tier as STD.MOD.107. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.decreased(faction=X, ring=Z)` matches confirmed §6.3 signature. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.107. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.107. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.107. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Standing shifts are a recurring event — not underfire. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.107 — not a race. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.109 = Card(
    id      = "STD.MOD.109",  card_id = "STD.MOD.109",  version = "v0.1",
    name    = "Quiet Reprimand",
    tagline = "Someone's standing slips, and Core is there to make a note of it.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.decreased(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = 1,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "A reprimand doesn't need to be loud to be effective. Core specializes in the quiet kind.",
    perspectives = None,
    design_note  = "Mirrors STD.MOD.107's template, opposite trigger direction. Closes Ring 1 (Core): 12 cards, STD.MOD.98–109 — first Ring ModReactCard set shipped (04-53/09-06).",
    arbiter_note = None,
)
```

---

### STD.MOD.110 — LINE REROUTED

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.98 Notified of Encroachment — same mechanic (`presence_chip.placed` → 1-chip reactive claim), renamed to Mid's operational-throughput voice per Art 00 §6.7.

#### Card Story
Traffic reroutes around whoever just staked a claim in Mid — right into someone else's hands.

**Design checklist:** verified independently against STD.MOD.98's basis, not copy-assumed — same trigger form (`presence_chip.placed(faction=X, district=Y, ring=Z)`, confirmed §6.3), same Territory×Add taxonomy pairing (valid per §5.1 matrix), same grey-area Portrait basis (automatic, reflexive, uniform across all 5 factions), same deferred persistence/resolution_type item, same open Stack-behavior question. All hold identically for ring=2 — no ring-specific delta found.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.98. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Mid operational-throughput register (Art 00 §6.7). Same open `perspectives=None` note as STD.MOD.98. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.98. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — same verified pairing as STD.MOD.98. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.98. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.98. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.98. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.98. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.98. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.110 = Card(
    id      = "STD.MOD.110",  card_id = "STD.MOD.110",  version = "v0.1",
    name    = "Line Rerouted",
    tagline = "Traffic reroutes around whoever just staked a claim — right into someone else's hands.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.placed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Mid's routing systems don't tolerate a new obstruction quietly. Whoever's watching the reroute gets there first.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.98 Notified of Encroachment — same mechanic, ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.111 — CAPACITY EXCEEDED

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.99 Structural Objection — same mechanic (structure placement draws a 1-chip removal from the same district), renamed to Mid's throughput/ceiling voice.

#### Card Story
Mid's infrastructure has a ceiling, and someone just tested it.

**Design checklist:** verified against STD.MOD.99's basis — same `structure_block.placed` trigger (confirmed §6.3), same Territory×Remove pairing (valid), same `doctrine_mod=None`-justified-by-Automatic-resolution reasoning despite `target_faction` being set, same grey-area Portrait basis weighed against the adversarial angle, same deferred schema items. No ring-specific delta.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.99. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Mid throughput/ceiling register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `target_faction` set, `doctrine_mod=None` justified — Automatic/no threshold-roll (same basis as STD.MOD.99). | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — same verified pairing as STD.MOD.99. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.99 (value_rating 2 — pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.99. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.99. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.99. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.99. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.111 = Card(
    id      = "STD.MOD.111",  card_id = "STD.MOD.111",  version = "v0.1",
    name    = "Capacity Exceeded",
    tagline = "Mid's infrastructure has a ceiling, and someone just tested it.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Remove,  subject = PresenceToken,

    trigger         = structure_block.placed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 2,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Mid's throughput has a hard limit. Building past it costs whoever built.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.99 Structural Objection — same mechanic, ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.112 — SALVAGE RIGHTS

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.100 Escort Withdrawn — same mechanic, renamed to Mid's salvage/leftovers voice.

#### Card Story
Nothing sits idle in Mid's infrastructure for long. Someone always moves in on the leftovers.

**Design checklist:** verified against STD.MOD.100's basis — inherits the same open `.removed()`-with-`ring=` vocabulary gap (schema log #3), same grey-area Portrait basis, same deferred schema items. No new ring-specific delta.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.100. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Mid salvage/leftovers register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — same verified pairing as STD.MOD.98/100. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.100. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | Same `ring=` on `.removed()` gap as STD.MOD.100 (schema log #3). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.100. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.100. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.100. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.100. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.112 = Card(
    id      = "STD.MOD.112",  card_id = "STD.MOD.112",  version = "v0.1",
    name    = "Salvage Rights",
    tagline = "What Mid abandons, Mid also claims — someone always moves in on the leftovers.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.removed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Nothing sits idle in Mid's infrastructure for long. Someone always moves in on the leftovers.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.100 Escort Withdrawn — same mechanic, ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.113 — GRID ANOMALY LOGGED

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.101 Overheard in the Commissary — same mechanic (`dominant_marker.placed` → Intel Token delivery), renamed to Mid's grid/relay-monitoring voice. Name repurposed from the Mid seed pool's originally-unbuildable covert-op-discovery concept.

#### Card Story
A district locked down draws load like a failing relay. The grid logs it before anyone announces it.

**Design checklist:** verified against STD.MOD.101's basis — same confirmed `dominant_marker.placed` trigger, same Information×Add pairing, same `faction(holder)` object-receiver syntax (04-n171, consistent usage), same genuinely-open Portrait question (this is the "capitalizing on a rival's public milestone" shape, not the reflexive-logistics shape — same uncertainty as 101, not resolved differently just because it's Mid).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.101. | Art 00 §7 |
| Voice fit | ✓ | Mid grid/relay register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.101. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — same verified pairing as STD.MOD.101. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.101 (value_rating 1 — pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.101. | Art 04 §6.3 |
| Portrait validity | ⚠ | Same genuinely-open question as STD.MOD.101 — capitalizing on a rival's public Dominant milestone reads more deliberate than the reflexive-logistics cards; not resolved here. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.101. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.101 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.101. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.101. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.113 = Card(
    id      = "STD.MOD.113",  card_id = "STD.MOD.113",  version = "v0.1",
    name    = "Grid Anomaly Logged",
    tagline = "When one relay draws all the load, the monitoring logs notice first.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Information,  function = Add,  subject = IntelToken,

    trigger         = dominant_marker.placed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.deliver(faction(holder), IntelToken(faction=trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "A district locked down draws load like a failing relay. The grid logs it before anyone announces it.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.101 Overheard in the Commissary — same mechanic, ring=2. Name drawn from the Mid seed pool's 'Grid Anomaly Logged' entry (originally a covert-op-discovery concept, not buildable — repurposed for the confirmed dominant_marker.placed mechanic).",
    arbiter_note = None,
)
```

---

### STD.MOD.114 — SERVICE LEVEL BREACH

#### Design Rationale
The one Ring 2 card that needed genuine redesign rather than direct duplication — STD.MOD.102 Access Log Pulled's `accord.placed(faction=Any)` trigger isn't ring-scoped, so copying it verbatim would give every ring an identical, undifferentiated card. Mid's own seed pool already had the right concept ("fires when an Accord involving Mid infrastructure is broken"), mapping to the confirmed `accord.removed` change-type rather than `.placed`. `accord.removed` chosen over `.corrupted` — dissolution/breach fits Mid's operational-consequence voice better than data-tampering, which reads more Ghost/Information-doctrine.

#### Card Story
An Accord's dissolution isn't just paperwork — whatever it was propping up now needs a new arrangement.

**Design checklist:** taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.102. Trigger, Portrait, and schema-deferral reasoning otherwise mirror STD.MOD.102.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord dissolution as an operational-consequence event is grounded for Mid specifically. | Art 00 §7 |
| Voice fit | ✓ | Mid operational-consequence register — deliberately distinct from STD.MOD.102's institutional-paperwork framing (per design_note). Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.102: `layer=Information` → `layer=Standing`, `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Floor tier, matches STD.MOD.102. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.removed(faction=Any)` matches confirmed §6.3 signature (distinct semantics from `.placed`/`.corrupted`, correctly chosen per Accord trigger semantics notes). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.102. | Art 04 §6.2 P11 |
| Supported by zones | ✓ (N/A) | `target_district=None` — Accords aren't zone-scoped, same as STD.MOD.102. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.102. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.102 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Accord dissolution is real but infrequent — moderate, not underfire given city-wide (not ring-filtered) scope. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | Same not-ring-scoped-trigger basis as STD.MOD.102 (accepted design). |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.114 = Card(
    id      = "STD.MOD.114",  card_id = "STD.MOD.114",  version = "v0.1",
    name    = "Service Level Breach",
    tagline = "When an agreement lapses, whatever infrastructure depended on it becomes everyone's problem — and someone's opportunity.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = accord.removed(faction=Any),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "An Accord's dissolution isn't just paperwork — whatever it was propping up now needs a new arrangement.",
    perspectives = None,
    design_note  = "Not ring-scoped, same as STD.MOD.102 (Accords have no ring dimension) — Mid flavor comes from doctrine (infrastructure-dependency framing), not a mechanical filter. `accord.removed` chosen over `.corrupted` — dissolution/breach fits Mid's operational-consequence voice better than data-tampering (which reads more Ghost/Information-doctrine).",
    arbiter_note = None,
)
```

---

### STD.MOD.115 — ROUTINE INSPECTION

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.103 Flagged for Review — same mechanic (−5 threshold hinder on a rival's submitted PA), renamed to Mid's inspection voice. Name drawn directly from the Mid seed pool's own Submission-reclassified entry (04-53 direction, PM02 L262).

#### Card Story
An inspection nobody asked for, timed to land before the paperwork clears.

**Design checklist:** verified against STD.MOD.103's basis — same `arbiter.modify` grounding in the existing BM-xx/M-11 threshold pipeline (not the invalid Burn Notice citation, which this card's design_note never repeated), same Submission×Modify pairing, same genuinely-open Portrait question.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.103. | Art 00 §7 |
| Voice fit | ✓ | Mid inspection register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.103. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — same verified pairing as STD.MOD.103. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.103 (value_rating 1, −5 threshold; pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.103. | Art 04 §6.3 |
| Portrait validity | ⚠ | Same genuinely-open question as STD.MOD.103 — deliberate obstruction of a rival's PA, not settled to None. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.103. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same BM-xx/M-11 pipeline grounding as STD.MOD.103 — not new ARBITER behavior. | Art 03 §9.4.1.1, §9.4.3.1.3 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.103 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `arbiter.modify` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.103. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.103. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.115 = Card(
    id      = "STD.MOD.115",  card_id = "STD.MOD.115",  version = "v0.1",
    name    = "Routine Inspection",
    tagline = "An inspection nobody asked for, timed to land before the paperwork clears.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Submission,  function = Modify,  subject = PublicAct,

    trigger         = public_act.placed_on_frg(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = trigger.card,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.modify(trigger.card, threshold, delta=-5),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Mid's inspectors don't announce a visit. They just show up when it's least convenient.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.103 Flagged for Review — same mechanic (−5 threshold, hinders the flagged PA), ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.116 — TOLL COLLECTED

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.104 Budget Reallocated — same mechanic, renamed to Mid's toll/chokepoint voice.

#### Card Story
Nothing gets built in Mid without crossing a toll line somebody controls.

**Design checklist:** verified against STD.MOD.104's basis — same `NativeResource(trigger.faction)` generalization (04-n171), same Economy×Add pairing, same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.104. | Art 00 §7 |
| Voice fit | ✓ | Mid toll/chokepoint register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.104. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.104. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.104. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.104. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.104. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.104. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.104 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(trigger.faction)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.104. |  |
| Firing window (ModReactCard) | ✓ | Shares its trigger event with STD.MOD.111 (both fire on `structure_block.placed`, ring=2) — same standard-practice basis as STD.MOD.104/99. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.104. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.116 = Card(
    id      = "STD.MOD.116",  card_id = "STD.MOD.116",  version = "v0.1",
    name    = "Toll Collected",
    tagline = "Every structure that goes up in Mid crosses a toll line somewhere.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Nothing gets built in Mid without crossing a toll line somebody controls.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.104 Budget Reallocated — same NativeResource(trigger.faction) generalization (04-n171), ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.117 — OVERTIME BILLED

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.105 Audit Trail — same mechanic, renamed to Mid's reconciliation voice.

#### Card Story
Every climb to Established in Mid triggers a reconciliation somewhere down the line.

**Design checklist:** verified against STD.MOD.105's basis — same `NativeResource(trigger.faction)` generalization, same Economy×Add pairing, same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.105. | Art 00 §7 |
| Voice fit | ✓ | Mid reconciliation register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.105. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.105. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.105. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.105. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.105. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.105. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.105 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(trigger.faction)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.105. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.105. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.117 = Card(
    id      = "STD.MOD.117",  card_id = "STD.MOD.117",  version = "v0.1",
    name    = "Overtime Billed",
    tagline = "Reaching Established in Mid means someone's books get reconciled — at a cost.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = established_marker.placed(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Every climb to Established in Mid triggers a reconciliation somewhere down the line.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.105 Audit Trail — same NativeResource(trigger.faction) generalization (04-n171), ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.118 — BACKUP GENERATOR

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.106 Emergency Reserve — same mechanic, renamed to Mid's backup-generator voice. Name drawn directly from the Mid seed pool — an exact conceptual match.

#### Card Story
Losing ground in Mid trips a contingency that's always been sitting there, waiting.

**Design checklist:** verified against STD.MOD.106's basis — same `NativeResource(holder)` generalization, same `.removed()`-with-`ring=` vocabulary gap (schema log #3), same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.106. | Art 00 §7 |
| Voice fit | ✓ | Mid backup/contingency register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` (self-triggered) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.106. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.106. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | Same `ring=` on `.removed()` gap as STD.MOD.106 (schema log #3). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.106. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.106. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.106 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.106. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.106. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.118 = Card(
    id      = "STD.MOD.118",  card_id = "STD.MOD.118",  version = "v0.1",
    name    = "Backup Generator",
    tagline = "When the line goes down, the backup kicks in before anyone notices the gap.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = presence_chip.removed(faction=holder, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(holder)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Losing ground in Mid trips a contingency that's always been sitting there, waiting.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.106 Emergency Reserve — same NativeResource(holder) generalization (04-n171), ring=2. Distinct from the existing Floor Act mechanic (PM02 VE-01), same as its Ring 1 counterpart.",
    arbiter_note = None,
)
```

---

### STD.MOD.119 — UNION STATEMENT

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.107 On the Docket — same mechanic, renamed to Mid's labor-apparatus voice.

#### Card Story
Every gain in Mid gets a statement from somebody with standing to make one.

**Design checklist:** verified against STD.MOD.107's basis — same `faction(holder)` syntax (04-n171), same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.107.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.107. | Art 00 §7 |
| Voice fit | ✓ | Mid labor-apparatus register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.107. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.107: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.107. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.107. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.107. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.107. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.107. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.121 — not a race. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.107. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.119 = Card(
    id      = "STD.MOD.119",  card_id = "STD.MOD.119",  version = "v0.1",
    name    = "Union Statement",
    tagline = "Every gain in Mid gets a statement from somebody with standing to make one.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.increased(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Mid's labor apparatus doesn't let a shift in standing pass without a formal word on it.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.107 On the Docket — same mechanic, ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.120 — ON RECORD

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.108 Precedent Cited — same mechanic, renamed to Mid's record-keeping voice.

#### Card Story
Mid keeps a file on every dispute. A contested line gets a citation before it gets resolved.

**Design checklist:** verified against STD.MOD.108's basis — same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.108.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.108. | Art 00 §7 |
| Voice fit | ✓ | Mid record-keeping register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ (N/A) | No `target_faction` (tension marker isn't faction-scoped) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.108: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.108. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.108. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.108. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.108. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.108. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.108 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.108. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 2 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.108. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.120 = Card(
    id      = "STD.MOD.120",  card_id = "STD.MOD.120",  version = "v0.1",
    name    = "On Record",
    tagline = "A contested line in Mid gets logged the moment the tension shows.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = tension_marker.placed(ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Mid keeps a file on every dispute. A contested line gets a citation before it gets resolved.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.108 Precedent Cited — same mechanic, ring=2.",
    arbiter_note = None,
)
```

---

### STD.MOD.121 — FORMAL NOTICE

#### Design Rationale
Direct Ring 2 duplicate of STD.MOD.109 Quiet Reprimand — same mechanic, renamed to Mid's paper-trail voice. Closes the 12-card Ring 2 (Mid) ModReactCard set.

#### Card Story
A formal notice doesn't need drama. Mid's bureaucracy just needs the paper trail.

**Design checklist:** verified against STD.MOD.109's basis — same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.109.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.109. | Art 00 §7 |
| Voice fit | ✓ | Mid paper-trail register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.109. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.109: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.109. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.109. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.109. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.107. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.107. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.109. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.119 — not a race. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.109. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.121 = Card(
    id      = "STD.MOD.121",  card_id = "STD.MOD.121",  version = "v0.1",
    name    = "Formal Notice",
    tagline = "Someone's standing slips, and Mid puts it on the record.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.decreased(faction=opponent, ring=2),
    beat            = None,
    ring_constraint = 2,
    ring_origin     = 2,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "A formal notice doesn't need drama. Mid's bureaucracy just needs the paper trail.",
    perspectives = None,
    design_note  = "Ring 2 duplicate of STD.MOD.109 Quiet Reprimand — same mechanic, ring=2. Closes Ring 2 (Mid): 12 cards, STD.MOD.110–121. Ring 3 (Baryo) is the last open leg of 09-06's Ring ModReactCard pass.",
    arbiter_note = None,
)
```

---

### STD.MOD.122 — CROWD GATHERS

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.98/110 — same mechanic, renamed to Baryo's gray-economy/community-network voice. Name drawn directly from the Baryo seed pool's matching Territory entry.

#### Card Story
Baryo doesn't wait for paperwork. Word moves faster than any filing ever could.

**Design checklist:** verified against STD.MOD.98's basis — same confirmed trigger, taxonomy, and grey-area Portrait reasoning, no ring-specific delta.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.98. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Baryo gray-economy register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.98. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — same verified pairing as STD.MOD.98. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.98. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.98. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.98. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.98. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.98. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.122 = Card(
    id      = "STD.MOD.122",  card_id = "STD.MOD.122",  version = "v0.1",
    name    = "Crowd Gathers",
    tagline = "The block notices a new face before anyone official does.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.placed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Baryo doesn't wait for paperwork. Word moves faster than any filing ever could.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.98/STD.MOD.110 — same mechanic, ring=3. Name drawn directly from the Baryo seed pool's matching Territory entry.",
    arbiter_note = None,
)
```

---

### STD.MOD.123 — PRICED OUT

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.99/111 — same mechanic, renamed to Baryo's rent/displacement voice.

#### Card Story
New construction changes the rent, one way or another.

**Design checklist:** verified against STD.MOD.99's basis — same `doctrine_mod=None`-justified-by-Automatic reasoning, same taxonomy pairing, same grey-area Portrait basis weighed against the adversarial angle.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.99. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Baryo rent/displacement register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.99. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — same verified pairing as STD.MOD.99. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.99 (value_rating 2 — pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.99. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.99. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.99. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.99. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.123 = Card(
    id      = "STD.MOD.123",  card_id = "STD.MOD.123",  version = "v0.1",
    name    = "Priced Out",
    tagline = "New construction changes the rent, one way or another.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Remove,  subject = PresenceToken,

    trigger         = structure_block.placed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 2,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Something goes up in Baryo, and somebody else finds themselves priced out of the corner they held.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.99/STD.MOD.111 — same mechanic, ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.124 — EVICTION NOTICE

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.100/112 — same mechanic, renamed to Baryo's voice. Name drawn directly from the Baryo seed pool — an exact conceptual match.

#### Card Story
The moment a foothold disappears, someone else is already moving their things in.

**Design checklist:** verified against STD.MOD.100's basis — inherits the same open `.removed()`-with-`ring=` vocabulary gap (schema log #3), same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.100. | Art 00 §7; 04-53 |
| Voice fit | ✓ | Baryo register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — same verified pairing as STD.MOD.98/100. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.100. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | Same `ring=` on `.removed()` gap as STD.MOD.100/112 (schema log #3). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.100. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.98. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.100. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.100. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.100. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.124 = Card(
    id      = "STD.MOD.124",  card_id = "STD.MOD.124",  version = "v0.1",
    name    = "Eviction Notice",
    tagline = "Baryo doesn't leave a spot empty for long.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.removed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=trigger.district, faction=holder, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "The moment a foothold disappears, someone else is already moving their things in.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.100/STD.MOD.112 — same mechanic, ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.125 — WORD TRAVELS

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.101/113 — same mechanic, renamed to Baryo's voice. Name drawn from the Baryo seed pool's Information entry.

#### Card Story
When someone locks down a piece of Baryo, the street knows before the ink's even dry — if there was any ink to begin with.

**Design checklist:** verified against STD.MOD.101's basis — same `faction(holder)` syntax (04-n171), same genuinely-open Portrait question (not resolved to None, same as 101/113).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.101. | Art 00 §7 |
| Voice fit | ✓ | Baryo street-information register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.101. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — same verified pairing as STD.MOD.101. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.101 (value_rating 1 — pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.101. | Art 04 §6.3 |
| Portrait validity | ⚠ | Same genuinely-open question as STD.MOD.101/113 — not resolved to None. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.101. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.101 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.101. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.101. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.125 = Card(
    id      = "STD.MOD.125",  card_id = "STD.MOD.125",  version = "v0.1",
    name    = "Word Travels",
    tagline = "Nothing stays quiet on the Strip for long.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Information,  function = Add,  subject = IntelToken,

    trigger         = dominant_marker.placed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.deliver(faction(holder), IntelToken(faction=trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "When someone locks down a piece of Baryo, the street knows before the ink's even dry — if there was any ink to begin with.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.101/STD.MOD.113 — same mechanic, ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.126 — QUIETLY REWRITTEN

#### Design Rationale
The one Ring 3 card needing genuine redesign, same as STD.MOD.102/114 before it — uses `accord.corrupted`, not `.removed`. A corrupted Accord (falsified/tampered terms) fits Baryo's informal, unfiled-agreement culture better than a formal dissolution.

#### Card Story
A handshake deal's terms are whatever the last conversation says they are.

**Design checklist:** taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.102/114. Trigger semantics distinct from both siblings (`.corrupted` vs `.placed`/`.removed`) but confirmed valid.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Falsified/renegotiated informal terms is a grounded premise specifically for Baryo's unfiled-agreement culture. | Art 00 §7 |
| Voice fit | ✓ | Baryo informal-agreement register, deliberately distinct from STD.MOD.102/114's institutional/operational framings. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.102/114: `layer=Information` → `layer=Standing`, `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Floor tier, matches STD.MOD.102/114. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.corrupted(faction=Any)` matches confirmed §6.3 signature and semantics (textual alteration of an active Accord, distinct from `.removed`). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.102/114. | Art 04 §6.2 P11 |
| Supported by zones | ✓ (N/A) | Not zone-scoped, same as STD.MOD.102/114. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.102. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Same open Art 06 gap noted for `accord.corrupted` generally (requires an explicit ARBITER corrupt step on the Accord form, tracked 06-n01) — not specific to this card. | Art 03; GR 6.1; PM05 06-n01 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.102 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Accord corruption is real but infrequent — moderate, not underfire given city-wide scope. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | Not ring-scoped trigger, same basis as STD.MOD.102/114. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.126 = Card(
    id      = "STD.MOD.126",  card_id = "STD.MOD.126",  version = "v0.1",
    name    = "Quietly Rewritten",
    tagline = "A handshake deal's terms are whatever the last conversation says they are.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = accord.corrupted(faction=Any),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Baryo's agreements aren't filed anywhere official. That's exactly what makes them so easy to quietly renegotiate.",
    perspectives = None,
    design_note  = "Not ring-scoped, same as STD.MOD.102/STD.MOD.114 (Accords have no ring dimension) — Baryo flavor comes from doctrine (informal/unfiled agreements), not a mechanical filter. `accord.corrupted` rather than `.removed` — Baryo's version of the unscoped card reacts to terms being falsified, not a formal breach.",
    arbiter_note = None,
)
```

---

### STD.MOD.127 — SOMEONE'S WATCHING

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.103/115 — same mechanic (−5 threshold hinder), renamed to Baryo's street-surveillance voice. Name drawn directly from the Baryo seed pool's own Submission-reclassified entry (04-53 direction, PM02 L262).

#### Card Story
An operation through Baryo draws attention before it ever gets a chance to land clean.

**Design checklist:** verified against STD.MOD.103's basis — same `arbiter.modify` grounding in the existing BM-xx/M-11 pipeline, same genuinely-open Portrait question.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.103. | Art 00 §7 |
| Voice fit | ✓ | Baryo street-surveillance register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.103. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — same verified pairing as STD.MOD.103. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.103 (value_rating 1 — pricing-model tier overrides the magnitude-mirror convention). | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.103. | Art 04 §6.3 |
| Portrait validity | ⚠ | Same genuinely-open question as STD.MOD.103/115. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.103. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same BM-xx/M-11 pipeline grounding as STD.MOD.103/115. | Art 03 §9.4.1.1, §9.4.3.1.3 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.103 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `arbiter.modify` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.103. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.103. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.127 = Card(
    id      = "STD.MOD.127",  card_id = "STD.MOD.127",  version = "v0.1",
    name    = "Someone's Watching",
    tagline = "Somebody's always got eyes on what's moving through Baryo.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Submission,  function = Modify,  subject = PublicAct,

    trigger         = public_act.placed_on_frg(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,  # diverges from the magnitude-mirror convention — pricing model places this tier here

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = trigger.card,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.modify(trigger.card, threshold, delta=-5),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "An operation through Baryo draws attention before it ever gets a chance to land clean.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.103/STD.MOD.115 — same mechanic (−5 threshold, hinders the flagged PA), ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.128 — INFORMAL TOLL

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.104/116 — same mechanic, renamed to Baryo's informal-economy voice.

#### Card Story
There's no filing cabinet for it, but everyone knows the toll gets paid regardless.

**Design checklist:** verified against STD.MOD.104's basis — same `NativeResource(trigger.faction)` generalization (04-n171), same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.104. | Art 00 §7 |
| Voice fit | ✓ | Baryo informal-economy register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.104. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.104. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.104. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.104. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.104. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.104. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.104 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(trigger.faction)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.104. |  |
| Firing window (ModReactCard) | ✓ | Shares its trigger event with STD.MOD.123 — same standard-practice basis as STD.MOD.104/99. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.104. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.128 = Card(
    id      = "STD.MOD.128",  card_id = "STD.MOD.128",  version = "v0.1",
    name    = "Informal Toll",
    tagline = "Nothing crosses Baryo without somebody taking a cut.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "There's no filing cabinet for it, but everyone knows the toll gets paid regardless.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.104/STD.MOD.116 — same NativeResource(trigger.faction) generalization (04-n171), ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.129 — CUT OF THE ACTION

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.105/117 — same mechanic, renamed to Baryo's voice.

#### Card Story
The gray economy notices every climb — and it always finds a way in.

**Design checklist:** verified against STD.MOD.105's basis — same `NativeResource(trigger.faction)` generalization, same grey-area Portrait basis.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.105. | Art 00 §7 |
| Voice fit | ✓ | Baryo gray-economy register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.105. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.105. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.105. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.105. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.105. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.105. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.105 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(trigger.faction)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.105. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.105. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.129 = Card(
    id      = "STD.MOD.129",  card_id = "STD.MOD.129",  version = "v0.1",
    name    = "Cut of the Action",
    tagline = "Reaching Established in Baryo means somebody local wants a piece.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = established_marker.placed(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "The gray economy notices every climb — and it always finds a way in.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.105/STD.MOD.117 — same NativeResource(trigger.faction) generalization (04-n171), ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.130 — VENDOR CREDIT CALLED

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.106/118 — same mechanic, renamed to Baryo's favor-economy voice. Name drawn directly from the Baryo seed pool — an exact conceptual match.

#### Card Story
Baryo runs on favors owed. This is one finally getting called in.

**Design checklist:** verified against STD.MOD.106's basis — same `NativeResource(holder)` generalization, same open `.removed()`-with-`ring=` vocabulary gap (schema log #3).

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.106. | Art 00 §7 |
| Voice fit | ✓ | Baryo favor-economy register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | No `target_faction` (self-triggered) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — same verified pairing as STD.MOD.106. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.106. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ⚠ | Same `ring=` on `.removed()` gap as STD.MOD.106/118 (schema log #3). | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.106. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.106. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.106 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `NativeResource(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.106. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.106. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.130 = Card(
    id      = "STD.MOD.130",  card_id = "STD.MOD.130",  version = "v0.1",
    name    = "Vendor Credit Called",
    tagline = "When the corner gets squeezed, credit from an old favor covers the gap.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = presence_chip.removed(faction=holder, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).resources.add(1, NativeResource(holder)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Baryo runs on favors owed. This is one finally getting called in.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.106/STD.MOD.118 — same NativeResource(holder) generalization (04-n171), ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.131 — NEIGHBORHOOD NOTICES

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.107/119 — same mechanic, renamed to Baryo's community-ledger voice.

#### Card Story
The neighborhood keeps its own ledger, and it's not shy about updating it out loud.

**Design checklist:** verified against STD.MOD.107's basis — same `faction(holder)` syntax (04-n171), same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.107.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.107. | Art 00 §7 |
| Voice fit | ✓ | Baryo community-ledger register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.107. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.107/119: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.107. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.107. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.107. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.98. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.107. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.107. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.133 — not a race. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.107. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.131 = Card(
    id      = "STD.MOD.131",  card_id = "STD.MOD.131",  version = "v0.1",
    name    = "Neighborhood Notices",
    tagline = "A gain in Baryo doesn't go unnoticed — or unremarked on.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.increased(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "The neighborhood keeps its own ledger, and it's not shy about updating it out loud.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.107/STD.MOD.119 — same mechanic, ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.132 — SIDES ARE TAKEN

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.108/120 — same mechanic, renamed to Baryo's voice.

#### Card Story
Baryo doesn't wait for an official ruling. The neighborhood picks its side the moment the tension shows.

**Design checklist:** verified against STD.MOD.108's basis — same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.108.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.108. | Art 00 §7 |
| Voice fit | ✓ | Baryo register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ (N/A) | No `target_faction` (tension marker isn't faction-scoped) — trivially correct. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.108/120: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.108. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.108. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.108. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.108. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.108. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.108 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.108. |  |
| Firing window (ModReactCard) | ✓ | No collision within Ring 3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.108. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.132 = Card(
    id      = "STD.MOD.132",  card_id = "STD.MOD.132",  version = "v0.1",
    name    = "Sides Are Taken",
    tagline = "When a block turns openly contested, everybody already knows where they stand.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = tension_marker.placed(ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "Baryo doesn't wait for an official ruling. The neighborhood picks its side the moment the tension shows.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.108/STD.MOD.120 — same mechanic, ring=3.",
    arbiter_note = None,
)
```

---

### STD.MOD.133 — THE CROWD REMEMBERS

#### Design Rationale
Direct Ring 3 duplicate of STD.MOD.109/121 — same mechanic, renamed to Baryo's long-memory voice. Closes the 12-card Ring 3 (Baryo) ModReactCard set — and closes 09-06's full Ring ModReactCard pass (36 cards, all 3 rings).

#### Card Story
Baryo's memory is longer than anywhere else in the city.

**Design checklist:** verified against STD.MOD.109's basis — same grey-area Portrait basis. Taxonomy is `Standing/Shift` (04-n173), same as STD.MOD.109.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as STD.MOD.109. | Art 00 §7 |
| Voice fit | ✓ | Baryo long-memory register. Same open `perspectives=None` note. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Same basis as STD.MOD.109. | Art 04 §6.5 |
| Card type fit | ✓ | Same basis as STD.MOD.98. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same fix as STD.MOD.109/121: `function=Add` → `function=Shift` (04-n173). | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ✓ (best-effort) | Same tier as STD.MOD.109. | Art 02 §6–7 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open item as STD.MOD.98. | Art 04 §6.2 |
| Trigger validity | ✓ | Same basis as STD.MOD.109. | Art 04 §6.3 |
| Portrait validity | ✓ | Same grey-area basis as STD.MOD.109. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same basis as STD.MOD.107. | Art 01 §6–7 |
| Supported by components | ✓ | Same basis as STD.MOD.107. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same basis as STD.MOD.98. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Same open item as STD.MOD.107 (persistence/resolution_type deferred, still open — schema_cleanup_log #41); `faction(holder)` now confirmed §6.3 MutationExpr vocabulary (04-n171). | Art 04 §6.1–§6.3; 04-n171 |
| Card narrative | ✓ | Card Story is a concrete event. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None`. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Same basis as STD.MOD.109. |  |
| Firing window (ModReactCard) | ✓ | Opposite-direction pair with STD.MOD.131 — not a race. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same basis as STD.MOD.109. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as STD.MOD.98. |  |
| Ring constraint (ModReactCard) | ✓ | Matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.MOD.133 = Card(
    id      = "STD.MOD.133",  card_id = "STD.MOD.133",  version = "v0.1",
    name    = "The Crowd Remembers",
    tagline = "Baryo's memory is longer than anywhere else in the city.",
    type    = ModReactCard,  subtype = Standard,  faction = All,
    layer   = Standing,  function = Shift,  subject = StandingMarker,

    trigger         = standing_marker.decreased(faction=opponent, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = 3,
    value_rating    = 1,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(holder).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    narrative    = "A slip in standing here doesn't fade quietly — the block holds onto it.",
    perspectives = None,
    design_note  = "Ring 3 duplicate of STD.MOD.109/STD.MOD.121 — same mechanic, ring=3. Closes Ring 3 (Baryo): 12 cards, STD.MOD.122–133. Closes 09-06's full Ring ModReactCard pass: 36 cards, all 3 rings (STD.MOD.98–133).",
    arbiter_note = None,
)
```

---

