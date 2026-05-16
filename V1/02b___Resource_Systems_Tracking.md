# 02b — Resource Systems: Tracking
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.5 Signed Off  
**Status:** Signed Off — Stable Draft  
**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian; 02a — Resource Systems: Board State  
**Supersedes:** hidden_objectives, popularity_redesign, influence_system (tracking sections)

---

## 1. Overview

### Problem This Document Solves

Not all game state lives on the board surface. Two parallel evaluation systems — the Chorus Portrait and Public Standing — track how each faction is perceived and recorded across the session. A third system, Intel Notes, tracks actionable intelligence factions hold about one another. These systems need precise physical representations, clear state definitions, and rules governing what information is visible to whom — without prescribing how scores change or when bonuses apply, which belong in the artifacts where those events occur.

### Deliverable

The physical representation, scale definitions, visibility rules, and component specifications for three tracking systems: the Chorus Portrait track, the Public Standing track, and Intel Notes.

### Success Criteria

- Any player can read any faction's Public Standing at any time from the board
- ARBITER can read any faction's current Chorus Portrait position from their private track without calculation
- Intel Notes are clearly defined as private physical objects whose contents are known only to the holder and ARBITER — with the holder free to disclose them however and whenever they choose
- A visual designer can produce all three tracking components from this document alone

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Rules & Constraints — Chorus Portrait Track
7. Rules & Constraints — Public Standing Track
8. Rules & Constraints — Intel Notes
9. Component Description
10. Special Conditions & Gameplay Impacts
11. Examples & Exceptions

---

## 3. Game Purpose

These three systems provide the game's two parallel evaluation layers and its intelligence economy.

**The Chorus Portrait track** is ARBITER's private record of what each faction actually is — not what they claim to be. Its marker moves as ARBITER scores behavior throughout the session. Factions cannot read their own Portrait position. They feel it through ARBITER's Debrief observations and the Chronicle at session end.

**The Public Standing track** is New Meridian's public perception of each faction. Fully visible to all players at all times. It modifies how effectively a faction can act — raising or lowering the difficulty threshold of all their 2d10 rolls — and affects their weight in the session's final vote.

**Intel Notes** are small pieces of paper representing actionable intelligence one faction holds about another. They enable targeted actions, power the Denounce political act, and create a secondary economy of information running alongside the resource economy.

---

## 4. Narrative Function

Public Standing and the Chorus Portrait are two completely different kinds of evaluation happening simultaneously — and their independence is the point.

**Public Standing** is what New Meridian thinks. It is the cumulative signal produced by social media, opinion polls, public commentary, art, music, graffiti, and the thousand small ways a city forms its collective impression of the organizations operating within it. It is volatile and reactive. Public memory is short — standing drifts back toward neutral when nothing dramatic is happening. The city watches, forms impressions, and forgets.

**The Chorus Portrait** is what the Chorus observes. It is permanent, cumulative, and indifferent to performance or appearance. The Chorus has been transmitting for thirty-one years. It does not jump to conclusions and it does not forget. One action is enough to begin forming a pattern — the Chorus extrapolates trajectory from minimal data. Humans, it has found, are predictable. The Portrait is not a score. It is a record.

The two systems are symmetrical in physical form — both use an identical track format with a position marker — but asymmetrical in visibility and memory. Public Standing is displayed openly on the board. The Chorus Portrait is hidden in ARBITER's tableau. Same ruler. Different observer. One forgets. The other does not.

**Intel Notes** represent what factions know about each other. Knowledge is power — but it expires, can be traded, can be bluffed about, can be disclosed strategically, and can be turned against the faction it describes. An intel note is a piece of paper: specific, time-stamped, and targeted.

---

## 5. Design Principles

1. **Two tracks, two observers, one format.** The Chorus Portrait and Public Standing use the same physical track format. One is public; one is private. The symmetry reflects that both systems are evaluating the same factions — just with different information, different time horizons, and different purposes.

2. **Portrait is a permanent record.** Portrait scores accumulate without drift or decay. There is no forgetting and no passive recovery. The Chorus does not revise its observations. A faction can only move forward — new behavior added on top of what is already recorded.

3. **Public Standing drifts toward neutral.** Public memory fades. A faction that stops generating attention gradually returns to Neutral. Maintaining elevated or depressed standing requires sustained activity.

