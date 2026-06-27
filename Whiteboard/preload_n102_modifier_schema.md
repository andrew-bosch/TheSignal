# Pre-load: 04-n102 Modifier Card Schema Definition
*Written S125 — pre-work for next session. Sources: Art 04 §6.1/§6.2/§11, design_reference_card_system.md, modifier_card_ideas.md + S125 design session.*

---

## What 04-n102 Is

Modifier card schema definition pass — Art 04 §6. Goal: define how modifier cards fit into (or beside) the `Card` class so that individual modifier card specs in §11.8 and the full design pass (09-06) have a clean schema to write against.

Gates: 09-06 (full modifier card design pass).

---

## Three Modifier Card Types (Architecture — S125)

"Instant" is retired — **React** is the canonical term. Three subclasses, not a ModifierCard parent:

| Subclass | Purpose | Schema similarity |
|----------|---------|-------------------|
| `ModActionCard` | Modifies an operation (CA/PA/Operative/Emergency/Apex) | Thin — threshold delta primary; outcome modification taxonomy TBD |
| `ModBattleCard` | Modifies Battlefield Strength threshold | Very thin — almost identity + effect only |
| `ModReactCard` | Fires in response to a publicly observable board state change | Closest to a CA/PA — gets full taxonomy + resolution model |

---

## ModActionCard

Modifies a submitted action card. Primary mechanism: threshold delta (make the action easier or harder). Other outcome modifications are possible but the taxonomy for those is not yet defined — that definition is in scope for 04-n102.

**Played:** Bundled inside Dispatch Case with the operation at Phase A.

**Drops from Card:**
- `layer / function / subject` — not a direct action; excluded from taxonomy
- `beat` — no independent beat; fires with host action
- `resolution / threshold / resolution_type` — no independent roll
- `ring_mod / doctrine_mod` — not applicable
- `outcome_type` — PA-only
- `success / fail / successcrit / failcrit` — no branching outcome
- `on_accept / on_decline` — ElectPlayer-only
- `boost` — modifier cards are the boost mechanism

**Keeps from Card:**
- All identity fields
- `trigger` — may constrain which action types this modifier applies to
- `restriction` — eligibility conditions
- `cost` — modifier cards have costs
- `affinity` — faction-specific pricing plausible
- `portrait` — applicable if applicable per §11.1
- `narrative / perspectives / design_note / arbiter_note`

**Adds:**
- `effect: ModActionExpr` — tagged union, one of: threshold delta (CA+PA) · success multiplier (CA+PA) · PS shift (CA+PA) · cost reduction (PA only — CA cost already resolved before modifier is evaluated)
- `value_rating: int` — 1–3, printed on card face
- `ring_constraint: Ring | None` — deployment constraint set at card design time by narrative; `Ring1/2/3` = usable only on actions targeting that ring's districts; `None` = deployable anywhere. Determined by card narrative: a location-anchored asset (scientist at research center) gets the ring value; a portable asset (gadget that can travel) gets None. For ModBattleCard, ring constraint applies to the Battlefield Strength district — can't use a Ring 2 battlefield mod in a tension battle for a Ring 1 district. *(S125: schema element confirmed — value is per-card narrative decision, not assumed from origin deck.)*

---

## ModBattleCard

Used during Battlefield Strength resolution. Maximally simple.

Effect: `+n` to submitting faction's threshold **or** `−n` to opponent's threshold. Andy: "such a simple system I don't think there's much more to it" — but tactical/equipment advantages are possible if design warrants.

**Drops from Card:** Everything except identity, cost, portrait (maybe), narrative, and effect.

**Keeps from Card:**
- All identity fields
- `cost`
- `portrait` — if applicable
- `narrative / arbiter_note`

**Adds:**
- `effect: ModBattleExpr` — threshold delta; direction (self | opponent) + magnitude
- `value_rating: int` — 1–3
- `ring_constraint: Ring | None` — if set, usable only in Battlefield Strength for a district in that ring

---

## ModReactCard

Most complex modifier type. Closest to a CA/PA card in schema terms.

**Trigger:** Any enumerated public board state delta — see trigger set below. Art 04 §5 P5 governs (publicly observable only; no hidden triggers).

**Played in:** Faction Resolution Grid (not inside Dispatch Case).

**React lifecycle — two paths (trigger fires once; never recurs):**

| Path | Sequence | Persistence |
|------|----------|-------------|
| Immediate | Trigger fires → effect resolves → card discards | `Immediate` |
| Standing effect | Trigger fires → standing effect created → card stays until standing effect resolves (via its own trigger or timing condition) → card discards | `Permanent` + `persistence_condition` + `persistence_effect` |

