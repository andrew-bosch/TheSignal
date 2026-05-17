# 08 — Player Toolkit
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 Draft — Placeholder  
**Status:** 🔄 Draft — Partially defined, pending Artifact 04 and 05 completion  
**Last Updated:** 2026-05-15  
**Depends on:** 00 — Factions & World; 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking; 04 — Action Card System; 05 — Operative & Apex System  
**Supersedes:** player_guide (retired artifact), hidden_objectives (classified directive sections, retired)

---

## 1. Overview

### Problem This Document Solves
Each player arrives at the table representing one of five factions with asymmetric starting conditions, asymmetric resources, and asymmetric access to certain card types. Without a player-facing document that defines what each faction starts with, how their private components are organized, and what their classified directive means, onboarding produces confusion before the game begins.

This artifact defines everything a faction player needs to begin and sustain a session: their starting assets, faction board layout, hand management rules, classified directive handling, and reference materials for rapid card and rule lookup.

### Deliverable
- Faction board specification (one per faction — layout, zones, reference information)
- Starting asset distribution (by faction)
- Hand management rules (card deck selection, hand size, draw)
- Classified directive handling
- Faction reference card — condensed play reference
- Setup procedure (player-facing)

### Success Criteria
- A player unfamiliar with the game can set up their faction correctly from this document
- A player running their faction mid-session can locate any rule reference they need on their faction board or faction reference card
- Starting asset asymmetry is correct and intentional — each faction begins where their doctrine places them

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Faction Board — Layout & Zones
7. Starting Assets — All Factions
8. Card Hand — Deck Selection & Management
9. Classified Directives
10. Faction Reference Card
11. Player Setup Procedure
12. Special Conditions & Gameplay Impacts
13. Examples & Exceptions

---

## 3. Game Purpose

The player toolkit is the physical and procedural home for everything a faction player owns and manages during a session. It is a reference tool, an organizational system, and a starting state definition.

Unlike ARBITER, faction players do not have access to full information about the board state at setup. Their starting assets, their deck selection, and their classified directive define the space within which they make decisions. This artifact defines that space precisely.

---

## 4. Narrative Function

Each faction came to The Table from somewhere. The Directorate arrived with institutional authority and the full weight of New Meridian's civic infrastructure behind them. The Researchers' Collective arrived with files — with knowledge that no other faction has been willing to pursue. The Capital Bloc arrived with leverage built over decades.

Starting assets are not arbitrary. They reflect what each faction is. A faction that begins with more resources has traded something else for them — influence they haven't yet established, or operational flexibility they'll have to build later. The game's starting conditions are not balanced in the sense of equal — they are balanced in the sense of fair. Every faction has a path.

---

## 5. Design Principles

1. **Starting conditions reflect doctrine.** A faction's starting resources, presence, and structure placements are derived from who they are, not from a balancing spreadsheet. Balance emerges from playtest, not from equalizing starting numbers.

2. **The faction board is a reference, not a scoreboard.** Players track their own resources and operatives. The faction board's primary function is organization and rule reference — not record-keeping that ARBITER maintains separately.

3. **Classified directives are private and permanent.** A faction may not trade, transfer, or replace their classified directive. They may reveal it voluntarily. They may not claim to have a different one.

4. **Deck selection is a pre-session commitment.** A faction's card deck is selected before the session begins and does not change during play. This selection is the first asymmetric decision a player makes.

---

## 6. Faction Board — Layout & Zones

*[TBD — visual design in Artifact 11. Functional zones defined here.]*

Each faction has one faction board. The faction board has the following zones:

| Zone | Contents | Notes |
|------|----------|-------|
| Resource track | Current asset token count by type | Player-maintained |
| Operative zone | Deployed operative cards | Organized by tier |
| Cooldown zone | Operatives on cooldown, with markers | |
| Hand zone | Current card hand | Face-down |
| Classified directive slot | Sealed directive card | Face-down until revealed |
| Emergency Response slot | Emergency Response card | Face-down until declared |
| Public Standing track position | Faction marker on shared track | Tracked on shared board |
| Accord holding zone | Copies of active Accords | Player's copies; ARBITER holds originals |
| Faction reference panel | Condensed rules, costs, and faction ability | Printed on board |

*[TBD — faction boards may be two-sided (setup side / play side) or single-sided with fold-out reference panel. Confirm with Artifact 11 visual design.]*

---

## 7. Starting Assets — All Factions

*[TBD — starting asset values require playtest validation. Extrapolated baseline below based on faction doctrine. All values are provisional.]*

Starting assets are distributed by ARBITER at setup from the Reservoir.

