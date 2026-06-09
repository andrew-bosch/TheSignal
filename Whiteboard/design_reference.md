# Design Reference — Working Summary
*Condensed from Art 00a, 01, 02a, 02b, 03. Use this instead of pulling full artifacts into context.*
*Updated: S58. Verify against source artifacts if a rule feels uncertain before proposing a change.*

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
| Beat 0 | ARBITER validates each case (token present, payment present); invalid ops returned |
| Beat 1 | Covert operation effects that fire before dice roll (Automatic resolution; block mechanics) |
| Beat 2 | Positional wager cards (Beat 2 cards) |
| Beat 3 | Covert operation dice rolls; outcomes applied; Portrait fires |
| Beat 4 | Public acts (all months) |
| Beat 5 | Post-resolution cleanup; Battlefield Strength if Contested |

### Dispatch Rules
- Each covert op requires 1 Dispatch Token in case; each public act requires 1 token on declared card at Phase B (Governing Rule 7.3c); no token = rejected at Beat 0 (covert) or voided (public act)
- Cases sealed before transmit; no modifications after sealing (Governing Rule 7.3)
- Submission order = tiebreaker within resolution priority tiers (Governing Rule 7.3b)
- Ghost: 4 Dispatch Tokens/Quarter; others: 3

### End of Quarter (§21)
1. Findings decay: 7–12 → lose 2; 13+ → lose 4 (Art 03: this fires after Debrief, before Session Timeline)
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
| SCIF Record card | New component (S58 design); placed in Dispatch Case; fields: `Q_ | Draw _ modifier cards` |

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
- **Chorus Node:** ARBITER's 8 presence tokens permanent; Dominant unreachable; no structures; conversion rate bonus for presence here
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
| **Governing Rule 8.2** HARD | Max 1 structure block per faction per district | C01, C14, P03, P09 + new |
| **Governing Rule 8.2b** HARD | Structures lost immediately on Absent; no card can prevent | All presence-removing cards |
| **Governing Rule 8.3** | "At least 1 presence token" includes deployment markers | All cards |
| **Governing Rule 8.3a** | Deployment markers never removed — always moved | All cards targeting markers |
| **Governing Rule 8.3b** | No faction is eliminated | All |
| **Governing Rule 8.1a** HARD | No structures at Chorus Node | C01, C14 + new build cards |
| **Design Pillar 4.8c** | Floor Act always available (1 native resource); cannot be blocked | Public act design |
| **Design Pillar 4.8d** HARD | Passive generation (+1 native/Quarter) cannot be blocked or reduced | Resource cards |
| **Design Pillar 4.8a** | District resource type never changes | District-targeting cards |
| **Art 03 §9** | Structure block resource choice declared publicly at Upkeep | Upkeep procedure |
| **Governing Rule 5.1a** | Portrait accumulates, no drift or decay | Portrait fields |
| **Governing Rule 9.1** | Public Standing modifies roll difficulty only; not resource income | PS-affecting cards |
| **Art 04 §5 P19** HARD | Effects: exactly one of four durations — Immediate, Transient, Seasonal, Permanent; no other duration valid | All card effects |
| **Art 04 §5 P20** HARD | Actions proceed with whatever resources are committed; shortfalls carry consequences (partial = threshold penalty; zero = voided) | All cards |
| **Art 04 §5 P21** | Crit success never adds cost | All cards |
| **Governing Rule 5.1c** | Portrait fires at Resolution; unconditional on act or conditional on outcome | Portrait fields |
| **Art 04 §5 P23** | Ring modifier cards target only their ring's districts | Modifier card design |
| **Art 04 §5 P5** HARD | React conditions must be publicly observable — no hidden triggers | All React cards |
| **Art 04 §5 P24** | Corrupt applies only to physically written/recorded values (Intel tokens, Accords) | Corrupt function cards |
| **Design Pillar [04-n6 pending]** | Ghost may use C05 (Gather) without adjacency; all other Ghost cards require adjacency | Ghost card design |
| **Governing Rule 10.1a** | No card flavor may imply any faction knows the content of the message *(description needs verification — actual rule is Missing Author Vacuum)* | All flavor text |
| **Governing Rule 7.3a** HARD | Phases don't overlap; no revisiting prior phases | Timing rules |
| **Governing Rule 7.3** HARD | Commitment irreversible once case sealed / act declared | All |
| **Design Pillar 4.8b** | Crits (01–05 / 96–00) apply regardless of modifiers | All dice cards |
| **Governing Rule 7.3b** | Submission order is tiebreaker within priority tiers | Dispatch procedure |
| **Art 03** | Findings decay fires after Debrief, before Session Timeline advance | Findings cards |
| **Governing Rule 7.3c** HARD | Each action (covert op or public act) requires 1 Dispatch Token | All covert ops and public acts |
| **Governing Rule 6.1** | ARBITER executes general procedures, not card-specific instructions. `arbiter_note` fields reference existing procedures defined in governing artifacts — they do not define new ones. When a card requires new ARBITER behavior, that behavior must be defined as a generalizable procedure in Art 03 or Art 07 before the card is finalized. *(Art 04 Principle 18)* | All cards with ARBITER-facing content |

