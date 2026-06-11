# Gap Card Sketches — S62
*Coverage analysis output. Draft S62. Migrate to Art 04 §8 (covert) or §9/§10 (PA) in next design pass.*
*Source: Art 04b §6.1 coverage gap analysis + S62 session design work.*

---

## Cards Requiring Full Spec (Phase 1 priority)

### DISPROVE
**Layer/Function/Subject:** Economy / Remove / IntelToken
**Type:** Standard CovertOperation
**Primary faction:** All (Ghost/Directorate affinity)

**Mechanic:**
- Covertly destroy Intel tokens held by a target faction naming a specified faction
- Declared at Phase A: acting faction names target faction + faction-name on token + age class to target
- Cost scales with token freshness:
  - Fresh: 2 native + d100/35
  - Stale: 1 native + d100/50
  - Expired: 1 native + Automatic
- Success: ARBITER removes one token of declared age/faction-name from target's supply; target unaware of who removed it
- Fail: no effect (cost sunk)
- No restriction — any faction; self-protection or third-party coverage

**Affinities:**
- Ghost: cost −1 (protecting own operational record)
- Directorate: cost −1 (institutional record management)

**Portrait:** Ghost +1; Network −1 (destroying evidence conflicts with transparency doctrine)

**PM05 reference:** 04-n17
**Standard equivalent note:** This IS the standard card. Ghost/Directorate faction-specific variants (stronger version) possible under Principle 17.

---

### DISINFORMATION CAMPAIGN
**Layer/Function/Subject:** Standing / Shift / PublicStanding
**Type:** Standard CovertOperation
**Primary faction:** All (Network/Ghost affinity)

**Mechanic:**
- Covert narrative operation targeting a faction's public standing in a named district
- Acting faction must have presence in target district
- Target: named faction
- Cost: 2 faction native
- d100 / threshold 40
- Success: target PS −2; acting PS +1
- Fail: acting PS −1
- Fail crit: acting PS −2; ARBITER dispatches NotificationSlip to target faction (they know someone ran against them; not who)

**Affinities:**
- Network: threshold +10 (broadcast infrastructure amplifies reach)
- Ghost: cost −1 (datastream manipulation is native capability)

**Portrait:** Network +1; Ghost −1 (public narrative manipulation attracts attention); Directorate −1 (covert image manipulation conflicts with institutional legitimacy doctrine)

**Design note:** First standard covert card with PS shift as primary effect. Fills gap flagged in Art 04b §8.2 and §8.3. Standard card enables all factions to contest standing via narrative; faction-specific variants under Principle 17 (Network/Ghost have superior in-house versions).

**PM05 reference:** 04-n17

---

### ASSET EXTRACTION
**Layer/Function/Subject:** Economy / Redirect / IntelToken (and/or ModifierCard)
**Type:** Standard CovertOperation
**Primary faction:** All (Syndicate/Ghost affinity)

**Mechanic:**
- Steal resources from target faction's supply into acting faction's dispatch case
- Target_object declared at Phase A: Intel tokens OR modifier cards (not both per submission)
- Cost: 1 native
- d100 / threshold 45
- Success: ARBITER transfers 1 resource of declared type from target faction's supply to acting faction's dispatch case
  - Public effect: target's count decreases visibly
  - Beneficiary: unknown at table until case opens at Beat 3 resolution
- Fail: no effect

