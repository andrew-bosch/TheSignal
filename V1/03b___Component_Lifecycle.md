# 03b — Component Lifecycle Register

**Version:** 0.1
**Status:** In Progress — S88 initial formalization from Whiteboard/component_lifecycle_S88.md
**Depends on:** 02 (component design descriptions), 03-init (setup counts/zones), 03 (procedures), 00b (DB registry)

**Information hierarchy:** DB (canonical registration) → Art 01 (board zones and physical layout) → Art 02 (component design descriptions) → 03-init (starting counts and zones) → Art 03 (procedural use) → Art 03b (lifecycle traceability)

---

## Purpose

This artifact is the authoritative traceability record for every physical game component. For each component it answers: where does it start at T=0, what states does it pass through during play, and where does it go when removed.

**Governance:** Any new component introduced to the game system must have a lifecycle row added here before or at the same time it is registered in 00b §4. Any Art 03 procedure change that affects component entry, movement, or exit must be reflected here.

**Relationship to 03-init:** 03-init §2 defines starting counts and supply zones. This document traces what happens after that.

**Relationship to 03a:** 03a defines formal state transitions as code. This document defines them as human-readable procedure steps.

---

## How to Read This Document

Each component section contains a lifecycle table with columns:

| State | When | Section |
|-------|------|---------|

- **State** — the physical status of the component (e.g., "In ARBITER supply", "On grid slot", "Held by faction")
- **When** — the trigger or action that produces this state
- **Section** — the governing Art 03 section reference

Open gaps are flagged inline with **[GAP]** and cross-referenced to PM05.

---

## 1. Structural / Permanent Board Fixtures

Placed at 03-init §3.2. Never removed during play.

| Component | 03-init Source | Notes |
|-----------|---------------|-------|
| The Overview (game mat) | §2.1 | Permanent infrastructure. |
| District tile ×21 | §2.1 | Permanent. Never moved. |
| Ring Modifier Deck ×3 | §2.1 | Cards drawn each Quarter (§7.5.3.1); discarded when used. Deck not reshuffled when exhausted. |
| Session Timeline | §2.1 | Pointer advances at §9.4.4.1 (month) and §12.4 (Quarter). |
| Initiative Strip | §2.1 | Faction order markers reordered at §7.1 each Quarter. |
| Chorus Activity Track | §2.1 | Markers updated per ARBITER script and §11.2. |
| Public Standing Track | §2.1 | Standing markers move at §7.2.4 and per card outcomes throughout. |
| Reservoir | §2.1 | Universal resource token pool. Tokens flow in/out throughout play; see Section 8. |
| ARBITER Screen | §2.1 (P6) | Permanent. Never moves. |
| ARBITER Tableau | §2.1 (P6) | Zone. Components placed here during play. |
| Portrait Track | §2.1 (P6, hidden) | Permanent behind screen. Markers move at §9.4.2.4.0 and §9.4.3.5.0. |
| Faction Screen ×5 | §2.1 (P1–P5) | Permanent per faction. |
| Faction Terminal ×5 | §2.1 (P1–P5) | Zone. Faction-held components stored here. |
| Faction Resolution Grid ×5 | §2.1 (P1–P5) | Zone. Cards placed at §9.2, §9.3, §9.4.1. Cleared per duration rules. |
| Backlog | §2.1 | Zone. Dispatch Tokens return here at §9.4.0.2 and §9.4.3.1.0.0. |

---

## 2. ARBITER Dominance Marker

| State | When | Section |
|-------|------|---------|
| Placed at Chorus Node | T=0 setup | §3.3 |
| Remains permanently | Never removed | §2.3 |

---

## 3. Faction Starting Supply

### Deployment Marker ×2

| State | When | Section |
|-------|------|---------|
| In faction hand | T=0 | §2.7 |
| Placed on board (Converting face) | §8 Placement | §8.0 |
| Flipped to Blocked face | Broadcast Card effect, targeting restriction, or card-specified fail | §7.2.5, §9.4.1.0, §9.4.2.2, §9.4.3.3 |
| Persists on board | Across §9–§12 and into next Quarter | — |
| Converting → presence chip placed; marker returned to hand | §7.3.1 of following Quarter | §7.3.1 |
| Blocked → returned to hand without chip | §7.3.2 of following Quarter | §7.3.2 |

