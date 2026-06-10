# 06 — Messaging System
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.2 Draft — Accord Governance Active; Messaging Sections Stub  
**Status:** 🟡 In Progress — §9 Accord Documents active design; §6–§8, §10–§12 non-canonical stubs  
**Last Updated:** 2026-06-05  
**Depends on:** 04 — Action Card System; 03 — Round Structure & Gameplay; 07 — ARBITER Toolkit  
**Supersedes:** arbiter_guide (messaging sections, retired), hidden_objectives (classified directive delivery, retired)

---

## 1. Overview

### Problem This Document Solves
The game operates on simultaneous hidden commitment. For that to function physically, there must be a defined protocol for how private information moves between players and ARBITER, how factions communicate with each other through official channels, how ARBITER delivers private notifications, and how formal agreements are documented and enforced.

Without a messaging system, hidden information becomes either unmanageable or unverifiable. This artifact defines the physical and procedural infrastructure that makes the game's information asymmetry real at the table.

### Deliverable
Complete specifications for:
- The dispatch case (physical covert operation submission)
- Faction-to-faction private communication protocols
- ARBITER-to-faction private notification procedures
- Accord documents (formal negotiated agreements)
- Classified directive delivery and management
- Message authentication and dispute resolution

### Success Criteria
- ARBITER can manage all private information flows without confusion at the table
- Players cannot accidentally expose private information through ambiguous procedure
- The physical act of submitting, receiving, and opening messages carries narrative weight
- Accords are verifiable — ARBITER can confirm whether a faction has honored one

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. The Dispatch Case — Covert Operation Submission
7. Faction Private Communication
8. ARBITER Notifications
9. Accord Documents — Negotiated Agreements
10. Classified Directives
11. Message Authentication & Dispute Resolution
12. Special Conditions & Gameplay Impacts
13. Examples & Exceptions

---

## 3. Game Purpose

The messaging system is the physical layer of the game's information architecture. It enforces the design principle that information has timing — that players cannot know what others have committed to until the moment of revelation.

The dispatch case, the Accord form, the private notification slip — these are not administrative conveniences. They are the mechanisms that make the game honest. Without them, the game devolves into negotiation theater with no binding commitments and no enforceable privacy.

---

## 4. Narrative Function

New Meridian's factions do not conduct their business in the open. Meetings happen. Documents are signed. Dispatches are sent to operatives before the world knows the plan. ARBITER receives and holds all of it — not because ARBITER needs to — but because The Table agreed that ARBITER would.

A dispatch case is a physical commitment. The operative is in the field. The operation is running. What ARBITER opens during Resolution is not a hypothetical — it happened.

An Accord is a document. It bears the faction's identifier. When an Accord is broken, ARBITER does not simply note the violation — ARBITER can produce the original document. There is a record. The Chorus has seen it. What that means for the faction's Portrait is something only ARBITER knows.

---

## 5. Design Principles

*Revised S69 — prior principles predated current design framework and have been replaced.*

1. **Placement is binding.** A signed Accord placed in the Accord Placement Area cannot be unilaterally withdrawn. The physical act of signing and placing the form is the point of no return.

2. **Accords are public.** All active Accords are placed face-up in the Accord Placement Area. Every player may read the terms at any time. There is no private Accord.

3. **Terms must be player-verifiable.** Accord terms must describe conditions any player can evaluate from the public board state without requesting private information from ARBITER. ARBITER adjudicates disputes — players are the primary compliance monitors.

4. **Breach is observable, not adjudicated in advance.** Violation is determined from the public board state. Any player may call a potential breach; ARBITER rules on it. ARBITER does not monitor compliance proactively.

5. **Accords carry narrative weight.** Written agreements are legible to The Table, The Chorus, and ARBITER. Breach, compliance, manipulation, and dissolution all carry Portrait implications.

---

## 6. The Dispatch Case — Covert Operation Submission

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

### 6.1 What the Dispatch Case Is
The dispatch case (in-world name: dispatch case; physical component: recipe box — see PM01 §2) is each faction's private submission container. Each faction has one dispatch case; ARBITER has one. All cases are identical in appearance to prevent identification.