**Ring mod:** standard (harder in Core, easier in Baryo — physical proximity to target's terminal)

**Affinities:**
- Syndicate: threshold +10 (capital intelligence infrastructure)
- Ghost: threshold +10 (covert acquisition is Ghost doctrine)

**Portrait:** Syndicate +1; Guild −1 ("we do not take what others have built"); Directorate −1 (covert acquisition bypasses legitimate process)

**Open question:** Split into two cards (one for Intel tokens, one for modifier cards) or keep as single card with target_object parameter? Single card pending balance review.

**PM05 reference:** 04-n17

---

## PA Cards Requiring Full Spec

### STANDING INJUNCTION
**Layer/Function/Subject:** Submission / Block / PoliticalAct
**Type:** PoliticalAct / FactionSpecific (Directorate)
**Persistence:** Seasonal (until triggered or Phase 21)

**Mechanic:**
- Directorate places a conditional block on a named faction's next PA of a named type
- Declared at Phase B: Directorate names target faction + PA type blocked
- Cost: 3 Mandate
- Beat 4, Automatic
- On placement: card stays on table face-up as active injunction marker; Directorate PS +1
- Trigger: next time target faction declares the named PA type → PA void; resources returned; target takes Public Pass; Injunction removed; target PS −1
- Expiry (untriggered): removed at Phase 21; Directorate recovers 1 Mandate (partial refund)
- Restriction: Directorate must have at least Established in same ring as target faction's primary operations

**Distinction from P11 (Regulatory Override):** P11 = cost increase on presence-placement; Standing Injunction = full block on specific PA type (more powerful, more targeted)

**Portrait:** Directorate +1; Network −1 (blocking public acts = anti-transparency); Ghost no entry

**PM05 reference:** 04-n17

---

## Standard Equivalents Queue (Principle 17)

*Cards to design as outsourced versions of Ghost intel manipulation trio. Higher cost or lower threshold.*

| Ghost card | Standard equivalent concept | Key difference |
|---|---|---|
| Source Substitution | "Plant Evidence" — hired data specialist falsifies a token | Higher Findings equivalent cost; lower threshold (35 vs 45) |
| Backdate | "Cold File" — hired fixer ages a token | Higher cost; lower threshold (20 vs 30) |
| Field Verification | "Cold Case Review" — hired PI re-investigates | Costs 1 native (vs free for Ghost); same threshold (35) |

**PM05 reference:** 04-n15

---

## Accord Prerequisite Note

**Group A gap cards (Economy/Remove/Accord, Economy/Redirect/Accord, Information/Corrupt/Accord) are BLOCKED pending Art 06 Accord procedure design.**

C-S3 (Accord Transfer — Syndicate) is already designed in concept but also blocked on Art 06.

Do not draft these cards until Art 06 establishes:
- What Accord terms can and cannot contain
- How Accords are played and modified at the table
- When an Accord can be dissolved and by whom
- The physical Accord document format (writable fields)

**PM05 reference:** 04-n19

---

---

## Grant Deed — Tripwire React Card (S67 sketch)

**Source:** Delivered by Syndicate Land Title (Beat 3 success). Blank card stored in ARBITER tableau; district name written on it at delivery; placed in Syndicate's Dispatch Case; moves to hand at Debrief.

**Card type:** New — Tripwire React. Held in faction player's hand. Not dispatched in a case.

**Named district:** Written on the physical card at issuance. Deed is district-specific.

**Trigger:** Any faction places a structure block in the named district.

**React window:** Immediately after the structure block is placed, before any other board state change. (New react class — needs Art 03 procedure addition; tracks under 04-n27.)

**Effect (sequence is fixed):**
1. Add 1 presence chip to `grant_deed.faction.owner` in the named district.
2. Remove the triggering faction's structure block from the named district.
3. Place 1 structure block for `grant_deed.faction.owner` in the named district.
   — Step 3 governed by Governing Rule 8.2: skip if `grant_deed.faction.owner` already holds a structure block there.

**Consumption:** Single use. Grant Deed is discarded after firing.

**Holding:** Syndicate may hold multiple Grant Deeds, including multiple deeds naming the same district.

**Narrative anchor:** "Surprise — that land you just built on is ours. Here's the title to prove it."

*Sketch S67 — full spec pending 04-n26 component registration*

---

---

## Accord Alteration Cards — S80

*Six faction-specific cards using the Art 06 §9.10 Alter mechanism. Covert versions: ARBITER makes the physical alteration (unattributed). Public versions: acting faction player makes the alteration (visible). All use Function=Corrupt per Art 04 §5 P24. Full spec requires 04-n74 (Accord cost calibration) to be resolved first.*

---

### SYNDICATE — ACCORD ALTER (Covert)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** CovertOperation, FactionSpecific (Syndicate)

**Narrative anchor:** Every accord is an asset. The question is who controls the terms — and when the terms change quietly, Syndicate was probably involved.

**Mechanic sketch:**
- Targets an active Accord in the Accord Placement Area
- Syndicate covertly applies one Alter type (Terms or Term removal or Duration) to the form
- ARBITER makes the physical change; no faction is named as the cause
- Affected parties observe the change on the form at their next read; no attribution

**Doctrinal grounding:** Capital doctrine — repositioning agreements to extract more value or remove obligations constraining Syndicate board presence. Quiet manipulation of binding contracts is Syndicate's natural register.

---

### DIRECTORATE — ACCORD ALTER (Covert)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** CovertOperation, FactionSpecific (Directorate)

**Narrative anchor:** The Directorate does not renegotiate in public. It adjusts the environment and moves on.

**Mechanic sketch:**
- Targets an active Accord; applies one Alter type
- ARBITER makes the physical change; unattributed
- Directorate preference: Duration or Terms — reshaping agreements to preserve institutional continuity

**Doctrinal grounding:** Mandate doctrine — survival requires control of the governing framework. Covert adjustment maintains the appearance of stability while shaping outcomes.

---

### GHOST — ACCORD ALTER (Covert)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** CovertOperation, FactionSpecific (Ghost)

**Narrative anchor:** Ghost avoids Accord commitments. When an Accord constrains factions whose behaviour Ghost is studying, removing the constraint is research methodology.

**Mechanic sketch:**
- Targets an active Accord; applies Term removal only (removes a clause row)
- Designed to neutralize terms that restrict information flows or bind a faction Ghost is monitoring
- ARBITER makes the change; unattributed

**Doctrinal grounding:** Findings doctrine — understanding must precede action. An Accord that constrains a subject distorts the observational record. Ghost removes it without implicating themselves.

---

### NETWORK — ACCORD ALTER (Public)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** PublicAct, FactionSpecific (Network)

**Narrative anchor:** The agreement is on the public record. If the terms are wrong, Network will correct them — on the floor, in front of everyone, so everyone knows.

**Mechanic sketch:**
- Declared at Phase B; targets an active Accord
- Network player makes the physical alteration visibly at Beat 4
- Affected parties notified; change is fully attributed to Network
- Possible: PS consequence for Network (transparency bonus) or portrait entry

**Doctrinal grounding:** Exposure doctrine — no one decides in the dark. Public alter is Network declaring that this renegotiation is on record and they own the action.

---

### GUILD — ACCORD ALTER (Public)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** PublicAct, FactionSpecific (Guild)

**Narrative anchor:** The Infrastructure Bond terms should reflect actual construction reality. Guild corrects the record when the agreement no longer matches what is being built.

**Mechanic sketch:**
- Declared at Phase B; targets an active Accord (likely one Guild is party to)
- Guild player makes the physical alteration visibly at Beat 4
- Designed for Terms or Presence Obligation rows — updating to match current board state

**Doctrinal grounding:** Capacity doctrine — agreements must demonstrate what humanity is capable of at its best. An Accord that no longer reflects the actual work is a liability, not an asset. Guild renegotiates openly.

---

### DIRECTORATE — ACCORD ALTER (Public)
**Layer/Function/Subject:** Economy / Corrupt / AccordAgreement
**Type:** PublicAct, FactionSpecific (Directorate)

**Narrative anchor:** This agreement is being corrected under proper authority. The Directorate does not require consent to enforce institutional compliance.

**Mechanic sketch:**
- Declared at Phase B; targets any active Accord (not required to be party to it)
- Directorate player makes the physical alteration visibly at Beat 4
- Authoritative framing: Duration or Terms — reasserting institutional parameters over bilateral private agreements

**Doctrinal grounding:** Mandate doctrine — restraint and continuity require that bilateral agreements operate within institutional bounds. Public alter by Directorate is a formal assertion of that authority, not a negotiation.

*Note: Directorate has both covert and public Alter options — different tactical profiles. Covert = quiet reshaping; Public = authoritative declaration. Two distinct cards.*

---

---

## Board State Manipulation — Add/Move for Self or Opponent — S80

*Four action types: covert add presence for opponent; covert add structure for opponent; covert move opponent's Deployment Marker; covert/public move own Deployment Marker. All create Accord breach opportunities via board-state rules (§9.3 — breach is board-state driven, not intent-driven). Taxonomy note: Move function (Deployment Marker relocation) may need formalisation — currently expressible as Remove(district A) + Add(district B) per Governing Rule 8.3a, or a dedicated Move primitive. Flag for ref_taxonomy.md.*

---

### COVERT ADD PRESENCE — FOR OPPONENT

**Layer/Function/Subject:** Territory / Add / PresenceToken (target = opponent)
**Type:** CovertOperation — faction-specific candidates: Syndicate, Directorate, Ghost

| Faction | Doctrinal angle | Narrative anchor |
|---------|----------------|-----------------|
| Syndicate | Reposition the board — plant opponent presence in a district where they have a Territorial Prohibition Accord, triggering breach on their behalf | "We moved a few pieces. The market corrected itself." |
| Directorate | Force exposure — drive a faction into contested or restricted territory, creating a political liability they cannot explain | "Their presence in that district is now a matter of record." |
| Ghost | Contaminate the observational record — plant presence for a faction being studied, then observe how they respond to being in a position they did not choose | "The data was incomplete. We corrected for that." |

**Mechanic notes:**
- Success: place n presence chips for faction(target) in named district; target is unaware of mechanism
- Interaction with Accord §9.3: if target has a Territorial Prohibition covering that district, presence placement constitutes breach (board state drives breach, regardless of cause)
- Interaction with Governing Rule 8.1: capped at 6 chips per faction per district
- Interaction with Governing Rule 8.2: if target goes Dominant, their structure is at risk — useful secondary effect

---

### COVERT ADD STRUCTURE — FOR OPPONENT

**Layer/Function/Subject:** Territory / Add / StructureBlock (target = opponent)
**Type:** CovertOperation — faction-specific candidates: Syndicate, Directorate

| Faction | Doctrinal angle | Narrative anchor |
|---------|----------------|-----------------|
| Syndicate | Entrap — place a structure for an opponent in a district where they have a Territorial Prohibition (Structures), triggering breach. Or fulfill their Presence Obligation (Structures) without their knowledge, locking in a term they might have wanted to avoid completing. | "The building permits cleared. Funny how that happens." |
| Directorate | Institutional placement — covertly establish a faction's structural presence in a district to trigger compliance or breach consequences on Directorate's schedule | "The development proceeded as required." |

**Mechanic notes:**
- Success: place 1 structure block for faction(target) in named district
- Governing Rule 8.2: only valid if target has no structure block there already
- Governing Rule 8.2b: if target subsequently goes Absent, structure lost immediately — this can be a second-order trap
- If target has a Structure Prohibition Accord term covering this district: breach triggered on placement

---

### COVERT MOVE OPPONENT'S DEPLOYMENT MARKER

**Layer/Function/Subject:** Territory / Move / DeploymentMarker (target = opponent)
**Type:** CovertOperation — faction-specific candidates: Syndicate, Directorate, Network

| Faction | Doctrinal angle | Narrative anchor |
|---------|----------------|-----------------|
| Syndicate | Territorial chess — move a competitor's marker into an Accord-prohibited district (Operational Marker Prohibition) to trigger breach, or out of their Presence Obligation area to cause obligation failure | "Their operation moved. Markets are fluid." |
| Directorate | Strategic displacement — move a faction's marker out of a Core or contested district without direct confrontation; deniable repositioning | "The deployment was… redirected." |
| Network | Exposure — move a faction's marker into a position that creates a visible political contradiction; then broadcast it | "They're operating in District 7. We thought everyone should know." |

**Mechanic notes:**
- Governing Rule 8.3a: Deployment Markers never removed — always moved. This card uses the same rule: marker relocates, does not leave play
- Target district for relocation must be declared at Phase A
- Interaction with Accord §9.3 Operational Marker Prohibition: any Deployment Marker of the bound faction present in the prohibited area = breach, regardless of how marker arrived
- Interaction with Accord §9.3 Presence Obligation: if marker was fulfilling presence count for an Obligation, removal of marker may cause obligation failure

---

### COVERT MOVE OWN DEPLOYMENT MARKER

**Layer/Function/Subject:** Territory / Move / DeploymentMarker (target = self)
**Type:** CovertOperation — faction-specific candidates: Ghost, Syndicate

| Faction | Doctrinal angle | Narrative anchor |
|---------|----------------|-----------------|
| Ghost | Operational invisibility — quietly reposition own marker without revealing deployment intentions at Phase 2; useful for establishing adjacency for information gathering before others can react | "We were never in District 9. Check the record." |
| Syndicate | Pre-positioning — reposition own marker out of a district where Syndicate has an active Accord Operational Marker Prohibition (self-breach covertly; §9.9 ARBITER Portrait consequence applies, no public breach unless discovered) or into a new district ahead of Phase 2 | "Capital flows where the opportunity is." |

**Mechanic notes:**
- Moves own Deployment Marker to a named district; standard entry rules apply
- No public declaration; other factions do not observe the relocation until board state is next examined
- Interaction with §9.9: if move places own marker in self-prohibited area, ARBITER may note Portrait consequence at discretion — no public breach unless displacement is observed

---

### PUBLIC ADD STRUCTURE / PRESENCE — FOR ALLY

**Layer/Function/Subject:** Territory / Add / StructureBlock or PresenceToken (target = ally / named faction)
**Type:** PublicAct — faction-specific candidates: Guild, Network

| Faction | Doctrinal angle | Narrative anchor |
|---------|----------------|-----------------|
| Guild | Infrastructure Bond fulfillment — publicly place a structure or presence for an Accord partner, demonstrating commitment to the terms and advancing mutual board position. Visible act of cooperative capacity. | "We said we'd build it. It's built." |
| Network | Broadcast network extension — publicly extend presence or infrastructure for a faction that has granted Network broadcast access, fulfilling an Accord Presence Obligation or establishing a shared footprint | "We go where the signal needs to reach." |

**Mechanic notes:**
- Declared at Phase B with named target faction and district
- Guild variant: likely tied to active Infrastructure Bond Accord — card may require active Accord as restriction
- Governing Rule 8.1/8.2 apply to target faction (max 6 chips, max 1 structure)
- PS consequence: +1 PS for acting faction (publicly demonstrating Accord compliance); potentially +1 PS for target faction (receiving visible investment)

---

---

## Strategic Patterns — C01/C03 Generalization (S80)

*Emergent plays identified during S80 design pass. All valid under existing ruleset. No new procedures required.*

---

### Pattern 1 — Forced Contested State

**Setup:** A district where Faction A is Dominant (3+ chips). Acting faction acquires Faction B's native resource (via Accord resource transfer, trade at Debrief, or covert gather).

**Play:** Covertly Campaign (C03, submitting Faction B's resource) one or more times to match Faction A's chip count at 3+ → Contested state. Battlefield Strength fires at Month 3 Beat 5. Both Faction A and B absorb resolution cost.

**Acting faction's position:** Does not need presence in the district. Watches from outside. If Present at low count, may emerge Established after both dominant factions take losses.

**Key constraint:** Requires Faction B's native resource in hand before submitting. Resource acquisition is the strategic prerequisite — and that acquisition leaves a trail (Accord terms are public; Debrief trades are observed).

---

### Pattern 2 — The Blind Weapon (Resource Trade as Setup)

**Setup:** Acting faction approaches Faction A at Debrief: "I'll give you 2 Capital for 1 Mandate." Fair trade. Faction A accepts without knowing the purpose.

**Play:** Acting faction uses the acquired Mandate to Campaign for Directorate in a district where Network sits Dominant at 3. Contested state. Directorate and Network fight Battlefield Strength. Acting faction was never in the district.

**Narrative:** "We didn't start the fight. We knew it was going to happen." — Syndicate register.

**Design note:** The trade is voluntary and fully observed. The intent is invisible. No deception rule is violated. This is legitimate play under existing ruleset.

---

### Pattern 3 — Accord Fulfillment as Weapon

**Setup:** Faction A has an active Accord with Faction B containing a Presence Obligation: "Faction A will achieve Established in District 7."

**Play:** Acting faction covertly Campaigns for Faction A in District 7, fulfilling their Accord obligation without their knowledge or consent — while simultaneously deepening the imbalance toward a Contested state.

**Double effect:**
- Faction A technically receives what the Accord required (Presence Obligation fulfilled — no breach)
- But the board state now favors a Contested resolution that neither Accord party wanted
- Acting faction used the Accord's own compliance mechanism as the delivery vehicle

**Design note:** The "helped" faction got what the Accord said they'd get. The acting faction used that fulfillment as the weapon. Neither Accord term nor any governing rule is violated.

---

### Pattern 4 — Accord Breach + Contested Combo

**Setup:** Faction A has a Territorial Prohibition Accord: "Faction A will not exceed Established in District 7." Faction A is currently at Established (2 chips).

**Play:** Acting faction covertly Campaigns for Faction A in District 7, bringing them to 3 chips → exceeds Established → Accord breach triggered (board state drives breach) → simultaneously pushes toward Contested if Faction B is also at 3+.

**Double effect:** Breach consequence fires (§9.6: form removed, Portrait −4, PS −1 for Faction A) AND Contested Battlefield Strength at Month 3. Faction A is politically damaged and territorially exposed in the same beat resolution.

**Narrative:** "The breach was their own presence. We just helped it along."

---

*All four patterns are valid under: C01/C03 generalization (04-n86); board-state breach rule (Art 06 §9.3 — breach regardless of how marker arrived); Contested resolution (Art 03 §11 Beat 5). No changes to existing ruleset required.*

*Last updated: S80 — 2026-06-10*