### Dispatch Case ×1

| State | When | Section |
|-------|------|---------|
| Case with 4 empty Dispatch Packets at faction position | T=0 | §2.7, §3.6 |
| Faction loads packets: op card + Dispatch Token + resources + Target Profile + Modifier Cards | §9.1.1 | §9.1 |
| Case sealed | §9.1.2 | — |
| Transmitted to ARBITER receive queue | §9.1.3 | — |
| Opened by ARBITER; packets extracted lane by lane | §9.4.0 Beat 0 | §9.4.0.1 |
| Resolved op cards + outcomes placed back into packet | §9.4.2 Beats 2–3 | §9.4.2.3 Step 3.1 |
| Case returned to faction with packets inside | §9.4.2.6.0 | — |
| Faction opens case → reads results → places packets back | §9.4.2.6.1 | §9.4.2.6.1.1 |
| Reused each Month | — | Case must be functionally clear before §9.1 |

*Dispatch Packet registration and physical spec: PM05 03-n06.*

### Emergency Response Card ×1

| State | When | Section |
|-------|------|---------|
| In faction terminal | T=0 (via §3.6) | §2.7 |
| Submitted to ARBITER (Apex only) | §14 Step 2 | §14 |
| Return / refresh after Apex failure | Pending Art 04/05 design | §14 |
| Apex success: session ends | §14 Step 4 | — |

### Operative Card ×1

| State | When | Section |
|-------|------|---------|
| In faction terminal | T=0 (via §3.6) | §2.7 |
| Submitted as Apex covert op | §9.1 — in Dispatch Packet | §14 |
| Apex cancelled: operative retained | §14 Step 3 | §14 |
| Apex success: session ends; operative retires | §14 Step 4 | — |

### Floor Act PA Card ×1

| State | When | Section |
|-------|------|---------|
| In faction terminal | T=0 (via §3.6) | §2.7 |
| Follows PA card lifecycle | §9.2 → §9.4.3 | See PA Cards (Section 5) |

### Countermeasure Card (CM-A ×1, CM-B ×2)

| State | When | Section |
|-------|------|---------|
| In faction terminal CM area | T=0 (via §3.7; issued, not drawn) | §2.7, §3.7 |
| Deployed to ARBITER (covert) or played publicly (PA) | §9.3.0 per Monthly window | §9.3 |
| Submitted CM: attached to dispatch case; matched at Beat 0 | §9.3.1, §9.4.0.1 item 0 | — |
| Publicly played CM: in CM zone of Faction Resolution Grid | §9.3.1 | — |
| CM-A applied at Beat 1 (covert) or Beat 4 (PA invalidation) | §9.4.1.2, §9.4.3.1.2 | — |
| CM-B: modifier token placed on targeted ops | §9.4.1.2 | — |
| CM card discarded after processing — removed from game | §9.4.1.2 item 4 | §17.2 |
| Unused: carry forward to next Monthly window | — | §17.5 |

*CM cards are not replenished — each faction has 3 for the entire session.*

### Classified Objective Card ×1

| State | When | Section |
|-------|------|---------|
| Sealed, distributed to faction | T=0 (via §3.8) | §2.7, §3.8 |
| Lifecycle | TBD — Art 06.x design pending | §3.8 |

### Target Profile

| State | When | Section |
|-------|------|---------|
| Blank, in faction tableau storage | T=0 | §2.7 (count TBD — PM05 03-n16) |
| Filled with target info before dispatch / declaration | Before §9.1 or §9.2 | — |
| Placed with covert op in Dispatch Packet | §9.1.1 | §9.1 |
| Placed with public act on Faction Resolution Grid | §9.2 | §9.2 |
| Used in resolution: ARBITER reads targeting info | §9.4.0.1, §9.4.2, §9.4.3 | — |
| Returned to faction via Dispatch Case (covert) | §9.4.2.6 | — |
| Extracted from packet by faction player | §9.4.2.6.1.0 | — |
| Returned to faction via PA cleanup (public) | §9.4.3.4 Step 5 | — |
| Recycled: erased if reusable / discarded if single-use | After each use | PM05 03-n16 (physical design TBD) |

