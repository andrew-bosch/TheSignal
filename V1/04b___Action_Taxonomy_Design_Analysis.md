# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.1  
**Status:** ✅ Reference Document — Active  
**Last Updated:** 2026-05-14  
**Companion to:** 04 — Action Card System  
**Purpose:** Preserve the taxonomy framework, development decisions, coverage analysis, and faction design recommendations that govern Artifact 04 and all future card design passes.

---

## 1. Overview

This document is the authoritative source for the action system taxonomy — the framework for categorizing what every card in The Signal can affect and how. It also contains the design analysis that produced it: coverage gap analysis, faction coverage matrix, and design recommendations for the next card pass.

Card definitions live in Artifact 04. This document does not reproduce card content. The taxonomy fields on each card (Category — Function — Target) reference this document for definitions.

---

## 2. Index

| Section | Content |
|---------|---------|
| §3 | Taxonomy Development — Key Decisions |
| §4 | Final Taxonomy Table |
| §5 | Card Taxonomy Index |
| §6 | Coverage Analysis — Gaps and Concentrations |
| §7 | Faction Coverage Matrix |
| §8 | Design Recommendations by Faction |
| §9 | Design Principles Derived from Taxonomy |

---

## 3. Taxonomy Development — Key Decisions

The following decisions were made during taxonomy development. Recorded to preserve reasoning behind the final structure.

### 3.1 Categories reflect what is being affected, not what is being done

A category answers: **what part of the game system is being affected?**
A function answers: **what happens to it?**

Early versions used function-first labeling (Build, Demolish) which described the action rather than the effect. Replaced with effect-first labeling (Add, Remove, Redirect, Recover) consistent across all categories.

### 3.2 Knowledge and Reputation collapse into Cross-Category

Knowledge (hidden information control) and Reputation (assessment track management) do not belong to a single category — they cut across Board, Resource, and Action states. Both were initially separate categories and were merged into Cross-Category:
- Knowledge targets (card hand, dispatch case, Intel tokens) contain elements from multiple categories
- Reputation tracks reflect behavior across all categories

Cross-Category functions (Reveal, Shift, Protect, Corrupt) apply to targets that don't belong cleanly to any single category.

### 3.3 Protect is cross-category and not constrained to adverse effects

Protect was initially defined as shielding against adverse effects only. Revised to: *preserve the current state of a named target against a specified effect — any named change, whether adverse or beneficial.* A faction could protect an Accord from being modified by anyone including themselves.

### 3.4 Corrupt applies only to physically written or recorded values

Corrupt was initially considered as a Knowledge function. Revised to Cross-Category with strict physical scope: applies only to values physically written or tracked in the paper prototype. Valid targets: Intel tokens (faction name and round number written on token), Accord agreements (terms written on document). Invalid: printed card text, marker positions (tracked by physical position not written value), Chronicle (ARBITER narrative — not a mechanical game element).

### 3.5 React is an Action function, not a separate category

React fires automatically when a named publicly-observable condition is met. It is a trigger mechanism classified under Action. The effect of a React card may span multiple categories — C12 Materials Acquisition is Action — React that produces Resource — Recover. The taxonomy records the trigger mechanism; the effect category is secondary.

### 3.6 Redirect unifies Convert and Transfer

Convert (changing ownership of a board element) and Transfer (moving resources between factions) are both instances of Redirect. Convert is Board — Redirect. Transfer is Resource — Redirect.

### 3.7 Accord agreements are valid Resource targets

Accord agreements are registered documents with binding mechanical effects. Valid targets for:
- Resource — Add (Propose Accord creates one)
- Resource — Remove (breaking an Accord covertly)
- Resource — Redirect (transferring an Accord to different parties — the "small print" mechanic)
- Cross-Category — Corrupt (altering recorded terms)
- Cross-Category — Protect (locking terms against modification)

### 3.8 No persistent temporary cross-round effects

Design Principle 11 (Artifact 04): all card effects are either immediate (this round only) or permanent (rest of session). This revised several cards:
- C19 Deep Cover: from "extend immunity one round" to "permanently remove prior operation from record"
- C22 Detain: from "block marker conversion for one round" to "permanently remove marker for remainder of session"
- C24 Surveillance Placement: from "monitor district for 2 rounds" to "permanent monitoring for remainder of session"

### 3.9 Paper vs Electronic ARBITER knowledge gap

In the paper prototype, ARBITER knows what happened (actions taken, board state, resolved effects) but does not know what is being considered (cards held, options available, choices not made). This is consistent with ARBITER's narrative character — ARBITER reads signals that have entered the causal chain; intent before action is not yet signal.

