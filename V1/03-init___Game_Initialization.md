# 03-init — Game Initialization
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.3 — Draft S84
**Status:** In progress — gaps surface during Art 03 rubric pass
**Depends on:** 01 — Game Board: New Meridian; 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking; 00c — Economy Manifest (pending); Art 04 §12 (card decks, pending)
**Called by:** 03 — at session start, before Quarter 1

---

## 1. Overview

Establishes all components, resources, and game state at T=0. Produces a valid starting configuration for Art 03 Quarter 1. ARBITER oversees setup; Faction Players set up their own Terminals and resources.

---

## 2. setup_state

T=0 snapshot. All runtime tables (`component_positions`, `faction_resources`, `faction_standing`, `district_control`) are seeded from this data at session start. Zone and component names are FK references to `game_zones` and `components`.

### §2.1 Board Components

All structural and environmental components placed before faction setup begins.

| Component | Zone | on_component_id | Notes |
|-----------|------|-----------------|-------|
| The Overview (game mat) | Central Area | — | Placed at center |
| District tile ×21 | The Overview | — | All 21 placed on mat; designated subzone |
| Ring Modifier Deck ×3 | The Overview | — | One per ring (Rings 1–3); designated subzone adjacent to respective ring |
| Session Timeline | The Overview | — | Designated subzone: left side (P1/P2 adjacency) |
| Initiative Strip | The Overview | — | Designated subzone: left side (P1/P2 adjacency) |
| Chorus Activity Track | The Overview | — | Designated subzone: right side (P5 adjacency) |
| Situation Report Zone | The Overview | — | Designated subzone: right side (P5 adjacency) |
| Public Standing Track | The Overview | — | Designated subzone: bottom (P3 adjacency) |
| Reservoir | The Overview | — | Designated subzone: shared resource supply (resource tokens only) |
| ARBITER Screen | P6 | — | — |
| ARBITER Tableau | P6 | — | — |
| Portrait track | P6 | — | Behind ARBITER screen |
| Faction Screen ×5 | P1–P5 | — | One per faction position |
| Faction Terminal ×5 | P1–P5 | — | One per faction position |
| Faction Resolution Grid ×5 | P1–P5 | — | One per faction position |
| Backlog | Supply | — | — |

### §2.2 Faction Starting Tokens

Only districts with starting tokens are listed. All other districts start empty.

| Component | District | Faction | Count | Influence Level |
|-----------|----------|---------|-------|-----------------|
| Presence chip | University Perimeter | Ghost | 1 | Present |
| Presence chip | University Perimeter | Network | 1 | Present |
| Presence chip | Media District | Network | 2 | Established |
| Presence chip | Industrial Fringe | Guild | 1 | Present |
| Presence chip | Commercial Strip | Syndicate | 1 | Present |
| Presence chip | Civic Center | Directorate | 1 | Present |
| Presence chip | Broadcast Tower | Network | 1 | Present |
| Presence chip | Power Grid | Guild | 3 | Dominant |
| Presence chip | Financial Clearinghouse | Syndicate | 3 | Dominant |
| Presence chip | Data Exchange | Ghost | 2 | Established |
| Presence chip | Communications Hub | Network | 2 | Established |
| Presence chip | Logistics Center | Guild | 1 | Present |
| Presence chip | Research Institute | Ghost | 1 | Present |
| Presence chip | Regulatory District | Directorate | 1 | Present |
| Presence chip | Government Citadel | Directorate | 1 | Present |
| Presence chip | Military Installation | Directorate | 2 | Established |
| Presence chip | Chorus Research | Ghost | 2 | Established |
| Presence chip | Financial Sanctum | Syndicate | 2 | Established |
| Presence chip | Chorus Node | Directorate | 1 | Present |

### §2.3 ARBITER Starting Components

| Component | Zone | Notes |
|-----------|------|-------|
| ARBITER Dominance Marker | Chorus Node | Never removed |

### §2.4 Faction Special Starting Conditions

| Faction | Condition |
|---------|-----------|
| The Network | Virtual structure block at University Perimeter. Not a physical block — cannot be demolished; does not count toward the 1-structure-per-faction-per-district limit. Counts toward modifier draw (§7.5.3) while Network holds any presence at University Perimeter. |

### §2.5 Track Starting Values

| Marker | Track / Strip | Starting Value |
|--------|--------------|----------------|
| Pointer marker | Session Timeline | Q1M1 |
| Activity marker | Chorus Activity Track | 1 |
| Threshold marker | Chorus Activity Track | 6 (default) |
| Standing marker ×5 | Public Standing Track | 10 (Neutral) — each faction |
| Portrait marker ×5 | ARBITER Portrait Track (hidden) | 0 (Ambiguous) — each faction |
| Faction order markers ×5 | Adjacent to Initiative Strip | — (order determined at §7.1) |

### §2.6 Starting Resources

| Faction | Resource | Amount |
|---------|----------|--------|
| Ghost | Findings | 5 |
| Ghost | Mandate | 1 |
| The Network | Exposure | 3 |
| The Network | Mandate | 2 |
| The Syndicate | Capital | 6 |
| The Syndicate | Mandate | 1 |
| The Guild | Capital | 1 |
| The Guild | Capacity | 4 |
| The Directorate | Findings | 1 |
| The Directorate | Capacity | 1 |
| The Directorate | Mandate | 4 |

