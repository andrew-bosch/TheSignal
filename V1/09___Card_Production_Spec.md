# 09 — Card Production Spec
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 Draft — Placeholder  
**Status:** ⬜ Not Started — Blocked by Artifact 04 completion  
**Last Updated:** 2026-05-15  
**Depends on:** 04 — Card System; 04b — Action Taxonomy & Design Analysis; 05 — Operative & Apex System  
**Supersedes:** card_designs (retired artifact)

---

## 1. Overview

### Problem This Document Solves
Artifact 04 defines card rules and design constraints. Artifact 05 defines operative systems. This artifact is the production table: every card in the game, in one place, in the format required to hand it to a printer, a laser cutter, or a physical card assembly process.

Artifact 09 does not define rules. It does not argue for design decisions. It contains card data.

### Deliverable
Complete production-ready card specifications for:
- All covert operations (standard C01–C10 and faction-specific C11–C35)
- All political acts (standard P01–P08 and faction-specific P09–P18)
- Modifier cards (player tableau and ring-specific decks)
- Pass cards
- Emergency Response cards (one per faction)
- Operative cards (Tier 1, Tier 2, Founding Figures)
- Classified directives (one per faction)
- Situation Reports (world event cards)

### Success Criteria
- A complete physical card set can be assembled from this document without reference to any other artifact
- Every card field is populated — no TBDs in the production version
- All card content uses in-world language per PM03 §1 and 00a §10

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Card Format Reference
7. Covert Operations — Standard (C01–C10)
8. Covert Operations — Faction-Specific (C11–C35)
9. Political Acts — Standard (P01–P08)
10. Political Acts — Faction-Specific (P09–P18)
11. Modifier Cards
12. Pass Cards
13. Emergency Response Cards
14. Operative Cards
15. Classified Directives
16. Situation Reports (World Event Cards)
17. Examples & Exceptions

---

## 3. Game Purpose

This artifact is a production document, not a design document. Its purpose is precision: exact card text, exact costs, exact field values, in a format that supports physical production without interpretation.

All design decisions that affect card content must be locked in Artifacts 04, 05, or their respective decision log entries (PM02) before this document can be finalized. Artifact 09 is downstream of every card design decision.

---

## 4. Narrative Function

Every word on every card is in the language of New Meridian and the factions that operate within it. A player should never read a card effect and be reminded they are playing a game. The card should feel like a decision their faction has made — not a mechanical instruction.

The discipline of in-world language is hardest under card space constraints. A card with thirty words must still sound like New Meridian. This artifact enforces that standard.

---

## 5. Design Principles

1. **Complete field population.** No production card has an empty or TBD field.
2. **No hardcoded variable values.** If a value is referenced on a card and subject to change, the card references the source (e.g., "per the current conversion rate" rather than "4:1") — see 00a Governing Principle 2 (Copy Design).
3. **In-world language throughout.** Mechanical terms appear only where necessary for clarity; narrative terms are used when available.
4. **Self-contained resolution.** A card, when read, provides everything ARBITER or the acting player needs to resolve it.

---

## 6. Card Format Reference

The 20-field card data structure is defined in Artifact 04 §6. This document uses that structure for all card entries.

| Field | Description |
|-------|-------------|
| Card ID | Unique identifier |
| Card Name | In-world name |
| Card Type | Covert Operation / Political Act / Modifier / Pass / Emergency Response |
| Card Subtype | Standard / Faction-Specific; if Faction-Specific: faction name |
| Card Faction | Faction or Universal |
| Beat | Phase when played |
| Primary Cost | Resource cost (type and amount) |
| Secondary Cost | Additional requirement if any |
| Difficulty | Modifier applied to resolution |
| Target | Valid targets for this card |
| Effect — Success | What happens when the operation succeeds |
| Effect — Failure | What happens when the operation fails |
| Modifier Cap | Maximum modifier cards allowed |
| Counter Eligible | Whether Countermeasure cards can be played against this |
| Countermeasure Response | Effect if successfully countered |
| Taxonomy | Category — Function — Target (per 04b) |
| Portrait | ARBITER-facing input [hidden from players — see 00a R30a] |
| Flavor Text | In-world narrative line, printed at bottom of card |
| Production Notes | Physical assembly notes (card dimensions, color, faction keying) |
| Version | Card version number |

---

## 7. Covert Operations — Standard (C01–C10)

*[BLOCKED — Artifact 04 §7 must be signed off before card specifications can be finalized. See PM02 for open decisions affecting C01–C10.]*

Card entries will be populated here in full 20-field format after Artifact 04 sign-off.

---

## 8. Covert Operations — Faction-Specific (C11–C35)

*[BLOCKED — Artifact 04 §8 must be completed and signed off. Ghost C16–C20 redesign (PM02 D04-02) is open.]*

Card entries will be populated here in full 20-field format after Artifact 04 sign-off.

