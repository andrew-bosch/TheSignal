# Design Reference — Card System
*Load for all card spec work: governing rules, card schema, design flags.*
*Updated: S95.*

---

## Quarter Procedure (Art 03)

### Phase Order — Hard Sequence (Governing Rule 7.3a: no overlap, no revisiting)

1. **Upkeep** (Phase 1)
2. **Placement** (Phase 2) — 2 deployment markers per faction, snake order
3. **Month 1** — Dispatch (A: Covert, B: Public Declaration) → Countermeasures (C) → Resolution (D, Beats 0–5)
4. **Month 2** — Dispatch (A: Covert, B: Public Declaration) → Countermeasures (C) → Resolution (D, Beats 0–5)
5. **Month 3** — Dispatch (A: Covert, B: Public Declaration) → Countermeasures (C) → Resolution (D, Beats 0–5) → Contested District Resolution
6. **Debrief** (Phase 19) — open discussion, Accord activity, distribution
7. **End of Quarter** (Phase 21) — Findings decay → Debrief reward → Session Timeline advance

### Upkeep Steps (Phase 1, §7)

| Step | Action |
|------|--------|
| 1 | Status Marker reset (yellow/Discussing) |
| 2 | Initiative determined, Initiative Strip updated |
| 3 | Situation Report drawn; Event Card effects applied; Standing markers moved; Blocked markers set |
| 4 | **Deployment Marker Conversion** — Converting face: place 1 permanent presence chip, return marker to hand; Blocked face: return to hand without chip |
| 5 | **Resource Collection** — presence chips + deployment markers generate; structure block resource declared publicly; passive generation (+1 native, unconditional) |
| 6 | Operations Preparation — Dispatch Tokens from Backlog (Ghost: 4, others: 3); card draws (covert: hand of 6; public act hand size: TBD); modifier card draws |

### Modifier Card Draw Formula (Upkeep Step 6)

**Faction modifier draw:** based on structure blocks owned
| Structure blocks | Cards drawn |
|-----------------|-------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 max |

**Ring modifier draw:** 1 card per qualifying ring (must have 1+ structure block AND Established+ in at least 1 district in that ring).

*Burst Play: trade ALL modifier cards to Reservoir (1 resource each); faction modifier deck removed for session.*

### Placement Phase (Phase 2, §8)

- Each faction places 2 deployment markers, initiative order, snake pattern (1→5 forward, 5→1 reverse)
- All markers placed Converting face by default
- Deployment marker = 1 temporary presence chip immediately on placement
- Entry requirements enforced per ring (see Board Structure below)
- Faction Player may pass either or both placements

### Resolution Beat Structure (§11 per Month)

| Beat | What happens |
|------|-------------|
| Beat 0 | ARBITER opens cases: validates each op (token present, payment present); builds Resolution Grid; Beat 2 cards placed in Beat 2 row; Beat 3 cards placed in Beat 3 rows; invalid ops returned |
| Beat 1 | Read Board State: SitRep effects applied as standing public acts; targeting restrictions scanned; covert ops in restricted districts voided |
| Beat 2 | Conditions Set: Beat 2 row processed L→R (Type A/B Countermeasures, Protect, Fortify Structure, DIR.CA.3); public acts can still be voided before Beat 4 payment |
| Beat 3 | Covert operations resolve: dice rolled per §12; outcomes applied; Portrait fires |
| Beat 4 | Public acts resolve: payment submitted to Reservoir; outcome applied; initiative order |
| Beat 5 | Post-resolution cleanup; Battlefield Strength if Contested |

### Dispatch Rules
- Each covert op requires 1 Dispatch Token in case; each public act requires 1 token on declared card at Phase B (Governing Rule 7.3c); no token = rejected at Beat 0 (covert) or voided (public act)
- Cases sealed before transmit; no modifications after sealing (Governing Rule 7.3)
- Submission order = tiebreaker within resolution priority tiers (Governing Rule 7.3b)
- Ghost: 4 Dispatch Tokens/Quarter; others: 3