In the electronic version, ARBITER would have access to hand contents and could generate Chronicles that include patterns of restraint alongside patterns of action. The unchosen path is also story. Flag for PM04 — Future Phases.

---

## 4. Final Taxonomy Table

| Category | Function | Definition | Scope | Valid Targets |
|----------|----------|-----------|-------|---------------|
| **1 — Board** | | *Physical state of districts* | | |
| | Add | Place a game element in a district | Permanent or temporary | Presence (token or claim marker), Structure block |
| | Remove | Remove a game element from a district | Permanent or temporary | Presence (token or claim marker), Structure block |
| | Redirect | Move a game element to a different district or faction | Location or ownership change | Presence (token or claim marker), Structure block |
| | Recover | Return a previously removed game element to play | From removed state to active | Presence (token or claim marker), Structure block |
| **2 — Resource** | | *Faction holdings of spendable or usable game elements* | | |
| | Add | Faction gains a resource | — | Native resource, Intel token, Modifier card, Accord agreement |
| | Remove | Faction loses a resource | — | Native resource, Intel token, Modifier card, Accord agreement |
| | Recover | Previously spent resource returned to faction | — | Native resource, Intel token, Modifier card |
| | Redirect | Resource moves from one faction to another | — | Native resource, Intel token, Modifier card, Accord agreement |
| **3 — Action** | | *Availability and parameters of submitted actions* | | |
| | Block | Named target cannot be submitted or resolved | At submission or resolution | Covert operation, Political act, Operative ability |
| | Modify | Named target's parameters are changed | Difficulty, cost, scope, duration, effect magnitude | Covert operation, Political act, Operative ability |
| | Copy | Acting faction replicates named elements of another faction's submitted target | Full action or named subset: target only, effect only, or cost only | Covert operation, Political act, Operative ability |
| | Remove Restriction | A precondition on a named target is waived | Presence, resource, timing, sequence | Covert operation, Political act, Operative ability |
| | React | Effect fires automatically when named condition is met | Condition must be publicly countable or observable | Presence token count, Structure block presence, Resource marker count, Public Standing position, Accord agreement existence, Action resolution outcome |
| **Cross-Category** | | *Functions applicable across any category or target type* | | |
| | Reveal | Hidden information disclosed to named recipients | Named faction(s) or whole table. Partial or full disclosure | Card hand contents, Dispatch case contents, Intel tokens held, Modifier cards held, Classified directives, Action attribution |
| | Shift | Assessment marker moves in named direction | Positive or negative. Named track specified on card | Public Standing, Chorus Portrait |
| | Protect | Preserve the current state of a named target against a specified effect | Effect type named on card. Not constrained to adverse effects only | Any valid target in any category |
| | Corrupt | Alter a recorded value on a named writable game element | Physically written or recorded values only | Intel token (faction name or round number), Accord agreement (any recorded term) |

---

## 5. Card Taxonomy Index

*Card definitions are in Artifact 04. This index provides Category — Function — Target assignments for all cards as a design reference. Use this table to identify coverage gaps and duplications.*

