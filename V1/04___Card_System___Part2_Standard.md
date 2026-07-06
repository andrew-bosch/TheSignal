## Standard
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#standard-covert-operations) · [Public Acts](#standard-public-acts)

---

### Standard — Covert Operations
[↑ Standard](#standard)

| Card | Name |
|------|------|
| [STD.CA.1](#c01-build-structure) | Build Structure |
| [STD.CA.2](#c02-demolish) | Demolish |
| [STD.CA.3](#c03-campaign) | Campaign |
| [STD.CA.4](#c04-undermine) | Undermine |
| [STD.CA.5](#c05-gather) | Gather |
| [STD.CA.6](#c06-broadcast-interference) | Broadcast Interference |
| [STD.CA.7](#c07-amplify) | Amplify |
| [STD.CA.8](#c08-buy-influence) | Buy Influence |
| [STD.CA.9](#c09-fund) | Fund |
| [STD.CA.10](#c10-protect) | Protect |
| [STD.CA.12](#c39-absolute-compromise) | Absolute Compromise |
| [—](#standard-disinformation-campaign) | Disinformation Campaign |
| [—](#standard-disprove) | Disprove |
| [—](#standard-intel-extraction) | Intel Extraction |
| [—](#standard-modifier-raid) | Modifier Raid |

### STD.CA.1 — BUILD STRUCTURE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory-control foundation card. Construction is publicly visible — the covert element is intent, not the act. Every faction must establish structured positions to hold territory; this is the universal mechanism. Cost vs reward: dual cost (1 faction native + 1 district native) models that building requires both faction resources and local knowledge; Automatic resolution is appropriate if prerequisites are met. Guild affinity waives the district-native cost: the Guild *is* the city's builder and does not purchase access to their own infrastructure ecosystem.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Physical construction as territorial assertion is core to New Meridian. The covert element is unannounced intent — the visible act is public. All five factions acknowledge building as a valid form of presence. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | All five perspectives are doctrinally distinct. Guild's "permanence is possible here" is the foundational argument; Syndicate's "the question is who captures it" reframes construction as economic extraction; Ghost's "commitments are data points" is cold and analytical. No faction sounds like another. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Building directly serves Guild doctrine (permanence, structural investment). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: every faction must establish structure; no faction-specific exclusivity warranted. CovertOperation: unannounced intent is the covert element, not the visible act. Fills the universal territorial foundation role — no standard card duplicates it. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — unambiguous. Layer is Territory because the target is a StructureBlock, not because of the Add verb. | Art 04b §4 |
| Balance | ✓ | Automatic resolution gated by dual cost + presence prerequisite + no-existing-structure restriction. Not independently playable without prior presence. Guild affinity waives district native only — cost-scoped, not difficulty. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — structure placement is permanent; persists until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`: permanence doctrine — core alignment (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: structure is a permanent visible commitment; Ghost doctrine is concealment, not construction (DIR.PA.1, SYN.PA.2). Directorate: no entry — builds pragmatically ("if it serves the mandate"); instrumental, not doctrinal. Network: no entry — presence-building via community relationships (STD.CA.3), not structures; observational stance confirms absence. Syndicate: no entry — doctrine is acquisition and capital flow; "who captures it" is observer framing, not builder framing. No direct Portrait track shift in effect fields (DIR.PA.2). All entries submitter-bounded (SYN.PA.2). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` — valid. Ring entry implicit via presence requirement in restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §6); presence token / deployment marker in restriction (Art 02 §6); faction native + district native cost (Art 02 §7). | Art 02 §6–§7 |
| Supported by game procedure | ✓ | Submitted in Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4). ARBITER places Structure Block at Beat 3 outcome. Guild affinity evaluated at dispatch. | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Dual-resource cost (faction native + district native) reads as cross-faction-resource tier, but `cost`'s first term is missing a resource-type attribute (see schema_cleanup_log.md) — can't confirm tier/power match until that's fixed. Flagged, not resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | ✓ S63 |

```python
STD.CA.1 = Card(
    id      = "STD.CA.1",  version = "v1.1",
    name    = "Build Structure",
    tagline = "Construct a physical installation in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

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
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Guild: cost.resource.district(native) = 0,
    restriction = (
        district(target).faction(acting).presence > 0 and
        district(target).faction(acting).structure == 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(acting).structure += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild: PortraitEntry(submitter=+1),
        Ghost: PortraitEntry(submitter=-1),
    },

    narrative    = "Every faction that wants to matter in New Meridian eventually has to build something.",
    perspectives = {
        Guild:       "This is what we do. Every structure we build is an argument that permanence is possible here.",
        Directorate: "Infrastructure serves order. We will use it if it serves the mandate.",
        Network:     "Building is a statement of intent. We watch carefully to understand what kind.",
        Ghost:       "A structure is a commitment. Commitments are data points.",
        Syndicate:   "Every structure generates value. The question is who captures it.",
    },
)
```

---

### STD.CA.2 — DEMOLISH
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory disruption card — the destructive mirror of STD.CA.1. Structure removal is publicly visible; source of removal is not announced. Cost vs reward: dual cost (1 faction native + 1 district native) reflects that demolition requires both capability and local knowledge; probabilistic resolution models genuine resistance — you do not control what you are destroying. Crit success yields salvage (1 native recovered); crit fail costs Public Standing, representing the reputational risk of publicly-failed covert demolition.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Demolition as covert territorial disruption is grounded — the act is visible, the source is not. The asymmetry with STD.CA.1 (probabilistic vs. Automatic) correctly reflects operating against someone else's infrastructure rather than your own. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Guild's "something has gone badly wrong" and Network's "infrastructure of control needs to come down" are the sharpest contrast in the set. Ghost's absence-as-data read is clean. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` is set; `doctrine_mod = None` is an explicit design choice — demolition difficulty reflects physical opportunity (ring, restriction), not doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in demolition as territorial disruption. CovertOperation: source undisclosed. Distinct from STD.CA.1 — Remove vs. Add, probabilistic vs. Automatic. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / StructureBlock. Layer is Territory because the target is a StructureBlock. | Art 04b §4 |
| Balance | ✓ | Same dual cost as STD.CA.1, probabilistic at threshold 50. Ring_mod {0:−15, 1:−10, 2:0, 3:+10} — harder near Chorus Node. Crit success salvage rewards execution; crit fail PS loss is a meaningful downside. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — structure removal is permanent; persists until rebuilt. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: demolition against permanence doctrine — "we do not unmake" (DIR.PA.1, SYN.PA.2). Network `submitter=+1`: counter-entrenchment doctrine — removing infrastructure of control is on-doctrine (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: structures represent institutional investment; doctrinal reluctance parallels STD.CA.4 (DIR.PA.1, SYN.PA.2). Ghost: no entry — analytical observer, not demolition-as-doctrine; absence justified. Syndicate: no entry — pragmatic asset-management framing, no doctrinal signal; absence justified. `failcrit standing -= 1` is Public Standing (Art 02), not Portrait — DIR.PA.2 clear. | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction uses self-or-adjacent presence — adjacency model required; district_adjacency confirmed (DB-09 ✅ S50). | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock target (Art 02 §6); presence in restriction (Art 02 §6); dual cost (§8); failcrit `standing -= 1` (Art 02 §11). | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with ring_mod. ARBITER removes Structure Block on success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Dual-resource cost (faction native + district native) reads as cross-faction-resource tier, but `cost`'s first term is missing a resource-type attribute (see schema_cleanup_log.md #22) — can't confirm tier/power match until that's fixed. Flagged, not resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | ✓ S63 |

```python
STD.CA.2 = Card(
    id      = "STD.CA.2",  version = "v1.1",
    name    = "Demolish",
    tagline = "Remove an opponent's structure from a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = StructureBlock,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
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
    target_object   = StructureBlock,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 and
        district(target).faction(target).structure > 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(target).structure -= 1,
    successcrit = resource.faction(acting).native += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "Not everything built in New Meridian was meant to last.",
    perspectives = {
        Guild:       "We build. We do not unmake. Every time we perform this action something has gone badly wrong.",
        Directorate: "Demolition is a last resort. Structures represent investment in the city we are here to protect.",
        Network:     "Sometimes the infrastructure of control needs to come down before something better can be built.",
        Ghost:       "A demolished structure tells us as much as a standing one. We note the absence.",
        Syndicate:   "Assets change hands. Sometimes the most efficient transfer is removal.",
    },
)
```

---

### STD.CA.3 — CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-deepening card — a deliberate structural parallel to STD.CA.1. To Campaign, you must already be present; this is not an entry card. Cost vs reward: dual cost mirrors STD.CA.1 (same principle, same gate). Automatic resolution because you're operating within your own established footprint, not against opposition. Network affinity waives the district-native cost because Network growth is relational, not material — it does not purchase access to local infrastructure.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence-deepening in a district you already occupy is grounded. Campaign is relational/operational deepening of an existing footprint — distinct from entry. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "presence creates exposure" explains why Ghost doesn't over-extend; Network's "relationships are how things actually change" directly justifies the affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Presence-deepening through community relationships directly serves Network doctrine (relational growth). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions build presence. CovertOperation: presence-building is done quietly. Structurally mirrors STD.CA.1 (presence vs. structure) — distinct role, not duplicative. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Automatic gated by presence prerequisite — same structure as STD.CA.1. Network affinity waives district native (relational, not material). Intentional cost symmetry with STD.CA.1. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — presence placement is permanent until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Network `submitter=+1`: relational growth is doctrinally core (DIR.PA.1, SYN.PA.2). Guild: no entry — STD.CA.1/structural investment is Guild's primary presence signal; Campaign is available but not doctrinally distinct; absence justified. Directorate: no entry — presence-building is instrumental ("where the mandate requires it"), not doctrinal; absence justified. Ghost: no entry — "presence creates exposure" frames expansion as calculated exception, not doctrinal endorsement; absence justified. Syndicate: no entry — community presence-building is not Syndicate's mode; capital and acquisition is; absence justified. No direct Portrait track shift in effect fields (DIR.PA.2). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Ring entry implicit via presence restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); faction native + district native cost (Art 02 §7). | Art 02 §6, §7 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4). ARBITER places PresenceToken on success. Network affinity evaluated at dispatch. | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Dual-resource cost (faction native + district native) reads as cross-faction-resource tier, but `cost`'s first term is missing a resource-type attribute (see schema_cleanup_log.md #22) — can't confirm tier/power match until that's fixed. Flagged, not resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | ✓ S63 |

```python
STD.CA.3 = Card(
    id      = "STD.CA.3",  version = "v1.1",
    name    = "Campaign",
    tagline = "Build local support and deepen presence in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = PresenceToken,

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
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.district(native) = 0,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(acting).presence += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Presence without roots is just occupation.",
    perspectives = {
        Guild:       "Presence is the foundation everything else is built on. We are methodical about this.",
        Directorate: "Authority requires visibility. We establish presence where the mandate requires it.",
        Network:     "Every person we reach in a district is a relationship. Relationships are how things actually change.",
        Ghost:       "Presence creates exposure. We expand only when the intelligence justifies the risk.",
        Syndicate:   "Market position requires footprint. We place ourselves where the returns justify it.",
    },
)
```

---

### STD.CA.4 — UNDERMINE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-disruption card — the destructive mirror of STD.CA.3, following the same build/demolish asymmetry as STD.CA.1/STD.CA.2. Probabilistic because you're operating against someone else's established footing. Cost vs reward: same dual cost as STD.CA.3; crit success doubles effect (−2 presence), crit fail costs PS. Portrait is selective: Guild and Directorate are negatively disposed to undercutting presence (institutional stability preference); Network is affirmative (disruption aligns with its counter-entrenchment doctrine). Ghost and Syndicate are absent — neither is doctrinally committed to presence disruption as a default.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert erosion of opponent presence is grounded — source undisclosed, structural parallel to STD.CA.2. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Directorate's conditional ("unless the target is The Network — then it is public safety") maps directly to the `where=faction(target) != Network` portrait exception. Ghost's "we prefer signal" explains their absence from affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit design choice. Doctrinal relationship does not affect disruption difficulty; ring_mod handles variation. Same rationale as STD.CA.2. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in presence disruption. CovertOperation: source undisclosed. Distinct from STD.CA.2 (presence vs. structure). | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Same dual cost as STD.CA.3. Crit success = −2 total (success + successcrit additive) — intentionally stronger than STD.CA.2 salvage; presence erosion compounds. Crit fail PS loss mirrors STD.CA.2. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — presence removal is permanent until replenished. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: undermining presence is doctrinally incongruent — "we do not erase what others have built" (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1, where=faction(target) != Network`: covert erosion conflicts with governance doctrine; exception when targeting Network — framed as "public safety," no doctrinal conflict; `where=` constrains by target identity, not outcome (DIR.PA.1, SYN.PA.2). Network `submitter=+1`: counter-entrenchment doctrine — eroding entrenched presence is on-doctrine (DIR.PA.1, SYN.PA.2). Ghost: no entry — "disruption without intelligence purpose is noise"; presence disruption is not Ghost's primary mode; absence justified. Syndicate: no entry — pragmatic observer framing, no doctrinal stake in presence disruption; absence justified. `failcrit standing -= 1` is Public Standing (Art 02), not Portrait — DIR.PA.2 clear. | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction requires self-or-adjacent presence AND target has presence > 0. Adjacency model required. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target (Art 02 §6); dual cost (Art 02 §7); failcrit `standing -= 1` (Art 02 §11). | Art 02 §6, §7; Art 02 §11 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with ring_mod. ARBITER removes PresenceToken on success; double on crit success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Dual-resource cost (faction native + district native) reads as cross-faction-resource tier, but `cost`'s first term is missing a resource-type attribute (see schema_cleanup_log.md #22) — can't confirm tier/power match until that's fixed. Flagged, not resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | ✓ S63 |

```python
STD.CA.4 = Card(
    id      = "STD.CA.4",  version = "v1.1",
    name    = "Undermine",
    tagline = "Erode an opponent's presence in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
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
    target_object   = PresenceToken,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 and
        district(target).faction(target).presence > 0
    ),
    cost        = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(target).presence -= 1,
    successcrit = district(target).faction(target).presence -= 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1, where=faction(target) != Network),
        Network:     PortraitEntry(submitter=+1),
    },

    narrative    = "The most effective opposition leaves no visible wound.",
    perspectives = {
        Guild:       "We do not erase what others have built. Even our enemies.",
        Directorate: "Covert erosion is not governance. Unless the target is The Network — then it is public safety.",
        Network:     "Entrenched presence does not become legitimate just because it has been there long enough.",
        Ghost:       "Disruption without intelligence purpose is noise. We prefer signal.",
        Syndicate:   "If their presence can be eroded, it was never well-positioned to begin with.",
    },
)
```

---

### STD.CA.5 — GATHER
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Universal intelligence card — the baseline for the Information layer. Observation does not consume local infrastructure, hence faction-native-only cost. Ghost adjacency exemption is doctrinal: remote analysis does not require physical proximity. Crit success is additive (both `success` and `successcrit` dispatch the same token type — 2 Intel Tokens total on crit). Crit fail reveals the attempt to the target, creating genuine operational risk for careless intelligence-gathering.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-gathering as a covert baseline is grounded. Ghost's adjacency exemption (remote analysis, L69) is doctrinally accurate. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "this is what we are here for" makes the affinity mechanically legible. Network's "gaps between what is said and what is true" is the sharpest perspective. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit choice. Intelligence-gathering effectiveness doesn't vary by doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions gather intelligence. CovertOperation: observation is covert. Ghost adjacency exemption is a doctrinal exception to the restriction, not a subtype change. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — intelligence-gathering generates IntelToken; dominant design intent is information acquisition, consistent with Art 04b §4.4. `doctrine_mod = None` — correct, doctrinal proximity does not affect intel-gathering effectiveness. | Art 04b §4 |
| Balance | ✓ | Single faction-native cost — cheapest intel card. Ghost effective threshold 75 (50+25 affinity). Crit success = 2 tokens total (additive). Crit fail NotificationSlip creates real operational risk. | Art 02 §7, §8, §9 |
| Effect duration | ✓ | No duration — Intel Token is a durable resource that persists until spent. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`: intelligence-gathering is core doctrine — "this is what we are here for" (DIR.PA.1, SYN.PA.2). Network: no entry — intel is a tool for Network, not their primary mode; relational growth and communication are doctrinal (absence justified). Guild: no entry — pragmatic use only; "we gather when we need to build smarter" (absence justified). Directorate: no entry — prefers formal collection; covert gathering is a tool, not a belief (absence justified). Syndicate: no entry — transactional framing, no doctrinal signal (absence justified). `failcrit` dispatches NotificationSlip — game effect, not Portrait shift (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: presence in self-or-adjacent OR Ghost exemption. | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §9); faction native cost (Art 02 §7); failcrit NotificationSlip (Art 02 §8 — subtype definition pending). | Art 02 §7, §8, §9 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with Ghost affinity. ARBITER delivers IntelToken on success, NotificationSlip to target on crit fail — Art 03 Beat 3 outcome steps (per L170; Art 07 ref is stale). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit populated identically (additive on crit), failcrit populated (fail=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Mono-resource (faction native only, single term) — matches Balance row's "cheapest intel card" floor-power framing. But `cost` is missing a resource-type attribute (see schema_cleanup_log.md #22), same gap as STD.CA.1–4; flagged, not resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.CA.5 = Card(
    id      = "STD.CA.5",  version = "v1.1",
    name    = "Gather",
    tagline = "Extract actionable intelligence about a specific faction's operations.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
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

    target_taxonomy=None,
    affinity    = faction(acting) == Ghost: threshold += 25,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 or
        faction(acting) == Ghost
    ),
    cost        = resource.faction(acting) * 1,

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, knowing is the first form of power.",
    perspectives = {
        Guild:       "Intelligence informs construction. We gather when we need to build smarter.",
        Directorate: "Information is the foundation of legitimate authority. We collect it formally.",
        Network:     "The city speaks constantly. We listen for the gaps between what is said and what is true.",
        Ghost:       "This is what we are here for. Everything else follows from understanding.",
        Syndicate:   "Information has market value. We acquire it when the return justifies the cost.",
    },
)
```

---

### STD.CA.6 — BROADCAST INTERFERENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Submission-layer Beat 2 card — places a cost modifier on Public Acts targeting a district this round. Broadcast interference is ambient, hence no presence requirement. Cost is Exposure-denominated: non-Network factions must acquire Exposure through incursion or trade, making this card natively affordable only to the Network. Network affinity reduces cost by 1 (net: 1 Exposure), making it a low-friction tactical tool for Network while remaining expensive for others.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast disruption as covert intelligence operation: ambient signal interference requires no physical presence in the district. No faction presence requirement is correct — you don't need to be there to jam a signal. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Tagline clear and grounded. Five perspectives doctrinally distinct: Guild (operational delays), Directorate (jurisdictional note), Network (strategic noise), Ghost (analytical cover), Syndicate (market inefficiency). | Art 00 §7 |
| Doctrine alignment | ✓ | Network is the primary aligned faction — signal disruption as tactical information control. Ghost benefits doctrinally (analytical cover). Directorate opposed — covert disruption conflicts with their institutional-authority doctrine. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: disruption mechanism is hidden even if cost increase is observable at Beat 4. Standard: all factions can disrupt broadcast infrastructure. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — modifies cost of a PA (submission-phase property). `function = Modify`, `subject = PublicAct` — correctly scoped and narrow. | Art 04b §4, §5 |
| Balance | ✓ | Beat 2 positional wager. Cost 2 Exposure (1 for Network via affinity). Raises PA cost +1 native — meaningful deterrence, not a hard block. No fail state. | Art 03 §9.4 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. Appropriate for a tactical cost modifier. | Art 03 §10 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: tactical information control — primary aligned faction (DIR.PA.1, SYN.PA.2). Ghost `submitter=+1`: interference creates analytical cover, consistent with Ghost's low-profile doctrine (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: covert disruption undermines institutional legitimacy; Directorate's tool is regulatory authority, not anonymous interference (DIR.PA.1, SYN.PA.2). Guild: no entry — operational delays are a cost, not a doctrinal signal; absence justified. Syndicate: no entry — market inefficiency is an opportunity, not a doctrinal stake; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — broadcast effect is ambient to the district. | Art 01 §6 |
| Supported by components | ✓ | PublicAct as target type; Exposure resource as cost. Both defined. | Art 02 §8; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0); moved to Beat 4 carry row during Beat 2 processing (Art 03 §9.4.2); arming and effect applied at Beat 4 (Art 03 §9.4.3). | Art 03 §9, §9.4, §10 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Exposure only, typed correctly). Restricted-acquisition resource narrows practical access mostly to Network/Ghost by design (per Design Rationale) — power/cost match not independently re-verified beyond that. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
STD.CA.6 = Card(
    id      = "STD.CA.6",  version = "v1.1",
    name    = "Broadcast Interference",
    tagline = "Disrupt public communications in a district, dampening public activity.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Submission,  function = Modify,  subject = PublicAct,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = PublicAct,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = game.ops(beat=4, type=PublicAct, at=district(target)).cost.native += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "People don't act naturally when they know they're being watched.",
    perspectives = {
        Guild:       "Disrupting communications delays approvals, permits, agreements. We feel this more than most.",
        Directorate: "Interference with public communications is a jurisdictional matter. We note who is responsible.",
        Network:     "Noise is a tool. Sometimes silence is louder than anything we could broadcast.",
        Ghost:       "Interference creates analytical cover. We appreciate the quiet.",
        Syndicate:   "Disrupted communications create market inefficiencies. Those can be profitable.",
    },
)
```

---

### STD.CA.7 — AMPLIFY
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Beat 2 modifier for the acting faction's own Public Act — the offensive counterpart to STD.CA.6. Amplification cuts both ways: a PA that wins +1 PS resolves as +2; a PA that loses −1 PS resolves as −2. Cost is Exposure-denominated (same as STD.CA.6), slightly favoring the Network. Restriction is None — ARBITER holds awareness through Beat 4; if no Public Act is submitted, Amplify fizzles and Exposure is spent.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covertly amplifying your own political messaging fits the covert operations frame. Ghost's categorical opposition ("volume attracts attention") is the clearest doctrinal test for the card. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's perspective is the sharpest. All five are doctrinally distinct — opposition, authority-sufficiency, tactical use, suppression logic, leverage framing. | Art 00 §7 |
| Doctrine alignment | ✓ | Amplifying public messaging strongly serves Network doctrine; strongly opposes Ghost (volume = exposure risk). Both captured via portrait entries. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: amplification mechanism is hidden. Standard: all factions can amplify their messaging covertly. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — scales the outcome (standing_impact) of a PA; Art 04b §4.2 "outcome scale" is a Resolution property. `function = Modify`, `subject = PublicAct`. Note: `resolution_type = "Transactional"` may be a misnomer — card fizzles if no PA is submitted (same positional-wager behavior as STD.CA.6). Minor schema inconsistency, not blocking. | Art 04b §4, §5 |
| Balance | ✓ | Symmetric multiplier: both success (+×2) and failure (−×2) scale. Prevents risk-free use. Fizzle (Exposure spent, no PA) ensures Beat 2 commitment is real. | Art 02 §11 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. | Art 03 §10 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: amplifying public messaging is core Network doctrine (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: amplification = attention = exposure risk — "volume attracts attention, attention ends operations" (DIR.PA.1, SYN.PA.2). Guild: no entry — "let our structures speak"; amplification is a substitute for physical evidence, not a doctrinal tool; absence justified. Directorate: no entry — institutional authority doesn't require amplification; tactical use only; absence justified. Syndicate: no entry — leverage framing is opportunistic, not doctrinal; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; card operates on acting faction's own PA submission, not a district. | — |
| Supported by components | ✓ | PublicAct as target; Exposure as cost; `standing_impact` for outcome (Art 02 §11). | Art 02 §8; Art 02 §11; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0 Beat 0); moved to Beat 4 carry row during Beat 2 processing (Art 03 §9.4.2 Beat 2); `standing_impact` multiplier applied at Beat 4 (Art 03 §17). | Art 03 §9, §11, §17 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Exposure only, typed correctly), same shape as STD.CA.6. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
STD.CA.7 = Card(
    id      = "STD.CA.7",  version = "v1.1",
    name    = "Amplify",
    tagline = "Boost the Public Standing impact of your own public act this round.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Resolution,  function = Modify,  subject = PublicAct,

    beat            = 2,
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
    target_faction  = faction.acting,
    target_object   = PublicAct,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = faction(acting).op(beat=4, type=PublicAct).standing_impact *= 2,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Network: PortraitEntry(submitter=+1),
        Ghost:   PortraitEntry(submitter=-1),
    },

    narrative    = "A message worth sending is worth sending loudly.",
    perspectives = {
        Guild:       "We let our structures speak. Amplification is for those who lack physical evidence.",
        Directorate: "Institutional authority does not require amplification. Though we note its effectiveness.",
        Network:     "Every message we send should land as hard as possible. This ensures it does.",
        Ghost:       "Amplification is the opposite of what we do. Volume attracts attention. Attention ends operations.",
        Syndicate:   "Leverage applied at the right moment can move markets. This is that tool.",
    },
)
```

---

### STD.CA.8 — BUY INFLUENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy-bypasses-Territory card — the only Standard CovertOperation with no restriction and no presence requirement. Capital buys presence directly, reflecting that money can substitute for community groundwork. Cost vs reward: 3 Capital is high but buys 2 presence on success (more than STD.CA.3's 1), and crit success adds a third. Syndicate affinity is difficulty reduction, not cost reduction — the Syndicate does not spend less; it converts capital to presence more reliably. Three portrait penalties represent strong doctrinal opposition: bought influence is an institutional threat to Guild's earned-presence model, Directorate's legitimate-process model, and Network's relational model.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Deploying capital to buy presence covertly fits the game's economic warfare frame. No presence requirement is a deliberate design feature — capital substitutes for community groundwork. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Syndicate's perspective ("capital determines which doors exist") is the sharpest statement of the card's design logic. All five perspectives doctrinally distinct. | Art 00 §7 |
| Doctrine alignment | ✓ | Card effect strongly opposes Guild (earned-presence model), Directorate (legitimate-process model), and Network (relational model); supports Syndicate doctrine. Captured via portrait entries (Guild/Directorate/Network submitter=−1, Syndicate submitter=+1). No target_faction → doctrine_mod not applicable; doctrinal signal is portrait-only by design. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: purchase mechanism is covert; resulting presence tokens are visible board state. Standard: all factions can deploy capital to buy presence. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing PresenceTokens is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | 3 Capital is the highest Standard cost. No presence restriction is the tradeoff. Success = +2 presence (superior to STD.CA.3's +1); crit = +3 total. Syndicate affinity: effective threshold 75%. Crit fail −2 PS is severe — publicly-failed capital deployment. | Art 02 §6, §8; Art 02 §11 |
| Effect duration | ✓ | Permanent: presence tokens persist until removed. Appropriate for a territorial placement card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: bought presence undermines earned-presence model (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: purchasing influence bypasses legitimate institutional process (DIR.PA.1, SYN.PA.2). Network `submitter=−1`: capital-as-power is exactly what Network opposes (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: bought presence is noisy — "draws the wrong kind of attention"; against low-profile doctrine (DIR.PA.1, SYN.PA.2). Syndicate `submitter=+1`: capital doctrine — "determines which doors exist" (DIR.PA.1, SYN.PA.2). All five entries present; four opposing, one aligned — STD.CA.8 is Syndicate's card by design. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — capital bypasses standard entry requirement. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Capital cost (Art 02 §8); failcrit PS −2 (Art 02 §11). | Art 02 §6, §8; Art 02 §11 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 3 row of Resolution Grid (Art 03 §9.4.0 Beat 0); d100 threshold 50 with ring_mod and affinity; resolved at Beat 3 (Art 03 §9.4.2 Beat 3). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Mono-resource (Capital only, typed correctly) — but Balance row already notes 3 Capital is "the highest Standard cost." P28 flags mono-resource + high-power as a check to confirm; not independently re-verified this pass. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
STD.CA.8 = Card(
    id      = "STD.CA.8",  version = "v1.1",
    name    = "Buy Influence",
    tagline = "Deploy capital to place presence tokens directly, without groundwork.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Syndicate: threshold += 25,
    restriction = None,
    cost        = resource.faction(acting).capital * 3,

    success     = district(target).faction(acting).presence += 2,
    successcrit = district(target).faction(acting).presence += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
        Network:     PortraitEntry(submitter=-1),
        Ghost:       PortraitEntry(submitter=-1),
        Syndicate:   PortraitEntry(submitter=+1),
    },

    narrative    = "In New Meridian, capital is a language everyone understands.",
    perspectives = {
        Guild:       "Presence earned through investment rather than community is fragile. We have seen it collapse.",
        Directorate: "Purchasing influence undermines the legitimate institutional processes we exist to maintain.",
        Network:     "This is exactly the kind of power we are here to expose and resist.",
        Ghost:       "Bought presence is noisier than earned presence. It draws the wrong kind of attention.",
        Syndicate:   "Capital does not just open doors. It determines which doors exist in the first place.",
    },
)
```

---

### STD.CA.9 — FUND
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Alliance-seeding card — the only card in the Standard set that transfers resources between factions. Source is anonymous by default; on success the acting faction receives an Overture modifier card (delivered from ARBITER tableau) that may be assigned to any of their PAs to initiate an Accord proposal per Art 06 §9.4. Cost vs reward: 2 Capital spent to transfer 2 Capital to the target — net zero to the actor at success, but crit success awards +1 PS and Overture opens alliance mechanics. Syndicate affinity is difficulty reduction — the Syndicate is the faction most practiced at informal financial transfers.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Anonymous resource transfer as covert act — the act of funding is covert; Overture is what potentially reveals it. Faction-to-faction relationship seeding fits the game's alliance layer. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Directorate's "we monitor these carefully" is the subtlest threat at the table. All five perspectives doctrinally distinct — relationship investment, institutional scrutiny, financial exposure, operational awareness, capital relationships. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` — `doctrine_mod = {Neighbor: +15, Opposed: -15}` applies. Syndicate affinity (+25) stacks — funding a Neighbor as Syndicate reaches effective threshold 90. Capital flows where doctrine is aligned; crosses resistance where it is not. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: anonymous transfer is covert; Overture preserves optionality on disclosure. Standard: all factions can fund others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — capital transfer is NativeResource flow, correctly Economy under Art 04b §4.4. `function = Redirect`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Net capital zero at success (2 Capital spent = 2 Capital delivered). Overture path to AccordForm costs 2 of 4 available action slots per Quarter (STD.CA.9 covert op slot + PA with Overture attached) — the slot cost is the real gate on this route, not the resource cost. Cost unchanged at 2 Capital (standard covert op cost). L201. | Art 02 §8; STD.MOD.1 |
| Effect duration | ✓ | Capital transfer is instantaneous. Overture modifier card lifecycle governed by STD.MOD.1 and Art 06 §9.4. | STD.MOD.1; Art 06 §9.4 |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Syndicate `submitter=+1`: capital-in-motion doctrine — "relationships create opportunities" (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: using anonymous financial transfer conflicts with legitimate-process doctrine; Directorate scrutinises these transfers in others — performing one is in-doctrine hypocrisy (DIR.PA.1, SYN.PA.2). Guild: no entry — relationship investment is pragmatic, not doctrinal; absence justified. Network: no entry — analytical framing only; no doctrinal stake as actor; absence justified. Ghost: no entry — observational framing; Ghost tracks capital flows for intelligence, not as participant; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; faction-level operation, no district target. | — |
| Supported by components | ✓ | Capital (Art 02 §8) ✓. Overture modifier card full spec written — STD.MOD.1. | Art 02 §8; STD.MOD.1 |
| Supported by game procedure | ⚠ | Dispatch and Beat 3 resolution ✓. Overture delivery procedure (ARBITER tableau → faction hand at Beat 3 resolution) pending Art 07 ARBITER subroutine pass. | Art 03 §9; STD.MOD.1 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital only, typed correctly); net-zero-to-actor transfer shape already covered in Balance row. | Art 00a §9.2 |

#### Outstanding Issues

- **Overture delivery procedure:** Overture delivered from ARBITER tableau to acting faction's hand at Beat 3 resolution of STD.CA.9. Exact procedure (ARBITER hands card; notation) pending Art 07 ARBITER subroutine pass.
- **Anonymous transfer case-return:** Resources delivered to target faction at Beat 3. Covert attribution preserved — acting faction not announced. Procedure pending Art 03/Art 07 pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.CA.9 = Card(
    id      = "STD.CA.9",  version = "v1.1",
    name    = "Fund",
    tagline = "Transfer resources to another faction as a gesture of support.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = NativeResource,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = None,
    doctrine_mod    = {Neighbor: +15, Opposed: -15},
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = faction(acting) == Syndicate: threshold += 25,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,

    success     = (
        faction(target).resource.capital += 2,
        arbiter.deliver(faction(acting), Overture),  # from ARBITER tableau supply
    ),
    successcrit = faction(acting).standing += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Directorate: PortraitEntry(submitter=-1),
        Syndicate:   PortraitEntry(submitter=+1),
    },

    narrative    = "Every alliance in New Meridian begins with someone extending a hand.",
    perspectives = {
        Guild:       "Investment in relationships is as important as investment in structures.",
        Directorate: "Financial transfers between factions warrant scrutiny. We monitor these carefully.",
        Network:     "Follow the money. It always leads somewhere interesting.",
        Ghost:       "Resources flowing between factions change the operational landscape. We note the direction.",
        Syndicate:   "Capital in motion creates relationships. Relationships create opportunities.",
    },
)
```

---

### STD.CA.10 — PROTECT
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Defensive Beat 2 positional wager — the only Standard card that explicitly protects existing assets. Applies only to the acting faction's assets in the named district, not the district broadly. Cost vs reward: 1 district-native paid regardless of whether an attack materializes; if it does, −25 threshold reduction (−45 for Guild/Directorate) meaningfully degrades opponents' attack probability. Guild and Directorate affinity reflects institutional defense as core competency, not exceptional response.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Defensive preparations as covert act — protection is installed silently; effect is felt at Beat 3. Positional wager structure makes the action genuinely risky (wrong read wastes the slot). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's "best protection is not being found" is the anti-use doctrine. All five perspectives distinct — obligation to defend, institutional resource, people-first, non-presence, value retention. | Art 00 §7 |
| Doctrine alignment | ✓ | Active asset defense serves Guild (protect what we build) and Directorate (institutional assets require defense) — both captured via portrait. Ghost is doctrinally opposed (concealment over fortification) — captured via portrait. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: defensive preparations are covert. Standard: all factions can protect their assets; Guild/Directorate affinity rewards institutional-defense doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — per Art 04b §4.6, Protect distributes to the target's layer. Target is CovertOperation (Resolution layer). `function = Protect`, `subject = CovertOperation` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; 1 native cost. Guild/Directorate affinity −45 locked (L179): near-nullification narratively justified — Guild knows every access point and structural vulnerability in their own infrastructure; Directorate's institutional security apparatus (personnel, protocols, access control) can effectively stop a covert demolition attempt. The 5% floor acknowledges no protection is absolute. Attacker does not know protection is installed (STD.CA.10 is covert) — near-nullification is a consequence of capability, not a visible deterrent. Base −25 (other factions) leaves 25% — acceptable risk. | Art 02 §8; Art 02 §11 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 3, does not persist past round. | — |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 3 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`: protecting built assets is non-optional doctrine — "we protect what we build" (DIR.PA.1, SYN.PA.2). Directorate `submitter=+1`: institutional assets require active defense — resourced accordingly (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: active fortification conflicts with concealment doctrine — "best protection is not being found" (DIR.PA.1, SYN.PA.2). Network: no entry — "we protect our people first; infrastructure is secondary"; situational use, not doctrinal; absence justified. Syndicate: no entry — rational asset-value framing, no doctrinal stake in fortification; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: acting presence in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (restriction); district native cost (Art 02 §8); threshold reduction applied to Beat 3 ops targeting acting assets. | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0); threshold reduction applied at Beat 3 resolution (Art 03 §9.4.3). Note: Art 03 §20 M-09 refs in prior version are stale (pre-S52 reorg). | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (district native only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Art 03 dependency:** Threshold reduction marker placement (ARBITER places −25/−45 marker on Beat 3 ops targeting acting faction's assets at Beat 2 resolution) to be defined in Art 03 §9.4 Beat 2 processing steps.
- **Status flag inconsistency (flagged S141, not resolved):** this open Art 03 dependency coexists with `Issues Resolved ✓` in the Status row below — unlike STD.CA.1's ⚠ checklist rows (which predate 04-n70/79 as tracked concepts), this is a live, undefined procedural gap in the same authoring era as the rest of the card. Left as-is per this pass's scaffold-only scope; flagging the inconsistency rather than changing the flag.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
STD.CA.10 = Card(
    id      = "STD.CA.10",  version = "v1.1",
    name    = "Protect",
    tagline = "Defend a district's assets from covert disruption this round.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Resolution,  function = Protect,  subject = CovertOperation,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = CovertOperation,

    target_taxonomy=None,
    affinity    = faction(acting) IN [Guild, Directorate]: threshold_protection = 45,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.district(native) * 1,

    success     = game.ops(beat=3, at=district(target), targeting=faction(acting).assets).threshold -= (threshold_protection if affinity else 25),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild:       PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "What you build is only worth as much as your willingness to defend it.",
    perspectives = {
        Guild:       "We protect what we build. This is not optional.",
        Directorate: "Institutional assets require active defense. We resource this accordingly.",
        Network:     "We protect our people first. Infrastructure is secondary.",
        Ghost:       "The best protection is not being found in the first place.",
        Syndicate:   "Protected assets retain value. Unprotected assets invite acquisition.",
    },
)
```

---

### STD.CA.11 — TORT INTERFERENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Standard card available to all factions — any faction with a stake in an active Accord can lock it against voluntary dissolution through back-channel means. Reflects the legal concept of tortious interference: a third party prevents two contracting parties from exiting an agreement the third party benefits from. Directorate invokes this with institutional standing; Ghost files paperwork no one can trace; Syndicate retains counsel; Network embeds the agreement in public record; Collective organizes pressure around it. Cost is 1 Mandate + 1 of the acting faction's native resource — the Mandate requirement means any faction must spend a unit of institutional authority to invoke this regardless of doctrine. Lock persists until game end or direct breach by the Accord parties; breach is not blocked, but consequences apply normally. Voluntary dissolution suspended; unilateral breach is not.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord lock — prevents voluntary dissolution of a named executed Accord; distinct from GHO.CA.4 (evidence destruction) and DIR.CA.3 (surveillance); any faction with a stake can invoke | Art 00 §7 |
| Voice fit | ✓ | Standard card; five faction perspectives by design — each faction arrives at the same outcome through different means | Art 00 §7 |
| Doctrine alignment | ✓ | Standard; 1 Mandate + 1 native resource; Mandate requirement gates casual play regardless of faction; lock/breach distinction is mechanically clean | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / Standard — lock filed covertly; acting faction not announced at resolution; effect (marked Accord) is publicly visible | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/Accord — corrupts the dissolution process; target is a defined physical component (executed Accord on table) | Art 04b §4, §5 |
| Balance | ✓ | 1 Mandate + 1 native — dual resource cost reflects invoking legal/institutional authority outside normal doctrine; balance deferred until lock enforcement defined | Art 02 §6–§7 |
| Effect duration | ✓ | Until game end or breach — not permanent in the absolute sense; releases on direct breach by parties | — |
| Persistence | ✓ | Until(game.end OR Accord(named).breach_by_party) — card leaves a physical lock marker on the Accord; lingering per design | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | No portrait entry — PS implications deferred to 04-n34 sweep | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — Accord is on table/overview, not district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | Accord (executed, on table) — physically verifiable by all players; no ARBITER ledger required | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; lock enforcement and breach detection outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Cross-faction-resource (Mandate + faction native, both typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

None — all resolved S68. District-keyed resource model makes Mandate acquirable by any faction (S68). `faction(acting).native` is existing notation precedent. Enforcement and breach detection are player-visible via the annotated public document per Governing Rule 6.1a — ARBITER does not track.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*Redesigned S68: Directorate FactionSpecific CovertOperation (Evidence Preservation) → Standard CovertOperation. Name: Evidence Preservation → Tort Interference.*

```python
STD.CA.11 = Card(
    id      = "STD.CA.11",  version="v2.0",
    name    = "Tort Interference",
    tagline = "Lock an executed Accord against voluntary dissolution until game end or breach.",
    type    = CovertOperation,  subtype = Standard,  faction = All,
    layer   = Information,  function = Corrupt,  subject = Accord,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Permanent,
    persistence_condition = not (game.end OR Accord(named).breach_by_party),
    persistence_effect    = None,
    target_district=None, target_faction=None, target_object=Accord(executed, on_table),
    target_taxonomy=None,
    affinity=None,
    restriction = Accord(named).is_executed == True AND Accord(named).on_table == True,
    cost        = resource.faction(acting).mandate * 1 + resource.faction(acting).native * 1,
    success     = game.lock(Accord(named), until=game.end OR Accord(named).breach_by_party),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The agreement stands. Whatever your reasons for wanting out, the record disagrees.",
    perspectives = {
        Directorate: "The agreement is now a matter of institutional record. Dissolution would require a filing no one is prepared to make.",
        Ghost:       "The paperwork has been submitted. Quietly. Neither party knows who filed it.",
        Syndicate:   "We have an interest in this arrangement continuing. Our lawyers agree.",
        Network:     "We have made this agreement part of the public record. Dissolving it now would be a story.",
        Collective:  "We hold both parties to what they agreed to. The community remembers.",
    },
    design_note  = "Redesigned S68: Directorate FactionSpecific CovertOperation (Evidence Preservation) → Standard CovertOperation. Any faction with a stake in an active Accord can lock it against voluntary dissolution. Cost: 1 Mandate + 1 faction native resource. Lock persists until game end or direct breach by Accord parties — breach not blocked, consequences apply normally.",
    arbiter_note = "ARBITER annotates the named Accord document at Beat 3 — writes 'cannot voluntarily dissolve' or marks equivalent field on the Accord blank (TBD Art 06). No new component. Annotation is public; faction players enforce. Annotation is voided if either party directly breaches the Accord terms — breach consequences apply normally. Acting faction identity is not announced at resolution.",
)
```

---

### STD.CA.12 — ABSOLUTE COMPROMISE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Standard counter-counter card — the only card available to all factions that removes active Block or Protect plays before they can apply. Addresses the problem that committed defensive plays (Invoke Jurisdiction, Regulatory Capture, Fortify Structure, Protect) otherwise have no counter in the same round.

**Scope (confirmed S119/S120):** Absolute Compromise targets all cards with `function=Block` or `function=Protect` in the Beat 2 row — CA cards in ARBITER's covert grid and Protect/Fortify modifier plays in the Faction Resolution Grid. ARBITER has full visibility of the covert grid and executes the removal sweep from that position; the acting faction commits a blanket sweep without disclosing what was removed. Countermeasure Cards (CM-A, CM-B) are not valid targets: they are processed at Beat 1 and discarded before Beat 2 begins (Art 03 §9.4.1.2). CM-B modifier tokens left on operations are also not targetable — they are not Block/Protect cards.

Intel token cost makes this a premium play — factions must hold Intel specifically to access this capability, reinforcing Intel as a cross-faction strategic resource. Positioned here from Art 04 §8 (retired) where it was misplaced: STD.CA.12 is subtype=Standard (all factions), not FactionSpecific.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Counter-counter card — removes a committed Beat 2 Block or Protect before it applies; fills gap where defensive positional wagers have no standard counter | Art 00 §7 |
| Voice fit | ✓ | Standard card; all-faction access; no faction-specific voice required; perspectives block expected for full Standard spec — confirm complete in code block | Art 00 §7 |
| Doctrine alignment | ✓ | N/A — Standard card; no faction doctrine alignment required; no affinity; portrait = {} | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / Standard / faction=All — all-faction counter-counter capability; no faction restriction | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — removes a submitted covert op's effect before it applies; Block function correct | Art 04b §4, §5 |
| Balance | ✓ | Intel token for one Beat 2 card removal — premium cost justified by cross-faction utility; resources on discarded card not refunded (confirmed S120 — GR 7.2b consistent) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: target card discarded at Beat 2 resolution; no lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces target Beat 2 card exists | — |
| Portrait validity | ✓ | portrait = {} — Standard card; no portrait entry confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — Beat 2 cards are district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; Beat 2 Block or Protect card as target (function=Block or function=Protect per Art 04b taxonomy) — scope resolved S119, CA-inclusive | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; target card must exist in Beat 2 row at resolution; discard occurs at Beat 2. CM cards are not valid targets — processed and discarded at Beat 1 (Art 03 §9.4.1.2) before CA.12 fires. Valid targets: CA cards (function=Block or function=Protect) and Protect/Fortify modifier plays. | Art 03 §9.4.1.2, §9.4.2 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. `cost = IntelToken(any) * 1` — Intel Token as `cost` is a discrete, individually-tracked object, not a fungible native/Capital/Mandate resource. Second confirmed instance of the open question logged in schema_cleanup_log.md #10 (first was DIR.MOD.9) — flagged, not resolved. | Art 00a §9.2 |

#### Outstanding Issues

None — all design questions resolved S119/S120:
- Scope: CA-inclusive (covert grid + public Protect/Fortify). ARBITER sweeps both domains at Beat 2. S119.
- CM interaction: Countermeasure Cards (both types) are Beat 1 — processed and discarded at §9.4.1.2 before Beat 2 begins. CA.12 never encounters a live CM card. S120 (Art 03 §9.4.1.2 read).
- Scope boundary: SYN.CA.4 Golden Parachute and SYN.CA.6 Parasitic are Beat 2 Automatic but not function=Block/Protect — not valid targets. S119.
- Resource refund: no refund (GR 7.2b consistent — committed resources are sunk). S120.
- Remaining: 04-n70 (schema) + 04-n79 (narrative) — infrastructure sweeps only.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Standard Covert section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
STD.CA.12 = Card(
    id      = "STD.CA.12",  version="v1.0",
    name    = "Absolute Compromise",
    tagline = "Some barriers are not barriers at all — just the illusion of one.",
    type    = CovertOperation,  subtype = Standard,  faction = All,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=None, target_object=Beat2BlockOrProtectCard,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target).beat2_row.has_block_or_protect_card == True,
    cost        = IntelToken(any) * 1,
    success     = game.discard(target_card, district(target).beat2_row),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "There are no walls. There are only varying degrees of access.",
    perspectives = {},
    design_note  = "Scope (S119): CA-inclusive — targets Block/Protect plays in both the Faction Resolution Grid (Type A CMs, Protect/Fortify modifier plays) and ARBITER's covert resolution grid (Beat 2 CA cards with function=Block or function=Protect). Cannot target Type B Countermeasures (faction defense — reduces difficulty, not a Block/Protect play). Intel token consumed is any held token.",
    arbiter_note = "At Beat 2 resolution: sweep both grid domains. (1) Faction Resolution Grid: discard any Type A Countermeasure or Protect/Fortify modifier play targeting the named district. (2) Covert grid: discard any Beat 2 CA with function=Block or function=Protect from the named district row. Resources committed to discarded cards are not refunded. Operations those cards would have affected proceed without the modifier.",
)
```

---

### STANDARD — DISINFORMATION CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
First Standard card with Public Standing shift as its primary covert effect — fills the Standing/Shift coverage gap flagged in Art 04b §8. Distinct from Public Act PS cards (STD.PA.4, STD.PA.7): this is a covert operation, so the acting faction is unknown to the target. Presence restriction grounds it in operational reality: you need a footprint in a district to run a local narrative operation. The failcrit NotificationSlip follows DIR.CA.2 precedent — a badly botched campaign leaves traces, and ARBITER notifies the target that a campaign ran in that district (not who ran it). Network affinity (threshold +10) reflects broadcast infrastructure amplifying covert narrative reach. Ghost affinity (cost −1) reflects datastream manipulation as native capability.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert narrative manipulation as a standard capability: all factions can conduct local perception operations against each other | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild notices effects rather than participating; Directorate opposes covert image manipulation on principle; Network values the tool but distinguishes signal from noise; Ghost flags the attention risk; Syndicate tracks market implications | Art 00 §7 |
| Doctrine alignment | ✓ | Network affinity (threshold +10): broadcast infrastructure amplifies narrative reach. Ghost affinity (cost −1): datastream manipulation is native capability. Directorate portrait −1: covert manipulation conflicts with institutional legitimacy doctrine. No doctrine_mod (no faction target for modifier) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: the source of the campaign is hidden. Standard: all factions can contest standing via covert narrative operations | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — first Standard covert card in this taxonomy slot | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 40, ring_mod standard. Success swing: target −2 PS, acting +1 PS (net 3). Fail: acting −1 PS. Presence restriction limits targeting. Failcrit exposure risk makes reckless use costly | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are Immediate; no lasting marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Network +1: broadcasting narrative to shift perception is core doctrine (DIR.PA.1, SYN.PA.2). Ghost −1: public narrative campaigns attract attention, conflicting with low-profile doctrine (DIR.PA.1, SYN.PA.2). Directorate −1: covert image manipulation undermines institutional legitimacy (DIR.PA.1, SYN.PA.2). Guild, Syndicate: no entry — neither has a doctrinal stake in covert narrative authorship | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; restriction checks acting faction's presence in that district | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. PS tracked on Public Standing track (Art 02 §7); NotificationSlip (failcrit, same as DIR.CA.2) | Art 02 §7; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; NotificationSlip failcrit follows DIR.CA.2 established procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/fail/failcrit populated (successcrit=None), no `game.choose_one()` or conditional branching in any tier — each resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (faction native only, typed correctly). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_DisinformationCampaign = Card(
    id      = "STD.CA.13",  version = "v1.0",
    name    = "Disinformation Campaign",
    tagline = "Run a covert narrative operation degrading a faction's public standing in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

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

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Network: threshold += 10,
        faction(acting) == Ghost:   cost.resource.native -= 1,
    ),
    restriction = faction(acting).presence(target_district) > 0,
    cost        = resource.faction(acting).native * 2,

    success     = (faction(target).standing -= 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = (
        faction(acting).standing -= 2,
        arbiter.dispatch(NotificationSlip(type="Disinformation Campaign", district=target_district), target_faction),
    ),

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "The city's opinion is infrastructure. It can be built. It can be demolished.",
    perspectives = {
        Guild:       "Narrative operations are not our toolset. We notice the shift after the quarter closes.",
        Directorate: "Covert image manipulation conflicts with the institutional legitimacy we exist to uphold. We note who deploys it.",
        Network:     "We have channels built for exactly this. Using them properly is what separates signal from noise.",
        Ghost:       "A successful operation leaves no signature. Campaigns draw attention. This is the compromise.",
        Syndicate:   "Standing shifts move markets and tables. We note who runs this and in which districts.",
    },
    design_note  = "First Standard covert card with PS shift as primary effect — fills Standing/Shift coverage gap. Presence restriction: must have operational footprint to run local narrative operation. Success swing: target −2 PS, acting +1 PS (net 3). Fail: acting −1 PS. Failcrit: acting −2 PS + NotificationSlip to target (campaign ran against you in [district] this Month; not who ran it). Ring modifier: harder in Core (denser institutional oversight). Standard equivalents under Principle 17: Network and Ghost have superior faction-specific versions.",
    arbiter_note = "Beat 0: confirm acting faction has presence (token or deployment marker) in target district; if not — op voided, resources returned. Beat 3: roll d100. Success: target −2 PS, acting +1 PS. Fail: acting −1 PS. Fail crit (01–05): acting −2 PS; dispatch NotificationSlip to target faction ('A disinformation campaign was run against you in [district] this Month'). Target does not learn who ran it.",
)
```

---

### STANDARD — DISPROVE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Fills the Economy/Remove/IntelToken coverage gap in the Standard card set. All factions have operational reason to destroy intelligence records held against them or a rival — no faction has a doctrine-native advantage for the act of destruction itself, so no affinity is warranted. Blind random removal: the acting faction names a target faction; ARBITER draws one Intel token at random from that faction's supply and removes it from play. Silent on success — the target receives no notification and discovers the loss only on a count. Cost 2 native reflects the offensive nature of a pure denial operation with no material return. Fails automatically if target holds no tokens at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert destruction of opponent's intelligence records is a standard operational capability — all factions have grounds for denial operations against intel supply | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild reads operational records as accountability; Directorate holds institutional record preservation as principle; Network frames destruction as information erasure; Ghost frames it as operational security; Syndicate reads it as supply-side intelligence management | Art 00 §7 |
| Doctrine alignment | ✓ | No affinity — no faction has doctrine-native advantage for destroying a third party's intelligence tokens. Ghost portrait +1: operational security doctrine aligns with removing incriminating records. Network portrait −1: information destruction conflicts with transparency doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source of removal is hidden. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/IntelToken — fills coverage gap per Art 04b §6 | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45, ring_mod None (no district target). Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Pure denial — no material gain | Art 02 §5 |
| Effect duration | ✓ | Immediate — token destroyed at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1: destroying records aligns with low-profile and operational security doctrine. Network −1: information erasure conflicts with transparency and broadcast doctrine. Guild, Directorate, Syndicate: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operation targets faction's supply directly | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02 §5); no new components required | Art 02 §5 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; ARBITER blind draw from supply is consistent with ARBITER draw authority | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success only populated (successcrit/fail/failcrit all None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (faction native only, typed correctly). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_Disprove = Card(
    id      = "STD.CA.14",  version = "v1.0",
    name    = "Disprove",
    tagline = "Covertly destroy one Intel token held in an opponent's supply.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Remove,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
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
    target_object   = IntelToken.any,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(IntelToken, source=faction(target).supply,
                      count=1, action=destroy),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Ghost:   PortraitEntry(submitter=+1),
        Network: PortraitEntry(submitter=-1),
    },

    narrative    = "What the record does not contain cannot be verified.",
    perspectives = {
        Guild:       "Operational evidence is a fact of the city. We account for what we do. Who removes the accounting is who fears it.",
        Directorate: "The record exists for a reason. Selectively removing it undermines the institutional process we exist to uphold.",
        Network:     "Every destroyed token is a story that will never be told. That is not intelligence. That is erasure.",
        Ghost:       "Evidence that does not exist cannot follow you. This is the most important lesson we teach.",
        Syndicate:   "Market intelligence has a half-life. The fastest way to extend it is to reduce the competition's supply.",
    },
    design_note  = "Standard covert op targeting an opponent's Intel token supply via blind random removal — ARBITER draws one token from target's supply without acting faction specifying which. No district restriction; no affinity (destroying evidence has no faction-native doctrine edge). Silent on success: target receives no notification. Automatic fail if target holds no tokens at Beat 3 (cost sunk).",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply and remove from play (return to box). Acting faction receives no information about the removed token. Target faction receives no notification.",
)
```

---

### STANDARD — INTEL EXTRACTION
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/IntelToken — splits Asset Extraction (S62) into two focused cards. Blind random draw: ARBITER transfers one Intel token from the target faction's supply to the acting faction's dispatch case, face-down. Acting faction discovers the token's content privately at Beat 3 resolution when the case opens; ARBITER does not announce content. Target faction's token count decreases visibly. Cost 2 native: extracting and getting away clean with a resource is operationally harder than destroying it. Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence infrastructure aligns Syndicate with resource acquisition by any means, but physical covert acquisition is not Syndicate's mechanical specialty — no threshold bonus warranted. Fails automatically if target holds no tokens at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's Intel tokens is a standard economic-denial operation — acting faction gains an intelligence asset while the target loses one | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take others' gathered work; Directorate opposes covert acquisition as bypassing sanctioned process; Network notes the token continues to exist; Ghost treats it as native operational methodology; Syndicate reads it as capital intelligence arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence motivation aligns Syndicate with resource acquisition — no mechanical threshold bonus, physical acquisition is not Syndicate-native. Directorate portrait −1: covert acquisition bypasses legitimate process. Guild portrait −1: taking what others gathered | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: acting faction unknown; target's count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/IntelToken — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Double effect (acting gains, target loses) justifies same cost as pure-denial Disprove | Art 02 §5 |
| Effect duration | ✓ | Immediate — token transferred at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking what others gathered conflicts with earned-value principle. Directorate −1: bypasses sanctioned intelligence handling. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's supply | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02 §5); dispatch case procedure established (Art 03 §9.4); no new components | Art 02 §5; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success only populated (successcrit/fail/failcrit all None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (faction native only, typed correctly). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_IntelExtraction = Card(
    id      = "STD.CA.15",  version = "v1.0",
    name    = "Intel Extraction",
    tagline = "Covertly transfer one Intel token from an opponent's supply into your dispatch case.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
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
    target_object   = IntelToken.any,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Ghost: threshold += 10,
    ),
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(IntelToken, source=faction(target).supply,
                      count=1, action=transfer(faction(acting).case, face_down=True)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Syndicate:   PortraitEntry(submitter=+1),
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "Information doesn't belong to anyone. It belongs to whoever holds it.",
    perspectives = {
        Guild:       "We do not take what others have built. The intelligence they gathered represents real work.",
        Directorate: "Covert acquisition bypasses every sanctioned process for handling intelligence. We treat the result accordingly.",
        Network:     "A token in a different hand does not cease to be information. The question is what it becomes.",
        Ghost:       "Their intelligence is now a liability. Ours is now an asset. The operation is the same.",
        Syndicate:   "Capital intelligence infrastructure exists precisely for this — locating value before the market prices it in.",
    },
    design_note  = "Economy/Redirect/IntelToken — splits Asset Extraction (S62) into two cards. Blind random draw from target's supply; acting faction receives token face-down in case, inspects privately at Beat 3 resolution. Target's token count decreases visibly (visible resource denial). Ghost affinity (threshold +10): covert acquisition doctrine. Syndicate portrait +1: capital intelligence motivation, no threshold bonus (physical acquisition is not Syndicate-native). Automatic fail if target holds no tokens at Beat 3.",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's token count decreases by 1 (visible).",
)
```

---

### STANDARD — MODIFIER RAID
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/ModifierCard — splits Asset Extraction (S62) alongside Intel Extraction, with modifier cards as the target resource. Same blind draw mechanic: ARBITER transfers one modifier card at random from the target faction's hand to the acting faction's dispatch case, face-down. Acting faction discovers the card privately at Beat 3 resolution. Target faction's card count decreases visibly. Modifier cards represent prepared tactical advantages — stealing one simultaneously strips the opponent's preparation and delivers that advantage to the acting faction. Same affinity structure as Intel Extraction (Ghost threshold +10; Syndicate portrait +1). Cost 2 native. Fails automatically if target holds no modifier cards at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's modifier cards simultaneously denies their tactical preparation and transfers that advantage to the acting faction | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take tools others made; Directorate opposes covert seizure of operational resources; Network notes the card's function shifts by context; Ghost targets the tactical disruption aspect; Syndicate reads it as operational arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition doctrine, same as Intel Extraction. Syndicate portrait +1: resource acquisition by covert means aligns with capital intelligence doctrine. Same affinity structure as Intel Extraction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source hidden; target's card count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/ModifierCard — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Parallel structure to Intel Extraction — same cost and threshold for same operational profile. Automatic fail if target holds no modifier cards at Beat 3 | Art 02 §5 |
| Effect duration | ✓ | Immediate — card transferred at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking tools others built conflicts with earned-value principle. Directorate −1: seizure of operational resources bypasses legitimate process. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's modifier card hand | Art 01 §6–§7 |
| Supported by components | ✓ | Modifier cards (Art 02); dispatch case procedure established (Art 03 §9.4); no new components | Art 02; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success only populated (successcrit/fail/failcrit all None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (faction native only, typed correctly). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_ModifierRaid = Card(
    id      = "STD.CA.16",  version = "v1.0",
    name    = "Modifier Raid",
    tagline = "Covertly transfer one modifier card from an opponent's hand into your dispatch case.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = ModifierCard,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
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
    target_object   = ModifierCard.any,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Ghost: threshold += 10,
    ),
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(ModifierCard, source=faction(target).hand,
                      count=1, action=transfer(faction(acting).case, face_down=True)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Syndicate:   PortraitEntry(submitter=+1),
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "They packed for an operation they will never run.",
    perspectives = {
        Guild:       "Tools are built for a purpose. Taking them from someone who made them is not the same as earning them.",
        Directorate: "Seizing operational resources outside any sanctioned process is the definition of what we are here to prevent.",
        Network:     "A modifier card in the wrong hand is a signal on the wrong frequency. It still transmits.",
        Ghost:       "Strip their tactical advantage before they deploy it. The modifier they held is now the one we use.",
        Syndicate:   "Their preparation becomes our edge. That is the nature of capital intelligence — arbitrage at the operational level.",
    },
    design_note  = "Economy/Redirect/ModifierCard — splits Asset Extraction (S62) into two cards alongside Intel Extraction. Blind random draw from target's modifier hand; acting faction receives card face-down in case, inspects privately at Beat 3 resolution. Target's card count decreases visibly. Ghost affinity (threshold +10); Syndicate portrait +1. Automatic fail if target holds no modifier cards at Beat 3.",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero modifier cards, op fails (cost sunk; do not announce reason). Otherwise, draw one modifier card at random from target faction's hand. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's modifier card count decreases by 1 (visible).",
)
```

---


---

### Standard — Public Acts
[↑ Standard](#standard)

Public acts use the same data schema as covert operations (§6) with two additional fields:

| Additional Field | Description |
|-----------------|-------------|
| **Popularity effect** | Popularity movement on success and failure. |
| **Declaration requirement** | Any verbal or physical declaration required at time of play. |

Public acts are Beat 4 cards unless otherwise specified.

| Card | Name |
|------|------|
| [STD.PA.1](#p01-open-operations) | Open Operations |
| [STD.PA.2](#p02-disputed-claim) | Disputed Claim |
| [STD.PA.3](#p03-public-commission) | Public Commission |
| [STD.PA.4](#p04-public-censure) | Public Censure |
| [STD.PA.5](#p05-on-the-record) | On the Record |
| [STD.PA.6](#p06-economic-sanction) | Economic Sanction |
| [STD.PA.7](#p07-public-address) | Public Address |
| [STD.PA.8](#p08-table-an-accord) | Table an Accord |

### STD.PA.1 — OPEN OPERATIONS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.3 (Campaign). Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. The trade: covert presence-building is hidden but risky (d100/50, fail wastes cost); Open Operations is visible from Phase B declaration but certain. Directorate's cost waiver reflects that formal institutional presence declaration is a zero-friction doctrinal act — the mandate is the permission. Ghost's portrait −1 captures the cost of committing to visibility against concealment doctrine.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public territorial declaration is a core political act in New Meridian — every faction makes formal presence claims | Art 00 §7 |
| Voice fit | ✓ | Five distinct perspectives: Guild grounds it in the build, Directorate in the record, Network in confirmation, Ghost in commitment-cost, Syndicate in sequencing | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate affinity (cost = 0) + portrait +1. Ghost portrait −1. Others no entry — justified | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — all factions make public presence claims; universally useful | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — unambiguous | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.3; Automatic vs. d100/50; +PS. Trade is visibility, not resources | Art 02 §6–§7 |
| Effect duration | ✓ | Presence tokens are Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded (SYN.PA.2). Ghost −1: submitter-bounded. No direct PS shift in portrait (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring entry enforced at Beat 0 by ARBITER | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4 resolution; ring entry rules enforced at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated (successcrit/fail/failcrit all `None`) — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 2), but `cost`'s term is missing a resource-type attribute. Cross-card claim ("same cost as STD.CA.3") also checked and found false. Tier assessment blocked until cost bug resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.1 = Card(
    id      = "STD.PA.1",  card_id="STD.PA.1",  version="v1.0",
    name    = "Open Operations",
    tagline = "Formally declare your operational presence in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Directorate: cost.faction(native) = 0,
    restriction = None,  # ring entry enforced universally at Beat 0
    cost        = resource.faction(acting) * 2,
    boost       = None,

    success     = (district(target).faction(acting).presence += 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "A formal declaration carries weight in New Meridian. Presence on the record is presence that cannot be denied.",
    perspectives = {
        Guild:       "We are here. What we build will say the rest.",
        Directorate: "Formal establishment of operations in this district. The record reflects it.",
        Network:     "Our presence here was always going to be known. This makes it official.",
        Ghost:       "Every formal declaration is a commitment we would rather not have made.",
        Syndicate:   "The first step is always claiming the position. Everything else follows.",
    },
    design_note  = "Public version of STD.CA.3 Campaign. Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. Trade: covert = hidden + risky vs. public = visible + certain. Directorate affinity: formal institutional presence declaration has no resource cost against mandate doctrine. Ghost −1: visibility conflicts with concealment doctrine. Ring entry rules still enforced by ARBITER at Beat 0.",
    arbiter_note = "Place 2 presence tokens for acting faction in declared district at Beat 4. Apply PS +1 to acting faction. Confirm ring entry requirements at Beat 0 — if not satisfied, PA voided; resources returned; acting faction takes Public Pass.",
)
```

---

### STD.PA.2 — DISPUTED CLAIM
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.4 (Undermine). Same cost (2 native), slightly better base threshold (45 vs 40), PS effects added. Going public here means accepting accountability: a failed challenge hurts the challenger's standing. Network and Directorate gain threshold bonuses reflecting doctrinal alignment with formal territorial dispute mechanisms. The fail/failcrit PS penalties make this meaningfully riskier than it looks — public challenges are public commitments.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal territorial challenges are institutionally grounded in New Meridian | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible and distinct: Guild's reluctance-but-will-defend, Directorate's formal-mechanism preference, Network's public-accountability, Ghost's attention-cost framing, Syndicate's leverage reading | Art 00 §7 |
| Doctrine alignment | ✓ | Network +10 threshold + portrait +1; Directorate +10 threshold + portrait +1 — formal dispute mechanisms align with both doctrines. Ghost portrait −1: public confrontation conflicts with concealment. doctrine_mod captures target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — all factions contest territory | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken — target is a PresenceToken being removed | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.4; slightly better threshold; PS effects add risk on fail. Contested marker fires on tie — procedural | Art 02 §6–§7 |
| Effect duration | ✓ | Presence token removal is a permanent state change; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: all submitter-bounded (SYN.PA.2). PS effects are game effects, not Portrait shifts (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring_mod calibrated to ring context | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — target removal (Art 02 §6); ContestedMarker — procedural (Art 03 §9.4); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 4; Contested marker placement governed by Art 03 §9.4; ring_mod applies | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. `resolution_type = "Contested"` — not in the confirmed 2-value vocabulary (`"Probabilistic"`/`"Transactional"`). Corpus-wide grep confirms 10 instances of `"Contested"` alone, plus 7 other unconfirmed values (`"Permanent public act"`, `"Positional wager"`, `"Conditional"`, `"Deceptive"`, `"Predictive"`, `"Verification"`, `"PlayerChoice(target)"`). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/fail/failcrit populated (successcrit=`None`), no `game.choose_one()` or conditional branching in any tier. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 2), but `cost`'s term is missing a resource-type attribute. Cross-card claim ("same cost, 45 vs 40 threshold, as STD.CA.4") checked directly and found false on both counts — STD.CA.4's actual cost is dual-resource, actual threshold is 50, not 40. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.2 = Card(
    id      = "STD.PA.2",  card_id="STD.PA.2",  version="v1.0",
    name    = "Disputed Claim",
    tagline = "Formally challenge another faction's presence in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = {Neighbor: +10, Opposed: -10},
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Network:    threshold += 10,
        faction(acting) == Directorate: threshold += 10,
    ),
    restriction = faction(target).influence_tier(target_district) >= Established,
    cost        = resource.faction(acting) * 2,
    boost       = None,

    success     = (
        district(target_district).faction(target).presence -= 1,
        if tie_condition(target_district): arbiter.place(ContestedMarker, target_district),
        faction(acting).standing += 1,
        faction(target).standing  -= 1,
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "A contested district is not a resolved one. Filing a formal challenge makes the dispute legible.",
    perspectives = {
        Guild:       "We would rather build than challenge. But we will not cede ground claimed without cause.",
        Directorate: "A formal challenge is the legitimate mechanism for resolving territorial disputes. We prefer it to ambiguity.",
        Network:     "Presence built on hollow ground should not stand. We will say so publicly.",
        Ghost:       "Public challenges create public attention. Attention is expensive.",
        Syndicate:   "Challenges are leverage. The willingness to file one changes the calculus of every faction at the table.",
    },
    design_note  = "Public version of STD.CA.4 Undermine. Same cost (2 native); threshold 45 vs STD.CA.4's 40; PS consequences added. Fail/failcrit penalise the challenger — public challenges are public commitments. Network/Directorate +10 threshold: doctrinal alignment with formal dispute mechanisms. Ghost −1: public confrontation conflicts with concealment doctrine. doctrine_mod: Neighbor +10, Opposed −10 on target faction relationship.",
    arbiter_note = "Beat 4. Remove 1 presence token from target faction. Check for tie at highest chip count — if tie at 3+ chips, place Contested marker. PS: acting +1, target −1 on success. Acting −1 on fail. Acting −2 on failcrit (no token removed on fail/failcrit).",
)
```

---

### STD.PA.3 — PUBLIC COMMISSION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.1 (Build Structure). Same cost; unlike STD.CA.1, the construction is publicly announced at Phase B and ARBITER records it. The covert element is absent — there is no hidden intent here. Going public provides certainty (Automatic) and PS +1 versus STD.CA.1's concealed attempt with failure risk. Guild's affinity (district native = 0) is maximally on-doctrine here: Guild building in public is the purest expression of permanence doctrine. Ghost's portrait −1 reflects that public structures are commitments Ghost would not voluntarily create.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public construction is a core territorial act — all factions build where the strategy demands it | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct and credible: Guild's open permanence, Directorate's mandate/record framing, Network's observation of public statements, Ghost's accountability-cost, Syndicate's visible-portion-of-investment framing | Art 00 §7 |
| Doctrine alignment | ✓ | Guild affinity (district native = 0) + portrait +1 — maximally on-doctrine (permanence through building). Ghost −1: permanent public structure conflicts with concealment. Others: no doctrinal stake in public construction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — structure building is universally available; Guild affinity appropriate but not exclusive | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.1; Automatic vs d100; PS +1. Trade: visibility for certainty. Guild effectively pays 1 native (affinity waives district native) | Art 02 §6–§7 |
| Effect duration | ✓ | StructureBlock = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1, Ghost −1: submitter-bounded. Same doctrine logic as STD.CA.1 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks district presence and structure state (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §7); PresenceToken — restriction (Art 02 §6); faction native + district native costs (Art 02 §8) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 4; restriction checked at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Dual-resource cost (faction native + district native), identical expression to STD.CA.1 — cross-card claim ("same cost as STD.CA.1") checked directly and confirmed true. Same missing resource-type attribute as its CA counterpart. Tier assessment blocked until cost bug resolved. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.3 = Card(
    id      = "STD.PA.3",  card_id="STD.PA.3",  version="v1.0",
    name    = "Public Commission",
    tagline = "Publicly announce and fund construction of a structure in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Guild: cost.resource.district(native) = 0,
    restriction = (
        district(target).faction(acting).presence > 0 and
        district(target).faction(acting).structure == 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,
    boost = None,

    success     = (district(target).faction(acting).structure += 1, faction(acting).standing += 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild: PortraitEntry(submitter=+1),
        Ghost: PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "Every faction that wants to be taken seriously in New Meridian eventually has to build something where everyone can see it.",
    perspectives = {
        Guild:       "We build in the open because the work is not something we need to hide.",
        Directorate: "Infrastructure serves the mandate. We build when the district requires it and the record supports it.",
        Network:     "Building is a public statement. We attend to what the statement claims.",
        Ghost:       "A structure in public view is a structure we have to account for.",
        Syndicate:   "The public commission is the visible portion of the investment. The value is in what follows.",
    },
    design_note  = "Public counterpart to STD.CA.1. Same cost; Automatic (no fail risk); PS +1. Guild affinity (district native = 0) on-doctrine. Ghost −1: public structure = permanent commitment against concealment doctrine. Counter to Guild's build pace: Directorate DIR.PA.1 (Regulatory Override) raises cost of presence-placement in district (prerequisite for this card); GUI.PA.1 (Civic Works Mandate) can be blocked by DIR.PA.1.",
    arbiter_note = "Place 1 structure block for acting faction in declared district at Beat 4. PS +1. Restriction at Beat 0: acting faction must have presence and no existing structure. If restriction fails, PA voided.",
)
```

---

### STD.PA.4 — PUBLIC CENSURE
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The PS attack card of the standard set. A formal public accusation carries both potential and risk — a failed censure reflects worse on the accuser than the target. Network and Directorate get cost reductions (accusation is their institutional/broadcast mode). An optional Fresh Intel token submitted at Phase B provides a +15 threshold bonus, rewarding prior intelligence work. The fail and failcrit costs ensure reckless censure is punished. Ghost's portrait −1 reflects that self-exposure is the cost of public accusation.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accusations are a core political act — all factions can and do make them | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible: Guild's evidence-based restraint, Directorate's formal mechanism framing, Network's public-fact stance, Ghost's attention-trace surveillance read, Syndicate's public-leverage calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network −1 cost + portrait +1; Directorate −1 cost + portrait +1 — formal accusation aligns with institutional/broadcast doctrines. Ghost −1 portrait: public accusation = self-exposure. Intel token affinity is doctrinally neutral. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ⚠ | Standing / Shift / PublicStanding — code correctly uses `subject = StandingMarker`; prose still says the retired term (corrected S126). Same pattern as DIR.CA.7/NET.CA.7 (schema_cleanup_log.md item 4-F); flagged, not corrected. | Art 04b §4 |
| Balance | ✓ | Base threshold 35 is demanding; Intel token affinity rewards preparation. Fail/failcrit PS penalties create real downside | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: submitter-bounded. PS shifts are game effects not Portrait (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (optional, Fresh — spent on resolution regardless; Art 02 §6); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case at Phase B; token spent regardless | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. `resolution_type = "Contested"` — same missed-then-caught vocabulary gap as STD.PA.2. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/fail/failcrit populated (successcrit=`None`), no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 2), untyped resource-type attribute. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.4 = Card(
    id      = "STD.PA.4",  card_id="STD.PA.4",  version="v1.0",
    name    = "Public Censure",
    tagline = "Formally accuse another faction of conduct contrary to the city's interest.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = d100,
    threshold       = 35,
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
    affinity    = (
        faction(acting).holds_intel_token(faction=target, age=Fresh): threshold += 15,  # token optional; spent on resolution
        faction(acting) == Network:     cost.faction(native) -= 1,
        faction(acting) == Directorate: cost.faction(native) -= 1,
    ),
    restriction = target_faction != faction(acting),
    cost        = resource.faction(acting) * 2,
    boost       = None,

    success     = (faction(target).standing -= 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "A formal accusation in New Meridian is not a rumor. It is a claim that goes into the record and demands a response.",
    perspectives = {
        Guild:       "We do not make accusations we cannot support. But we do not stay silent when the conduct is clear.",
        Directorate: "Formal censure is the legitimate response to misconduct. The mechanism exists for a reason.",
        Network:     "The city deserves to know. We are not making an allegation — we are making a fact public.",
        Ghost:       "Public censure creates public attention. We note that the accusation traces back to whoever filed it.",
        Syndicate:   "Censure is leverage applied publicly. The question is always: what does the target do next?",
    },
    design_note  = "PS attack card of the standard set. Base threshold 35 — demanding. Fresh Intel token (optional, placed on PA at Art 03 §9.2.0, spent regardless of outcome) provides +15 threshold. Network/Directorate −1 cost each. Fail/failcrit PS penalties punish reckless censure. Ghost −1 portrait: public accusation = self-exposure. PS shifts in success/fail are game effects, not Portrait (DIR.PA.2).",
    arbiter_note = "At Art 03 §9.2.0: acting faction places PA with Target Profile face-down; Intel token (if submitted) placed on card. At Art 03 §9.4.3.1.1: flip Target Profile face-up; note target faction. Beat 4: threshold = 35 + 15 if Fresh Intel token on card. On success: target −2 PS, acting +1 PS; Intel token spent. On fail: acting −1 PS; Intel token still spent. On failcrit: acting −2 PS.",
)
```

---

### STD.PA.5 — ON THE RECORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Formal public attribution of a covert action. Requires an Intel token naming the target faction (spent regardless of outcome) — you cannot make the accusation without evidence. Token age determines confidence: Fresh = threshold 50, Stale = 35. Network gains +10 threshold bonus (broadcasting attribution is their mode). Ghost's portrait at −2 (the highest negative in the set) reflects that Ghost's doctrine protects operational anonymity across the entire table — attributing any faction's covert operation is a violation of Ghost's belief that understanding accumulates privately.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public attribution of covert operations is a core political act — creates accountability where covert ops sought deniability | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's evidence-responsibility framing, Directorate's institutional/conditional support, Network's right-to-know, Ghost's doctrine of operational privacy (principle not preference), Syndicate's leverage-timing calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network portrait +1: broadcasting attribution is doctrinal. Ghost portrait −2 (highest negative in set): attributing any faction's op violates Ghost's belief that operational anonymity protects the whole table's intelligence discipline. Others: no doctrinal stake in the attribution mechanism itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — any faction can attribute | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ✓ | Token cost + resource cost; token age tiers threshold (Fresh 50, Stale 35); Expired excluded. Fail: self-PS loss (false or botched attribution). High success PS reward reflects the significance of public attribution | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1 (doctrine), Ghost −2 (doctrine): both submitter-bounded. No Portrait shifts in effect fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted attribution; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (faction=target, age=Fresh or Stale — Expired excluded per restriction; Art 02 §6); faction native × 1 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case; token age determined at Beat 4 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. `resolution_type = "Contested"` — same missed-then-caught vocabulary gap as STD.PA.2. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/fail populated (successcrit/failcrit=`None`), no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Cross-resource cost (faction native + Intel Token) — `resource.faction(acting)` term untyped; Intel Token as cost is the 10th confirmed corpus instance and first in Standard PA, using a new notation form (`intel_token(target=faction(target))`) not seen elsewhere in the corpus. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.5 = Card(
    id      = "STD.PA.5",  card_id="STD.PA.5",  version="v1.0",
    name    = "On the Record",
    tagline = "Formally attribute a recent covert action to a named faction before the city.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = 35,  # base = Stale token; Fresh → +15 via affinity; Network → +10 via affinity
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
    affinity    = (
        faction(acting).holds_intel_token(faction=target, age=Fresh):  threshold += 15,
        faction(acting) == Network: threshold += 10,
    ),
    restriction = faction(acting).holds_intel_token(faction=target, age__in=[Fresh, Stale]),  # Expired excluded — too degraded to constitute usable attribution evidence
    cost        = resource.faction(acting) * 1 + intel_token(target=faction(target)) * 1,
    boost       = None,

    success     = (
        arbiter.announce(attribution=target_faction, context=intel_token.quarter),
        faction(target).standing  -= 2,
        faction(acting).standing  += 2,
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = None,

    portrait = {
        Network: PortraitEntry(submitter=+1),
        Ghost:   PortraitEntry(submitter=-2),
    },
    ps_framing   = None,

    narrative    = "In New Meridian, there are very few true secrets. There are only secrets that haven't been made public yet.",
    perspectives = {
        Guild:       "If we can prove it, we will say it. What someone did with their dispatch case is their own responsibility.",
        Directorate: "Public attribution is the mechanism for accountability. We support it when the evidence supports us.",
        Network:     "The city has a right to know who is operating in its districts. We are providing that record.",
        Ghost:       "We do not publish what we know about other factions' operations. That is a principle, not a preference.",
        Syndicate:   "Attribution is leverage. The question is always: what is the information worth on the table versus in hand?",
    },
    design_note  = "Standard information-attribution PA. Restriction requires Fresh or Stale token — Expired excluded (too degraded to constitute usable attribution evidence). Token spent regardless of outcome. Threshold from token age (Fresh = 50, Stale = 35) + Network +10. Ghost portrait −2: attributing any faction's covert op violates Ghost's belief that operational anonymity protects the intelligence discipline of the whole table — the highest negative portrait value in the set.",
    arbiter_note = "At Art 03 §9.2.0: Intel token placed on PA card with Target Profile face-down. At Art 03 §9.4.3.1.1: flip Target Profile face-up; verify token age — Fresh or Stale satisfies restriction; Expired does not. Beat 4: threshold = age-based (50 Fresh / 35 Stale) + 10 if Network. On success: announce '[Acting faction] attributes [op type, quarter] to [target faction].' Target −2 PS, acting +2 PS. Token spent. On fail: acting −1 PS. Token spent regardless.",
)
```

---

### STD.PA.6 — ECONOMIC SANCTION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The economic attack card of the standard PA set. PS is intentionally reversed from intuitive expectation: the faction applying sanctions takes a public standing penalty (aggressor optic), while the target gains sympathy. The card's value is purely the resource damage (target loses 2 native) — players trade PS for economic impact. This creates meaningful faction differentiation: Ghost plays it readily (low PS concern), Network is reluctant (PS-dependent), Syndicate is the natural primary user (Capital leverage, threshold bonus). Fail/failcrit penalise the acting faction — a failed public sanction looks worse than not attempting one.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic sanctions are a legitimate public instrument — all factions can apply financial pressure | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's last-resort restraint, Directorate's formal instrument framing, Network's neutral observation, Ghost's collateral-attention awareness, Syndicate's capital-discipline framing | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate +15 threshold + portrait +1: Capital leverage doctrine aligns with economic pressure. Guild portrait −1: economic weapons conflict with permanence-through-building doctrine. doctrine_mod accounts for target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Remove / NativeResource | Art 04b §4 |
| Balance | ✓ | Acting faction absorbs −1 PS on success as the cost of the aggressor position. Threshold 40 + Syndicate +15. Value = resource denial (up to 2 native, floor = 0), not PS gain | Art 02 §6–§7 |
| Effect duration | ✓ | Resource removal and PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1, Guild −1: submitter-bounded. PS shifts are game effects, not Portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target's supply, Art 02 §8); faction native × 1 cost (Art 02 §8). Floor clause is procedural | Art 02 §8 |
| Supported by game procedure | ✓ | Beat 4; ARBITER removes up to 2 native resources from target (floor = 0 — all available if fewer than 2) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. `resolution_type = "Contested"` — same missed-then-caught vocabulary gap as STD.PA.2. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/fail/failcrit populated (successcrit=`None`), no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 1), untyped resource-type attribute. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.6 = Card(
    id      = "STD.PA.6",  card_id="STD.PA.6",  version="v1.0",
    name    = "Economic Sanction",
    tagline = "Publicly impose economic pressure on a faction, forcing resource loss.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Remove,  subject = NativeResource,

    beat            = 4,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = None,
    doctrine_mod    = {Neighbor: +10, Opposed: -10},
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
    affinity    = faction(acting) == Syndicate: threshold += 15,
    restriction = None,
    cost        = resource.faction(acting) * 1,
    boost       = None,

    success     = (
        faction(target).resource(native) -= min(2, faction(target).resource(native)),  # floor = 0
        faction(acting).standing -= 1,  # aggressor optic
        faction(target).standing += 1,  # sympathy
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Syndicate: PortraitEntry(submitter=+1),
        Guild:     PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "Economic pressure in New Meridian is always visible. The faction applying it accepts that visibility as part of the cost.",
    perspectives = {
        Guild:       "Economic weapons undermine the table's capacity to build. We use them only when other options are exhausted.",
        Directorate: "Sanctions are a formal instrument of institutional pressure. Applied correctly, they do not require apology.",
        Network:     "We note who imposes economic sanctions on whom. The city will form its own judgment.",
        Ghost:       "Public economic aggression makes enemies. We observe the transaction and its aftermath.",
        Syndicate:   "Capital discipline is a legitimate instrument. The target chose to be in a position where this was possible.",
    },
    design_note  = "PS reversed by design: acting −1 (aggressor optic), target +1 (sympathy) on success. Value is purely resource denial (target loses up to 2 native; floor = 0 — remove all available if fewer than 2). Faction differentiation: Ghost plays freely (PS-agnostic), Network avoids (PS-dependent), Syndicate primary user (+15 threshold). Guild −1 portrait: economic weapons conflict with permanence-through-building doctrine.",
    arbiter_note = "Beat 4. d100 vs threshold 40 (+15 Syndicate; doctrine_mod Neighbor +10 / Opposed −10). On success: remove 2 native resources from target, or all available if fewer than 2 (floor = 0); acting −1 PS; target +1 PS. On fail: acting −1 PS only. On failcrit: acting −2 PS.",
)
```

---

### STD.PA.7 — PUBLIC ADDRESS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Self-directed PS building — fills the gap in the standard set (STD.PA.4 attacks opponent's PS; STD.PA.7 builds own). Cheap (1 native), certain (Automatic), grants +2 PS in exchange for having presence in the target district. No faction monopolises public communication — all factions make public statements — but the portrait reflects who finds it doctrinally meaningful (Directorate, Network) versus costly (Ghost). The requirement to already have presence prevents factions from claiming standing in districts where they have no legitimacy.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public statements and rallies are universal political acts | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's building-primary-but-does-speak, Directorate's institutional communication expectation, Network's terse "this is what we do", Ghost's analytical surveillance framing of own public acts, Syndicate's investment/return calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate +1, Network +1: institutional communication and broadcasting are both core doctrinal expressions. Ghost −1: public address = attention = exposure risk. Others: no strong doctrinal alignment with the act itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ⚠ | Standing / Shift / PublicStanding — code correctly uses `subject = StandingMarker`; prose still says the retired term (corrected S126). Second Standard PA instance of the DIR.CA.7/NET.CA.7 pattern (schema_cleanup_log.md item 4-F); flagged, not corrected. +2 PS is a relative position change, not an unconditional grant | Art 04b §4 |
| Balance | ✓ | 1 native for +2 PS with presence restriction. Cheap but not free; presence requirement prevents abuse | Art 02 §6–§7 |
| Effect duration | ✓ | PS shift is immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Network +1, Ghost −1: submitter-bounded. No direct PS shift in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction checks presence in target district ✓ | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — restriction check (Art 02 §6); faction native × 1 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; restriction at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 1), untyped resource-type attribute. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
STD.PA.7 = Card(
    id      = "STD.PA.7",  card_id="STD.PA.7",  version="v1.0",
    name    = "Public Address",
    tagline = "Rally public support in a district where you operate.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.faction(acting) * 1,
    boost       = None,

    success     = faction(acting).standing += 2,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "Presence without voice is presence waiting to become something else.",
    perspectives = {
        Guild:       "We speak through what we build. But occasionally, we also speak.",
        Directorate: "A formal address in a district we operate in is institutional communication. It is expected.",
        Network:     "This is what we do. The address is the point.",
        Ghost:       "Public addresses are signals. We note the frequency, the district, and the audience.",
        Syndicate:   "Standing is a resource. We invest in it when the return is clear.",
    },
    design_note  = "Self-directed PS building — the missing card type in the standard set. STD.PA.4 attacks opponent PS; STD.PA.7 builds own. Automatic, 1 native, +2 PS. Presence requirement: cannot claim standing in districts where you have no legitimacy. Directorate +1 and Network +1: institutional communication and broadcasting are doctrinal for both. Ghost −1: public address = attention = exposure risk.",
    arbiter_note = "Beat 4. Restriction at Beat 0: acting faction must have at least 1 presence token in declared district. If restriction fails, PA voided. On success: acting faction +2 PS.",
)
```

---

### STD.PA.8 — TABLE AN ACCORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The formal bilateral agreement mechanism of the standard set. Playing STD.PA.8 at Phase B publicly declares an intent to propose an Accord with a named target faction. ARBITER delivers a blank AccordForm to the submitting faction at Beat 4. The faction drafts the terms and places the completed form in the Accord Placement Area at their discretion; formation and execution procedure per Art 06 §9.4. PS consequences apply at Debrief on acceptance or decline. Cost is 1 native flat — the PA submission slot (3 per Quarter; draw-dependent) is the primary gate on Accord access; the resource cost signals accessible diplomacy rather than gating potential. Ghost portrait −1: Accords create commitments, which Ghost avoids structurally.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accord proposals are a core political act — every faction can and does make bilateral agreements | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's pragmatic/permanence framing, Directorate's institutional mechanism preference, Network's record-and-observe stance, Ghost's obligation-aversion (not value-aversion), Syndicate's asset/exit-cost calculus | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate portrait +1: bilateral stability is Directorate institutional doctrine. Ghost −1: Accords create commitments. Syndicate affinity removed — Syndicate manipulates Accords through faction-specific cards, not standard proposals. doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — BilateralAgreement outcome type | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement | Art 04b §4 |
| Balance | ✓ | Cost 1 native flat (all factions). PA slot is the primary gate — 3 PA slots per Quarter, card is draw-dependent. PS vote mechanic gates proposal quality. At 1 native the form price signals accessible diplomacy; the slot cost and PS mechanics provide volume and quality control. L200. | Art 02 §6–§7 |
| Effect duration | ✓ | AccordForm delivery is Immediate. Form lifecycle and cross-Quarter persistence governed by Art 06 §9.4. | Art 04 §5 P19; Art 06 §9.4 |
| Persistence | ✓ | Immediate — PA delivers blank AccordForm at Beat 4; form lifecycle governed by Art 06 §9.4. | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Ghost −1: submitter-bounded. No PS shifts in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | AccordForm (Art 06 §9.2). No new components. | Art 06 §9.2 |
| Supported by game procedure | ✓ | Phase B: target faction named publicly. Beat 4: blank AccordForm delivered to submitting faction. Faction drafts and places per Art 06 §9.4. Execution at Debrief. | Art 03 Phase B; Art 06 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated (`arbiter.deliver(...)`) — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Mono-resource (faction native × 1), untyped resource-type attribute. | Art 00a §9.2 |

#### Outstanding Issues

- **Upkeep income tracking:** n/a — no ongoing income on STD.PA.8 itself (Accord income terms are player-drafted per Art 06 §9.3).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
STD.PA.8 = Card(
    id      = "STD.PA.8",  card_id="STD.PA.8",  version="v1.0",
    name    = "Table an Accord",
    tagline = "Formally propose a binding agreement with another faction, placed on the public record.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = BilateralAgreement,
    persistence     = Immediate,  # AccordForm delivery resolves at Beat 4; form lifecycle governed by Art 06 §9.4
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,  # named publicly at Phase B declaration
    target_object   = AccordForm,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        target_faction != faction(acting) and
        accord(faction(acting), faction(target)).active == False
    ),
    cost = resource.faction(acting) * 1,
    boost = None,

    success = arbiter.deliver(faction(acting), AccordForm(blank)),
    # Faction drafts terms per Art 06 §9.3; places in Accord Placement Area at their discretion.

    # BilateralAgreement resolution at Debrief: PS consequences per Art 06 §9.4

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },
    ps_framing   = None,

    narrative    = "The Table exists to make agreements. This is one of the few acts that uses it as intended.",
    perspectives = {
        Guild:       "We make agreements when they serve what we are building. We honor them for the same reason.",
        Directorate: "A formal accord is the institutional mechanism for bilateral stability. We prefer it to informal arrangements.",
        Network:     "Every formal agreement is a piece of the city's record. We observe the terms and what follows.",
        Ghost:       "Accords create obligations. We are not opposed to what they achieve — only to what they commit us to.",
        Syndicate:   "Every accord is an asset. The question is who controls the terms and what the exit costs.",
    },
    design_note  = "Accord initiation PA. Cost = 1 native flat (all factions). PA slot is the primary gate: 3 PA slots per Quarter, card is draw-dependent. PS vote at decline gates proposal quality (unreasonable proposal = proposer −1 PS). Blank form is a proposal, not a contract; 1 native signals that diplomacy is accessible. L200. Ghost −1: Accords are commitments.",
    arbiter_note = "Phase B: target faction named publicly. Beat 4: deliver blank AccordForm from ARBITER tableau supply to submitting faction. No timing constraint on drafting or placement — form queued for next Debrief when placed in Accord Placement Area. At Debrief: target reviews, accepts or declines per Art 06 §9.4. PS consequences per Art 06 §9.4.",
)
```

---