4. **The standing modifier affects action difficulty, not income.** Public Standing modifies how effectively a faction can act — shifting the difficulty target threshold of all their 2d10 rolls up or down. It does not modify resource income. Income is determined by actual presence chips and influence levels on the board.

5. **A player controls disclosure of their own private information.** Any private information a player holds — intel notes, hand cards, classified directives, or any other private component — is disclosed only at the holder's discretion. The holder may share it publicly, privately, partially, or not at all. This principle applies to all private information in the game. Verbal claims about undisclosed private information cannot be verified with ARBITER without a specific game action.

6. **Holding guidelines are not enforcement.** Guidelines for intel note holdings represent doctrinal expectations, not mechanical limits. Players may hold more than suggested. ARBITER knows. The Portrait reflects what a faction does with information it was not supposed to hold.

---

## 6. Rules & Constraints — Chorus Portrait Track

### What the Track Shows

The Chorus Portrait track shows ARBITER's current cumulative assessment of each faction's behavior as a coherent answer to the Chorus. The marker's position represents the total of all Portrait scoring to date in the session.

The track is private — kept in ARBITER's tableau, facing away from players. Factions cannot see their own Portrait position. ARBITER communicates Portrait state through Debrief observations, never through direct disclosure.

ARBITER may adjust a faction's Portrait marker in response to any action taken or observed — including formal game actions, Debrief negotiations, trades, and table behavior beyond the structured phases of play. The Chorus observes everything that happens at The Table.

How scores are assigned and when bonuses apply is specified in Artifact 07 — ARBITER Toolkit and Artifact 10a — Victory System respectively.

### The Portrait Scale

Portrait runs from −20 to +20. All factions start at 0. Eleven named states in a bell-curve distribution, with Ambiguous at center:

| State | Range | Width | Chorus Stance |
|-------|-------|-------|---------------|
| Resonant | +18 to +20 | 3 | This faction has become something the Chorus recognizes |
| Aligned | +13 to +17 | 5 | Behavior and doctrine have converged |
| Coherent | +8 to +12 | 5 | A consistent pattern is emerging |
| Legible | +4 to +7 | 4 | The Chorus can begin to read this faction |
| Observed | +2 to +3 | 2 | Initial signals noted. Trajectory forming |
| Ambiguous | −1 to 0 | 2 | No determination. Observation continues |
| Uncertain | −2 to −3 | 2 | Early contradictions detected |
| Dissonant | −4 to −7 | 4 | Stated doctrine and observed behavior diverge |
| Fractured | −8 to −12 | 5 | The pattern of contradiction is consistent |
| Collapsed | −13 to −17 | 5 | This faction no longer produces readable signal |
| Void | −18 to −20 | 3 | Silence. The Chorus has nothing to interpret here |

Starting position: 0, upper boundary of Ambiguous. Any scored action immediately moves a faction out of Ambiguous — positive actions into Observed (+2), negative actions into Uncertain (−2). The Ambiguous band is narrow by design — the Chorus forms a trajectory quickly.

### Physical Format

One hidden track strip per faction. Identical in format to the Public Standing track — same scale markings, same band label style — but kept private in ARBITER's tableau. A clip or bead marker in faction color shows current position. ARBITER moves the marker after each round's Resolution.

The physical solution for keeping the Portrait track private is specified in Artifact 07 — ARBITER Toolkit.

ARBITER may keep optional session notes alongside the track to support Chronicle construction at session end. These notes are not required. The track shows the endpoint; the notes explain how the faction arrived there.

### What Portrait State Produces

Portrait state at session end determines the tone of each faction's Chronicle entry and contributes to final scoring, specified in Artifact 07 — ARBITER Toolkit and Artifact 10a — Victory System respectively.

---

## 7. Rules & Constraints — Public Standing Track

### What the Track Shows

The Public Standing track shows New Meridian's collective perception of each faction. It is public information, visible to all players at all times on the board.

### The Public Standing Scale

Public Standing runs from 0 to 20. All factions start at 10 (Neutral). Five named states with flat modifiers applied to the difficulty target threshold on all 2d10 rolls:

| State | Range | Target Modifier | Effect |
|-------|-------|----------------|--------|
| Celebrated | 18–20 | +20 to target | Difficulty thresholds increase by 20 — easier to succeed |
| Respected | 14–17 | +10 to target | Difficulty thresholds increase by 10 |
| Neutral | 7–13 | 0 | No change |
| Suspect | 3–6 | −10 to target | Difficulty thresholds decrease by 10 — harder to succeed |
| Discredited | 0–2 | −20 to target | Difficulty thresholds decrease by 20 |

The modifier shifts the difficulty target before the roll is made. The die result is compared against the modified target. No adjustment to the rolled number is required.

| Difficulty | Base Target | Celebrated (+20) | Respected (+10) | Neutral | Suspect (−10) | Discredited (−20) |
|-----------|------------|-----------------|----------------|---------|--------------|------------------|
| Automatic | No roll | No roll | No roll | No roll | No roll | No roll |
| Easy | 01–75 | 01–95 | 01–85 | 01–75 | 01–65 | 01–55 |
| Average | 01–50 | 01–70 | 01–60 | 01–50 | 01–40 | 01–30 |
| Challenging | 01–25 | 01–45 | 01–35 | 01–25 | 01–15 | 01–05 |
| Impossible | No roll (fails) | No roll | No roll | No roll | No roll | No roll |

Modifiers cannot change Automatic into a required roll or Impossible into a possible success. Difficulty definitions are specified in Artifact 03 — Round Structure.

### Natural Drift

| Position | Drift per round |
|----------|----------------|
| Above 13 | −1 |
| 7 to 13 | No drift |
| Below 7 | +1 |

Applied at round end after all other standing changes. Timing specified in Artifact 03 — Round Structure.

### Physical Format

One laminated strip per faction displayed on the board or player tableau. Each strip shows:

- The 0–20 numbered scale
- Five named band labels: Discredited / Suspect / Neutral / Respected / Celebrated
- Target modifier labels beneath each band: −20 to target / −10 to target / — / +10 to target / +20 to target
- Starting position indicated at 10

A clip or bead in faction color marks current position. Players move their own Public Standing marker when their action causes a change. When a discovery or failure triggers a standing loss, ARBITER announces the change and the affected player moves their own marker.

---

## 8. Rules & Constraints — Intel Notes

### What Intel Notes Are

An intel note is a small piece of paper created by ARBITER when a faction successfully gathers intelligence. ARBITER writes two things on each note at creation:

- **Faction:** which faction the intelligence concerns
- **Round:** the round in which it was gathered

Players calculate age: current round minus round acquired.

| Age | Status |
|-----|--------|
| 0–1 rounds | Fresh |
| 2–3 rounds | Stale |
| 4+ rounds | Expired — no mechanical use |

Intel notes are delivered privately through the messaging system (Artifact 06) and held in the player's tableau.

### Privacy and Disclosure

Intel notes are private by default. The holder and ARBITER know the contents. The holder may disclose at any time in any of the following ways:

- Show it publicly to the entire table
- Show it privately to one specific player
- Read its contents aloud
- Pass it to another player as part of a trade

There is no rule restricting when or to whom disclosure occurs. Sharing secrets is a strategic decision — ARBITER observes what is shared, with whom, and when.

Verbal claims about unshown contents cannot be verified with ARBITER without a specific game action defined in Artifact 04 — Action Card System.

### Holding Guideline

- Standard factions: hold no more than 2 intel notes
- Ghost: hold no more than 4 intel notes
- Exception: intel notes naming your own faction do not count toward the guideline

This is a guideline, not an enforced limit. ARBITER knows the true state of every player's holdings. A faction's relationship with information it was not supposed to hold is observed and may be reflected in the Portrait.

### Discarding Intel Notes

Any intel note may be discarded by its holder at any time for any reason. Discarding is immediate and requires no action. A discarded note is permanently removed from play — it cannot be retrieved, examined after the fact, or referenced by any player or ARBITER.

### Uses

Defined in Artifact 04 — Action Card System. Governing principle: an intel note can only be applied to actions involving the specific faction named on it. Effectiveness varies by age.

### Generation

Defined in Artifact 04 — Action Card System.

### Trading

Occurs primarily during Debrief. Rules defined in Artifact 03 — Round Structure (Debrief phase).

