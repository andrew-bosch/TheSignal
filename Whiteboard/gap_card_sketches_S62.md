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

*Last updated: S62 — 2026-06-02*