### End of Quarter (§21)
1. Findings decay: 7–12 → lose 2; 13+ → lose 4 (after Debrief, before Session Timeline)
2. Debrief reward (TBD design)
3. Operation Resolution cards returned to ARBITER
4. Session Timeline advances

---

## Components (Art 02a, 02b, 01)

### Board Components

| Component | Description | Visibility |
|-----------|-------------|-----------|
| Presence chip | Small disc in faction color; stacks; max 6 per faction per district (Governing Rule 8.1) | Public |
| Deployment marker | Large piece in faction color; placed Phase 2; = 1 temp presence chip; converts to permanent chip at next Upkeep Step 4; counts toward 6-chip limit | Public |
| Structure block | Small square chit in faction color; max 1 per faction per district (Governing Rule 8.2); lost when faction goes Absent (Governing Rule 8.2b) | Public |
| Control flag | Gold; placed on Dominant faction's chip stack | Public |
| Established marker | Silver; each Established faction places own marker; up to 5 can coexist | Public |
| Tension marker | Neutral; placed when Contested condition triggered | Public |
| ARBITER Dominance Marker | Single fused piece at Chorus Node; permanent; = 8 ARBITER presence tokens; never removed | Public |
| District tile | Printed name, resource type, base generation value | Public |
| World Event card (active) | Placed in Situation Report Area when active | Public |
| Accord document | Placed in Accord Placement Area face-up when active | Public |

### Track Components

| Component | Description | Visibility |
|-----------|-------------|-----------|
| Portrait track (×5) | Scale −20 to +20; eleven named bands | **Private — ARBITER tableau only** |
| Portrait position marker (×5) | Clip or bead in faction color | Private |
| Public Standing track (×5) | Scale 0–20; five bands; modifies all roll thresholds | Public |
| Standing marker (×5) | Clip or bead in faction color | Public |
| Intel Token | Created by ARBITER on gather; records faction + quarter; aging: 0–1 Fresh, 2–3 Stale, 4+ Expired | **Private — holder + ARBITER** |
| Session Timeline | Advances at End of Quarter; 8 Quarters total | Public |
| Initiative Strip | Updated each Upkeep Step 2 | Public |
| Chorus Activity Track | Tracks Chorus signal activity | Public |

### Player Area Components

| Component | Description |
|-----------|-------------|
| Faction Screen | Upright divider; conceals hand, held resources, Terminal |
| Faction Terminal (tableau) | Work surface behind screen; modifier area, hand area, dispatch case |
| Dispatch Case | Physical case; sealed before transmit; contains op cards, tokens, resources, target slips, modifiers |
| Dispatch Token | 1 per covert op in case; drawn from Backlog at Upkeep; Ghost draws 4, others draw 3 |
| Modifier cards (faction + ring) | Drawn at Upkeep; assigned to ops in case or held; unassigned stay in modifier area |
| SCIFRecord (SR-xx) | DebriefActionCard type; sits in ARBITER tableau. Fields: `quarter \| target_faction \| draw_ring1/2/3 \| draw_faction`. Filled by ARBITER at Debrief when Ghost SCIF resolves; delivered to Ghost case. |
| IntelDeliverySlip (IS-xx) | Private ARBITER-to-faction slip; never seen by other factions. Delivered at Beat 2 (DIR.CA.3 column read) or Beat 3 (GHO.CA.3 row read); contains grid data scoped to delivery conditions. |

### Resources

| Resource | Faction | Physical Token |
|----------|---------|----------------|
| Findings | Ghost | Translucent layered fragments |
| Capacity | Guild | — |
| Exposure | Network | — |
| Mandate | Directorate | — |
| Capital | Syndicate | — |

- Passive generation: +1 native resource/Quarter, unconditional, cannot be blocked (Design Pillar 4.8d)
- Findings decay: 7–12 lose 2; 13+ lose 4 at End of Quarter (Art 03)
- Intel Token holding guideline: Ghost ≤4, others ≤2; own-faction tokens exempt

---

## Board Structure (Art 01)

### Ring Structure & Entry Requirements