| Card ID | Name | Category | Function | Target |
|---------|------|----------|----------|--------|
| C01 | Build Structure | Board | Add | Structure block |
| C02 | Demolish | Board | Remove | Structure block |
| C03 | Campaign | Board | Add | Presence |
| C04 | Undermine | Board | Remove | Presence |
| C05 | Gather | Resource | Add | Intel token |
| C06 | Broadcast Interference | Action | Modify | Political act (cost) |
| C07 | Amplify | Action | Modify | Political act (effect magnitude) |
| C08 | Buy Influence | Board | Add | Presence |
| C09 | Fund | Resource | Redirect | Native resource |
| C10 | Protect | Cross-Category | Protect | Covert operation (difficulty) |
| C11 | Fortify Structure | Cross-Category | Protect | Structure block |
| C12 | Materials Acquisition | Resource + Action | Recover + React | Native resource |
| C13 | Foundation Rights | Board | Add | Presence |
| C14 | Construction Crew | Action | Remove Restriction | Covert operation (presence requirement) |
| C15 | Infrastructure Yield | Resource | Add | Native resource |
| C16 | Pattern Match | Action | Copy | Covert operation (full) |
| C17 | Archive Recovery | Resource | Recover | Intel token |
| C18 | Identity Blind | Cross-Category | Protect | Action attribution |
| C19 | Deep Cover | Cross-Category | Protect (permanent) | Action attribution |
| C20 | Misdirection | Resource | Add | Intel token (corrupt content) |
| C21 | Invoke Jurisdiction | Action | Block | Covert operation (C01, C03) |
| C22 | Detain | Board | Remove (permanent) | Presence (claim marker) |
| C23 | Evidence Preservation | Cross-Category | Protect (permanent) | Written record |
| C24 | Surveillance Placement | Resource | Add (permanent) | Intel token |
| C25 | Sealed Border | Action | Block | Covert operation (presence placement) |
| C26 | Leak | Cross-Category | Reveal | Action attribution |
| C27 | Source Protection | Cross-Category | Protect | Action attribution |
| C28 | Open Channel | Cross-Category | Reveal | Private communications |
| C29 | Network Cascade | Action | Modify | Covert operation (scope) |
| C30 | Community Anchor | Board | Add | Presence |
| C31 | Leveraged Acquisition | Resource | Add | Native resource |
| C32 | Short the Market | Resource | Remove | Native resource |
| C33 | Hostile Acquisition | Board | Redirect | Structure block |
| C34 | Golden Parachute | Cross-Category | Protect | Native resource |
| C35 | Regulatory Capture | Action | Block | Covert operation + Political act |
| P01 | Establish Presence | Board | Add | Presence |
| P02 | Contest | Board | Remove | Presence (contested) |
| P03 | Commission | Board | Add | Structure block (both districts) |
| P04 | Denounce | Cross-Category | Shift | Public Standing (−) |
| P05 | Broadcast | Cross-Category | Reveal | Action attribution |
| P06 | Leverage | Resource | Remove | Native resource |
| P07 | Invoke the Table | Action | Block | Any (procedural) |
| P08 | Propose Accord | Resource | Add | Accord agreement |
| P09 | Public Works Declaration | Board | Add | Structure block |
| P10 | Infrastructure Bond | Resource | Add | Native resource (target faction) |
| P11 | Issue Directive | Action | Block | Political act |
| P12 | Convene an Inquiry | Resource | Add | Intel token |
| P13 | Public Disclosure | Cross-Category | Reveal | Action attribution |
| P14 | Open Record Request | Cross-Category | Reveal | Written record |
| P15 | Acquisition Offer | Board | Redirect | Presence |
| P16 | Market Pressure | Action | Modify | Covert + Political act (cost) |
| P17 | Publish Analysis | Cross-Category | Shift | Chorus Portrait |
| P18 | Signal Review Request | Action | Modify | Covert operation (difficulty) |

---

## 6. Coverage Analysis — Gaps and Concentrations

### 6.1 Unused taxonomy combinations

The following combinations exist in the taxonomy but have no current card. These represent available design space for future card development.

| Category | Function | Target | Priority | Notes |
|----------|----------|--------|----------|-------|
| Board | Redirect | Presence | Medium | Move tokens between districts |
| Board | Redirect | Structure | Low | Transfer structure faction — C33 partially covers |
| Board | Recover | Presence | Medium | Return removed tokens — Guild candidate |
| Board | Recover | Structure | High | Reconstruct demolished structure — strong Guild card |
| Resource | Remove | Intel token | Low | Strip opponent Intel tokens |
| Resource | Remove | Modifier card | Medium | Strip opponent modifier cards |
| Resource | Remove | Accord agreement | High | Break Accord covertly — important missing mechanic |
| Resource | Recover | Modifier card | Low | Return spent modifier card |
| Resource | Redirect | Accord agreement | High | "Small print" mechanic — Syndicate doctrine |
| Resource | Redirect | Modifier card | Low | Partially covered by trade rules |
| Action | Copy | Political act | Low | Copy opponent political act |
| Action | Copy | Subset only | Medium | Copy target or effect only — Ghost doctrine |
| Action | React | Resource condition | Low | Fire on resource state change |
| Action | React | Accord existence | Medium | Fire on Accord creation or breach |
| Cross-Category | Reveal | Card hand contents | High | Disclose opponent's held cards |
| Cross-Category | Reveal | Classified directives | Low | Very high impact — use carefully |
| Cross-Category | Reveal | Modifier cards held | Medium | Disclose modifier card contents |
| Cross-Category | Reveal | Named faction only | High | Targeted disclosure — Ghost intelligence delivery |
| Cross-Category | Shift | Chorus Portrait (primary covert) | High | Portrait as primary covert effect — Ghost doctrine |
| Cross-Category | Shift | Public Standing (primary covert) | High | Standing as primary covert effect — Network doctrine |
| Cross-Category | Corrupt | Intel token | High | Falsify Intel token content |
| Cross-Category | Corrupt | Accord agreement | High | Alter Accord terms — Syndicate doctrine |

