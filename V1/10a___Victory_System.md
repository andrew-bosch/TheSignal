# 10a — Victory System
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 Draft — Placeholder  
**Status:** ⬜ Not Started — Requires upstream decisions before design can begin  
**Last Updated:** 2026-05-15  
**Depends on:** 00 — Factions & World; 02 — Components; 03 — Round Structure; 05 — Operative & Apex System  
**Integrated into:** 10 — Game Manuals (summary); defined authoritatively here  
**Supersedes:** (no retired predecessor — victory system defined for first time in V1 artifact set)

---

## 1. Overview

### Problem This Document Solves
The game ends in one of two ways: at the completion of Round 8, or when an Apex ability resolves and triggers session end. In either case, someone wins. This document defines what winning means, how it is measured, and in what order the scoring sequence is resolved.

Victory in THE SIGNAL is not purely additive. The board state, the Chorus Portrait, classified directives, and a final vote all feed into the result. The complexity is intentional: a faction that dominated the board may lose to a faction that played a quieter game with greater narrative alignment.

### Deliverable
- Definition of all victory point sources
- Chorus Portrait conversion procedure
- Scoring sequence (order of operations)
- Tiebreaker rules
- The vote mechanic — how the vote on humanity's response to the Chorus is conducted and what it means

### Success Criteria
- A complete session can be scored in [TBD] minutes following this document
- No scoring scenario is unresolvable or ambiguous
- The vote result is meaningful independent of the VP total — a faction can lose points and still win the vote

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Session End Conditions
7. Victory Point Sources
8. Chorus Portrait Conversion
9. Scoring Sequence
10. The Vote
11. Tiebreakers
12. Winning — What It Means
13. Special Conditions & Gameplay Impacts
14. Examples & Exceptions

---

## 3. Game Purpose

The victory system is the game's answer to the question every faction has been asking for eight rounds: *Was what we did enough?*

It is not a simple measure. A faction that spent the session accumulating resources and dominating districts may find that the Chorus saw something in their methods that a purely mechanical count does not capture. A faction that played carefully, honored their Accords, and positioned for the vote may find that the session's quiet game was exactly what the scoring system rewards.

The vote at the end of the session is not a formality. It is the moment when factions commit publicly to what they believe should happen — and those commitments interact with everything they did to get there.

---

## 4. Narrative Function

Eight rounds. Approximately two years of operations. The Table's deliberation ends with a vote on humanity's official response to the Chorus.

The vote is not advisory. Whatever the vote produces, that is humanity's position. The factions have spent two years maneuvering to ensure that the response aligns with their doctrine. The vote is the last move in a very long game.

What ARBITER does with the vote result — what the Chorus makes of it — is beyond the scope of the paper prototype. The game ends with a result. What comes after is the question that future layers of the game will ask.

### The Governing Design Principle — Internal

The two victory paths are the two sides of a question the game lets players explore but does not answer for them. This principle is not stated to players. It governs how the victory system is designed.

**VP path** = human-agency theory. The factions are authors. The Chorus is the occasion. What the factions achieved — board control, resources, classified directives, vote outcome — is the measure of the session. Winning by VP is a claim: *we determined what happened*.

**Portrait path** = Chorus-agency theory. The factions were being evaluated throughout. What the Chorus recorded — their Portrait — is not what they controlled; it is what they revealed. Winning by Portrait is not achievement. It is recognition by something that was already watching.

A player optimizing for VP is implicitly betting that human agency is the operative frame. A player playing toward Portrait is accepting that something else has been keeping score. Most players do both — which is the honest position of anyone who hasn't resolved the question.

**The victory system should not make this explicit.** Players discover it through play. The Chronicle reading and the vote — not the point totals — are the game's actual conclusion. After a session, a player should have arrived somewhere they can sit with: a stance on the question, earned through eight rounds, that they could not have stated before they sat down.

The game's objective statement, per PM02 FD-04: *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*

Every element of the victory system should be consistent with this — that both clauses are real, neither names the other, and what makes the session complete is not the arithmetic but the moment after the Chronicle is read.

---

## 5. Design Principles

1. **Winning is multidimensional.** Board control, resource accumulation, Chorus Portrait, classified directives, and the vote all feed the final result. No single dimension dominates.

2. **The vote produces a result independent of VP.** The faction that wins the vote may not have the highest VP total. Both outcomes are recorded. In the game's fiction, the vote result is what happened — regardless of which faction "won" by points.