---

## 4. ARBITER Starting Supply

### Presence Chip

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed at starting positions | §3.4 | §2.2 |
| Placed (marker conversion) | §7.3.1 | — |
| Placed (covert success) | §9.4.2.2.0 | — |
| Placed (PA success) | §9.4.3.3.0 | — |
| Moved from adjacent district in Press | §10.1.4.0.2 | — |
| Removed by winning faction in contest | §10.1.4.0 | — |
| Returned to ARBITER supply | §10.1.4.0, §10.1.5 | — |
| *Gap:* §7.3.3 and §8.2 update language lacks explicit return instruction | — | Fixed S88 — return language added |

### Established Marker

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed at starting Established positions | §3.4 | §2.2 |
| Placed / removed when IL-02 threshold met / lost | §7.3.3, §8.2, §9.4.2.2.0, §9.4.3.3.0, §10.1.5 | §13.7 |
| Returned to ARBITER supply on removal | §7.3.3, §8.2, §10.1.5 | §13.7 |

### Dominant Marker

*Canonical name confirmed S88. DB-14 = rename "Control flag" → "Dominant marker" in component table.*

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed when faction achieves IL-01 in a district | Any influence board change producing IL-01 | §13.7 |
| Removed when faction is no longer Dominant | Any board change removing IL-01 | §13.7 |
| Returned to ARBITER supply on removal | §7.3.3, §8.2, §10.1.5 | §13.7 |

### Tension Marker

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed when IL-01 tie occurs in a district | Any board change producing two+ factions at IL-01 | §13.7 |
| Scanned by ARBITER at Resolve District Tension | §10.0 | §10 |
| Removed (winner): returned to ARBITER supply | §10.1.4.0 | — |
| Removed (tie): ARBITER removes | §10.1.4.1 | — |
| Removed when tie breaks by any means | — | §13.7 |

### Structure Block

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed by faction via covert / PA success | Per card spec | §9.4.2.2.0, §9.4.3.3.0 |
| Counted in Battlefield Strength | §10.1.2 | — |
| Removed per card effect | Card-specific | — |
| Removed when faction influence → 0 in district | Any board change causing count = 0 | §13.7 |
| Returned to ARBITER supply on removal | All removal paths | §13.7 |

### Intel Token

| State | When | Section |
|-------|------|---------|
| In ARBITER supply (The Dossier) | T=0 | §2.8 |
| Quarter number + faction written by ARBITER at issuance | Per card spec success outcome | §9.4.0.1 |
| Delivered via Dispatch Packet (covert) | §9.4.2.2.0 | — |
| Held by faction; persists across Quarters | — | General faction-asset principle |
| Submitted with covert op: placed in Dispatch Packet | §9.1.1 | — |
| Age calculated at Beat 0 (covert) | §9.4.0.1 | §13.6 |
| Reset (erased) and returned to The Dossier; or discarded if single-use | §9.4.0.1 | — |
| Submitted with public act: handed to ARBITER at Beat 4 | §9.4.3.1.0.1 | — |
| Age calculated; reset and returned | §9.4.3.1.0.1 | §13.6 |
| Played in district contest | §10.1.2 — handed to ARBITER; reset; returned | §10.1.2 |

### Status Marker

| State | When | Section |
|-------|------|---------|
| Listed in ARBITER supply | T=0 | §2.8 |
| Distribution step: **[GAP — XA-07 open]** | — | XA-07 |
| Flipped to Discussing | Each Quarter Open | §7.0 |
| Flipped to Ready | Debrief close readiness | §11.3 |

### Modifier Tokens (M-06 Partial Payment, M-09 Protect, M-11 CM-B)