### 6.2 Overrepresented combinations

| Category | Function | Target | Cards | Issue |
|----------|----------|--------|-------|-------|
| Board | Add | Presence | C03, C08, C13, C30, P01 | 5 cards — differentiation critical |
| Action | Block | Covert operation | C21, C25, P07, P11 | 4 Block cards across standard and faction |
| Cross-Category | Protect | Action attribution | C18, C19, C27 | 3 cards, 2 same faction, same function |
| Cross-Category | Reveal | Action attribution | C26, C28, P05, P13 | 4 Reveal cards, two pairs with same scope |

---

## 7. Faction Coverage Matrix

| Category | Function | Target | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|----------|----------|--------|----------|-------|-------|-------------|---------|-----------|
| **Board** | | | | | | | | |
| | Add | Presence | C03, C08 | C13 | — | — | C30 | — |
| | Add | Structure | C01 | C14 | — | — | — | — |
| | Remove | Presence | C04 | — | — | — | — | — |
| | Remove | Structure | C02 | — | — | — | — | — |
| | Redirect | Presence | — | — | — | — | — | — |
| | Redirect | Structure | — | — | — | — | — | C33 |
| | Recover | Presence | — | — | — | — | — | — |
| | Recover | Structure | — | — | — | — | — | — |
| **Resource** | | | | | | | | |
| | Add | Native resource | — | C15 | — | — | — | C31 |
| | Add | Intel token | C05 | — | — | C24 | — | — |
| | Add | Accord agreement | P08 | — | — | — | — | — |
| | Remove | Native resource | — | — | — | — | — | C32 |
| | Remove | Accord agreement | — | — | — | — | — | — |
| | Recover | Native resource | — | C12 | — | — | — | — |
| | Recover | Intel token | — | — | C17 | — | — | — |
| | Redirect | Native resource | C09 | — | — | — | — | — |
| | Redirect | Accord agreement | — | — | — | — | — | — |
| **Action** | | | | | | | | |
| | Block | Covert operation | — | — | — | C21, C25 | — | C35 |
| | Block | Political act | P07 | — | — | P11 | — | — |
| | Modify | Cost | C06 | — | — | — | — | P16 |
| | Modify | Effect magnitude | C07 | — | — | — | — | — |
| | Modify | Scope | — | — | — | — | C29 | — |
| | Modify | Difficulty | C10 | — | — | — | — | P18 |
| | Copy | Full action | — | — | C16 | — | — | — |
| | Copy | Subset | — | — | — | — | — | — |
| | Remove Restriction | Presence | — | C14 | — | — | — | — |
| | React | Action outcome | — | C12 | — | — | — | — |
| **Cross-Category** | | | | | | | | |
| | Reveal | Action attribution | — | — | — | — | C26, C28 | — |
| | Reveal | Named faction | — | — | — | — | — | — |
| | Shift | Public Standing | P04 | — | — | — | — | — |
| | Shift | Chorus Portrait | — | — | P17 | — | — | — |
| | Protect | Structure block | — | C11 | — | — | — | — |
| | Protect | Native resource | — | — | — | — | — | C34 |
| | Protect | Action attribution | — | — | C18, C19 | — | C27 | — |
| | Protect | Covert operation | C10 | — | — | — | — | — |
| | Corrupt | Intel token | — | — | C20 | — | — | — |
| | Corrupt | Accord agreement | — | — | — | — | — | — |

---

## 8. Design Recommendations by Faction

These recommendations inform the redesign decisions D-04-02 through D-04-05 in Artifact 04 §16.

### 8.1 Ghost — Priority redesign targets

Current Ghost set (C16–C20) is doctrinally coherent but mechanically narrow. Two cards duplicate the same function (Cross-Category — Protect — Action attribution).

**High priority:**
1. **Cross-Category — Reveal — Named faction:** Ghost delivers targeted intelligence to a specific faction privately rather than the whole table. *Targeted intelligence disclosure that strengthens relationships without public exposure.*
2. **Cross-Category — Shift — Chorus Portrait (primary covert):** Ghost's doctrine is understanding the Chorus. A card whose primary effect is Portrait improvement through demonstrated understanding is the most doctrinally correct gap. Candidate: *Calibrated Analysis — submit a specific interpretation of current board state; ARBITER evaluates accuracy; Portrait shift based on correctness.*
3. **Action — Copy — Subset:** Ghost should have a partial copy card — copy only the target (apply your own operation to the same district as named faction) without replicating the full cost and effect.
4. **Replace C18 Identity Blind:** Both C18 and C19 are Cross-Category — Protect — Action attribution. C19's permanent effect is stronger and more interesting. C18 could be replaced with Resource — Add — Intel token (generate intelligence through analysis without physical presence — Findings spent, Intel token received, no adjacency restriction).