| Ring | Name | Base Generation | Entry Requirement |
|------|------|----------------|-------------------|
| 0 | Chorus Node | — (special) | Established+ in adjacent Core district |
| 1 | Core | 3/Quarter | Established+ in adjacent Mid district |
| 2 | The Mid | 2/Quarter | None (−25 modifier if no presence in adjacent Core) |
| 3 | Baryo | 1/Quarter | None; unconditional fallback for all factions |

*Temporary presence from first deployment marker this phase satisfies entry requirements for second marker placement in same phase (Art 03 §8).*

### Districts by Ring

**Ring 0**
| # | District | Resource |
|---|----------|----------|
| 21 | Chorus Node | None |

**Ring 1 — Core**
| # | District | Resource | Notes |
|---|----------|----------|-------|
| 17 | Government Citadel | Mandate | Directorate predates city here |
| 18 | Military Installation | Mandate | Adjacent to Gov Citadel; outward-facing |
| 19 | Chorus Research | Findings | Adjacent to Chorus Node |
| 20 | Financial Sanctum | Capital | East edge; Syndicate presence |

**Ring 2 — The Mid**
| # | District | Resource | Notes |
|---|----------|----------|-------|
| 10 | Power Grid | Capacity | Guild-adjacent to Military Installation |
| 11 | Financial Clearinghouse | Capital | Syndicate primary anchor |
| 12 | Data Exchange | Findings | Ghost analytical networks |
| 13 | Communications Hub | Exposure | Network Mid foothold |
| 14 | Logistics Center | Capacity | Supply chain; Guild |
| 15 | Research Institute | Findings | Secondary research |
| 16 | Regulatory District | Mandate | Directorate administrative presence |

**Ring 3 — Baryo**
| # | District | Resource | Notes |
|---|----------|----------|-------|
| 4 | Industrial Fringe | Capacity | Guild Baryo foothold |
| 6 | Transit Hub | Capacity | Transport link |
| 7 | Civic Center | Mandate | Directorate public-facing |
| 3 | Residential Quarter | Mandate | Most populated; PS amplifier |
| 1 | University Perimeter | Findings | Ghost + Network anchor |
| 2 | Media District | Exposure | Network primary anchor |
| 8 | Broadcast Tower | Exposure | Network secondary broadcast |
| 9 | Observation Post | Exposure | Network eastern edge |
| 5 | Commercial Strip | Capital | Syndicate Baryo presence |

### Adjacency Summary (key relationships)
- Chorus Node (21) adjacent to: all Ring 1 (17, 18, 19, 20)
- Military Installation (18) adjacent to: Node, Gov Citadel, Power Grid (10), Financial Clearinghouse (11)
- Gov Citadel (17) adjacent to: Node, Military Install, Chorus Research, Financial Clearinghouse, Regulatory District
- Full adjacency table: Art 01 §6 (104 bidirectional rows; feeds `district_adjacency` DB table)

### Special Districts
- **Chorus Node:** ARBITER's 8 presence tokens permanent; Dominant unreachable; no structures; 2:1 Translation rate at Established
- **Residential Quarter (3):** PS amplifier — PS effects amplified for factions with presence here
- **University Perimeter (1):** Network virtual structure conversion (Exposure or district native)

---

## Influence Level Rules (Art 02a §6)

| Level | Chip Minimum | Rank Condition | Resource Generation | Structure Defense |
|-------|-------------|----------------|--------------------|--------------------|
| Dominant | 3+ | Strictly more than all others | Full + affinity bonus | Challenging to demolish |
| Established | 2+ | Second place | Full | Average |
| Present | 1+ | Third or lower | Half (round down) | Easy |
| Absent | 0 | — | None | All structures removed immediately |
| Contested | — | Tie at 3+ chips | Flat 1 resource for tied factions | Average (not Dominant-level) |

- Max 6 presence chips per faction per district (deployment markers count) (Governing Rule 8.1)
- Deployment markers: always move, never removed from play (Governing Rule 8.3a)
- "At least 1 presence token" = includes deployment markers (Governing Rule 8.3, Art 04 §5 P25)
- Structure blocks lost immediately on Absent (Governing Rule 8.2b)

