# 05 — Operative & Apex System
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 Draft — Placeholder  
**Status:** 🔄 Draft — Blocked by Artifact 04 completion  
**Last Updated:** 2026-05-15  
**Depends on:** 04 — Action Card System; 03 — Round Structure & Gameplay; 02 — Components  
**Supersedes:** l1_operatives (retired artifact), apex_system (retired artifact)

---

## 1. Overview

### Problem This Document Solves
Faction cards represent doctrine at scale — what the organization does. Operatives represent individuals: singular people whose capabilities exceed what any card system can express. This artifact defines what operatives are, how they enter play, what they can do, and what it costs to deploy them at their full potential.

The Apex trigger is the mechanism by which an operative's sealed power is unlocked — and, if resolved, ends the session early. It is the highest-stakes moment in the game.

### Deliverable
A complete system definition for all operative cards across five factions (Tier 1–3), the Apex trigger and resolution procedure, Founding Figure operatives, cooldown rules, and emergency response card integration.

### Success Criteria
- ARBITER can determine at any moment which operatives are in play, on cooldown, and eligible for Apex
- Players understand operative deployment as a resource decision with narrative stakes
- Every faction has asymmetric operative capabilities that reflect faction doctrine
- Apex resolution is unambiguous, significant, and survivable — it changes the game without breaking it

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Operative Card Data Structure
7. Operative Deployment Rules
8. Cooldown & Recovery
9. Tier 1 Operatives — All Factions
10. Tier 2 Operatives — All Factions
11. Tier 3 — Founding Figures
12. Apex Trigger — Rules & Procedure
13. Emergency Response Integration
14. Special Conditions & Gameplay Impacts
15. Examples & Exceptions

---

## 3. Game Purpose

Operatives represent the individuals behind the factions — the people whose judgment, reputation, and capability change what is possible. They sit outside the card hand system. Deploying an operative is a decision with permanence: they remain in play, accumulate consequences, and eventually unlock capabilities that no card can replicate.

The Apex mechanic exists because some operatives reach a threshold of commitment that transforms what a faction can do. Apex resolution may end the session early — meaning that a faction capable of triggering Apex holds not just influence but the power to determine when the vote happens.

---

## 4. Narrative Function

One quarter — one round — is enough time for a person to become significant. The Table is not populated by anonymous representatives. Behind every faction are individuals who have staked their reputations, their resources, and in some cases their safety on what happens in New Meridian.

An operative card is not a game token. It is a person. When they are placed, they are in the field. When they are on cooldown, they are recovering, reassessing, or lying low. When they are activated at Apex, something unprecedented is happening — something New Meridian will not forget.

Each faction's Founding Figure represents the idea made human: the person who most completely embodies what the faction believes and why the stakes are what they are.

---

## 5. Design Principles

1. **Operatives are irreversible commitments.** Once deployed, an operative is in play. Factions cannot voluntarily withdraw them.

2. **Tier reflects investment, not timeline.** A faction may deploy Tier 1 or Tier 2 operatives in any order once prerequisites are met. Tier 3 (Founding Figure) requires specific board conditions — not just time.

3. **Every operative embodies faction doctrine.** Ghost operatives reveal. Network operatives amplify. Syndicate operatives transact. Guild operatives build. Directorate operatives authorize. No operative's ability should be usable by another faction without narrative distortion.

4. **Apex is powerful and visible.** When an Apex trigger is declared, the table knows. The board state shifts. The session may end. This is not a subtle maneuver.

5. **Cooldowns are narrative.** A person under pressure needs time to recover. The cooldown duration reflects how exposed or depleted the operative's use left them.

---

## 6. Operative Card Data Structure

*[TBD — design decision required. Extrapolated structure below; confirm alignment with 04 §6 data structure and 00a governing rules.]*