### 8.2 Directorate — Priority redesign targets

Directorate is over-indexed on Action — Block: C21, C25 (covert), P07, P11 (political) — four Block cards.

**High priority:**
1. **Replace C25 Sealed Border with Resource — Add — Native resource (Mandate):** Institutional authority generates Mandate when exercised and respected. *"When The Directorate issues an instruction that is complied with this round — no faction contests a Directive, no faction enters a sealed district — Mandate is generated as institutional validation."*
2. **Cross-Category — Shift — Public Standing (primary covert):** The Directorate managing public perception through institutional channels. A covert card that shifts Public Standing positively when an institutional action succeeds.

**Medium priority:**
3. **Action — Modify — Difficulty (increasing, against all factions):** Institutional scrutiny raises difficulty of all covert operations in a named district this round. Distinct from C10 Protect (which only protects the protecting faction's assets).

### 8.3 Network — Priority redesign targets

Network has duplicate Reveal cards and a doctrinal contradiction in C27.

**High priority:**
1. **Replace C27 Source Protection with Resource — Add — Exposure:** The Network generating Exposure through information activity. *"When The Network successfully Reveals information this round, gain 1 Exposure — the act of disclosure generates the resource that enables further disclosure."* Creates positive feedback loop consistent with Network doctrine.
2. **Cross-Category — Shift — Public Standing (primary covert):** Network managing city-wide public perception through covert information operations. *"Targeted community outreach in a named district shifts Public Standing based on the district's current control state."*
3. **Action — React — Action resolution outcome:** Network responding to opponent public actions. *"When any faction's political act succeeds this round, The Network may trigger — placing 1 presence token in the district where the political act resolved."*

**Medium priority:**
4. **Consolidate C26 and C28:** Both are Cross-Category — Reveal with different scopes (Action attribution vs Private communications). Consider whether both are needed or one broader Reveal card covers the design space.

### 8.4 Syndicate — Priority redesign targets

Syndicate has excellent Resource coverage but zero information capability despite being an economic intelligence operation.

**High priority:**
1. **Cross-Category — Corrupt — Accord agreement:** Alter the recorded terms of an existing Accord. *"The Syndicate may alter one numeric value in any registered Accord — changing a resource amount, duration, or threshold. The alteration is physically made to the Accord document. Both parties notified in case."* Requires ARBITER to manage Accord document integrity.
2. **Resource — Redirect — Accord agreement:** The "small print" mechanic. *"The Syndicate transfers an existing Accord's obligations from one faction to another. The receiving faction is privately notified — they may accept or contest at the start of the next round."*
3. **Cross-Category — Reveal — Intel tokens held:** Economic intelligence. *"The Syndicate names a faction. ARBITER announces the count (not content) of Intel tokens that faction holds. The Syndicate may offer to purchase one token from the named faction at 3 Capital — the named faction may accept or decline."*

---

## 9. Design Principles Derived from Taxonomy

The following principles were established or confirmed during taxonomy development. They supplement the principles in Artifact 04 §5.

**Taxonomy principle 1 — Every card has a primary function.**
Cards may have secondary effects across multiple categories but their primary category and function must be clear. A card that does too many things across categories is a design problem.

**Taxonomy principle 2 — Faction-specific cards should fill gaps, not duplicate standard cards.**
Where standard cards already cover a function/target combination, faction-specific cards should either fill a gap or provide a meaningfully differentiated version (different restriction, scope, or scale).

**Taxonomy principle 3 — Symmetric categories enable symmetric learning.**
Board and Resource have the same four functions (Add, Remove, Recover, Redirect). A player who understands one category understands the other by analogy. New categories should maintain this symmetry where possible.

**Taxonomy principle 4 — Cross-Category functions need a clear reason for cross-category status.**
A function belongs in Cross-Category when its targets genuinely span multiple categories (Reveal, Shift) or when it modifies any target regardless of category (Protect, Corrupt).

**Taxonomy principle 5 — React conditions must be publicly observable.**
React fires on publicly countable or observable conditions. Hidden conditions are not valid React triggers. This maintains information integrity — you cannot react to information you shouldn't have.

**Taxonomy principle 6 — Permanent effects are more interesting than temporary ones.**
Principle 11 (Artifact 04) eliminated cross-round temporary effects. When designing new cards, prefer permanent effects over temporary ones.

---

*End of Artifact 04b — Action Taxonomy & Design Analysis v1.1*