---

## Ghost-Specific Rules

- **Dispatch Tokens:** 4/Quarter (vs 3 for others) — extra covert op capacity
- **Adjacency exception:** C05 Gather only; all other Ghost cards require adjacency (Design Pillar [04-n6 pending])
- **Findings decay:** 7–12 lose 2; 13+ lose 4 (end of Quarter, after Debrief)
- **Intel Token holding:** max 4 (others max 2); own-faction tokens exempt
- **Deployment markers:** standard 2 per Quarter, placed in Phase 2 like all factions; convert to permanent chips at Upkeep Step 4; Ghost presence accumulates as operational residue even without territorial intent

---

## Design Flags for New Card Proposals

Before writing any new card spec, check:
1. Duration — one of: Immediate / Transient / Seasonal / Permanent (Art 04 §5 P19)
2. Resource payment — full proceeds at stated difficulty; partial incurs threshold penalty; zero voids the action (Art 04 §5 P20)
3. Does it target a deployment marker? → it moves, doesn't remove (Governing Rule 8.3a)
4. Does it affect Ghost adjacency? → only C05 is exempt (Design Pillar [04-n6 pending])
5. React trigger — is it publicly observable? (Art 04 §5 P5)
6. Does it affect passive generation? → not allowed (Design Pillar 4.8d)
7. Chorus Node — no structures ever (Governing Rule 8.1a)
8. Portrait field — fires at resolution (Governing Rule 5.1c); submitter-bounded (P16/L178)

---

## Gap Analysis — New Cards Required (S58)

*12 net new cards identified from faction playstyle summaries. Design priority: Ghost covert first, then remaining factions, then Art 04 Outstanding Issues.*

**Housekeeping**
- C39 Absolute Compromise — move from §8 to Standard Covert section (no redesign needed)

**Ghost — Covert (5 new)**

| ID | Card | Mechanic summary |
|----|------|-----------------|
| C-G1 | Station | Faction-keyed gather; place 1–2 Intel tokens for named faction; multiple deck copies |
| C-G2 | Full Take | Burst gather; n Intel → 2n faction-keyed tokens; 1 copy; NOT "Deep Cover" (C19 taken) |
| C-G3 | SCIF | Spend faction-keyed Intel token → place SCIF Record card in Dispatch Case (`Q_ \| Draw _ modifier cards`); at debrief draw modifier cards = target faction's building count at time of play |
| C-G4 | Flip | Spend faction-keyed Intel token → ARBITER loads target faction's native resources into Ghost's Dispatch Case at debrief |
| C-G5 | Signals Analysis | High-cost; Classified Directive deduction |

*Ghost adjacency applies to all five (Design Pillar [04-n6 pending] — only C05 exempt). Operations require deployment marker or presence chip in an adjacent district.*

**Guild — Covert (1 new)**

| ID | Card | Mechanic summary |
|----|------|-----------------|
| C-Gu1 | Labor Contract | Placeholder pending design; PM05 04-n3 |

**Directorate — Covert (2 new), Public (1 new)**

| ID | Card | Type | Mechanic summary |
|----|------|------|-----------------|
| C-D1 | Regulatory Downgrade | Covert | Suppress a faction's influence tier in a district |
| C-D2 | Regulatory Freeze | Covert | Block tier advancement for a faction in a district |
| P-D1 | Entry/Exit Controls | Public | Persistent World Event; threshold penalty |

**Syndicate — Covert (3 new)**

| ID | Card | Mechanic summary |
|----|------|-----------------|
| C-S1 | Land Title | Capital purchase of district native resource without presence requirement |
| C-S2 | Hostile Takeover | Transfer presence tokens from target faction to Syndicate (distinct from C33 structure purchase) |
| C-S3 | Accord Transfer | Transfer or modify an existing active Accord |

*Network: Tripwire confirmed as universal modifier card type, not a Network PA. Network PA stubs (P10–P14) may be sufficient pending full PA design pass.*

---

## Card Schema — Open Fields (Research Notes S23)

*Full reference: `~/Projects/Whiteboard/researchNotes_CardDesign.md`. Items below are actionable for new card specs.*

When writing a new card spec, include these fields (some are gaps not yet in all existing cards):

| Field | Status | Notes |
|-------|--------|-------|
| `Card version` | Gap — L108 | Add "v1.0" to all new cards; enables errata tracking on physical copies |
| `Trigger condition` | Gap — React/Tripwire only | Structured field: when does the card activate? `N/A` for standard ops |
| `Outcome type` | Gap — Public Acts only | `Binary \| Elect player \| Bilateral agreement \| Unilateral` etc. |
| Per-field VS-xx | Gap — L2+ | Effect fields = VS-06 (Conditional); Portrait = VS-04 (ARBITER-only); card face fields = VS-01 |

*Intra-Beat priority: covered by Art 03 §7 submission order rule — no card-level field needed. Compound effect text: known L108 violation, deferred until card content locked (documented in 00b).*
