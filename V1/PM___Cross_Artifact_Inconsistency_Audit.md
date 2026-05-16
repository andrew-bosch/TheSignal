# PM — Cross-Artifact Inconsistency Audit
## THE SIGNAL P1 — Paper Prototype

**Generated:** 2026-05-15 (session 3 — remaining-cycle pass)  
**Scope:** Full suite — Artifacts 00, 00a, 01, 02a, 02b, 03, 04, 04b, PM03  
**Method:** Fresh read of all signed-off artifacts, cross-referenced against session 2 design decisions and 00a v0.2  
**Status:** For review — items to be migrated to PM02 punch list after Andy review  

**Priority key:** ⚠️ Requires decision or rewrite | ❓ Requires clarification or confirm | 📌 Minor — note for future pass

---

## Summary of Findings

| Source Artifact | Count | Highest Priority |
|----------------|-------|-----------------|
| Artifact 00 | 2 | ❓ |
| Artifact 01 | 3 | ⚠️ |
| Artifact 02a | 7 | ⚠️ |
| Artifact 02b | 2 | ❓ |
| Artifact 03 | 6 | ⚠️ |
| Artifact 04 / 04b | 2 | ❓ |
| PM03 | 3 | ⚠️ |
| Cross-artifact | 4 | ⚠️ |

---

## Artifact 00 — Factions, World & Narrative Context

### 00-IQ-01 ❓ Ghost and Network colors are both green
**Location:** 00 §7 faction entries  
**Issue:** Ghost is listed as "Charcoal green" and Network is "Bright signal green." Two distinct factions sharing the same color family at the table creates visual ambiguity — presence tokens must be distinguishable at arm's length in dim lighting.  
**Question:** Confirm that charcoal/bright distinction is sufficient, or revise one faction's color. (Artifact 11 will need to address this for colorblind accessibility regardless.)  
**Affects:** Artifact 11 — Visual Design System

### 00-IQ-02 ❓ Design pillars list only five — sixth pillar pending formal addition
**Location:** 00 §5 Design Principles  
**Issue:** Artifact 00 lists five design pillars. "Narrative and World Consistency" (the sixth pillar established during session 2) exists in 00a §1 and is tracked in PM02 (00-02) for formal addition to Artifact 00 §5. Until that addition is made, the two documents list different numbers of pillars. A reader of Artifact 00 gets an incomplete picture.  
**Action:** Complete PM02 punch list item 00-02 — add sixth pillar to Artifact 00 §5. Re-sign-off required (material change).

---

## Artifact 01 — Game Board: New Meridian

### 01-IQ-01 ⚠️ "Hex / board space" in PM03 terminology table vs. non-hexagonal board
**Location:** PM03 §1 Narrative Language Convention (first row); Artifact 01 §6  
**Issue:** PM03 §1 lists the mechanical term "Hex / board space" being replaced by the in-world term "District." But Artifact 01 §6 explicitly states: "New Meridian is printed as an organic, non-hexagonal map." The board has no hexes. Using "hex" in the terminology table implies a hex grid that does not exist.  
**Action:** Update PM03 §1 — change "Hex / board space" to "Board space" (or simply "Space"). No gameplay impact; only documentation precision.

### 01-IQ-02 ❓ "Chorus Question" is referenced but never defined
**Location:** Artifact 01 §5 (Design Principle 3), Artifact 02a §10 (Chorus Node benefits table)  
**Issue:** Both artifacts mention "Chorus Question access" as a benefit of presence at the Chorus Node. "Chorus Question" is not defined in any artifact. It is unclear whether this is a mechanic (something ARBITER administers), a narrative event, or a card-type benefit.  
**Action:** Define "Chorus Question" or confirm it is a future-layer mechanic and remove from L1 artifacts. If it belongs in L1, add a definition to 00a (as a governing rule), 02a §10, and 03 (as a Phase event).