Standing effect uses the existing card-as-condition schema: `persistence_condition` is the resolution condition (when False, card discards); `persistence_effect` is the ongoing board state while active. Same mechanics as Regulatory Freeze / Standing Injunction — different narrative origin (played in reaction, not as a deliberate deployment).

**04-n29 resolution:** No formal Art 03 persistence check step needed. Governing Rule 6.1a (faction self-policing — playing faction monitors and discards when resolution condition fires) + Governing Rule 6.1c (ARBITER ruling is final on disputes) covers all cases including React standing effects. **Close 04-n29 in PM05 during 04-n102.**

**TriggerExpr notation for ModReactCard:**

```
TriggerExpr:
  Any                                              # fires on any public board state delta
  | component[.scope][.attribute].change(faction)  # filtered trigger

Examples:
  Any
  district.ring1.influence.increase(Any)   # influence rises in any Ring 1 district, any faction
  structure.removed(Any)                   # any structure removed, any faction
  district.ring2.tension.placed(Any)       # tension marker placed in any Ring 2 district
  presence.placed(Directorate)             # Directorate places a presence chip anywhere
  accord.created(Any, Any)                 # any Accord placed between any two factions
  standing.decreased(Any)                  # any faction's PS track drops
```

Fields:
- `component` — the physical object or tracked state (presence | structure | influence | tension | standing | accord | world_event | deployment_marker | control_flag | established_marker | resolution_grid | ...)
- `scope` — optional filter (ring1/2/3 | district.{id} | global)
- `attribute` — optional sub-state on the component (influence level, chip count, etc.)
- `change` — the delta event (placed | removed | increased | decreased | created | corrupted | revealed | converted | ...)
- `faction` — `Any` or a named faction

`trigger` is a **required** field on ModReactCard (never None — it defines what activates the card). Contrast with base `Card.trigger` which is timing-only and defaults None.

**React Trigger Set — Sourcing (task for 04-n102):**
Pull from Art 03b component lifecycle (filter to public lifecycle events only) + Art 02 movement paths. These artifacts already enumerate what moves and when — the trigger list is the public-only subset.

Confirmed inclusions (physical tokens that move):
- Presence chips — placed or removed
- Structure blocks — placed or lost (Absent trigger)
- Deployment markers — placed (Phase 2) or converted (Upkeep Step 4)
- Control flags — placed or removed (Dominant status change)
- Established markers — placed or removed
- Tension markers — placed (Contested condition)
- Public Standing markers — shifted (Beat resolution)
- World Event cards — played or expired
- Accord documents — placed (new Accord) or corrupted (Accord Corrupt effect)
- Resolution Grid contents — after Beat 0 public reveal (declared op, Target Profile face-up, payment tokens)

Confirmed exclusions (static — never change):
- District tiles, board geography, ARBITER Dominance Marker

Excluded by principle (public but not player-driven):
- Initiative Strip, Session Timeline / Quarter marker, Month marker — procedural, not player action or card resolution

**Gets from Card (unlike other modifier types):**
- `layer / function / subject` — React cards have full taxonomy
- `resolution / threshold / resolution_type` — may roll dice
- `success / fail / successcrit / failcrit` — may have branching outcomes
- `boost` — may accept boost
- `outcome_type` — may apply (if ElectPlayer React is ever designed)
- `on_accept / on_decline` — if outcome_type = ElectPlayer
- `persistence / persistence_condition / persistence_effect` — Tripwire = Permanent; immediate React = Immediate
- `ring_mod / doctrine_mod` — if relevant to React targeting

**Drops from Card:**
- `beat` — replaced by `trigger` (React fires on condition, not at a beat)

**Keeps from Card:** Everything else in the standard Card class.

**Adds:**
- `value_rating: int` — 1–3
- `ring_constraint: Ring | None` — set by card narrative; None = no deployment restriction

**Note on standing effects:** Tripwire uses the existing `persistence = Permanent` + `persistence_condition` + `persistence_effect` pattern. The React fires at `trigger`; the standing condition is the deferred resolution. No new field needed — but this needs verification during 04-n102 that the existing persistence model covers the Tripwire case cleanly.

---

## Thematic Frame — Naming & Narrative

Cards represent **Assets**, **Equipment**, and **Tactics** — but any of these representations can apply to any of the three modifier types. This is a flavor/naming convention, not a schema field.

