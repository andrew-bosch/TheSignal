# 06 — Messaging System
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 Draft — Placeholder  
**Status:** ⬜ Not Started — Blocked by Artifact 05 (implicitly) and Artifact 04 completion  
**Last Updated:** 2026-05-15  
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

1. **Physical commitment is binding.** A card in the dispatch case cannot be retrieved. A signed Accord cannot be unsigned. The physical act of closing the case or signing the form is the point of no return.

2. **ARBITER is the sole witness.** ARBITER opens all dispatch cases. ARBITER delivers all private notifications. No player may access another player's private information except through ARBITER.

3. **Ambiguity defaults to ARBITER.** If a message's content or intent is disputed, ARBITER's reading is authoritative.

4. **Accord terms must be mechanical.** Accords cannot bind vague intentions — they bind specific, verifiable game actions ("Faction A will not place presence tokens in District 7 for two rounds"). ARBITER can verify this.

5. **Messages are in-world.** All written communications between factions use in-world language. There is no mechanical shorthand in an Accord. If you cannot say it in the language of New Meridian, you cannot put it in an Accord.

---

## 6. The Dispatch Case — Covert Operation Submission

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

### 7.1 Direct Faction Messages
Factions may send written private messages to other factions at **any time during Phase 2 (Placement) and Phase 4 (Declaration)**. Messages are written on blank message slips (see PM01 §2 — *[TBD component: message slips]*) and delivered by handing the slip to the recipient faction directly or through ARBITER.

*[TBD — confirm whether Phase 3 messaging is permitted. During Phase 3 all factions are supposed to be submitting in private. Recommend: no private messaging during Phase 3.]*

### 7.2 Message Contents
Private messages between factions are unregulated in content — any language, any proposal, any information. Messages are not binding in any game-mechanical sense unless they are formalized as an Accord (see §9).

### 7.3 False Information
Factions may write false information in private messages. ARBITER does not verify the content of faction-to-faction messages. The risk of discovery and the Portrait consequence of demonstrated deception are the only constraints.

---

## 8. ARBITER Notifications

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
An Accord is a formal, verifiable agreement between two or more factions. It is written on an Accord form (see PM01 §2 — *[TBD component: Accord forms]*), signed by all parties, and held by ARBITER.

### 9.2 Accord Terms
Accord terms must be:
- **Specific:** name the factions, the actions, and the duration ("for rounds 3 and 4")
- **Verifiable:** ARBITER must be able to determine at any point whether the Accord is being honored
- **Mechanical:** terms must reference observable game actions, not intentions

### 9.3 Accord Execution
1. Proposing faction drafts the Accord in writing on an Accord form.
2. All named parties review and sign.
3. ARBITER receives and holds the signed Accord.
4. ARBITER monitors compliance. Violations are noted by ARBITER — *[TBD: what is the mechanical consequence? Recommend: Portrait input for the violating faction; ARBITER reveals the violation at Debrief. No automatic mechanical penalty — consequences emerge through the faction's reputation and Portrait.]*

### 9.4 Accord Dissolution
An Accord may be dissolved only by mutual written agreement of all parties, counter-signed and presented to ARBITER. Unilateral dissolution is a violation. *[TBD — whether a dissolved Accord has Portrait consequence for the dissolving party even if mutual. Recommend: yes, slight Portrait input — the Chorus notes the renegotiation regardless of consent.]*

---

## 10. Classified Directives

### 10.1 What a Classified Directive Is
A classified directive (in-world name: classified directive; mechanical term: hidden objective — see PM03 §1) is a secret objective assigned to each faction at session setup. It describes a condition the faction should achieve by session end, and the VP reward for achieving it.

### 10.2 Delivery
At setup, ARBITER delivers one classified directive to each faction via sealed envelope. Factions may not reveal their directive to other factions *unless they choose to*. Factions may bluff about their directive's contents.

### 10.3 Resolution
At end of session scoring (Artifact 10a), each faction reveals their classified directive. ARBITER verifies whether the condition was met. VP is awarded or withheld per the directive's terms.

*[TBD — classified directive content belongs in Artifact 05 (if operative-tied) or Artifact 08 (if player-kit). Recommend: directive card design in Artifact 08; delivery procedure here in Artifact 06.]*

---

## 11. Message Authentication & Dispute Resolution

### 11.1 Disputed Accord Terms
If factions dispute what an Accord says, ARBITER produces the original document. ARBITER's reading of the written text is final.

### 11.2 Forged Messages
A faction may claim to show another faction a notification from ARBITER. *[TBD — L1 recommendation: ARBITER notification slips use a standard form that factions cannot replicate; ARBITER's slips are distinguishable from faction-authored messages. Prevents forgery. Confirm with PM01 component design.]*

### 11.3 Timing Disputes
If the order of message receipt or submission is disputed, initiative order from Phase 2 resolves it. ARBITER's record of receipt order is authoritative.

---

## 12. Special Conditions & Gameplay Impacts

### Chorus Node and Messaging
*[TBD — are there special messaging rules at the Chorus Node? Recommend: no mechanical special cases for L1. ARBITER observes all messaging regardless of district.]*

### Underfunded Operations
*[TBD — defined in Artifact 04. Reference here once confirmed.]*

---

## 13. Examples & Exceptions

*[TBD — populate after 04, 07, and 08 are finalized. Key scenarios: disputed Accord, voided operation, ARBITER notification timing.]*

---

*End of Artifact 06 — Messaging System v0.1 Draft Placeholder*  
*Core protocol design extrapolated. Accord forms, notification slips, classified directive delivery, and message slip component specs require PM01 component confirmation and Artifact 04/07/08 sign-off.*