### 01-IQ-03 📌 Version mismatch: 01 says v1.2; PM03 says v1.0
**Location:** Artifact 01 header; PM03 §3 registry  
**Issue:** Artifact 01 header reads "Version: 1.2 Signed Off." PM03 §3 lists Artifact 01 as version 1.0. PM03 was updated in session 2 (to v1.4) but the individual artifact version for 01 was not corrected.  
**Action:** Update PM03 §3 to reflect current artifact versions for 01, 02a, and 02b (see PM03-IQ-01 below for full list).

---

## Artifact 02a — Resource Systems: Board State

### 02a-IQ-01 ⚠️ ARBITER Dominance Marker design not reflected — "Control flag" language throughout
**Location:** Artifact 02a §6 Component Names, §9 Component Description, §10 Chorus Node  
**Issue:** 02a describes ARBITER's presence at the Chorus Node using "Control flag" (same type as faction control flags) and "Dominant" (a faction influence level). Session 2 established:  
1. The ARBITER Dominance Marker is a distinct, fused piece — not a control flag (PM01 §2.08a)
2. ARBITER is not "Dominant" in the faction sense — ARBITER is constitutive of the Node (00a R04)  
3. Dominant is structurally impossible for factions at the Node because ARBITER's 8 tokens exceed the faction maximum of 6 — not prohibited by rule but made impossible by board state (00a R04)  