| Faction | Card IDs | Status |
|---------|----------|--------|
| Ghost (Researchers' Collective) | C11–C15 (✅ signed off), C16–C20 (🔄 redesign pending) | Partial |
| Network (Signal Collective) | C21–C25 | ⬜ Pending |
| Syndicate (Capital Bloc) | C26–C30 | ⬜ Pending |
| Guild (Builders' Federation) | C31–C35 (may shift — confirm ID range) | ⬜ Pending |
| Directorate (Municipal Authority) | *[TBD — ID range]* | ⬜ Pending |

---

## 9. Political Acts — Standard (P01–P08)

*[BLOCKED — Artifact 04 §9 must be signed off.]*

---

## 10. Political Acts — Faction-Specific (P09–P18)

*[BLOCKED — Artifact 04 §10 must be signed off.]*

| Faction | Card IDs | Status |
|---------|----------|--------|
| Ghost (Researchers' Collective) | P09–P10 | ⬜ Pending |
| Network (Signal Collective) | P11–P12 | ⬜ Pending |
| Syndicate (Capital Bloc) | P13–P14 | ⬜ Pending |
| Guild (Builders' Federation) | P15–P16 | ⬜ Pending |
| Directorate (Municipal Authority) | P17–P18 | ⬜ Pending |

*Note: P17 Publish Analysis redesign is open (PM02 00a-A02 / 04-11).*

---

## 11. Modifier Cards

*[BLOCKED — Artifact 04 §11 must be signed off.]*

Modifier cards have two populations:
- **Player tableau modifiers:** faction-specific, drawn from each faction's modifier deck
- **Ring-specific modifiers:** board-location modifiers drawn from the relevant ring's deck

Full card entries in 20-field format after Artifact 04 §11 sign-off.

---

## 12. Pass Cards

*[Per Artifact 04 §12. One design, four copies per faction. Universal.]*

| Field | Value |
|-------|-------|
| Card ID | PASS |
| Card Name | *[TBD — in-world name for declining to act. Candidate: "Standing Down" / "No Declaration"]*  |
| Card Type | Pass |
| Card Subtype | Universal |
| Card Faction | Universal |
| Beat | Phase 3 (Dispatch) or Phase 4 (Declaration) |
| Primary Cost | None |
| Effect | No operation submitted / no political act declared this quarter |
| Portrait | None |
| Flavor Text | *[TBD]* |

---

## 13. Emergency Response Cards

*[BLOCKED — design pending. One card per faction, faction-specific. Used only during Apex trigger window. See Artifact 05 §13.]*

| Faction | Card ID | Status |
|---------|---------|--------|
| Ghost (Researchers' Collective) | ER-GHO | ⬜ Pending |
| Network (Signal Collective) | ER-NET | ⬜ Pending |
| Syndicate (Capital Bloc) | ER-SYN | ⬜ Pending |
| Guild (Builders' Federation) | ER-GLD | ⬜ Pending |
| Directorate (Municipal Authority) | ER-DIR | ⬜ Pending |

---

## 14. Operative Cards

*[BLOCKED — Artifact 05 must be signed off. Full card entries for all Tier 1, Tier 2, and Tier 3 (Founding Figure) operatives.]*

Format: 13-field operative data structure per Artifact 05 §6.

---

## 15. Classified Directives

*[BLOCKED — directive content design pending. One directive per faction. See Artifact 08 §9.]*

| Faction | Directive ID | Status |
|---------|-------------|--------|
| Ghost (Researchers' Collective) | CD-GHO | ⬜ Pending |
| Network (Signal Collective) | CD-NET | ⬜ Pending |
| Syndicate (Capital Bloc) | CD-SYN | ⬜ Pending |
| Guild (Builders' Federation) | CD-GLD | ⬜ Pending |
| Directorate (Municipal Authority) | CD-DIR | ⬜ Pending |

---

## 16. Situation Reports (World Event Cards)

*[TBD — Situation Report design is partially defined in Artifact 01 §[TBD]. Full card content for the world event deck belongs here.]*

Situation Reports represent significant events at the city or global scale. One is revealed at each Debrief, applying a board state modifier for the following quarter.

Design considerations:
- Reports should be written as in-world news or intelligence summaries — the language of someone who does not know the factions are operating behind the scenes
- The event effect should be mechanical (modifies resource generation, movement, costs, or VP) and should not require ARBITER to adjudicate intent
- Reports should be re-shuffled once depleted — the world continues to generate events for as long as the session runs

*[TBD — number of unique Situation Reports in L1 deck. Recommend: at minimum 16 (two per quarter) so the deck never runs dry in an 8-quarter session with no shuffled repeats.]*

---

## 17. Examples & Exceptions

*[TBD — card interaction examples, edge case text disambiguation.]*

---

*End of Artifact 09 — Card Production Spec v0.1 Draft Placeholder*  
*This document is fully blocked pending Artifact 04 and 05 completion. Structure and field definitions are confirmed. Card content will be populated after upstream sign-offs.*