### §2.7 Faction Starting Supply

Per-faction components at faction tableau at T=0. All counts TBD unless noted.

| Component | Count | Notes |
|-----------|-------|-------|
| Deployment marker | 2 | — |
| Dispatch Case | 1 | Empty at T=0 |
| Emergency Response card | 1 | — |
| Operative card | 1 | Distributed at §3.6 |
| Floor Act PA card | 1 | Distributed at §3.6 |
| Countermeasure card (CM-A) | 1 | Distributed at §3.7 |
| Countermeasure card (CM-B) | 2 | Distributed at §3.7 |
| Classified Objective card | 1 | Distributed sealed at §3.8 |

### §2.8 ARBITER Starting Supply

Components at ARBITER Tableau at T=0. Subzones TBD. All counts TBD unless noted.

| Component | Notes |
|-----------|-------|
| Presence chip | — |
| Established marker | — |
| Dominant marker | Pending DB registration (DB-14) |
| Structure block | — |
| Control flag | — |
| Tension marker | — |
| Intel token | — |
| Status marker | — |
| Modifier token | — |
| Accord agreement | — |
| Notification Slip (NS-xx) | — |
| Intel Delivery Slip (IS-xx) | — |
| Target Profile | — |
| Sealed Apex ability | One per operative; pending DB registration (DB-15) |
| Broadcast Deck | 1 deck | Situation Report Zone (designated subzone on Overview) |
| Broadcast Effect Deck | 1 deck | ARBITER Tableau (subzone TBD) |

---

## 3. Setup Procedure

### §3.1 Seat Players

Assign positions P1–P5 (Faction Players) and P6 (ARBITER). Confirm faction assignments before proceeding.

### §3.2 Lay Out Board Components

Place all components per §2.1 in their designated zones.

### §3.3 Place ARBITER Components

1. ARBITER places the ARBITER Dominance Marker at the Chorus Node (§2.3).
2. ARBITER positions Screen and Tableau at P6. Tableau clear.

### §3.4 Seed Starting Tokens

1. Place all presence chips per §2.2.
2. Place an influence marker on each district stack whose Influence Level column shows Established (Established marker) or Dominant (Dominant marker).
3. Verify influence levels match the table.
4. Note Network virtual structure block (§2.4) — no physical component placed.

### §3.5 Set Track Starting Values

Set all markers per §2.5:

1. Session Timeline → Q1M1
2. Chorus Activity Track → threshold marker at 6; activity marker at 1
3. Public Standing Track → all five faction markers at 10
4. ARBITER Portrait Track (hidden) → all five faction markers at 0

*Faction order markers placed adjacent to Initiative Strip at T=0. Order determined during §7.1 Upkeep.*

### §3.6 Faction Terminal Setup

Each Faction Player simultaneously:

1. Places Faction Screen at assigned position
2. Places Faction Terminal at assigned position
3. Places Dispatch Case at assigned position — empty
4. Collects starting resources from Reservoir per §2.6
5. Collects starting hand: 1 Operative card, 1 Floor Act PA card

*[TBD — distribution source: Art 04 §12]*

### §3.7 Distribute Countermeasures

Each faction receives 3 Countermeasure cards: 1 CM-A and 2 CM-B. Place in designated Terminal area.

*[TBD — card design: Art 04]*

### §3.8 Distribute Classified Directives

ARBITER distributes one sealed Classified Directive to each faction.

*[TBD — design pending: Art 06.x]*

### §3.9 Distribute and Shuffle Card Decks

*[TBD — deck construction and distribution: Art 04 §12. Decks required: covert operation deck (per faction), public act deck (per faction), faction modifier deck (per faction), Ring Modifier Decks ×3, Broadcast Deck, Broadcast Effect Deck, Battlefield Modifier deck.]*

### §3.10 ARBITER Verification

ARBITER confirms before proceeding:

| Check | Source |
|-------|--------|
| All board components in position | §2.1 |
| All starting tokens placed; influence levels correct | §2.2 |
| ARBITER Dominance Marker at Chorus Node | §2.3 |
| All tracks at starting values | §2.5 |
| All factions hold starting resources | §2.6 |
| All card decks shuffled and in position | §3.9 |
| All factions hold 3 Countermeasure cards (1 CM-A + 2 CM-B) | §3.7 |
| ARBITER supply in position | §2.8 |
| All factions hold 1 sealed Classified Directive | §3.8 |
| All Dispatch Cases at faction positions — empty | §3.6 |
| Backlog holds full Dispatch Token supply | §2.1 |

---

## 4. First Quarter Entry Conditions

All of the following must be true before Art 03 §7 Upkeep begins:

- [ ] All components in setup_state positions (§2.1–§2.4)
- [ ] All tracks at starting values (§2.5)
- [ ] All factions hold starting resources (§2.6)
- [ ] All card decks shuffled and in position
- [ ] All factions hold 3 Countermeasure cards (1 CM-A + 2 CM-B)
- [ ] All factions hold 1 sealed Classified Directive
- [ ] All Dispatch Cases at faction positions — empty
- [ ] Backlog holds full Dispatch Token supply
- [ ] ARBITER Tableau clear; ARBITER Screen in place

---

*03-init v0.3 — Draft S84*