| Faction | Starting Resource | Amount | Starting Presence | Starting Structures |
|---------|-----------------|--------|-------------------|---------------------|
| Ghost (Researchers' Collective) | Findings | [TBD] | [TBD] tokens in [TBD districts] | None |
| Network (Signal Collective) | Exposure | [TBD] | [TBD] tokens in [TBD districts] | None |
| Syndicate (Capital Bloc) | Capital | [TBD] | [TBD] tokens in [TBD districts] | 1 structure in [TBD] |
| Guild (Builders' Federation) | Capacity | [TBD] | [TBD] tokens in [TBD districts] | 1 structure in [TBD] |
| Directorate (Municipal Authority) | Mandate | [TBD] | [TBD] tokens in [TBD districts] | 1 structure in [TBD] |

*Design rationale (extrapolated):*
- **Ghost** begins with informational advantage — more Findings, fewer presence tokens. Ghost is a back-channel faction that gathers before it moves.
- **Network** begins with spread presence — Exposure is generated by visibility, so Network needs to be seen in multiple districts from the start.
- **Syndicate** begins with Capital advantage and a structure — economic infrastructure already in place.
- **Guild** begins with Capacity and a structure — the builders arrived with something already built.
- **Directorate** begins with Mandate and institutional placements in civic districts (Ring [TBD] priority).

*[TBD — also define: starting card hand size (likely zero — hands are built from deck selection during setup); starting intel token count (likely faction-specific).]*

---

## 8. Card Hand — Deck Selection & Management

### 8.1 Pre-Session Deck Selection
Before the session begins, each faction assembles their card decks:

**Covert Operations Deck:**
- All 10 Standard Covert Operations are available to every faction.
- Each faction selects from their faction-specific Covert Operations (5 available, select [TBD]).
- Combined deck size: [TBD] cards. Draw: [TBD] per quarter. *[Per Artifact 04 §[TBD].]*

**Political Acts Deck:**
- All 8 Standard Political Acts are available to every faction.
- Each faction includes both of their faction-specific Political Acts.
- Combined deck size: [TBD] cards. *[TBD — political acts may be available-always rather than drawn.]*

### 8.2 Modifier Cards
Modifier cards are not part of either deck. They are drawn during play per rules defined in Artifact 04 §11.

### 8.3 Hand Size
*[TBD — confirm with Artifact 04. Extrapolated: each faction draws [TBD] covert operation cards at the start of each quarter (Upkeep phase). Maximum hand size [TBD]. Excess cards are discarded or held per Artifact 04 rules.]*

### 8.4 Pass Cards
Each faction has 4 Pass cards. They are held outside the deck and may be submitted at any time in place of an operation or political act. See Artifact 04 §12.

### 8.5 Emergency Response Card
Each faction has 1 Emergency Response card. It is held outside the deck and sealed until an Apex trigger is declared. See Artifact 05 §13.

---

## 9. Classified Directives

### 9.1 At Setup
ARBITER delivers one sealed classified directive to each faction (see Artifact 06 §10). Factions may open and read their directive in private and may not share it with other players except by voluntary choice.

### 9.2 Directive Design
*[TBD — full directive content design is a separate design pass. Extrapolated parameters:]*

Each classified directive contains:
- A secret objective (board state condition to achieve by session end)
- VP reward for success
- Faction alignment (each directive reflects its faction's doctrine)
- *[TBD — are directives faction-locked or randomly distributed? Recommend: faction-locked in L1. Random distribution is a layer expansion candidate.]*

Sample directive categories (by faction, extrapolated):
- **Ghost:** intelligence-based objectives (hold X intel tokens at session end; be the first to target [specific faction] with a Surveillance operation)
- **Network:** exposure-based objectives (have presence in X districts at session end; maintain Public Standing above [threshold] for X consecutive rounds)
- **Syndicate:** economic objectives (hold X Capital at session end; complete X Translations via ARBITER)
- **Guild:** construction objectives (place X structures by quarter [Y]; hold Established status in [ring] at session end)
- **Directorate:** institutional objectives (hold the most presence in [civic districts] at session end; have X Accords on record honored)

### 9.3 At Session End
All factions reveal their classified directive simultaneously after final board state is locked. ARBITER verifies conditions. VP awarded per Artifact 10a.

---

## 10. Faction Reference Card

*[TBD — content design after 04 and 05 complete. Structure below.]*

Each faction has a faction reference card — a double-sided condensed reference for the faction player. It is separate from the faction board and may be held in hand or placed for reference.

**Side A — Round Structure**
- Six-phase summary with player actions per phase
- Timing constraints (when can I do X?)
- Resource collection reminder

**Side B — Faction Summary**
- Faction name and narrative identity (one sentence)
- Native resource type and its narrative meaning
- Faction ability (if any — *[TBD: do factions have a passive ability? Recommend: yes, one per faction, defined here]*)
- Starting asset summary
- Classified directive reminder (blank — player writes their directive objective on this line)

*[TBD — whether faction reference cards are printed per faction (five unique cards) or use a template with a faction-specific insert.]*

---

## 11. Player Setup Procedure

*[TBD — full setup in Artifact 10. Player-specific tasks listed here.]*

### 11.1 Player Setup Tasks (in order)
1. Receive faction board and place in front of you.
2. Receive starting assets from ARBITER (per §7 above).
3. Receive classified directive from ARBITER — sealed. Read privately.
4. Receive Emergency Response card — sealed. Do not open until Apex trigger.
5. Select covert operations deck (see §8.1).
6. Confirm political acts deck (see §8.1).
7. Confirm Pass cards (4) are with your hand.
8. Place faction markers on Public Standing track at starting position ([TBD — confirm starting position with Artifact 02b]).
9. Place starting presence tokens in starting districts per §7.
10. Place starting structures in starting districts per §7.
11. Confirm Chorus Node has ARBITER Dominance Marker in place (ARBITER confirms).

---

## 12. Special Conditions & Gameplay Impacts

### Faction Absence
*[TBD — what happens if a faction player cannot complete a quarter (emergency, etc.)? Recommend: ARBITER controls the absent faction for the quarter, submitting Pass cards. Faction player resumes control next quarter.]*

### Two-Player Variant
*[TBD — two-player rules, if any, belong in Artifact 10. Reference here if player toolkit components differ for two-player.]*

---

## 13. Examples & Exceptions

*[TBD — populate after 04 and 05 complete. Key scenarios: deck selection edge cases, directive dispute, emergency response card mistimed play.]*

---

*End of Artifact 08 — Player Toolkit v0.1 Draft Placeholder*  
*Starting asset values, deck selection sizes, and classified directive content require playtest validation and Artifact 04/05 sign-off. Faction reference card design requires Artifact 11 visual design pass.*