---

## Key Governing Rules (Art 00a) — Card Design Constraints

Rules marked **HARD** cannot be overridden by card design without a PM02 locked decision.

| Rule | Summary | Applies To |
|------|---------|-----------|
| **Governing Rule 8.1** HARD | Max 6 presence per faction per district; deployment markers count | All presence-placing cards |
| **Governing Rule 8.2** HARD | Max 1 structure block per faction per district | STD.CA.1, GUI.CA.4, STD.PA.3, GUI.PA.1 + new |
| **Governing Rule 8.2b** HARD | Structures lost immediately on Absent; no card can prevent | All presence-removing cards |
| **Governing Rule 8.3** | "At least 1 presence token" includes deployment markers | All cards |
| **Governing Rule 8.3a** | Deployment markers never removed — always moved | All cards targeting markers |
| **Governing Rule 8.3b** | No faction is eliminated | All |
| **Governing Rule 8.1a** HARD | No structures at Chorus Node | STD.CA.1, GUI.CA.4 + new build cards |
| **Design Pillar 4.8c** | Floor Act always available (1 native resource); cannot be blocked | Public act design |
| **Design Pillar 4.8d** HARD | Passive generation (+1 native/Quarter) cannot be blocked or reduced | Resource cards |
| **Design Pillar 4.8a** | District resource type never changes | District-targeting cards |
| **Art 03 §9** | Structure block resource choice declared publicly at Upkeep | Upkeep procedure |
| **Governing Rule 5.1a** | Portrait accumulates, no drift or decay | Portrait fields |
| **Governing Rule 9.1** | Public Standing modifies roll difficulty only; not resource income | PS-affecting cards |
| **Art 04 §5 P19** HARD | Effects: exactly one of four durations — Immediate, Transient, Seasonal, Permanent | All card effects |
| **Art 04 §5 P20** HARD | Actions proceed with whatever resources are committed; shortfalls carry consequences | All cards |
| **Art 04 §5 P21** | Crit success never adds cost | All cards |
| **Governing Rule 5.1c** | Portrait fires at Resolution; unconditional on act or conditional on outcome | Portrait fields |
| **Art 04 §5 P23** | Ring modifier cards target only their ring's districts | Modifier card design |
| **Art 04 §5 P5** HARD | React conditions must be publicly observable — no hidden triggers | All React cards |
| **Governing Rule 7.2b** HARD | Committed board states cannot be retroactively nullified or modified by any subsequent card, Accord, World Condition, or ARBITER script. "Committed" = board state that existed and resolved. This is why Recover is retired, Field Verification and Backdate are BLOCKED. | All cards with retroactive or restoration effects |
| **Governing Rule 7.2a** HARD | All board state is always publicly visible. No card may create hidden state on the board surface (The Overview). Faction terminal and dispatch case contents are private zones — not board surface. | Reveal cards; any card touching information visibility |
| **Governing Rule 10.1** HARD | No card may compel disclosure. A Reveal effect creates a stake (consequence for revealing or withholding) — the decision remains the player's. ARBITER-initiated reveal is governed by GR 10.1b (see below). | All Reveal cards; distinguish faction-compelled vs. ARBITER-sourced reveal |
| **Governing Rule 10.1b** | ARBITER may reveal any content from its own domain — Intel Tokens, covert ops, dispatch contents, Broadcast Effect Cards, board state — without triggering 10.1's discretional framework. No faction may invoke 10.1 to prevent a prescribed ARBITER reveal. Portrait is the sole exception: never disclosed by any ARBITER procedure. *(Art 00a §10.1b — S108)* | All ARBITER-sourced Reveal effects; GHO.PA.4 and any card triggering ARBITER disclosure |
| **Governing Rule 9.1 (expanded)** HARD | Income generation comes from presence and structure output only. No card may directly modify upkeep income generation — including suppression (Regulatory Downgrade was BLOCKED on this basis). InfluenceTier is not a targetable component; tier is derived from token counts. Only changes to underlying board state (add/remove tokens) can affect tier, which then affects income naturally. | All income-adjacent cards; territory suppression designs |
| **Art 04 §5 P24 / §4.10** | Corrupt applies only to physically written/recorded values. Valid targets: Intel token faction-name field (location constraint applies — L222), Accord terms, Accord named party (L227), Target Profile in dispatch bundle. Invalid: printed card text, marker positions, Chronicle, Intel token round-number field (7.2b). Intel token location constraint (L222): tokens are valid Corrupt targets ONLY when publicly placed (on PA as payment, Beat 0–4). Tokens in faction terminal or ARBITER terminal are not reachable. | Corrupt function cards |
| **Art 04 §5 P26** (locked S78, L199) | Every card must be expressible as a 1–2 sentence narrative story. If "What is happening in the world when this card is played?" has no coherent answer, the card is a design problem. Narrative is the first test of whether mechanics are right. | All cards — checked via Card Story block + checklist row 15 |
| **Design Pillar [04-n6 pending]** | Ghost may use STD.CA.5 (Gather) without adjacency; all other Ghost cards require adjacency | Ghost card design |
| **Design Pillar 4.6b** | Missing Author Vacuum — no card flavor, perspective, or authored content may assert or imply any faction knows what the message to the Chorus should say | Narrative/perspectives fields |
| **Design Pillar 4.7b** | ARBITER Cognitive Efficiency — every rule, card effect, and procedure involving ARBITER must minimize ARBITER player cognitive load. Preference order: (1) physical objects carry state, (2) faction players self-police, (3) general procedures applied uniformly, (4) ARBITER-specific per-instance only as last resort | All cards with ARBITER-facing content |
| **Governing Rule 7.3a** HARD | Phases don't overlap; no revisiting prior phases | Timing rules |
| **Governing Rule 7.3** HARD | Commitment irreversible once case sealed / act declared | All |
| **Design Pillar 4.8b** | Crits (01–05 / 96–00) apply regardless of modifiers | All dice cards |
| **Governing Rule 7.3b** | Submission order is tiebreaker within priority tiers | Dispatch procedure |
| **Art 03** | Findings decay fires after Debrief, before Session Timeline advance | Findings cards |
| **Governing Rule 7.3c** HARD | Each action (covert op or public act) requires 1 Dispatch Token | All covert ops and public acts |
| **Governing Rule 6.1** | ARBITER executes general procedures, not card-specific instructions. `arbiter_note` fields reference existing procedures — they do not define new ones. New ARBITER behavior must be defined as a generalizable procedure in Art 03 or Art 07 before the card is finalized. *(Art 04 Principle 18)* | All cards with ARBITER-facing content |