### 6.2 Submission Protocol
During **Phase 3 (Dispatch)**:
1. Each faction privately places their covert operation card(s) face-down into their dispatch case, along with any modifier cards they are submitting for the operation.
2. Required resources are placed in the dispatch case alongside the card(s).
3. The faction closes their dispatch case.
4. All closed cases are presented to ARBITER simultaneously (or in initiative order — *[TBD: confirm with Artifact 03 Phase 3 procedure]*).

### 6.3 ARBITER's Opening Procedure
During **Phase 6 (Resolution)**:
1. ARBITER opens each dispatch case in initiative order.
2. ARBITER reads the submitted card(s) and resolves effects.
3. Resources submitted are collected by ARBITER (or returned if the operation fails — *[TBD: confirm with Artifact 04 failure handling]*).
4. Opened case contents are revealed to the table at the moment of resolution.

### 6.4 Incomplete Submissions
*[TBD — what happens if a faction submits insufficient resources, an invalid target, or conflicting cards? Recommend: ARBITER determines resolution per Artifact 07 resolution beats. Operation may be voided or partially resolved.]*

### 6.5 Pass Cards
A faction submitting a Pass card places it face-down in the dispatch case. No resources accompany a Pass. When ARBITER opens a Pass submission, there is no announcement — ARBITER simply sets the case aside. *[TBD — confirm with Artifact 04 §12 Pass Card rules.]*

---

## 7. Faction Private Communication

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

### 7.1 Direct Faction Messages
Factions may send written private messages to other factions at **any time during Phase 2 (Placement) and Phase 4 (Declaration)**. Messages are written on blank message slips (see PM01 §2 — *[TBD component: message slips]*) and delivered by handing the slip to the recipient faction directly or through ARBITER.

*[TBD — confirm whether Phase 3 messaging is permitted. During Phase 3 all factions are supposed to be submitting in private. Recommend: no private messaging during Phase 3.]*

### 7.2 Message Contents
Private messages between factions are unregulated in content — any language, any proposal, any information. Messages are not binding in any game-mechanical sense unless they are formalized as an Accord (see §9).

### 7.3 False Information
Factions may write false information in private messages. ARBITER does not verify the content of faction-to-faction messages. The risk of discovery and the Portrait consequence of demonstrated deception are the only constraints.

---

## 8. ARBITER Notifications

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

ARBITER communicates with individual factions via private notification slips. A notification slip is placed face-down in front of the receiving faction. The faction reads it privately and places it in their hand.

### 8.1 When ARBITER Sends Notifications
- When a covert operation targets a faction and that faction is entitled to know they were targeted (*[TBD — confirm with Artifact 04 per-card resolution rules]*)
- When an operative enters cooldown or a condition changes that only ARBITER tracks
- When a classified directive condition is met
- When ARBITER determines a Portrait-relevant event has occurred *[TBD — confirm scope with 00a R07 and R31]*

### 8.2 Notification Content
Notification slips are written in the narrative registers defined in Artifact 07. ARBITER does not use mechanical language in notification slips. *[See Artifact 07 §[TBD] — Narrative Registers.]*

### 8.3 Notification Confidentiality
No faction may demand to read another faction's notification. Factions may reveal notification content voluntarily. ARBITER does not confirm or deny the existence of notifications to other factions.

---

## 9. Accord Documents — Negotiated Agreements

### 9.1 What an Accord Is

An Accord is a written, binding agreement between two or more factions, initiated by card submission and executed at Debrief. It is a physical component — a completed Accord form bearing the terms of the agreement and signature marks from all parties. Active executed Accords are placed face-up in the Accord Placement Area on The Overview and are public record. Proposed but unexecuted Accord forms also remain on the table in the Accord Placement Area as a record of the proposal.

### 9.2 Accord Form — Physical Component

An Accord form (see PM01 §2 — *[TBD component: Accord forms]*) is a structured guided contract. It provides pre-printed clause types (obligation, prohibition, resource payment), fill-in-the-blank fields for faction names, districts, resources, and duration, and a signature checkbox per party. Players select from structured terms; free-form text is not permitted on the form.

Fields:
- **Parties** — checkboxes for each faction party to the agreement (minimum two)
- **Terms** — one or more clauses selected from pre-printed types; fill-in fields for names, values, districts, duration
- **Duration** — fill-in field: Quarter range, named condition, or "until game end"
- **Signatures** — one checkbox per named party; checking the box constitutes execution