**Implication for 04-n102 and 09-06:**
- Card titles should evoke the faction-specific or ring-specific origin of the asset/equipment/tactic
- Narrative and perspectives fields should anchor the card to where it came from (ring presence = infrastructure, networks, or territory; faction deck = doctrine and institutional capability)
- `ring_origin` drives this narrative anchor even if it doesn't constrain deployment

---

## Schema Decision: 3 Direct Subclasses of Card

**Agreed direction (S125):** Option A — 3 direct subclasses of `Card`, not a `ModifierCard` intermediate class.

```
Card
├── ModActionCard
├── ModBattleCard
└── ModReactCard
```

All three remain under `type: CardType` where `Modifier` was the single value — the subclass distinction appears in the spec structure (separate Python class definitions in §6), not via a new enum field.

**In Art 04 §6:**
- Keep `Card` class as-is
- Add `ModActionCard(Card)`, `ModBattleCard(Card)`, `ModReactCard(Card)` below it in §6.1
- Add data dictionary rows for new fields in §6.2
- No new enum value needed — `type = Modifier` covers all three; subclass is the schema-level distinction

---

## Open Decisions (Surface During 04-n102)

| Item | Question | Status |
|------|----------|--------|
| **Ring deployment constraint** | Schema field confirmed: `ring_constraint: Ring \| None`. Value set per card at design time by narrative — location-anchored assets get the ring value; portable assets get None. Applies to all three subclasses. | **Decided S125** |
| **ModActionExpr vocabulary** | Confirmed (S125): threshold delta (CA+PA), success multiplier (CA+PA), PS shift (CA+PA), cost reduction (**PA only** — CA cost committed at dispatch before Beat 0; PA cost captured at Beat 4 while modifier is visible in grid). Outcome addition excluded (too complex for splay). Tagged union — one effect per card. | **Decided S125** |
| **`applies_to` field on ModActionCard** | Cost reduction being PA-only surfaces whether ModActionCard needs `applies_to: CardType` (CA \| PA \| Operative \| Emergency \| Apex \| Any) to constrain valid bundling and effect timing. Decide during 04-n102. | Open |
| **Battlefield tactical modifiers** | Equipment/tactical advantages beyond threshold delta? | Probably not, but confirm during 04-n102 |
| **ps_framing on modifier cards** | Do any modifier cards shift PS? If no current candidate, drop from all three subclasses | Likely None for ModBattle/ModAction; possible for ModReact |
| **ModActionCard trigger** | How does the schema express "this modifier applies only to [op type]"? Via `trigger` or a new `applies_to` field? | Resolve during 04-n102 |
| **D-04-07 / XA-35** | "Modifier cards" / "Assets" naming — don't lock CardType enum value until resolved | Pending |
| **04-52** | Modifier token Beat 4 disposition — does schema need `discard_timing`? | Pending |
| **04-56** | Deck types — confirm whether `ring_origin` covers the design intent | Pending |
| **React/Tripwire cost rule** | Governing rule needed: cost paid at time of play — needs Art 03 or §6 home | Pending |

---

## Suggested 04-n102 Sequence (Next Session)

1. Pull React trigger enumeration from Art 03b (public lifecycle events) + Art 02 (movement paths) — filter to public-only; confirm against confirmed inclusions list above.
2. Resolve ring deployment constraint — sets whether `ring_constraint` gates a `restriction` field or is schema-only documentation.
2. Define `ModActionExpr` vocabulary — threshold delta only, or broader? (This scopes ModActionCard.)
3. Write `ModActionCard(Card)` class in §6.1.
4. Write `ModBattleCard(Card)` class in §6.1.
5. Write `ModReactCard(Card)` class in §6.1 — verify Tripwire coverage via existing persistence model.
6. Update §6.2 data dictionary for all new fields.
7. Update §6.3 enum vocabularies if any new enums added.
8. Add governing rule pointer for React cost timing (PM05 item or Art 03 forward-ref).
9. Bump version: v0.9.50 → v0.9.51.
10. Update PM03 + PM05.
11. Run `mysql the_signal_db < Database/audit_card_alignment.sql` — confirm all new modifier cards show Legalized; no Rules Gaps.

**Audit heads-up for mod card sessions:**
- New modifier card subjects may not be in `card_subject_map` yet — audit will surface these immediately.
- `Modify` and `Block` functions are currently unmapped in `function_verb` (15 Abstract Function cards). Modifier cards using these functions will land in that bucket until `function_verb` is extended.
- Fix pattern for any Rules Gap that surfaces: see `Database/schema_reference.md §10`.

---

*Load this file at session open before beginning 04-n102. No other pre-reads required beyond design_reference_card_system.md (always loaded).*