| Token | State | When | Section |
|-------|-------|------|---------|
| M-06 | In ARBITER supply | T=0 | §2.8 |
| | Placed on card | Beat 0 (§9.4.0.1) or Beat 4 (§9.4.3.1.0.2) when partial payment submitted | — |
| | Applied to threshold | §9.4.2.1.0, §9.4.3.2.0 | §13.5 |
| | Returned to ARBITER supply | §9.4.2.3 Step 3, §9.4.3.4 Step 1 | — |
| M-09 | In ARBITER supply | T=0 | §2.8 |
| | Placed on card | Beat 2 per card effect | §13.5 |
| | Applied | §9.4.2.1.0 | §13.5 |
| | Returned to ARBITER supply | §9.4.2.3 Step 3 | — |
| M-11 | In ARBITER supply | T=0 | §2.8 |
| | Placed on targeted covert ops | §9.4.1.2 Step 2 (Beat 1) | §13.5 |
| | Applied | §9.4.2.1.0, §9.4.3.2.0 | §13.5 |
| | Returned to ARBITER supply | §9.4.2.3 Step 3, §9.4.3.4 Step 1 | — |

### BM-xx (Boost Marker)

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Retrieved from ARBITER supply; n tokens placed on covert op grid slot | Beat 0: n = floor(excess ÷ boost unit cost) | §9.4.0.1 |
| Retrieved from ARBITER supply; placed on public act | Beat 4 | §9.4.3.1.0.0 |
| Applied: threshold modified; effects × (1+n) | §9.4.2.1.0, §9.4.2.2; §9.4.3.2.0, §9.4.3.3 | §13.5 |
| One NS-xx delivered regardless of n | §9.4.2.2, §9.4.3.3 | — |
| Returned to ARBITER supply | §9.4.2.3 Step 3 item 4 (covert), §9.4.3.4 Step 1 (PA) | — |

### VM-xx (Visibility Marker)

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Placed on target faction's grid card | Beat 2: per card effect (C28 Breaking News success) | Card-effect-driven |
| Triggers public resolution mode | §9.4.2.0.1 — announce card, type, targets | §9.4.2 |
| Returned to ARBITER supply | §9.4.2.3 Step 3 item 4 | — |

### Accord Agreement (Accord Form)

| State | When | Section |
|-------|------|---------|
| In ARBITER supply (blank) | T=0 | §2.8 |
| Delivered to faction (blank) via Overture success | Beat 4 per card spec | Art 04 §11.8 |
| Drafted: faction fills in terms | After receipt; anytime | Art 06 §9.4 |
| Placed in Accord Placement Area | After drafting; anytime | Art 06 §9.4 |
| Active: governs per Accord terms | Until Dissolved or Completed | Art 06 §9 |
| Dissolved: Debrief only | Art 06 §9.6 | — |
| Completed: per completion clause | Art 06 §9.7 | — |

### Notification Slip (NS-xx)

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Written + placed in Dispatch Packet by ARBITER | Per card spec — covert/PA success/fail | §9.4.2.2.0/1, §9.4.3.3.0/1 |
| Held by faction after case return | §9.4.2.6.1.1 | — |
| Returned to ARBITER supply | §12.3 Quarter Close | §12.3 |

### Intel Delivery Slip (IS-xx)

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Written + placed in Dispatch Packet by ARBITER | Per card spec — covert outcome; Beat 2 delivery (C24, pending 04-n44) | §9.4.2.2.0 |
| Held by faction indefinitely | — | By design — IS-xx carries substantive intelligence. No return step. |

### Sealed Apex Ability

| State | When | Section |
|-------|------|---------|
| In ARBITER supply (one per operative; pending DB-15) | T=0 | §2.8 |
| Held sealed until Apex triggers | — | §14 |
| Opened by ARBITER | §14 Step 4 — Apex succeeds | §14 |
| One-use; session ends immediately | §14 Step 4 | — |
| Remains sealed if Apex cancelled | §14 Step 3 | §14 |

### Broadcast Deck

| State | When | Section |
|-------|------|---------|
| In Situation Report Zone | T=0 | §2.8 |
| Top card drawn each Quarter | §7.2.0 | §7.2 |
| Drawn card placed face-up in Situation Report Zone | §7.2.0 | — |
| Removed at Quarter Close (Seasonal) | §12.0 | — |
| Removed at Close Month (Transient) | §9.4.4.0 | — |
| Remains if Permanent | Per card text | — |
| Deck stays in place; not reshuffled | — | — |

### Broadcast Effect Deck

| State | When | Section |
|-------|------|---------|
| In ARBITER Tableau | T=0 | §2.8 |
| Matching card located and placed on ARBITER Tableau | §7.2.1 | §7.2 |
| Applied at Beat 1 (standing effects, silent) | §9.4.1.1 | — |
| Applied at Beat 4 pre-resolution | §9.4.3.0.1 | — |
| Expired cards moved to expired area | §7.2.6 (start of next Quarter) | — |