3. **ARBITER's role in scoring is procedural.** ARBITER administers the scoring sequence, reveals the Portrait board, and facilitates the vote. ARBITER does not determine outcomes. The rules determine outcomes.

4. **The Chorus Portrait can swing the result.** A faction that played for board control but accumulated significant negative Portrait may find the final conversion reverses their position. This is intentional.

5. **The victory system should accommodate players who define winning differently.** During the design session for this artifact, discuss: does the scoring system reward or penalize players who pursued the session on their own terms — whether that means board dominance, narrative alignment, collective action, or disruption? Does the final scoring sequence produce a result that feels consistent with how each faction actually played, or does it flatten all sessions into the same competitive frame? *See PM01 §2 — Core Assumption — Replayability.*

---

## 6. Session End Conditions

The session ends when:
1. **Round 8 Debrief is complete** — all eight rounds have been played and the final Debrief is resolved, OR
2. **An Apex ability resolves and specifies session end** — the triggering faction's Founding Figure ability includes a session-end clause (see Artifact 05 §12.4)

In both cases, proceed immediately to scoring.

---

## 7. Victory Point Sources

*[TBD — complete VP source list requires design decision. Extrapolated sources below. All values provisional — subject to playtest.]*

### 7.1 Board Control

| Condition | VP | Notes |
|-----------|-----|-------|
| Established status in a district at session end | [TBD] per district | Per Art 02 §6 — Established presence |
| Present status in a district at session end | [TBD] per district | |
| Structure in a district at session end | [TBD] per structure | |
| Majority presence in a ring at session end | [TBD] | *[TBD — define ring majority threshold]* |

### 7.2 Resources

| Condition | VP | Notes |
|-----------|-----|-------|
| Excess native resource held at session end | [TBD] per token (or ratio) | *[TBD — recommend diminishing returns to prevent pure hoarding strategy]* |
| Cross-faction resources held (via Translation) | *[TBD — may not award VP for non-native resources]* | |

### 7.3 Operatives

| Condition | VP | Notes |
|-----------|-----|-------|
| Founding Figure deployed and not on cooldown | [TBD] | |
| Tier 2 operative deployed at session end | [TBD] per operative | |

### 7.4 Classified Directives

| Condition | VP | Notes |
|-----------|-----|-------|
| Classified directive objective met | [TBD] | Per directive; varies by objective difficulty |

### 7.5 Accords

| Condition | VP | Notes |
|-----------|-----|-------|
| Active Accords honored at session end | [TBD] per Accord | ARBITER verifies |
| Accords broken by this faction | *[TBD — negative VP?]* | *[TBD — design decision: does an Accord violation cost VP, or is Portrait consequence sufficient?]* |

### 7.6 Public Standing

| Condition | VP | Notes |
|-----------|-----|-------|
| Public Standing track position at session end | [TBD] | Convert position to VP via table |

---

## 8. Chorus Portrait Conversion

At session end, ARBITER reveals the Chorus Portrait board.

*[This is the only moment in the session when the Portrait board is publicly visible.]*

