# STD + GUI Combined Set Audit — S122
*04-n92 · Follows STD+DIR audit (S121). Same structure. STD section is abbreviated — full STD coverage documented in card_analysis_STD_GHO.md §A.*

---

## Pre-Audit Notes (S121)

*Written before the full audit. These findings are based on a card-body read of the full Guild set in S121. Flag items are hypotheses to test, confirm, or resolve during the S122 audit — they are not conclusions.*

### Guild Set at a Glance

9 active cards: 6 CA + 2 PA + 1 MOD stub. Smallest faction set in the game.

| Card | Layer | Function | Subject | Beat | Cost |
|------|-------|----------|---------|------|------|
| GUI.CA.1 Fortify Structure | Territory | Protect | StructureBlock | 2 | C×1 |
| GUI.CA.2 Materials Acquisition | Economy | Add | NativeResource | 2 | free |
| GUI.CA.3 Foundation Rights | Territory | Add | PresenceToken | 3 | C×1 |
| GUI.CA.4 Construction Crew | Submission | RemoveRestriction | CovertOperation | 3 | C×3 |
| GUI.CA.5 Infrastructure Yield | Economy | Add | NativeResource | 3 | free |
| GUI.CA.6 Labor Contract | Economy | Add | NativeResource | 2 | free |
| GUI.MOD.1 Return to Site | Territory | Add | PresenceToken | — | C×? |
| GUI.PA.1 Civic Works Mandate | Territory | Add | StructureBlock | 4 | C×4 |
| GUI.PA.2 Infrastructure Bond | Economy | Add | AccordAgreement | 4 | C×1 |

**Legend:** C = Capacity (native).

### Layer Coverage (pre-audit)

| Layer | Guild cards | Assessment |
|-------|------------|------------|
| Territory | CA.1 · CA.3 · PA.1 · MOD.1 | Depth — build and defend |
| Economy | CA.2 · CA.5 · CA.6 · PA.2 | Heavy — 4 of 9 cards |
| Submission | CA.4 | Single card |
| Standing | — | **Gap** |
| Information | — | **Gap** |
| Resolution | — | **Gap** |

Three of six layers empty. Every other faction covers at least four layers.

---

### Pre-Audit Flag Items

Five open questions to drive the S122 analysis. Each should be explicitly addressed in Sections B–F.

---

**FLAG 1 — Passive income: governing rule or wager card?**

§5a describes: *"+1 Capacity when any opponent completes STD.CA.1 in a district where Guild has presence."* This reads as an automatic passive trigger — no slot cost, no prediction, fires across all opponents.

What's in the deck: GUI.CA.2 Materials Acquisition and GUI.CA.6 Labor Contract are Beat 2 positional wager cards. Guild names a specific faction, bets an action slot, and collects only if the named faction builds or demolishes. A wrong read wastes the slot entirely.

**Question:** Is the Labor Contract doctrine a governing rule (00a or Art 03 upkeep trigger) that makes CA.2/CA.6 the enhanced ceiling version — or are the wager cards the canonical implementation and §5a needs to be updated to reflect the prediction requirement? This is the most fundamental economic coherence question in the Guild set. The answer changes how the deck feels to play.

**Audit action:** Check whether there is any upkeep or passive rule in Art 03 or 00a that implements the §5a passive income description. If not, decide: add the rule or revise §5a.

---

**FLAG 2 — Defense does not scale with win condition**

Win condition = structures on board. GUI.CA.1 Fortify Structure provides immunity to demolition for **one structure per Quarter**. If Guild holds 6 structures in 6 districts, five are open to STD.CA.2 Demolish each Quarter.