### Debrief Action Card

| State | When | Section |
|-------|------|---------|
| In ARBITER supply | T=0 | §2.8 |
| Delivered via Dispatch Packet on card success | Per card spec | §9.4.2.2.0 |
| Returned to faction inside Dispatch Case | §9.4.2.6 | — |
| Moves to faction hand at case unpack | §9.4.2.6.1.1 | — |
| Held in faction hand until Debrief | — | — |
| Resolved at §11.1: announced + executed + handed to ARBITER | §11.1 | — |
| Removed from game or returned to ARBITER supply per card text | §11.1 | — |

### ARBITER Threshold Slider

| State | When | Section |
|-------|------|---------|
| **Not in 03-init — pending 03-n11** | — | 03-n11 |
| Proposed: ARBITER Tableau at T=0 | — | — |
| Used at Beat 0/2/3 covert resolution | §9.4.2.1.0 | — |
| Persistent; never leaves ARBITER Tableau | — | — |

### Faction Threshold Slider

| State | When | Section |
|-------|------|---------|
| **Not in 03-init — pending 03-n12** | — | 03-n12 |
| Proposed: open area on Overview at T=0 | — | — |
| Retrieved by first Faction Player in initiative order | §9.4.3.0.0 | Beat 4 |
| Passed player to player during Beat 4 | §9.4.3.6 | — |
| Returned to Overview by last player | §9.4.3.6 | — |

---

## 5. Card Types (Drawn from Decks)

**General principle:** Faction-held assets (cards in hand, modifier cards, resources, Intel Tokens, IS-xx) persist across Quarters and Months. Only components with an explicit exit step leave faction possession at a defined moment.

### Covert Operation Card

| State | When | Section |
|-------|------|---------|
| In draw deck | Setup / after reshuffle | §3.9 |
| Drawn to faction hand | §7.5.2.0 each Quarter | §7.5 |
| Deck exhausted mid-draw: shuffle discard → new draw deck → continue | §7.5.2.0 | §7.5.2 |
| Placed in Dispatch Packet | §9.1.1 | §9.1 |
| Placed face-up or face-down in Resolution Grid | §9.4.0.1 | — |
| Resolved: outcome applied | §9.4.2 | — |
| Placed in Dispatch Packet for return | §9.4.2.3 Step 3 | — |
| Returned in case to faction | §9.4.2.6 | — |
| Placed in CA discard deck → available for reshuffle | §9.4.2.6.1.1 | — |

### Public Act Card

| State | When | Section |
|-------|------|---------|
| In draw deck | Setup / after reshuffle | §3.9 |
| Drawn to faction hand | §7.5.2.1 each Quarter | §7.5 |
| Declared: placed face-up on Faction Resolution Grid with Target Profile + Dispatch Token + resources | §9.2 | §9.2 |
| Resolved: Beat 4 | §9.4.3 | — |
| Cleared per duration: | | |
| — Immediate or invalidated | §9.4.3.4 item 3 → PA discard | §15 |
| — Transient | §9.4.4.0 → PA discard | §15 |
| — Seasonal | §12.0 → PA discard | §15 |
| — Permanent: removed per card text | Per card | §15 |

### Modifier Card (Faction, Ring, or Battlefield)

| State | When | Section |
|-------|------|---------|
| Drawn to modifier area of faction tableau | §7.5.3.0 (faction) / §7.5.3.1 (ring) | §7.5 |
| Held in modifier area | — | — |
| Assigned: placed in Dispatch Packet (covert) | §9.1.1 | §9.1 |
| Assigned: placed alongside PA on Resolution Grid | §9.2 | §9.2 |
| Applied: threshold modifier read | §9.4.2.1.0 (covert), §9.4.3.2.0 (PA) | §13.5 |
| Discarded — removed from game | §9.4.2.3 Step 3 item 3 (covert), §9.4.3.4 Step 2 (PA) | — |
| Battlefield variant: played at §10.1.2; removed from game | §10.1.2 | §10 |
| Unassigned: carries forward to next Quarter | §7.5.1 | §7.5 |