---

## Ghost-Specific Rules

- **Dispatch Tokens:** 4/Quarter (vs 3 for others) — extra covert op capacity
- **Adjacency exception:** C05 Gather only; all other Ghost cards require adjacency (Design Pillar [04-n6 pending])
- **Findings decay:** 7–12 lose 2; 13+ lose 4 (end of Quarter, after Debrief)
- **Intel Token holding:** max 4 (others max 2); own-faction tokens exempt
- **Deployment markers:** standard 2 per Quarter, placed in Phase 2 like all factions; convert to permanent chips at Upkeep Step 4

---

## Card Data Schema (Art 04 §6)

*Condensed field reference. Full definitions: Art 04 §6.1–§6.3.*

**Schema first-pass discipline:** Before drafting any card spec, read §6.1–§6.3 and verify: all required fields are present, all enum values are valid. Do not draft and correct later — catch at spec time. The design checklist "Data schema validation" row confirms this was done; it should pass on first draft, not be deferred.

**Easy-to-miss required fields:** `card_id` · `doctrine_mod` · `boost` · `ps_framing` — all must appear in the spec (as `None` if not used). Omitting them is a schema error.

**resolution_type vocabulary (str, not enum):** Use `"Probabilistic"` for d100 cards. Use `"Transactional"` for Automatic cards only. Do not use `"Positional wager"` unless matching an established pattern.