### 8.1 Conversion Table
*[TBD — Portrait values convert to VP at session end. Portrait is ARBITER's private running assessment — conversion makes it a visible, significant swing factor. Draft ranges:]*

| Portrait Value | VP Modifier |
|---------------|-------------|
| Strongly Positive | +[TBD] VP |
| Positive | +[TBD] VP |
| Neutral | No modifier |
| Negative | -[TBD] VP |
| Strongly Negative | -[TBD] VP |

*[TBD — is the conversion linear (each Portrait point = X VP) or bracketed (range of Portrait values = single modifier)? Recommend: bracketed, to prevent granular tracking and to emphasize that the Chorus's assessment is categorical, not numerical.]*

### 8.2 Portrait Revelation Protocol
ARBITER reveals the Portrait board at the start of scoring, before VP totals are calculated. Factions see their Portrait value and all other factions' Portrait values simultaneously for the first time.

*[Design note: the simultaneous reveal is intentional. Factions have spent the session uncertain of their Portrait standing. The reveal should feel significant.]*

---

## 9. Scoring Sequence

Scoring is performed in the following order. ARBITER administers.

1. **Lock the board.** No changes to board state after the session ends.
2. **Reveal the Portrait board.** ARBITER reveals all five faction Portrait values simultaneously.
3. **Apply Portrait conversion.** Add/subtract VP modifier per §8.
4. **Count board control VP.** ARBITER and players survey the board together. District status (Established/Present), structures, and ring majorities are counted.
5. **Count resource VP.** Each faction declares their resource holdings. ARBITER confirms against starting state and known transactions.
6. **Count operative VP.** ARBITER confirms operative deployment status.
7. **Reveal classified directives.** All factions reveal simultaneously. ARBITER verifies each objective and awards VP.
8. **Count Accord VP.** ARBITER references Chronicle. Active Accords status is confirmed.
9. **Count Public Standing VP.** Board positions are read.
10. **Calculate totals.** Each faction totals their VP from all sources.
11. **Conduct the vote.** (See §10.)
12. **Announce results.** VP winner announced. Vote result announced. *[TBD — is one result declared "the winner" or are both results independently meaningful?]*

---

## 10. The Vote

The vote is the final action of the session. It is conducted after VP totals are calculated but before the winner is formally announced.

### 10.1 What the Vote Is
Each faction publicly declares their faction's recommended response to the Chorus. This is the moment for which The Table was convened.

### 10.2 Response Options
*[TBD — response options require design decision. Candidate categories:]*

| Response Category | Description |
|------------------|-------------|
| Engage | Humanity should initiate formal contact with the Chorus |
| Observe | Humanity should continue monitoring without initiating contact |
| Fortify | Humanity should treat the Chorus as a threat and prepare accordingly |
| Defer | The decision should be delayed — more data is required |
| Silence | Humanity should cease all response to the Chorus entirely |

*[TBD — are these the right categories? Are they mutually exclusive? Is there a Chorus-aligned response option?]*

### 10.3 Vote Procedure
1. Each faction writes their response choice privately.
2. Choices are revealed simultaneously.
3. ARBITER records the vote in the Chronicle.
4. The plurality response is the **declared position** — humanity's official response to the Chorus in this session's fiction.
5. In case of plurality tie: *[TBD — ARBITER casts the deciding vote? The Chorus decides? The session ends without a declared position?]*

### 10.4 Vote and VP
The vote result does not alter VP totals. It is a separate, parallel outcome. A faction can:
- Win the VP count and lose the vote (the Chorus sees what they built; the city did not follow them)
- Lose the VP count but win the vote (the city followed their vision; the Chorus has its own view)
- Win both (the rarest outcome — and the one the Chorus found most interesting)

### 10.5 Portrait and the Vote
*[TBD — design decision: does a faction's vote alignment with their Portrait affect any scoring? Recommend: no mechanical effect in L1. Portrait has already been converted. Vote is a narrative conclusion. Future layer: vote alignment with Portrait unlocks something.]*

---

## 11. Tiebreakers

*[TBD — define tiebreaker sequence. Extrapolated:]*

If two or more factions are tied on VP total after full scoring:

1. **Portrait rank** — faction with the most positive Portrait wins the tiebreak
2. **Classified directive** — faction that met their directive wins the tiebreak (if tied on Portrait)
3. **Accord count** — faction with the most honored Accords at session end
4. **Shared victory** — if still tied after the above, the tied factions share the session

---

## 12. Winning — What It Means

*[This section is intentionally brief. The design of THE SIGNAL resists clean victory. The following is the intended framing for the manuals.]*

There is no clean win in THE SIGNAL. A faction that accumulates the most points has demonstrated something — that their theory of power, in this city, at this moment, was the most effective. That is not the same as being right. That is not the same as what the Chorus concludes about them.

The session ends with three things on record: a VP result, a vote, and a Chorus Portrait. They do not always agree. That is the game.

---

## 13. Special Conditions & Gameplay Impacts

### Apex-Triggered Session End
*[TBD — does Apex session end alter the scoring sequence? Recommend: no. All same VP sources apply. Board is locked at the moment Apex resolves.]*

### Faction Absence at Scoring
*[TBD — if a faction player is absent at scoring, ARBITER administers their scoring per Chronicle and known board state.]*

---

## 14. Examples & Exceptions

*[TBD — include one worked scoring example: board state, Portrait values, classified directive outcomes, vote. Show the full sequence from §9 with sample numbers.]*

---

*End of Artifact 10a — Victory System v0.1 Draft Placeholder*  
*VP source list, Portrait conversion table, vote response categories, and tiebreakers all require design decisions. Portrait conversion is the highest-stakes design choice in this artifact — it determines how much the Chorus's assessment can swing a session outcome. Prioritize this decision before playtesting.*