The drafted form is placed in the Accord Placement Area at Beat 4, whether or not it is ultimately executed or signed.

### 9.3 Accord Terms

Valid Accord terms must be:

- **Specific** — name the bound factions, the actions or restrictions, and the duration.
- **Player-verifiable** — any player at the table must be able to evaluate compliance from the public board state alone. Terms requiring ARBITER private knowledge are not valid. *(Example: "Faction A will not place a Structure Block in District 7" — valid. "Faction A will not submit more than two covert operations" — not valid; case count is ARBITER-private.)*
- **Written in New Meridian language** — all terms use in-world names for places, resources, and factions.

Ongoing obligations (e.g., resource transfers per Upkeep) are valid — they must be performed publicly at the named phase and are player-visible.

### 9.4 Formation

All Accords must be initiated by card submission.

**Delivery (Beat 4)**

Three cards may initiate Accord formation. Each causes ARBITER to deliver a blank AccordForm to the submitting faction at Beat 4:

| Card | How the submission is created |
|------|-------------------------------|
| P08 Table an Accord | Declared at Phase B; ARBITER delivers blank AccordForm to submitting faction at Beat 4 as PA resolution outcome |
| P10 Infrastructure Bond | Declared at Phase B; ARBITER delivers blank AccordForm to submitting faction at Beat 4 as PA resolution outcome |
| Overture modifier card (from C09 Fund) | Assigned to any PA at Phase B; ARBITER delivers blank AccordForm to submitting faction when host PA resolves at Beat 4 — any outcome; per Art 04 §11.8 |

**Drafting**

After receiving the blank form, the submitting faction fills in the terms per §9.3. Once completed, the faction places the drafted form in the Accord Placement Area. This may happen at any point after drafting is complete. A form placed outside a Debrief window is queued for the next Debrief.

**Execution Window (Debrief)**

At Debrief, for each drafted Accord form in the Accord Placement Area:

- **Execute** — all named parties check their signature box; the Accord becomes active immediately. Per Art 06 §9.9 Portrait entries apply.
- **Negotiate** — terms may be amended by mutual agreement before signing. All physical amendments to the form occur during Debrief only.
- **Withdraw** — the proposing faction may physically remove and discard the form at any time during Debrief. No consequence.

The target faction may verbally decline. If declined and no further negotiation is pursued by either party before the end of that Debrief, the form is removed and discarded.

Physical alterations to drafted forms — signing, amendments — may only occur during Debrief. Verbal discussion of terms is permitted at any time.

**Persistence**

Drafted Accord forms remain in the Accord Placement Area until one of the following:
- The submitting faction physically withdraws and discards the form (no consequence).
- The target faction verbally declines and no further negotiation is pursued by either party by the end of that Quarter's Debrief (removed and discarded at Debrief close).
- The Accord is executed (§9.5).

Drafted forms not resolved by any of the above persist across Quarters.

### 9.5 Compliance Monitoring

Active Accords are face-up in the Accord Placement Area. All players may read the terms at any time. Compliance monitoring is the table's collective responsibility — any player may call a potential breach.

ARBITER may raise a breach unprompted if observed during resolution or Debrief. ARBITER does not proactively audit for breach between phases.

### 9.6 Breach

A breach occurs when a party fails to fulfill a term while the Accord is active.

1. Any player (including ARBITER) may call a potential breach, naming the term and the apparent violation.
2. ARBITER evaluates the call against the written Accord text. ARBITER's ruling is final.
3. On confirmed breach: ARBITER removes the Accord form from the Accord Placement Area to the ARBITER area. Other players observe the removal.
4. Any cards or effects attached to or acting on the Accord are released on removal.
5. ARBITER notes a Portrait entry for the breaching faction. *(Values: ARBITER reference only — see §9.9.)*

### 9.7 Accord Completion

When an Accord's stated duration expires with no breach:

1. Any player may call completion by naming the expired condition.
2. ARBITER confirms compliance over the full duration.
3. ARBITER removes the form from the Accord Placement Area to the ARBITER area.
4. ARBITER notes Portrait entries for all complying parties. *(Values: ARBITER reference only — see §9.9.)*