**fail=None means "No effect, cost spent."** Do not write the string `"No effect."` in the spec field — use `None`.

**Private information gate (00a §10.1):** No card may target privately held information — IntelTokens in a faction's pool, hand cards, directives. Cards cannot reach into a faction's private domain. The ONLY valid cross-faction IntelToken target is one submitted on a PA in the Faction Resolution Grid (§9.2). See ref_tracking.md for full targeting rules.

---

### Field Groups

**Identity**
| Field | Type | Notes |
|-------|------|-------|
| `card_id` | CardID | Canonical ID — `[FAC].[TYPE].n` per L219; e.g., `"GHO.CA.4"` |
| `id` | str | Legacy sequence integer (e.g., `id=19`); preserved for traceability |
| `version` | Semver | Per-card; v[major].[minor] |
| `name` | str | In-world name — not a mechanical label |
| `tagline` | str | One-line in-world description |
| `type` | CardType | Top-level category; governs deck assignment and resolution handling |
| `subtype` | Subtype | Distribution scope |
| `faction` | Faction | All = standard; named = faction-specific |

**Taxonomy** *(static; dimension-backed — Art 04b §4)*
`layer` · `function` · `subject`

**Metadata**
| Field | Type | Notes |
|-------|------|-------|
| `beat` | int | 1–5; order within beat = submission order |
| `resolution` | Resolution | `d100` or `Automatic` |
| `resolution_type` | str | `"Probabilistic"` (d100) · `"Transactional"` (Automatic) — str, not enum |
| `threshold` | int \| None | None when Automatic |
| `ring_mod` | dict[Ring, int] \| None | Per-ring threshold adjustment; positive = easier |
| `doctrine_mod` | dict[PentagramRelation, int] \| None | Per-doctrinal-relationship threshold adjustment; None when no faction target |
| `trigger` | TriggerExpr \| None | None = default beat timing |
| `outcome_type` | OutcomeType \| None | Public acts only |
| `persistence` | Persistence | Immediate / Transient / Seasonal / Permanent; covert op default = Immediate |
| `persistence_condition` | BoolExpr \| None | **None unless Permanent.** Card discarded immediately when False. |
| `persistence_effect` | MutationExpr \| None | **None unless Permanent.** Ongoing board condition while card is in play. |

**Targeting**
| Field | Type | Notes |
|-------|------|-------|
| `target_district` | DistrictExpr | District scope |
| `target_faction` | FactionExpr \| None | None = no faction target |
| `target_object` | ObjectExpr \| None | None = no object target |
| `target_taxonomy` | TaxonomyExpr \| None | Targets a class of actions; declared at Phase B alongside target_faction; None = no taxonomy target |
| `declared_params` | DeclaredParamsExpr \| None | Faction-declared free-form parameters written on TP declared-parameters line at §9.2 or Covert Dispatch — e.g., N tokens + consideration (SYN.PA.3), clause + new value (SYN.CA.11), incoming party (SYN.CA.10); None = no declaration required. Art 02 v2.4 / L233. Full §6.1 addition pending 04-n106. |

**Logic**
| Field | Type | Notes |
|-------|------|-------|
| `affinity` | ConditionalExpr \| None | Faction-based cost modifier; evaluated before cost |
| `restriction` | BoolExpr \| None | Card unplayable if False |
| `cost` | CostExpr | Fungible resources only; PS and presence tiers are not valid cost values |
| `boost` | BoostExpr \| None | Variable multiplier — player submits additional resources beyond base cost; ARBITER detects at Beat 0; success fires (1 + n) times. None = no boost. |

**Effects**
`success` · `successcrit` (additive delta on crit) · `fail` · `failcrit` (additive delta on crit)

**ElectPlayer Effects** *(ElectPlayer outcome_type only — None on all other cards)*
`on_accept: MutationExpr | None` · `on_decline: MutationExpr | None`

**Portrait**
`portrait: dict[Faction, PortraitEntry]` — valid params: `flat` · `submitter` · `where` · `modifier` · `mod_where` — `failcrit=` is NOT a valid PortraitEntry parameter