| Field | Description |
|-------|-------------|
| Operative ID | Unique identifier (format: [Faction Code]-OP-[##]) |
| Operative Name | In-world name of the individual |
| Faction | Faction affiliation |
| Tier | 1, 2, or 3 (Founding Figure) |
| Deploy Cost | Resources required to place operative |
| Deploy Condition | Board state prerequisite (if any) |
| Active Ability | What the operative does when activated |
| Cooldown | Rounds before re-activation |
| Apex Ability | Sealed power (face-down until Apex trigger) |
| Apex Condition | What must be true to declare Apex |
| Apex Cost | Resources / board state required to trigger |
| Portrait | ARBITER-facing input [hidden from players — see Artifact 00a R30a] |
| Narrative Role | One line describing the person |

---

## 7. Operative Deployment Rules

*[TBD — design decisions required. Extrapolated baseline below.]*

- Operatives are deployed during **Phase 2 (Placement)** by paying their Deploy Cost.
- Each faction begins the session with no operatives in play.
- Operatives occupy a dedicated operative zone on the player's faction board.
- An operative in play may be **activated** during **Phase 3 (Dispatch)** by including a designated activation notice in the dispatch case, OR during **Phase 4 (Declaration)** if the operative's ability is a political act.
- Each operative may be activated once per round unless their card states otherwise.
- Tier 3 (Founding Figure) deployment requires: [TBD — board state conditions per faction].

---

## 8. Cooldown & Recovery

After activation, an operative enters **cooldown** for a number of rounds equal to their Cooldown value.

- A marker is placed on the operative card indicating cooldown status.
- At the start of each Upkeep phase, all cooldown markers advance one step.
- An operative at zero cooldown is **available** — they may be activated again.
- A Founding Figure on cooldown **cannot** be used for an Apex trigger.
- *[TBD: does cooldown affect deployment cost for a second deployment? Recommend: no — once deployed, always in play, cooldown only affects activation.]*

---

## 9. Tier 1 Operatives — All Factions

*[TBD — complete design required after Artifact 04 sign-off. Faction doctrine extrapolations below.]*

### Ghost — The Researchers' Collective
Ghost Tier 1 operatives are field analysts: people who observe, document, and extract intelligence in environments where attention is dangerous. Their abilities center on information asymmetry — knowing things others do not.

- **GHO-OP-01:** *[Name TBD]* — Analyst embedded in target district. Active ability: draw one intel token from the district's supply; opponent receives no notification. Cooldown: 1 round.
- **GHO-OP-02:** *[Name TBD]* — Counterintelligence specialist. Active ability: [TBD — counter-surveillance / intel denial].

### Network — The Signal Collective
Network Tier 1 operatives are amplifiers: people who make things visible, frame narratives, and shape the information environment. Their abilities involve exposure, Public Standing shifts, and forcing other factions' choices into the open.

- **NET-OP-01:** *[Name TBD]* — Broadcast coordinator. Active ability: [TBD — Public Standing effect / exposure play].
- **NET-OP-02:** *[Name TBD]* — [TBD].

### Syndicate — The Capital Bloc
Syndicate Tier 1 operatives are deal-makers: people who move resources and create obligations. Their abilities involve resource acquisition, trading terms, and creating dependencies.

- **SYN-OP-01:** *[Name TBD]* — Regional broker. Active ability: [TBD — Capital generation / favorable exchange].
- **SYN-OP-02:** *[Name TBD]* — [TBD].

### Guild — The Builders' Federation
Guild Tier 1 operatives are constructors: people who make things that endure. Their abilities involve structures, Capacity generation, and physical presence in districts.

- **GLD-OP-01:** *[Name TBD]* — Site coordinator. Active ability: [TBD — structure acceleration / Capacity generation].
- **GLD-OP-02:** *[Name TBD]* — [TBD].

### Directorate — The Municipal Authority
Directorate Tier 1 operatives are administrators: people who hold institutional power and know how to use procedural authority as a weapon.

- **DIR-OP-01:** *[Name TBD]* — Regulatory officer. Active ability: [TBD — Mandate generation / action disruption].
- **DIR-OP-02:** *[Name TBD]* — [TBD].

---

## 10. Tier 2 Operatives — All Factions

*[TBD — design required after Tier 1 finalized and 04 complete. Tier 2 operatives have more powerful abilities and longer cooldowns than Tier 1. Deploy conditions likely require established presence in relevant districts.]*

---

## 11. Tier 3 — Founding Figures

Founding Figures are not deployed — they are **revealed**. Each faction has exactly one. They represent the individual who most completely embodies what the faction believes: not an operative executing a task, but an idea walking into the room.

*[TBD — complete design required. One Founding Figure per faction. Notes below.]*

- **Ghost Founding Figure:** *[Name TBD]* — The person who first understood the Chorus was not random noise. Their Apex ability concerns intelligence: revealing something that cannot be un-revealed.
- **Network Founding Figure:** *[Name TBD]* — The voice of New Meridian's information age. Their Apex ability concerns exposure: making something permanently visible.
- **Syndicate Founding Figure:** *[Name TBD]* — The architect of economic interdependence in New Meridian. Their Apex ability concerns leverage: a transaction that reshapes what other factions can do.
- **Guild Founding Figure:** *[Name TBD]* — The builder who made the city what it is. Their Apex ability concerns permanence: something is built that cannot be removed.
- **Directorate Founding Figure:** *[Name TBD]* — The official who knows exactly which authority to invoke and when. Their Apex ability concerns legitimacy: a declaration that changes what is permitted.

---

## 12. Apex Trigger — Rules & Procedure

*[TBD — design requires finalization of Founding Figure abilities. Baseline procedure below.]*

### 12.1 Apex Condition
An Apex trigger may be declared by a faction when ALL of the following are true:
1. Their Founding Figure is in play (deployed, not on cooldown).
2. The Apex Condition stated on their Founding Figure card is met.
3. They have the Apex Cost resources available.

### 12.2 Trigger Declaration
- Apex is declared publicly during **Phase 4 (Declaration)** before other political acts.
- The declaring faction pays the Apex Cost immediately.
- ARBITER acknowledges the declaration and announces to The Table that Apex resolution will occur at end of Phase 6 Resolution.

### 12.3 Emergency Response Window
Following an Apex declaration, all other factions may play their **Emergency Response card** during Phase 5 (Countermeasures). Emergency Response is a one-use card — once played, it is removed from the game. See Artifact 04 for Emergency Response card content.

### 12.4 Apex Resolution
- At end of Phase 6 Resolution, ARBITER resolves the Apex ability.
- ARBITER reveals the Founding Figure's sealed Apex ability panel.
- Effect is applied per the card text.
- **If the Apex condition specified session end:** the session ends after full Debrief. Proceed directly to Artifact 10a — Victory System.
- **If the Apex condition does not specify session end:** play continues. Founding Figure enters maximum cooldown ([TBD] rounds). A second Apex trigger by the same faction is not possible.

### 12.5 ARBITER's Role
ARBITER does not judge whether Apex should happen. ARBITER verifies the condition, acknowledges the trigger, manages the Emergency Response window, and resolves the ability. The Apex trigger is a legal action. What it means for the Chorus Portrait is recorded.

---

## 13. Emergency Response Integration

See Artifact 04 §[TBD] for individual Emergency Response card content.

Emergency Response cards are faction-specific. They are held in reserve from session start and may only be played in response to an Apex declaration. They are not part of the standard card hand and are not subject to hand size limits.

Design intent: Emergency Response cards should not prevent Apex — they should complicate it. The triggering faction must still be able to resolve their Apex ability even if all other factions play Emergency Response.

*[TBD — confirm with Artifact 04 review. Emergency Response design is pending.]*

---

## 14. Special Conditions & Gameplay Impacts

### Operative Elimination
*[TBD — can operatives be removed from play? Recommend: no operative elimination in L1. Cooldown is the only consequence. Escalation to operative elimination is a candidate layer mechanic.]*

### Chorus Node and Operatives
An operative activated in a district adjacent to the Chorus Node is noted by ARBITER. *[TBD — whether this has mechanical consequence or only Portrait input. Recommend: Portrait input only in L1.]*

### Multiple Apex Declarations
If two factions meet their Apex conditions simultaneously: *[TBD — recommend ARBITER determines priority based on initiative order, or players negotiate. This needs a locked decision before sign-off.]*

---

## 15. Examples & Exceptions

*[TBD — populate after operative card designs are finalized.]*

---

*End of Artifact 05 — Operative & Apex System v0.1 Draft Placeholder*  
*Blocked by Artifact 04 completion. All operative card content is placeholder — do not finalize until 04 is signed off.*