The faction whose entire doctrine is permanence of physical form has a single-target defense tool. Directorate (which directly targets Guild's build model via Regulatory Override and the demolition suppression dynamic) can systematically pressure Guild's unprotected structures.

**Question:** Is a second structure-defense card needed? Candidates: (A) district-level protection (all Guild structures in one district immune for a Quarter); (B) cost-raise card (increases demolition cost of Guild structures globally — closer to DIR.PA.1 Regulatory Override but building-focused); (C) React card that triggers on demolition of a Guild structure (Return to Site MOD.1 addresses this partially — assess fit).

**Audit action:** Assess GUI.MOD.1 Return to Site as the designed response to this gap. If it covers the gap adequately, no new card needed. If it doesn't, flag as design gap.

---

**FLAG 3 — Standing card absent (04-n108)**

Guild has no faction-specific Standing card. PS gain comes from building (PA.1 yields +3, CA portrait submitter=+1). Guild has no PS recovery tool and no PS attack capability against opponents.

The STD floor for PS management is Mandate-denominated — cross-resource for Guild. Guild is uniquely exposed to Standing attacks with no faction-level PS response.

**Question:** What is the Guild's intended Standing posture? If Guild is the build-and-hold faction, their PS should compound with structures. A faction Standing card that yields +PS proportional to structure count (parallel to DIR.CA.6/CA.7 Permanent-investment model) would be doctrinally coherent. Or: passive rule (structures provide PS floor — each Guild structure contributes to PS floor per ring).

**Audit action:** Confirm whether 04-n108 (design new Standing card for Guild) is the right vehicle, or whether this is a governing rule issue. Note in Section F §5a verdict.

---

**FLAG 4 — No territorial response**

Guild has zero Remove, Block, or Move cards. If a faction systematically removes Guild presence tokens, Guild has no faction-specific counter. The suppression toolkit available to Guild is entirely Standard (STD.CA.4 Undermine at Mandate×3+N×1 — cross-resource; STD.PA.6 Economic Sanction for resource-layer pressure).

**Question:** Is no removal a doctrinal choice (Guild builds, doesn't fight) or a gap? If doctrinal: what is Guild's intended response to sustained territorial suppression? If gap: what form should a Guild-specific territorial response take — likely lower-force than STD.CA.4, possibly framed as "workforce protection" or "site security" rather than offensive removal.

**Audit action:** Assess whether Guild can survive sustained territorial suppression using only STD cards. If not, flag design gap. Cross-check against §5a "heavy, deliberate, permanent" — a permanent faction that can be systematically dismantled has a doctrine/mechanism mismatch.

---

**FLAG 5 — §9.2 cross-resource compliance (pre-flag)**

Guild economy is heavily mono-Capacity. From the pre-audit read: CA.1 (C×1), CA.3 (C×1), CA.4 (C×3), PA.1 (C×4); CA.2/CA.5/CA.6 are free. PA.2 (C×1). Only cross candidate is CA.4 Construction Crew — which has district native in its crit-fail outcome (as a penalty flowing to Syndicate, not as a cost).

No identified cross-resource *cost* card in the Guild set at pre-audit read. If confirmed during full audit: same §9.2 inversion problem as DIR — high-power effects (PA.1 dual structure build, CA.4 premium rush build) priced at mono.

**Audit action:** Verify during full audit. If all costs are mono-Capacity, flag under §9.2 compliance (same pattern as 04-n118 for DIR). Identify cross-resource ceiling candidates.

---

*Full audit (Sections A–G) to follow in S122. All five flags above should be explicitly addressed in Section B (coverage + doctrinal assessment), Section C (open design decisions), and Section F (§5a verdict).*

---

## A. STANDARD SET

*Abbreviated. Full STD coverage documented in card_analysis_STD_GHO.md §A.*

The standard set provides a shared 27-card floor (16 CA + 5 MOD + 6 PA). For this audit, relevant STD cards are those Guild will realistically play or that define the threat context for Guild's model.

**STD cards with direct Guild relevance:**

| Card | Layer | Cost | Guild context |
|------|-------|------|---------------|
| STD.CA.1 Build Structure | Territory | cross: own-N×1 + district-N×1 | Trigger for GUI.CA.6 Labor Contract wager |
| STD.CA.2 Demolish | Territory | cross: own-N×1 + district-N×1 | Trigger for GUI.CA.2; primary demolition threat to Guild structures |
| STD.CA.4 Undermine | Territory | cross: own-N×1 + district-N×1 | Guild's only non-faction territorial disruption tool |
| STD.CA.10 Protect | Territory | cross | Threshold penalty on one PA targeting Guild structure |
| STD.CA.13 Disinformation Campaign | Standing | mono: own-N×2 | Guild pays 2 Capacity. Covert PS attack. |
| STD.PA.4 Public Censure | Standing | mono: own-N×2 | Guild pays 2 Capacity. Contested PS attack. |
| STD.PA.6 Economic Sanction | Economy | mono | Income reduction; does not remove presence |
| STD.PA.7 Public Address | Standing | mono: own-N×1 | Guild pays 1 Capacity. Automatic +2 PS. |
| STD.PA.8 Table an Accord | Economy | mono: own-N×1 | Accord access for Guild's PA.2 chains |

**STD cross cards (CA.1–4, CA.6–9, CA.11, PA.3):** For Guild as acting faction, cross cost = 1 Capacity + 1 district-native. Guild can play all cross STD cards; the constraint is acquiring the district-native component.

**STD Standing floor (FLAG 3 fact-check):** STD.CA.13, STD.PA.4, and STD.PA.7 are all mono-own-native. Guild pays Capacity for all three. Guild is not cross-resource disadvantaged on Standing tools relative to other factions.

**STD territorial suppression fact-check (FLAG 4):** STD.CA.4 Undermine cost = `resource.faction(acting) * 1 + resource.district(native) * 1`. For Guild: 1 Capacity + 1 district-native. Moderate cost, not 3 Mandate as the pre-audit stub stated. Guild access to territorial disruption is practical at moderate cross cost.

---

## B. GUILD SET

### B1. Coverage Map (active cards)

| Card | Layer | Function | Subject | Beat | Cost | DB cost_type | IR |
|------|-------|----------|---------|------|------|---------|-----|
| GUI.CA.1 Fortify Structure | Territory | Protect | StructureBlock | 2 | C×1 | mono | — |
| GUI.CA.2 Materials Acquisition | Economy | Add | NativeResource | 2 | free | free | — |
| GUI.CA.3 Foundation Rights | Territory | Add | PresenceToken | 3 | C×1 | mono | ⚠ balance |
| GUI.CA.4 Construction Crew | Submission | RemoveRestriction | CovertOperation | 3 | C×3 | mono | — |
| GUI.CA.5 Infrastructure Yield | Economy | Add | NativeResource | 3 | free | free | — |
| GUI.CA.6 Labor Contract | Economy | Add | NativeResource | 2 | free | free | ⚠ id=TBD |
| GUI.MOD.1 Return to Site | Territory | Add | PresenceToken | — | C×? | mono | stub |
| GUI.PA.1 Civic Works Mandate | Territory | Add | StructureBlock | 4 | C×4 | mono | — |
| GUI.PA.2 Infrastructure Bond | Economy | Add | AccordAgreement | 4 | C×1 | mono | — |

*IR = Issues Resolved status. All cards have Design Pass and Signed Off pending; not tracked here.*

### B2. Layer Coverage Summary

| Layer | Guild faction cards | STD floor cards | Coverage verdict |
|-------|-------------------|-----------------|-----------------|
| Territory | CA.1 · CA.3 · PA.1 · MOD.1(stub) | STD.CA.1 · CA.2 · CA.4 · CA.10 | Deep — build, defend, claim |
| Economy | CA.2 · CA.5 · CA.6 · PA.2 | STD.CA.5 · PA.6 · PA.8 | Deep — 4 faction cards; doctrine layer |
| Submission | CA.4 | STD.CA.6–9 | Single card; intentional narrow |
| Standing | — | STD.CA.13 · PA.4 · PA.7 | STD floor sufficient at Capacity cost |
| Information | — | STD.CA.15 · CA.16 | Gap; no faction-specific tool |
| Resolution | — | STD.PA.1–3 · PA.5 · PA.7 | Gap; doctrinal (Guild builds, negotiates via PA.2) |

Three of six layers have no faction-specific card. Standing gap is softer than pre-audit stub framed (STD tools mono at own-native cost). Information gap is real but low-priority for build model. Resolution gap is doctrinal.

### B3. Beat Timing Distribution

| Beat | Cards | Notes |
|------|-------|-------|
| Beat 2 | CA.1 · CA.2 · CA.6 | Covert — positional wagers (CA.2/CA.6) and structural defense (CA.1) |
| Beat 3 | CA.3 · CA.4 · CA.5 | Covert — build, claim, income draw |
| Beat 4 | PA.1 · PA.2 | Public — structures and Accords |
| React | MOD.1 (stub) | Chip-triggered; exact beat and cost undefined in stub |

No Beat 0 cards. Guild's tempo is slow by design: Beat 2 wagers set up Beat 3 income collection; Beat 3 builds compound into Beat 4 PA plays. The wager mechanic (CA.2/CA.6) is the one place where Guild reads an opponent's intent early.

### B4. Doctrinal Assessment

**Guild doctrine:** "The Builders" — Capacity economy / permanence doctrine / *"Humanity's response must demonstrate what it's capable of at its best."*

**How the card set expresses the doctrine:**

- **Build first:** Territory layer (CA.1, CA.3, PA.1) is the primary depth layer — all about establishing and defending structures and presence. Every card in the set either builds, defends what was built, or funds the next build.
- **Compound income:** Economy layer (CA.2, CA.5, CA.6, PA.2) captures revenue from the building activity itself. CA.5 Infrastructure Yield is the clearest expression — the Guild draws from what it already built; income compounds with territorial control.
- **Permanence as win condition:** PA.1 Civic Works Mandate is the signature card — dual structure in one PA slot, Automatic, +3 PS. The highest-power public act in the set costs 4 Capacity but carries no dice risk. Structures are Permanent by default.
- **Wager as intelligence:** CA.2/CA.6 positional wagers are the one place Guild acts on information — naming a faction that will build or demolish this Quarter. A correct read generates income; a wrong read wastes the slot. This is Guild's version of information play.

**FLAG 1 — §5a passive income (RESOLVED — see Section F):**

The Art 03/00a search found no passive-income trigger implementing the §5a description. However, GUI.CA.6 design_note references "04-n2 passive rule" explicitly: *"Together with GUI.CA.2 and 04-n2 passive rule: no faction demolishes or builds in New Meridian without Guild being paid."* The passive trigger is **designed but not yet implemented** — it exists as PM05 item 04-n2. §5a describes the complete intended system; the wager cards are the ceiling implementation; the governing rule (04-n2) is the floor implementation. The flag is not a contradiction — it is an unimplemented design item. See Section F1.

**FLAG 2 — Defense does not scale:**

Confirmed gap. GUI.MOD.1 Return to Site is a React card triggered by chip removal (when a structure token is about to fall). The stub explicitly states: *"structure block removal is simultaneous with chips hitting 0 — no React window can catch it."* MOD.1 places a presence token (recovery), not a structure; it cannot prevent demolition. Guild's defense toolkit:
- CA.1 Fortify Structure: total immunity for one structure per Quarter (Beat 2 wager)
- STD.CA.10 Protect: −45 modifier on one PA targeting Guild (requires predicting which PA)

With 6+ structures, 5+ are open to STD.CA.2 Demolish each Quarter. The defense scales at 1 card per Quarter regardless of structure count. Whether this is a gap or an intentional doctrine tension (permanence doctrine = costly to maintain, not easy to defend) is a design decision. See Section C2.

**FLAG 3 — STD Standing cost (PREMISE CORRECTED):**

Pre-audit stub stated "STD floor is Mandate-denominated — cross-resource for Guild." This is wrong. Verified against card bodies:
- STD.CA.13 Disinformation Campaign: `cost = resource.faction(acting).native * 2` — 2 Capacity for Guild
- STD.PA.4 Public Censure: `cost = resource.faction(acting) * 2` — 2 Capacity for Guild
- STD.PA.7 Public Address: `cost = resource.faction(acting) * 1` — 1 Capacity for Guild

All three are mono. Guild pays the same resource category as every other faction. Guild is **not uniquely exposed** to PS attacks due to resource-type mismatch. The Standing gap is doctrinal depth (no faction-specific PS compounding with structures), not survival access. 04-n108 (design Standing card for Guild) remains a valid enhancement but is not a survival item.

**FLAG 4 — Territorial response (COST CORRECTED):**

Pre-audit stub stated STD.CA.4 Undermine costs "Mandate×3 + own-native×1 (cross, very expensive for Guild)." This is wrong. Verified cost: `resource.faction(acting) * 1 + resource.district(native) * 1` — 1 Capacity + 1 district-native. DB confirms cross. Moderate cost for Guild, not prohibitive. Guild can play STD.CA.4 at 1 Capacity + 1 district-native. The territorial response gap is not about cost barriers — it is about having zero faction-specific recovery (no faction-card Remove/Move/Block). Whether Guild needs a dedicated territorial recovery card is a doctrinal design decision. See Section C4.

**FLAG 5 — §9.2 cross-resource (CONFIRMED):**

DB confirms zero cross-resource cost cards in the Guild set. **CA.4 (C×3) is genuinely mono** — no district-native term in the cost; district-native appears only in the crit-fail outcome as a resource flowing to Syndicate. **PA.1 (C×4) is cross-but-waived** — base cost carries district-native for both target districts; Guild affinity zeroes both terms, reducing effective cost to 4 Capacity. The DB encodes effective (post-waiver) cost, so both read as mono — but neither carries cross-economy commitment. §9.2 principle: mono plays = floor; cross plays must exist at proportionally higher power = ceiling. Both exceed floor power with zero cross commitment = §9.2 inversion. Remedies differ: CA.4 needs a new cross-cost card at higher power tier; PA.1's lever is the waiver itself (design question at PA.1 power level). Same structural shape as DIR (04-n118). See Section E1.

### B5. Win Path Tension

Guild's win path: structures on board (Core/Mid priority) → CA.5 passive income → Accord network via PA.2 → PS compounding through building. PA.1 is the primary win-path accelerator.

**Load-bearing tensions:**

1. **Defense gap (FLAG 2):** The win condition accumulates structures; the defense toolkit protects one per Quarter. High structure counts = high exposure to STD.CA.2 campaigns.

2. **§9.2 inversion (FLAG 5):** CA.4 (genuinely mono) and PA.1 (cross-but-waived via Guild affinity) — the two cards that do the most structural work — both commit zero cross-economy. No cross ceiling means no economic check on Guild's highest-power plays. Remedies differ: CA.4 needs a new cross-cost card at higher power tier; PA.1's lever is whether the affinity waiver should require cross commitment at this power level.

3. **Income prediction dependency:** CA.2/CA.6 wager income requires a correct read on the named faction. A wrong read in back-to-back Months is 2 slots lost with no income. The planned 04-n2 passive rule would provide a floor that makes the wager cards genuinely additive.

4. **Accord dependency:** PA.2 Infrastructure Bond yields an AccordAgreement — Guild's formal economic relationships. The win path assumes Accord completion, which requires a cooperative counterparty. Guild has no coercive Accord mechanism.

The win path is coherent and doctrinally distinct. The primary structural risk is defense gap: Guild can be systematically demolished faster than it can rebuild if a faction targets Guild structures consistently across Quarters.

### B6. Cross-Faction Differentiation

**Guild vs. DIR (sustained institutional pressure):**
DIR shapes the table's environment through standing board conditions; Guild accumulates resources and structures through economic compounding. DIR constrains what others can do; Guild creates board facts that others must react to. Temporal model: DIR wins through environmental control (present effects); Guild wins through structural accumulation (future compounding). Both use Permanent cards — DIR for constraint, Guild for accumulation. Differentiation is clean at the mechanical level. The cross-resource gap mirrors: DIR and Guild both have the same §9.2 inversion problem (04-n118 for DIR; new PM05 item for Guild).

**Guild vs. NET (distributed reactive pressure):**
NET intercepts, redirects, reveals; Guild accumulates and defends. NET is fast/reactive/ephemeral (Beat 2–3 covert intercepts, Immediate persistence); Guild is slow/deliberate/permanent (Beat 3–4 builds, Permanent persistence). NET's win path runs through information control; Guild's runs through structural board density. Beat cadence differs completely: NET plays to disrupt; Guild plays to compound. Differentiation is strong.

**Guild vs. GHO (covert disruption):**
Ghost disrupts covert ops and presence; Guild builds presence and structures. Ghost's presence-removal creates the condition that Guild's CA.4 Construction Crew is designed to escape (CA.4 bypasses the Established prerequisite via CovertOp removal). Guild and Ghost have an implicit predator-prey dynamic that makes their card sets complement each other in terms of interaction design.

---

## C. Open Design Decisions

### C1. FLAG 1 — Implement 04-n2 passive rule

**Status:** 04-n2 is a PM05 item referencing a planned passive income rule: "+1 Capacity when any opponent completes STD.CA.1 in a Guild-presence district." This governing rule is unimplemented. GUI.CA.6 design_note explicitly references it as part of the complete Guild income model.

**Stakes:** Without the passive rule, Guild income is entirely prediction-dependent (wager cards). A missed read wastes a slot AND generates zero income. The passive rule would provide a floor that fires automatically when the structural precondition is met, making wager cards the active ceiling rather than the only income mechanism. This is the correct structural model per the design_note.

**Open interaction questions before implementation:**
- CA.2 triggers on STD.CA.2 (Demolish), not STD.CA.1 (Build). There is no passive counterpart for CA.2. The floor/ceiling layering holds on the build side only; CA.2 has no passive floor under it.
- CA.6 and 04-n2 both trigger on the same event (opponent completes STD.CA.1 in a Guild-presence district). If both are active, Guild would collect +2 (CA.6 wager) AND +1 (passive) on one build. Stacking behavior unspecified — must be resolved at implementation.
- Placement must be Art 03 §9.4.3 (Beat resolution event yield), not 00a upkeep. 00a §9.2 limits upkeep income to "passive generation, district presence, and Structure Block output" — an opponent's action qualifies as none of these; 00a upkeep placement would contradict 00a §9.2 directly.

**Decision needed:** Implement 04-n2 at Art 03 §9.4.3. Resolve CA.6 stacking at spec time. This is an upstream artifact change (material — requires sign-off). §5a description is a preview of the intended complete system, not an error.

→ PM05 (04-n2 — implement passive income rule; upstream artifact change)

### C2. FLAG 2 — Defense scaling: second structure-defense card

**Status:** CA.1 protects one structure per Quarter. MOD.1 (React) addresses chip removal but cannot prevent demolition. Defense does not scale with structure count.

**Candidates:**
- (A) District-level Fortify: all Guild structures in one named district immune for a Quarter. Higher cost than CA.1, different strategic value (concentration defense vs. single-asset defense).
- (B) Demolition cost-raise: a standing PA that raises the difficulty of STD.CA.2 against Guild structures globally (parallel to DIR.PA.1 Regulatory Override but focused on Guild builds). Permanent.
- (C) Accept as doctrine: permanence doctrine = structures are worth protecting; Guild should accumulate enough resources to repair or rebuild, not make demolition impossible. If doctrinally, STD costs for rebuilding after loss should be assessed.

**Decision needed:** Is one structure-defense card per Quarter sufficient for the build model, or is the defense scaling gap a design problem?

→ PM05 (new item — Guild defense scaling: second structure-defense card decision)

### C3. FLAG 3 — Standing card (04-n108)

**Status:** No urgent gap. STD Standing tools are accessible at Capacity cost. The faction-specific card is a design enhancement for doctrinal compounding (structures → PS), not a survival item.

**Confirm 04-n108** as the right vehicle. No new PM05 item; 04-n108 already covers this.

### C4. FLAG 4 — Territorial response: doctrinal or gap

**Status:** Guild has no faction-specific presence-recovery card. STD.CA.4 Undermine is available at 1 Capacity + 1 district-native (moderate cross cost). Guild's territorial response to sustained pressure is: economic sanction (STD.PA.6), income pressure via Accords (PA.2), or cross-investment in STD.CA.4. No fast recovery mechanism.

**Note:** Guild structures count toward Battlefield Strength (+1 each in the contested district and adjacent districts). In §10 contested resolution, Guild's structural density is a natural territorial defense. This partially offsets the lack of an active recovery card.

**Decision needed:** Is Guild's territorial model "build so much presence/structure that removal cannot outpace accumulation" — or does a dedicated recovery card belong in the set?

→ PM05 (new item — Guild territorial recovery: doctrinal or gap decision)

---

## D. Systemic Blockers

**None for S122 scope.**

GUI.MOD.1 Return to Site is a stub (beat and cost undefined) — not a blocker for this audit but blocks final set completeness. Covered in existing PM05.

GUI.CA.6 Labor Contract `id=TBD` — pre-existing issue tracked under 04-n70. Not a blocker for this audit.

04-n2 passive rule unimplemented — not a blocker for the card set audit but is required before §5a can be called stable.

---

## E. Audit Bucket

### E1. §9.2 Cross-Resource Compliance — FLAG 5 (confirmed)

**Finding:** DB confirms all Guild faction cards are mono or free. Zero cross-resource cost cards.

| Card | DB cost_type | Power level | §9.2 status |
|------|-------------|-------------|-------------|
| GUI.CA.1 | mono | Low-moderate (1 structure immune) | Floor — acceptable |
| GUI.CA.3 | mono | Low (1 presence, first-entry) | Floor — acceptable |
| GUI.CA.4 | mono (genuine) | **High** (C×3, bypasses prereq, places presence+structure) | Inversion — no cross term; new cross-cost card needed |
| GUI.PA.1 | mono (effective) | **High** (C×4, dual structure, Automatic, +3 PS) | Inversion — cross-but-waived; lever is the affinity waiver |
| GUI.PA.2 | mono | Moderate (Accord, C×1) | Floor — acceptable |

CA.4 is genuinely mono — the cost structure carries no district-native; the district-native in the crit-fail outcome is a resource delivered to Syndicate, not a cost paid by Guild. PA.1 is cross-but-waived — the base build cost for two districts carries district-native for both; Guild's affinity zeroes them. The DB encodes effective (post-waiver) cost, so both read as mono, but neither card requires cross-economy commitment from Guild.

§9.2 requires cross commitment for ceiling-power plays. Remedies differ: CA.4 needs a new card at higher power with cross cost (no existing cross structure to leverage). PA.1's lever is a design question about the waiver: the cross element is designed into the base cost but zeroed by Guild doctrine — is that the intended ceiling mechanism (Guild earns the waiver by being present in both districts), or does a non-waivable cross cost need to exist at this power level?

**Action:** PM05 item 04-n119 added — Guild §9.2 ceiling gap; split remedies documented there.

### E2. GUI.CA.2 Success Expression — Code/Comment Mismatch

**Finding:** GUI.CA.2 success block:
```python
success = (
    faction(acting).resource.native += 1,
    faction(acting).resource.native += 1   # mirrors STD.CA.2.cost: 1 faction native + 1 district native
),
```

The design rationale states: "Success mirrors STD.CA.2's cost exactly (1 native + 1 district native)." The comment repeats this. But the success expression gives `faction(acting).resource.native += 1` *twice* — 2 Capacity, not 1 Capacity + 1 district-native.

GUI.CA.6 does the same but its arbiter_note is definitive: "deliver 2 Capacity to Guild's Dispatch Case." CA.6 intent is confirmed 2 Capacity. CA.2 has no equivalent arbiter clarification.

**Two readings:**
- **As-coded:** 2 Capacity. No off-faction resource generation. Generation check: passes.
- **As-commented/design-rationale:** 1 Capacity + 1 district-native. Guild acquires the district-native resource type (potentially off-faction). Generation check: would need spending path assessment for off-faction resources.

The generation check passes on either reading. But the code/comment mismatch on CA.2 needs resolution to confirm which behavior is canonical before sign-off.

**Action:** Flag for spec audit pass. Clarify CA.2 success intent: 2 Capacity (matching CA.6 model) or 1 Capacity + 1 district-native (matching design rationale comment)? Likely the same as CA.6: 2 Capacity. The comment is inaccurate if so.

### E3. §5a Descriptive Completeness — FLAG 1 (remapped)

**Finding:** §5a describes a passive income trigger. Art 03 and 00a upkeep rules contain no such trigger (00a §9.2: "upkeep income derives from three sources only: passive generation, district presence, and Structure Block output"). The passive rule is referenced in GUI.CA.6 design_note as "04-n2 passive rule" — a planned but unimplemented PM05 item.

**Status:** §5a is **complete and accurate as a design statement** — it describes the intended system. The passive rule is not yet implemented. §5a is not wrong; 04-n2 is unimplemented.

**Action:** No §5a text change needed. Track as 04-n2 implementation item (PM05, upstream artifact — Art 03 §9.4.3 Beat resolution event yield).

---

## F. §5a Guild Flavor Assessment

### F1. FLAG 1 — Passive income and wager cards

§5a correctly describes the **intended** Guild income system: passive floor (04-n2, unimplemented) + wager cards as ceiling (CA.2/CA.6, implemented). The three-part system — passive trigger, CA.5 infrastructure yield, CA.2/CA.6 wager premium — is coherent when complete. The gap is implementation.

Two open questions the floor/ceiling framing does not yet resolve: (1) CA.2 and CA.6 are a matched wager pair (demolish/build triggers), but 04-n2's passive fires only on STD.CA.1 (Build). No passive counterpart to CA.2's trigger (STD.CA.2 Demolish). The floor is build-side only. (2) 04-n2 and CA.6 both trigger on an opponent completing STD.CA.1 in a Guild-presence district — stacking behavior (additive +3? CA.6 suppresses passive? passive suppresses?) is unspecified. Resolve at implementation. Also: 04-n2 must be placed at Art 03 §9.4.3 (Beat resolution event yield) — 00a upkeep placement would contradict 00a §9.2's explicit upkeep sources.

§5a requires no edit — it describes the complete intended system. Upstream governing rule (04-n2) requires implementation at Art 03 §9.4.3.

### F2. FLAG 2 — Defense scaling

§5a frames Guild as "heavy, deliberate, permanent." The card set supports permanence of action (Permanent structures, Automatic PA.1) but not permanence of defense — one structure is defensible per Quarter. §5a framing does not fully match the mechanical reality if Guild holds many structures. No §5a text change yet; this is a mechanical gap question to resolve first.

### F3. FLAG 3 — STD Standing access (premise corrected)

Pre-audit stub framing incorrect. STD Standing tools are all mono own-native. Guild has identical Standing-tool access to other factions at Capacity cost. §5a should not describe Guild as "uniquely exposed" to PS attacks if it currently does. No immediate edit required unless §5a text makes this claim explicitly.

### F4. FLAG 4 — Territorial response

§5a doctrine ("heavy, deliberate, permanent") implies resistance to territorial suppression. Mechanical support: STD.CA.4 available at moderate cross cost; Battlefield Strength from structures provides passive territorial defense in §10 contested resolution. Active presence-recovery is absent from faction-specific cards. The doctrine implies endurance, but the endurance mechanism is structural (build faster/more) not restorative (recover what was removed). Whether this is sufficient is a design decision (Section C4).

### F5. §5a Summary Verdict

**One item prevents §5a from being fully stable:**

1. **04-n2 unimplemented (FLAG 1):** §5a describes a passive income trigger that does not exist in any governing rule. Implement 04-n2 at Art 03 §9.4.3 (Beat resolution event yield) for §5a to be mechanically complete. ⚠ Stacking behavior with CA.6 on the same trigger event unresolved — must be specified at implementation. ⚠ Floor is build-side only: CA.2's trigger (STD.CA.2 Demolish) has no passive counterpart in 04-n2 as written.

No §5a re-sign-off until 04-n2 is implemented. FLAG 3 correction (non-material, if §5a makes the incorrect STD cost claim) can be done in a standard copy-edit pass without re-sign-off.

---

## G. Art 04b Updates Required

### G1. §6.4 — Add STD+GUI 5-check results (new subsection)

**5-check results for STD+GUI:**

| Check | Result | Notes |
|-------|--------|-------|
| 1. Generation | ✓ | CA.5 (free, structure-gated) + CA.2/CA.6 wager payouts (2 Capacity each). Passive quarterly +1 income. CA.2 code/comment mismatch on payout type — see Section E2. |
| 2. Spending | ✓ | Capacity has deep spending paths (CA.1, CA.3, CA.4, PA.1, PA.2, STD affinity). Off-faction resources from wagers (if CA.2 mirrors district-native) have STD cross card paths. No unspendable resource on either reading. |
| 3. Floor calibration | ⚠ | CA.4 (C×3) genuinely mono — district-native in crit-fail outcome only. PA.1 (C×4) cross-but-waived — Guild affinity zeroes district-native for both target districts. Both are high-power plays with zero cross-economy commitment. §9.2 floor/ceiling inversion on both; remedies differ. |
| 4. Ceiling coverage | ✗ | Zero cross-resource cost cards. DB encodes effective (post-waiver) costs; all read as mono. No cross ceiling exists. Same §9.2 compliance shape as DIR (04-n118). |
| 5. Gap verdict | ✗ | No unspendable resources. §9.2 inversion on CA.4 (genuinely mono) and PA.1 (cross-but-waived). CA.4 → new cross-cost card at higher power tier. PA.1 → design question on waiver scope. PM05 item: 04-n119. |

### G2. §8.5 — Guild faction section (staleness fix)

Current §8.5 (S106) lists CA.1–CA.6 only; does not include PA.1, PA.2, or MOD.1 stub. Needs update:
- Add PA.1 Civic Works Mandate and PA.2 Infrastructure Bond to card list
- Add GUI.MOD.1 Return to Site (stub status, high priority)
- Revise design targets: MOD.1 still high priority; also add 04-n2 passive rule implementation and 04-n108 Standing card
- Update design notes to reflect S122 audit findings

### G3. Version and status

Update version v2.3 → v2.4. Update status header (S121 → S122). Add STD+GUI entry to §6.4 audit log.

### G4. PM05 new items

| Item | Description | Priority |
|------|-------------|---------|
| 04-n2 (existing) | Implement passive income governing rule (Art 03 or 00a) — §5a and CA.6 design_note reference it | High — blocks §5a stability |
| New | Guild §9.2 ceiling gap — CA.4 and PA.1 need cross-resource ceiling card (same shape as 04-n118 for DIR) | High |
| New | Guild defense scaling — second structure-defense card decision (C1/C2/C3 candidates) | Medium |
| New | Guild territorial response — doctrinal or gap decision | Medium |
| 04-n108 (existing) | Guild Standing card — doctrinal compounding (structures → PS); not survival gap | Low |
| New | GUI.CA.2 success expression mismatch — confirm payout intent (2 Capacity or 1C + district-native) | Spec audit |

### G5. 04-n92 status

**Mark 04-n92 ✅** (STD+GUI combined set audit complete, S122).

---

*Audit complete S122 (04-n92 ✅). Art 04b updates and PM05 items: Section G.*