### 9.8 Dissolution

**Mutual dissolution** — available at Debrief only. All parties countersign a dissolution annotation on the form and present it to ARBITER. ARBITER removes the form to the ARBITER area. No Portrait consequence.

**Unilateral dissolution** — not permitted. A party that ceases to honor terms is in breach (§9.6).

### 9.9 Portrait Scale — Accord Events

*ARBITER reference only. These values are not revealed to players.*

| Event | Parties affected | Portrait entry | Register |
|-------|-----------------|----------------|---------|
| Breach confirmed | Breaching party only | −4 | The Record |
| Per-Quarter compliance (active Accord) | All complying parties | +1 | The Record |
| Accord completed (full duration, no breach) | All complying parties | +2 | The Record |
| Mutual dissolution | None | — | — |

### 9.10 Accord Manipulation

Cards and effects may interact with active Accords. The following interaction types define what is mechanically possible; specific card implementations are governed by card text. Additional interaction types may be registered as new card effects are designed.

**Lock** — Prevents voluntary dissolution of the named Accord until a stated condition releases it. All locks are released when the Accord is removed from the Accord Placement Area for any reason (breach, completion, or dissolution).

**Alter** — Changes one or more physically written values on the Accord form (numeric values, faction names, district names, duration conditions). The alteration is made directly on the form. The Accord remains active; affected parties are notified per card text.

**Transfer** — Replaces one named party in the Accord. The outgoing party is struck from the form; the incoming party is written in. All obligations and benefits transfer to the incoming party. The Accord remains active; affected parties are notified per card text.

---

## 10. Classified Directives

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

### 10.1 What a Classified Directive Is
A classified directive (in-world name: classified directive; mechanical term: hidden objective — see PM03 §1) is a secret objective assigned to each faction at session setup. It describes a condition the faction should achieve by session end, and the VP reward for achieving it.

### 10.2 Delivery
At setup, ARBITER delivers one classified directive to each faction via sealed envelope. Factions may not reveal their directive to other factions *unless they choose to*. Factions may bluff about their directive's contents.

### 10.3 Resolution
At end of session scoring (Artifact 10a), each faction reveals their classified directive. ARBITER verifies whether the condition was met. VP is awarded or withheld per the directive's terms.

*[TBD — classified directive content belongs in Artifact 05 (if operative-tied) or Artifact 08 (if player-kit). Recommend: directive card design in Artifact 08; delivery procedure here in Artifact 06.]*

---

## 11. Message Authentication & Dispute Resolution

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

### 11.1 Disputed Accord Terms
If factions dispute what an Accord says, ARBITER produces the original document. ARBITER's reading of the written text is final.

### 11.2 Forged Messages
A faction may claim to show another faction a notification from ARBITER. *[TBD — L1 recommendation: ARBITER notification slips use a standard form that factions cannot replicate; ARBITER's slips are distinguishable from faction-authored messages. Prevents forgery. Confirm with PM01 component design.]*

### 11.3 Timing Disputes
If the order of message receipt or submission is disputed, initiative order from Phase 2 resolves it. ARBITER's record of receipt order is authoritative.

---

## 12. Special Conditions & Gameplay Impacts

> ⚠ *Draft Stub — Non-Canonical. This section was written prior to the current design framework and has not been reviewed against signed-off artifacts. Content is placeholder only and should not be treated as established procedure.*

### Chorus Node and Messaging
*[TBD — are there special messaging rules at the Chorus Node? Recommend: no mechanical special cases for L1. ARBITER observes all messaging regardless of district.]*

### Underfunded Operations
*[TBD — defined in Artifact 04. Reference here once confirmed.]*

---

## 13. Examples & Exceptions

*[TBD — populate after 04, 07, and 08 are finalized. Key scenarios: disputed Accord, voided operation, ARBITER notification timing.]*

---

*End of Artifact 06 — Messaging System v0.3. §9 signed off (L198). §§10–13 draft stubs — non-canonical.*  
*Core protocol design extrapolated. Accord forms, notification slips, classified directive delivery, and message slip component specs require PM01 component confirmation and Artifact 04/07/08 sign-off.*