The current 02a language ("ARBITER is always Dominant. The Control flag at the Chorus Node belongs to ARBITER and is never moved.") contradicts this design. Also: 02a §9 Component Description says "1 permanent ARBITER flag for Chorus Node" — the ARBITER Dominance Marker is a fused multi-piece component, not a single flag.  
**Action:** Update 02a §6, §9, §10 to:
- Remove "ARBITER is always Dominant" and replace with language reflecting ARBITER's constitutive presence
- Remove "permanent ARBITER flag" from component list; replace with ARBITER Dominance Marker (reference PM01 §2.08a)
- Note that Dominant is structurally unreachable for factions at the Node (ARBITER's 8 tokens > faction max of 6)  
*PM02 punch list item 02a-03 tracks this update. Re-sign-off required.*

### 02a-IQ-02 ⚠️ 4:1 conversion rate hardcoded in 02a §8
**Location:** Artifact 02a §8 Resource Conversion  
**Issue:** 02a §8 states: "Any faction may exchange resources with the bank at a 4:1 rate at any time." This hardcodes a value that is:
1. Under active consideration for revision (PM02 D02a-01 — Chorus Node Translation rates)
2. Potentially variable based on presence at the Chorus Node (Established = 2:1, Present = 3:1, Contested = 5:1 are proposed)
3. In direct violation of 00a Governing Principle 2 (Copy Design — no hardcoded variable values)  

The base rate (no presence at Chorus Node) may stay at 4:1, but the existence of variable rates based on Chorus Node presence means "4:1" is not the complete story.  
**Action:** Rewrite 02a §8 to say the conversion rate is determined by the faction's current presence status at the Chorus Node, and reference the rate table in [Artifact 03 §X — or wherever D02a-01 ultimately lands]. Do not hardcode the value. *Requires D02a-01 decision first.*

### 02a-IQ-03 ⚠️ Chorus Node "Tension marker" used differently from standard definition
**Location:** Artifact 02a §10 Chorus Node — ARBITER's District  
**Issue:** The general Tension marker rule (02a §6) defines Contested as requiring 3+ chips in a tie. At the Chorus Node, §10 says "If two or more factions reach 2+ chips and tie, the Tension marker is placed" — triggering at 2 chips (the Established threshold), not 3. The same physical marker is being used for a different trigger condition in a special district, which creates confusion.  
**Action:** In 02a §10, either: (a) use a different name for the Chorus Node tie condition to distinguish it from the standard Contested condition, or (b) add an explicit callout that the Chorus Node modifies the Tension marker trigger from "3+ chips" to "2+ chips." This should also be reflected in 00a as a governing exception.

### 02a-IQ-04 ❓ "Established" Chorus Node = only 1 faction — contradicts general Established definition
**Location:** Artifact 02a §6 Influence Levels (Established definition); Artifact 02a §10 Chorus Node  
**Issue:** General rule says "Multiple factions may hold Established simultaneously if tied for second place." Chorus Node rule says only one faction may hold Established. This is an intentional exception, but the general Established definition does not note the Chorus Node as an exception. A reader of §6 alone would not know about this.  
**Action:** Add a cross-reference note in the general Established definition: "Exception: at the Chorus Node, only one faction may hold Established at a time — see §10."

### 02a-IQ-05 ❓ Portrait Amplifier at Chorus Node defined in 02a rather than 00a or 02b
**Location:** Artifact 02a §10 "Portrait amplifier" rule  
**Issue:** 02a §10 defines a specific Portrait track movement rule: "Each round a faction holds Established at the Chorus Node, their Chorus Portrait score moves further in its current direction." Portrait rules are governed by 00a and defined in 02b. This is a Portrait mechanic embedded in a board state artifact. Additionally, ARBITER is the sole mover of the Portrait track (00a R01), but 02a defines a rule that implies automatic movement under a specific condition.  
**Action:** The Portrait Amplifier should appear in 00a as a governing rule (or be referenced there), and in 02b's special conditions. The 02a §10 reference should be a cross-reference, not the defining location.

### 02a-IQ-06 📌 Version mismatch: 02a says v1.2; PM03 says v1.0
**See PM03-IQ-01 below.**

### 02a-IQ-07 ❓ "Asset token" terminology conflict between 02a and PM03
**Location:** Artifact 02a §8; PM03 §1  
**Issue:** 02a §8 explicitly states: "There is no abstract 'asset token' wrapper. When a player receives Findings, they take Findings chips." PM03 §1 lists "Resource token → Asset token" as the mechanical-to-narrative term conversion (the in-world term for resource tokens is "asset token"). These two documents directly contradict each other. 02a says there's no "asset token" concept; PM03 says that IS the in-world term.  
**Action:** Reconcile. Either: (a) Remove "Asset token" from PM03 §1 terminology table — resources have proper names (Findings, Exposure, Capital, Capacity, Mandate) and the generic container doesn't exist; or (b) Define "asset token" as the in-world generic term when referring to resources collectively, and make 02a consistent.  *Recommend option (a) — the faction-specific resource names are more narratively grounded.*

---

## Artifact 02b — Resource Systems: Tracking

### 02b-IQ-01 ❓ Portrait affects initiative — not mentioned in 00a or 02b governing rules
**Location:** Artifact 03 §7 Step 7 (Initiative); Artifact 00a (Portrait governance); Artifact 02b §6  
**Issue:** Artifact 03 establishes that ARBITER uses the hidden Portrait track to rank factions for initiative order. This is a significant mechanical use of the Portrait track that is not mentioned in 00a (which governs Portrait) or 02b (which defines the Portrait track). A designer reading only 00a and 02b would not know that Portrait determines initiative.  
**Action:** Add a cross-reference in 00a (new rule in §3 ARBITER Authority or §10 Narrative Consistency) and in 02b §6 Portrait rules: Portrait ranking is used by ARBITER to determine initiative order each round (per Artifact 03 §7).

### 02b-IQ-02 📌 Version mismatch: 02b says v1.5; PM03 says v1.0
**See PM03-IQ-01 below.**

---

## Artifact 03 — Round Structure & Gameplay

### 03-IQ-01 ⚠️ "The Record register" vs. three narrative registers in 07
**Location:** Artifact 03 (multiple references); Artifact 02a §10 (structure removal announcement); Artifact 07 §9 (Narrative Registers)  
**Issue:** Artifacts 02a and 03 both reference "The Record register" as a specific ARBITER communication mode. Artifact 07 §9 defines three narrative registers: Procedural, Advisory, and Reactive. "The Record" is not one of them. This may mean:
(a) "The Record register" was an earlier name for what is now the "Procedural" register — they describe similar things (exact, terse, factual announcements)
(b) "The Record" is a fourth register not included in 07's three  
**Action:** Confirm whether "The Record" = "Procedural" and update all references in 02a and 03 accordingly. Or add "Record" as a fourth register in 07 and 00a.

### 03-IQ-02 ⚠️ "Broadcast Card" and "Effect Card" are undefined terms
**Location:** Artifact 03 §7 Phase 1, Step 2  
**Issue:** Step 2 describes "ARBITER draws the top Broadcast Card from the session deck and reads the narrative aloud. Places it face-up in the Event Zone. Privately applies the matching Effect Card." This introduces two named card types (Broadcast Card, Effect Card) and a "matching" relationship between them. These terms do not appear in PM03 §1 terminology table. The in-world term for world event cards is "Situation Report" (PM03 §1).  
**Questions:** Is the Situation Report deck composed of two-sided cards (public narrative / private effect)? Or two physically separate decks? If two-sided, the "Effect" face should be described in Artifact 01 (board layout) or Artifact 09 (card specs). If two decks, that's a component not in PM01.  
**Action:** Define Broadcast Card / Effect Card relationship in Artifact 01 (board spec includes the Situation Report deck) and Artifact 09 (card specifications). Update PM03 §1 terminology if "Broadcast Card" becomes a named in-world term.

### 03-IQ-03 ⚠️ Ghost gets extra dispatch case slot — asymmetric rule not in 00a or 04
**Location:** Artifact 03 §9 Phase 3  
**Issue:** Phase 3 specifies "Up to 3 covert operation cards (standard factions) or up to 4 (Ghost, if passing their political act this round)." This Ghost asymmetric ability — an additional operation card for forgoing a political act — is a significant faction mechanic defined in a phase description, not in an artifact governing faction abilities. Artifact 04 (which governs card play rules) is where this should live. Artifact 00a should govern whether asymmetric hand size limits are permitted as a design rule.  
**Action:** Move Ghost's extra operation slot rule to Artifact 04 (faction-specific constraints). Cross-reference in Artifact 03. Consider whether 00a needs a rule about asymmetric slot sizes.

### 03-IQ-04 ❓ "Sand timer" introduced but not in component list
**Location:** Artifact 03 §9 Phase 3  
**Issue:** "The sand timer starts" is mentioned for Phase 3 (Dispatch). A sand timer is not listed in PM01's component list and is not referenced in Artifact 01 (board layout). This is a physical component whose presence at the table matters for play.  
**Action:** Add "Sand timer" to PM01 components list. Confirm timer duration for Dispatch phase.

### 03-IQ-05 ❓ "Personal Tiebreaker card" undefined
**Location:** Artifact 03 §7 Step 7, D10 Roll table (result 9)  
**Issue:** D10 initiative roll result 9 triggers "ARBITER draws a Personal Tiebreaker card; players sort by that criterion. Detail in Artifact 07 — ARBITER Toolkit." Personal Tiebreaker cards are not defined in any artifact and don't appear in PM01's component list.  
**Action:** Define Personal Tiebreaker cards in Artifact 07 (ARBITER Toolkit). Add as a component in PM01. Cross-reference in 03.

### 03-IQ-06 ❓ "Status marker" undefined and not in component list
**Location:** Artifact 03 §7 Phase 1, Step 1  
**Issue:** "Each player flips their Status marker to the Discussing side (yellow/text)." The Status marker (with at least two sides: Discussing and presumably a different state) is a component per faction. It is not in PM01's component list and is not defined elsewhere.  
**Action:** Define Status marker states and add to PM01 component list. Confirm whether there's a third state (beyond Discussing and [?]).

---

## Artifact 04 / 04b — Action Card System

### 04-IQ-01 ❓ Portrait Shift taxonomy retired in 04b but retirement mechanics not confirmed
**Location:** Artifact 04b §4 taxonomy; Artifact 00a A01 punch list  
**Issue:** 00a punch list item A01 tracks retirement of "Cross-Category — Shift — Chorus Portrait" from player-facing taxonomy. 04b is an active reference document. Whether the retirement modifies any cards currently in 04 (C16–C20 being redesigned is D04-02) or changes 04b's taxonomy table needs confirmation before either artifact is signed off.  
**Action:** Complete A01 audit — identify any cards in 04 using the Cross-Category — Shift — Chorus Portrait taxonomy and confirm they are being redesigned or are already redesigned.

### 04-IQ-02 📌 "Burst Play" referenced in 03 but defined in 04
**Location:** Artifact 03 §7 Phase 1 Step 6; Artifact 04 §12.6 (cited)  
**Issue:** Artifact 03 references "Burst Play" twice — in the card draw step ("A faction that has triggered Burst Play this session skips this step entirely") and with "Burst Play window" callout. Artifact 04 §12.6 is the defining location. Since 04 is not yet signed off, the Burst Play rules aren't locked. If Burst Play is removed or renamed, 03 needs updating.  
**Note:** This is expected cross-reference behavior, not a structural inconsistency. Flag for re-check when 04 is signed off.

---

## PM03 — Master Artifact Index

### PM03-IQ-01 ⚠️ Version numbers in artifact registry do not match actual artifact versions
**Location:** PM03 §3 Design Artifact Registry  
**Issue:** Multiple artifacts list different version numbers than what PM03 §3 records:

| Artifact | PM03 says | Actual file says |
|----------|-----------|-----------------|
| 01 — Game Board | 1.0 | 1.2 |
| 02a — Resource Systems: Board State | 1.0 | 1.2 |
| 02b — Resource Systems: Tracking | 1.0 | 1.5 |
| 00a — Governing Rules | 0.1 | 0.2 |

**Action:** Update PM03 §3 to reflect current artifact versions. Consider adding a "last updated" column to the registry to make version drift easier to catch.

### PM03-IQ-02 ❓ "Hex / board space" terminology (duplicated from 01-IQ-01)
**See 01-IQ-01 above.**

### PM03-IQ-03 📌 "Asset token" terminology conflict (duplicated from 02a-IQ-07)
**See 02a-IQ-07 above.**

---

## Cross-Artifact Issues

### XA-IQ-01 ⚠️ "Chorus Question" — undefined mechanic referenced in two signed-off artifacts
**Location:** Artifact 01 §5; Artifact 02a §10  
**Issue:** Both signed-off artifacts reference "Chorus Question access" as a named benefit. Neither defines what it is. This is a placeholder mechanic that has accumulated two canonical references without a definition.  
**Decision needed:** Is the Chorus Question a:
- Round-based event (ARBITER poses a question to the faction, with mechanical consequence)?
- Voting privilege (Present factions can participate in some vote during the session)?
- Narrative access (faction may ask ARBITER a question in-character)?
- Future-layer mechanic that should be removed from L1 until defined?  
*Recommend: if not designed for L1, remove from both 01 and 02a and track in PM04 (Future Phases). If L1, design it now.*

### XA-IQ-02 ⚠️ Faction colors defined in Artifact 00 conflict with Artifact 11 placeholder
**Location:** Artifact 00 §7 (signed off); Artifact 11 §6 (placeholder)  
**Issue:** My drafted Artifact 11 placeholder used inferred colors that don't match what Artifact 00 already established. The canonical faction colors (as signed off in Artifact 00) are:
- Ghost: Charcoal green
- Network: Bright signal green  
- Syndicate: Metallic gold
- Guild: Industrial orange
- Directorate: Deep institutional blue  

Artifact 11's placeholder §6 listed different colors (Ghost = grey, Network = amber, etc.). Since Artifact 00 is signed off, it is authoritative.  
**Action:** Update Artifact 11 §6 to match Artifact 00 §7 colors. Note the Ghost/Network green adjacency as a question for Artifact 11's design pass.

### XA-IQ-03 ❓ "ARBITER as sixth faction at The Table" — narrative established in 00a but not in 00
**Location:** Artifact 00a R04; Artifact 00 §8 (The Table)  
**Issue:** 00a R04 establishes that ARBITER is technically a faction at The Table — "six parties, not five." Artifact 00 §8 (The Table) describes The Table without mentioning ARBITER as a sixth party. Since 00 is the narrative foundation document, this absence creates an inconsistency: the governing rules document says six parties, the world document doesn't acknowledge it.  
**Action:** Track in PM02 00-02 or as a new punch list item — add to Artifact 00 §8 or §9 (ARBITER section) a note that ARBITER is the sixth party at The Table, and what distinguishes it. (May be part of the narrative enrichment pass — 00-04.)

### XA-IQ-04 ❓ "Incursion" referenced in signed-off artifacts but defined in 04 (unsigned)
**Location:** Artifact 01 §5; Artifact 02a §6; Artifact 03 (multiple)  
**Issue:** "Incursion" and "Incursion Battlefield Strength" appear in signed-off Artifacts 01, 02a, and 03 as if a known mechanic. Incursion is a card action defined in Artifact 04, which is not yet signed off. If Incursion is renamed, redesigned, or removed in Artifact 04's final design, all three signed-off artifacts need updating.  
**Action:** Flag for re-check when Artifact 04 is signed off. If the Incursion mechanic changes materially, update 01, 02a, and 03 with the revised terminology.

---

## Not Inconsistencies — Confirmed Correct

These were checked and are consistent:
- "District" used correctly throughout (PM03 terminology works in practice)
- "Presence token" / "presence chip" — some variation in naming between artifacts (02a uses "chip," others use "token") — PM03 §1 says the in-world term is "Presence token." Confirm whether "chip" vs "token" is a physical material descriptor or a terminology drift issue. *Low priority.*
- ARBITER capitalization: consistent throughout
- "Dispatch case" naming: consistent throughout
- "The Table" naming: consistent throughout
- Findings decay: defined once in 02a, cross-referenced nowhere — this is intentional (only Ghost has decay)
- 2d10 dice: present in PM01 component list (2 dice); initiative uses 1d10 (one of the two dice) — not an inconsistency, but worth confirming in the Player Guide

---

## Recommended Priority Order for Resolution

1. **02a-IQ-01** — ARBITER Dominance Marker language (tracked as PM02 02a-03; needs rewrite)
2. **02a-IQ-02** — Hardcoded 4:1 rate (after D02a-01 decision)
3. **XA-IQ-01** — Define or remove "Chorus Question" from L1
4. **03-IQ-01** — "The Record register" vs. Procedural — confirm and rename
5. **03-IQ-02** — Broadcast Card / Effect Card definition
6. **00-IQ-02** — Add sixth pillar to Artifact 00 (tracked as PM02 00-02)
7. **PM03-IQ-01** — Update version numbers in registry
8. **XA-IQ-02** — Fix Artifact 11 placeholder colors (trivial — done)
9. **01-IQ-01 / PM03-IQ-02** — Remove "hex" from terminology table
10. **XA-IQ-03** — Add ARBITER as sixth party to Artifact 00 §8

Items 03-IQ-03 through 03-IQ-06 (Ghost slot, sand timer, tiebreaker card, status marker) should be addressed during Artifact 03 re-sign-off review — they are components and rules that may already exist in design intent but need to be formally defined.

---

*End of Cross-Artifact Inconsistency Audit*  
*Migrate flagged items to PM02 punch list. Update PM03 version registry. Fix XA-IQ-02 (Artifact 11 colors) immediately.*