**Public Standing**
`ps_framing: PSFraming | None` — required field; `None` = card produces no PS shift. Do not omit.

**Narrative**
`narrative` · `perspectives` · `design_note` · `arbiter_note`

### Enum Vocabularies (§6.3)

```
CardType:    CovertOperation | PublicAct | Pass | Countermeasure | Modifier | EmergencyResponse
Subtype:     Standard | FactionSpecific
Faction:     All | Ghost | Network | Syndicate | Guild | Directorate
Resolution:  d100 | Automatic   ← NOT "Dice" — d100 is the exact enum value
Persistence: Immediate | Transient | Seasonal | Permanent
Layer:       Territory | Economy | Information | Submission | Resolution | Standing
Function:    → Art 04b §4 / ref_taxonomy.md
Subject:     → Art 04b §4 / ref_taxonomy.md
```

---

## Card-as-Condition Pattern

Permanent public acts that create ongoing board conditions use the card-on-board as the condition — no separate marker component needed.

- `persistence = Permanent`
- `persistence_condition` = the BoolExpr that, when False, auto-discards the card
- `persistence_effect` = the ongoing board mutation active while the card is in play
- Card sits face-up in the acting faction's play area
- Factions self-police per Design Pillar 4.7b; ARBITER adjudicates calls (Governing Rule 6.1a)
- Persistence monitoring: faction self-policing under GR 6.1a covers all Permanent cards and React standing effects; GR 6.1c (ARBITER ruling final on disputes) covers edge cases. No Art 03 procedure step required.

*Examples: Regulatory Downgrade, Regulatory Freeze, Standing Injunction, Entry/Exit Controls*

**Seasonal persistence with timed effects** uses a different mechanism: `persistence_condition`/`persistence_effect` are None; the timed effect is encoded as `game.world_condition()` in the `success` field. This is not in conflict with the Permanent pattern — they serve different durations. Example: SYN.PA.2 Public Dividend (DividendMarker world_condition in success).

---

## Design Flags for New Card Proposals

Before writing any new card spec, check:
1. **Duration** — one of: Immediate / Transient / Seasonal / Permanent (Art 04 §5 P19)
2. **Resource payment** — full proceeds at stated difficulty; partial incurs threshold penalty; zero voids the action (Art 04 §5 P20)
3. **Deployment marker target?** → it moves, doesn't remove (Governing Rule 8.3a)
4. **Ghost adjacency?** → field collection ops (Station/Full Take/Flip) require Ghost presence in district adjacent to target; analytical ops (GHO.CA.1–5, SCIF, Source Substitution) have no adjacency restriction; STD.CA.5 grants analytical adjacency exemption. See design_reference.md Ghost op classification.
5. **React trigger** — is it publicly observable? (Art 04 §5 P5)
6. **Passive generation?** → not allowed (Design Pillar 4.8d)
7. **Chorus Node** — no structures ever (Governing Rule 8.1a)
8. **Portrait field** — fires at resolution (Governing Rule 5.1c); submitter-bounded (P16/L178)
9. **Card-as-condition?** → use Permanent + define `persistence_condition` + define `persistence_effect` + no board marker
10. **New ARBITER behavior?** → define as generalizable procedure in Art 03/07 first; `arbiter_note` references, does not define (Design Pillar 4.7b + Governing Rule 6.1)
11. **Narrative field** → Missing Author Vacuum: no flavor implies any faction knows what the message to the Chorus should say (Design Pillar 4.6b)
12. **Card Story block** → Can you write 1–3 sentences answering "What is actually happening in the world when this card is played?" as an event in New Meridian (not a mechanical description)? If not, redesign before finalizing spec. (Art 04 §5 P26 — locked S78)
13. **Arbiter notes** → Prefer structured spec fields (`success`/`fail`/`on_accept`/`on_decline`) over prose in `arbiter_note`. `arbiter_note` should reference existing Art 03/07 procedures, not encode effects that belong in spec fields.