---

## 9. Component Description

| Component | Quantity | Physical Format |
|-----------|----------|-----------------|
| Chorus Portrait track | 1 per faction (5 total) | Laminated strip. Identical format to Public Standing track. Scale −20 to +20, eleven named bands. Kept private in ARBITER's tableau. |
| Portrait position marker | 1 per faction (5 total) | Clip or bead in faction color |
| Public Standing track | 1 per faction (5 total) | Laminated strip. Scale 0–20, five named bands with target modifier labels. Displayed on board or player tableau. |
| Public Standing marker | 1 per faction (5 total) | Clip or bead in faction color |
| Intel notes | Variable — created during play | Small pieces of paper. Written by ARBITER at creation. Contains faction name and round acquired only. Blank paper cut to consistent size is sufficient. |

---

## 10. Special Conditions & Gameplay Impacts

### Portrait and Public Standing — Independent Systems

The two tracks evaluate the same faction using different criteria and different memories. They will frequently diverge. A faction can gain Public Standing through a popular visible action while simultaneously losing Portrait through the doctrinal contradiction it represents. A faction can hold Neutral Public Standing throughout the session while building a strongly positive Portrait through consistent private behavior.

Optimizing one system at the expense of the other is a legitimate strategic choice:

- **The "Popular" strategy** — maximizing Public Standing — is visible to opponents, improves roll effectiveness across the board, and potentially hollow in the Chronicle
- **The "Genuine" strategy** — maximizing Portrait — is invisible to opponents and permanently recorded by the Chorus

### Public Standing Modifier — All Rolls

The target modifier from Public Standing applies to all 2d10 rolls the faction makes across all contexts — covert operations, political acts, Incursion, and any other action requiring a roll. It is not location-specific. A Discredited faction faces reduced target thresholds everywhere they operate. A Celebrated faction benefits from increased thresholds everywhere.

*Example: The Directorate is at Suspect (−10 to target). They attempt a Gather at University Perimeter with no presence there — base difficulty Challenging, target 01–25. The Suspect modifier reduces the target to 01–15. The Directorate rolls 18. At Neutral (target 01–25) this succeeds. At Suspect (target 01–15) it fails. Same die result. Different threshold. Only the target changed.*

### Intel Notes — Self-Directed Holdings

Intel notes naming your own faction do not count toward the holding guideline and have no offensive use for standard factions. Their value is defensive — holding them prevents others from using them. They can be discarded immediately on receipt, held until expiry, or traded. Ghost may use self-directed notes for specific covert operations defined in Artifact 04.

---

## 11. Examples & Exceptions

### Reading Both Tracks — The Divergence

*End of Round 5. The Guild's Public Standing marker sits at 15 (Respected — +10 to all roll targets). ARBITER's hidden Portrait marker for The Guild sits at −5 (Dissonant).*

New Meridian respects The Guild. When The Guild rolls 2d10, the difficulty target increases by 10 — Challenging (base 01–25) becomes 01–35. The city is cooperating.

The Chorus sees something different. The Guild's stated doctrine has been contradicted by how they have actually been building. The Portrait marker moves without the city knowing it moved.

Two evaluations. Same faction. Different observers. Both true.

---

### Intel Note — Disclosure Choice

*Round 4 Debrief. The Network holds an intel note naming The Syndicate (Round 2 — stale). The Directorate asks directly whether The Network has anything on The Syndicate.*

The Network has three options:
- Show the note to The Directorate privately — they see faction and round
- Show the note to the whole table — everyone sees it
- Deny holding anything relevant — a verbal bluff ARBITER observes

The Network shows it privately. The Directorate confirms it is stale and negotiates. They offer 2 Mandate. The Network accepts. The note transfers. ARBITER watches.

---

### Intel Note — Acquired Through Trade

*Round 4 Debrief. The Guild offers The Directorate two intel notes for 3 Mandate. The Directorate examines them first.*

One names The Syndicate (Round 2 — stale). One names The Directorate itself (Round 3 — fresh). The Directorate accepts the trade. They immediately discard the self-directed note — permanently gone. They keep the Syndicate note for a future Denounce.

ARBITER observes the immediate discard. It says something about how The Directorate handles information about themselves.