---

## 6. Dispatch Token

| State | When | Section |
|-------|------|---------|
| In Backlog | T=0 | §2.1, §3.10 |
| Distributed to factions (4 per faction per Quarter) | §7.5.0 | §7.5 |
| Placed in Dispatch Packet with covert op | §9.1.1 | §9.1 |
| Placed on declared PA card | §9.2 | §9.2 |
| Collected from grid (covert): returned to Backlog | §9.4.0.2 | — |
| Returned from PA card: to Backlog | §9.4.3.1.0.0 | — |

*Dispatch Token allotment (4/Quarter) to be registered in 03-init as a game parameter — PM05 §21 note.*

---

## 7. Track Markers (Persistent — Never Leave Their Tracks)

| Component | Track | Key Movements |
|-----------|-------|---------------|
| Standing marker ×5 | Public Standing Track | Placed at 10 (T=0, §2.5). Moves per §7.2.4, card outcomes at §9.4.2.2, §9.4.3.3. |
| Portrait marker ×5 | Portrait Track (hidden) | Placed at 0 (T=0, §2.5). Moves at §9.4.2.4.0, §9.4.3.5.0. ARBITER-only. |
| Faction order markers ×5 | Initiative Strip | Adjacent at T=0 (§2.5). Order set at §7.1 each Quarter. |
| Pointer marker | Session Timeline | Q1M1 at T=0 (§2.5). Advances at §9.4.4.1 (month) and §12.4 (Quarter). |
| Activity marker | Chorus Activity Track | Position 1 at T=0 (§2.5). Updated per ARBITER script and §11.2. |
| Threshold marker | Chorus Activity Track | Position 6 at T=0 (§2.5). Default for Chorus Question Window. |

---

## 8. Resource Tokens

All faction resource types (Findings, Exposure, Capital, Capacity, Mandate). Tokens are not faction-specific in physical form — faction doctrine determines which types are native.

| State | When | Section |
|-------|------|---------|
| In Reservoir | T=0 | §2.1 |
| Distributed to factions as starting resources | §3.6 Step 4: collect from Reservoir per §2.6 | §2.6, §3.6 |
| Collected as income each Quarter | §7.4 | §7.4 |
| Carried forward across Quarters and Months | — | General faction-asset principle |
| Spent (drained to Reservoir) — covert ops | §9.4.0.1 Beat 0 | §9.4.0.1 |
| Spent — public acts | §9.4.3.1.0.0 Beat 4 | §9.4.3.1.0.0 |
| Retained (resource-retaining cards) | §9.4.0.1: placed on card, not drained | §9.4.0.1 |
| Traded between factions | §11.0 Debrief | §11.0 |
| Findings Decay — Ghost only | §12.1: returns Findings to Reservoir per bracket | §12.1 |

---

## 9. Open Gaps

| ID | Gap | Severity | Status |
|----|-----|----------|--------|
| GAP-5 / S88 | Established/Dominant marker return language in §7.3.3, §8.2 | Resolved | Fixed S88 |
| GAP-1 / S88 | Tension marker placement trigger undefined | Resolved | §13.7 added S88 |
| GAP-2/3 / S88 | Structure block removal + return rule missing | Resolved | §13.7 added S88 |
| GAP-4 / S88 | Target Profile missing from 03-init §2.7 | Resolved | Added S88 |
| 03-n06 | Dispatch Packet physical spec | Open | PM05 03-n06 |
| 03-n11 | ARBITER Threshold Slider — register + add to 03-init | Open | PM05 03-n11 |
| 03-n12 | Faction Threshold Slider — register + add to 03-init | Open | PM05 03-n12 |
| 03-n16 | Target Profile cleanup procedure (physical design TBD) | Open | PM05 03-n16 |
| XA-07 | Status Marker distribution step missing | Open | PM05 XA-07 |
| DB-14 | Dominant marker rename in component table | Open | PM05 DB-14 (agy) |
| DB-15 | Split id=15 into Operative Card + Sealed Apex Ability | Open | PM05 DB-15 |

---

*v0.1 — S88. Formalized from Whiteboard/component_lifecycle_S88.md. Whiteboard source file to be deleted after PM03 registration.*
