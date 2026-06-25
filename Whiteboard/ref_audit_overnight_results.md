# Ref File Audit — Overnight Batch Results
**Session 115 — 2026-06-23**
**6 agents, 6 ref files audited against source artifacts. READ-ONLY — no files modified.**

---

## Priority Summary — Apply First

| Priority | Ref File | Finding | Severity |
|----------|----------|---------|----------|
| 1 | ref_resources.md | Dispatch Token PA cost: contradiction — ref says PAs cost none; Art 02 DB:12 movement_path shows a PA spend path. Resolve before next session. | High |
| 2 | ref_resources.md | Passive generation absent from formula — Ghost +1 Findings/Quarter unconditional floor missing | High |
| 3 | ref_board_narrative.md | Residential Quarter (DB:3) missing from district/faction geography table (20 listed, should be 21) | High |
| 4 | ref_board_narrative.md | Adjacency model entirely absent — no summary, no `district_adjacency` pointer, no ingress/egress rules | High |
| 5 | ref_card_types.md | Critical ranges wrong — ref says 01–05 / 96–00; schema says roll<5 / roll≥95 (i.e., 01–04 / 95–00) | High |
| 6 | ref_card_types.md | ring_mod direction convention absent from table — positive = easier (raises threshold) not stated | High |
| 7 | ref_card_types.md | EmergencyResponse stated as "full design pending D-04-10" — §14.1 has the complete 5-card effect table | High |
| 8 | ref_card_types.md | P26 (Card Narrative Test) and P27 (outcome determinacy) absent — both referenced in the card design checklist | High |
| 9 | ref_design_pillars.md | Pillars 4.6b through 4.8d (9 items) entirely absent — includes Missing Author Vacuum, ARBITER design principles, all Guaranteed Effects | High |
| 10 | ref_taxonomy.md | Layer × Function validity matrix entirely absent — primary tool for checking card taxonomy legality | High |
| 11 | ref_taxonomy.md | §4.2 cited for Layer Vocabulary — §4.2 does not exist in Art 04b; correct citation is §5.1 | High |
| 12 | ref_taxonomy.md | Duration types: ref lists binary (immediate / permanent); Transient (Month-end) and Seasonal (Quarter-end) missing | High |
| 13 | ref_taxonomy.md | §4.15 Reveal creates a stake, not a compulsion — entirely absent; applies to every Information\|Reveal card | High |
| 14 | ref_taxonomy.md | §4.16 GR 9.1 income protection absent — blocks direct income-suppression / income-amplification cards | High |
| 15 | ref_world_narrative.md | "Something is sending it. Something that has noticed us." — cross-faction consensus fact absent | High |
| 16 | ref_world_narrative.md | ARBITER "not neutral" and "not necessarily aligned with human success" missing — critical for Chronicle and Debrief design | High |
| 17 | ref_resources.md | Residential Quarter PS amplifier: ref presents as settled; PM05 02-n27 is still open and unplaced | High |

---

## Agent 1 — ref_card_types.md vs Art 04 §5 / §6 / §11

### Structural Issue
The ref header claims "Art 04 §1–§5" as source for card type definitions. Card types are in **§6** (schema/enums) and **§11** (modifier card rules). §5 is Design Principles only. Source attribution is wrong throughout.

### High Severity
- **Critical ranges incorrect:** Ref says 01–05 / 96–00. Schema §6.1 says `successcrit` fires on "roll < 5" (= 01–04) and `failcrit` on "roll ≥ 95" (= 95–00). Off by one on both boundaries.
- **ring_mod direction absent:** Table lists values but never states the convention. Per §6.2: "positive = easier, negative = harder."
- **EmergencyResponse stale:** Ref says "full design pending D-04-10." Art 04 §14.1 has complete effect text for all five ER cards (Emergency Fortification, Emergency Injunction, Counter-Analysis, Emergency Broadcast, Hostile Takeover Bid).
- **STD.CA.12 Type B targeting presented as settled:** Art 04 line 1560 explicitly flags this as an open outstanding issue ("Type A / Type B distinction — confirm defined somewhere"). Ref presents it as a locked rule.
- **P26 and P27 absent:** P26 (Card Narrative Test — every card expressible as 1–2 sentence story) and P27 (outcome determinacy — one determinate outcome per resolution tier) are referenced in the design checklist for every card but are not in the ref. P14 (card entries contain card-specific info only), P17 (outsourced equivalents), P20, P24, P25 also absent.
- **Design Rationale and Card Story block requirements absent:** Both are required in every card entry (§5). Card Story is the P26 deliverable.
- **Post-Burst modifier card trade exception missing:** Per §11.6, post-Burst factions can still receive and use modifier cards through trade. Ref omits this.
- **Outcome addition modifier:** Ref omits that outcome addition "requires no Dispatch Token" and fires at host action resolution beat regardless of host success/failure (unless card specifies otherwise). Directly affects Overture-style designs.

### Medium Severity
- `resolution` enum: Ref uses "Probabilistic" — schema enum value is "d100." These are different terms for the same concept; "d100" is the field value.
- `doctrine_mod = None`: Ref says "when no target_faction." Source adds "or no doctrinal variation" — a card can have a target_faction but still have None.
- One-draw-per-qualifying-ring-per-round limit absent from modifier draw rules.
- No-hand-limit rule and public-count/private-content rule absent from modifier hand section.
- "No total per-round limit" and "Burst Play supersedes" absent from modifier submit rules.
- React trigger's binding force absent: P5 says violation "invalidates the card design" — ref records the rule without the consequence.

### Low Severity
- Modifier ring deck names: ref uses Ring 3/2/1 numbers; source uses Sprawl/Infrastructure/Core names.
- Grant Deed "first registered example" for React cards — cannot confirm against §5 or §11; may be stale.

---

## Agent 2 — ref_design_pillars.md vs Art 00a §4

### Structural Issue
The ref covers §4.1 through §4.6a (6 pillars/corollaries) and misses everything from §4.6b onward. Spurious second "4.6" entry for the Narrative Origin Principle — it is the second paragraph of §4.6, not a separate pillar. The duplicate number will confuse any design check that cites a pillar by number.

### High Severity (all Missing)
- **4.6 (Narrative Origin):** Final sentence absent — "A narrative statement that does not have its origin in Art 00 is not canonical." And the 4.6 numbering error creates a false duplicate.
- **4.6b — Missing Author Vacuum:** Entirely absent. Hard constraint: no card flavor text, Chronicle entry, or authored content may assert or imply any faction knows what the message to the Chorus should say.
- **4.7 — ARBITER vs. ARBITER Player:** Entire section absent. Terminological separation between in-world ARBITER and human ARBITER player.
- **4.8 — Guaranteed Effects frame:** Absent. "Not defaults or guidelines — invariants."
- **4.8a — District Character Is Intrinsic:** Hard constraint on district-affecting card design. "No card may change what a district fundamentally produces."
- **4.8b — Irreducible Chance:** Hard floors/ceilings on probability — no modifier can override. References Art 03 §9.4 and Art 04 crit ranges.
- **4.8d — Passive Generation Is Inviolable:** "No game action may reduce, block, redirect, or affect a faction's passive resource generation."

### Medium Severity (text drift, missing sentences)
- **4.3:** "Cooperation is incentivized even when it is politically uncomfortable." — second sentence absent.
- **4.5:** "What becomes inevitable emerges from what The Table does." — affirmative half of pillar absent.
- **4.7a — ARBITER Player Is Human:** Absent. Frames simplification as the protection mechanism.
- **4.7b — ARBITER Cognitive Efficiency:** Absent. Implementation preference order for ARBITER-touching card effects.
- **4.8c — Playable Floor:** Absent. "No faction may ever be without a valid action."

### Low Severity
- **4.2:** "Secrecy is temporary" vs. source "Secrecy exists but only temporarily." Minor, but ref is not quoting canonical language.

---

## Agent 3 — ref_resources.md vs Art 02 §7/§8/§9/§11/§12

### High Severity
- **PA Dispatch Token cost — contradiction:** Ref states political acts cost no Dispatch Token. Art 02 DB:12 movement_path shows a PA spend path explicitly. Contradicts PM02 L146. This is a genuine unresolved ambiguity between PM02 and Art 02's movement_path — needs resolution in Art 03 before ref can be corrected.
- **Passive generation absent:** Ghost receives +1 Findings/Quarter as an unconditional passive floor (Art 00c §4.4). The ref's Generation Formula omits this entirely — Ghost income is systematically underestimated by any calculation using the ref.
- **Residential Quarter PS amplifier — premature:** Ref presents the full multiplier table as settled content. PM05 02-n27 is still open: the mechanic has no canonical artifact home and has not been signed off. The table values appear stable (match PM05 02-n27) but should be flagged as pending sign-off.

### Medium Severity
- **Intel Token states absent:** Art 02 §9 (DB:9) defines four states (Blank / Fresh / Stale / Expired per Art 03 §13.6). Ref covers none of this.
- **Intel Token economics absent:** Movement path (gather delivery, covert/public spend, faction-to-faction trade) defined in Art 02 §9 but absent from ref. Ref scope header promised this coverage.
- **Portrait amplifier rate:** Art 02 §12 (DB:50) is silent on the per-Quarter movement rate for Established Chorus Node holders. Mechanic is in Art 00c §4.5, not Art 02. Ref carries correct value from 00c but it cannot be validated against Art 02.
- **Translation 5:1 Contested rate:** Art 02 DB:8 movement_path lists only three rates (4:1/3:1/2:1). The 5:1 Contested rate is correct per Art 00c §4.5 but is absent from Art 02's text. This is an Art 02 gap, not a ref error.
- **Ghost Dispatch Token asymmetry incorrect source:** Art 02 records 4 tokens per faction uniformly. The 4-vs-3 asymmetry is locked in PM02 L146 / Art 03. Ref attributes it implicitly to Art 02.

### Low Severity
- **Chorus Node tie behavior:** "Both drop to Present-equivalent" on tie — not described in Art 02 (it's in Art 03). Ref carries this correctly but without a traceable Art 02 source.

---

## Agent 4 — ref_board_narrative.md vs Art 01

### High Severity
- **Residential Quarter missing:** District/faction geography table lists 20 districts. Residential Quarter (DB:3, Ring 3, Mandate resource) is entirely absent. Has 5 adjacencies per Art 01 §6.5 adjacency map.
- **Adjacency model absent:** No section on the adjacency principle, district_adjacency table, ingress/egress rules, or the Ring Adjacency Penalty (M-12) for The Mid. These govern action targeting and placement legality.

### Medium Severity
- **Starting configuration claim not in Art 01:** Ref states "Directorate holds the only faction presence at Chorus Node at game start (1 token, Present level)." Art 01 §8 delegates all setup to Art 03-init entirely. Claim needs verification against Art 03-init; should not be attributed to Art 01.
- **Track placement (left/right/bottom) unverifiable:** Ref asserts specific spatial positions (left = Session Timeline + Initiative Strip; right = Chorus Activity Track + Situation Report; bottom = PS Track). Art 01 names the subzones but gives no P1-P5 directional positions. May be from a stale wireframe Art 01 flags as non-canonical.

### Low Severity
- **Ring 0 "Origin" name absent:** Art 01 §6.4 labels Ring 0 as "Ring 0 — Origin." Ref covers Chorus Node narrative but never uses the "Origin" label.
- **"Sprawl" synonym not captured:** Art 01 §5 Design Principle 3 still uses "Sprawl districts" for Ring 3 even though "Baryo" is canonical. Ref uses "Baryo" only, giving no anchor for the surviving synonym in the source.
- **Faction geography table lacks ring annotations:** No ring labels per district in the faction geography table. Not an error, but reduces usability.

---

## Agent 5 — ref_world_narrative.md vs Art 00 / Art 00a §1–§4

### High Severity
- **Cross-faction consensus fact absent:** "Something is sending it. Something that has noticed us." (Art 00 §6.1) — the one claim all factions agree on — absent from ref.
- **ARBITER "not neutral" missing:** Art 00 §9 explicitly states "ARBITER is not a referee. It is not a facilitator. It is not neutral." And: "should feel like a system that is fair — but not necessarily aligned with human success." Both absent. Critical for Chronicle and Debrief scripting.

### Medium Severity
- **Guild/Network pair reasoning incorrect:** Ref says "both believe the answer must be public." Source (§7.7) says Guild's position is about *built permanence*, not publicity. Art 00 §7.5 explicitly states "The Guild does not share the Network's politics." The framing could misrepresent Guild doctrine in card design.
- **ARBITER voice absent from faction voice table:** Art 00 §11.3 includes ARBITER in the voice table ("Exact, observational | Describes humans as systems"). Ref table covers 5 factions only.
- **Ghost "suppressed" vs "not published":** Ref says Ghost "suppressed" the mid-cycle evidence. Source says Ghost "has not published" the analysis. Suppression implies active concealment; the source is more ambiguous. Ghost's identity is as cautious analysts, not active concealers.
- **§6.3 two-question structure absent:** Art 00 §6.3 poses "Was humanity finally ready?" vs. "Was humanity finally noticed?" as a named design tension. The distinction (humanity as achiever vs. humanity as discovery) affects faction voice and Chronicle tone.
- **ARBITER causation question absent:** Art 00 §9.1 — "Did ARBITER cause The Table to convene, or did The Table convene because of ARBITER?" — including ARBITER's canonical response line. Relevant for Debrief scripting.
- **00a §4.6b Missing Author Vacuum absent:** The constraint that no authored content may imply any faction knows what to say to the Chorus is the most frequently violated narrative principle. Absent from this ref.
- **Apex sacrifice framing missing:** Ref describes the Apex as a clean victory condition. Source (§14.8): "What they spend is total and unrepeatable." The sacrifice element is load-bearing for Field Operative Dossier and Chronicle design.

### Low Severity
- Syndicate doctrine line: "Whatever this is, it has value." (first clause) dropped from ref.
- MIRROR/New Meridian city-naming ambiguity absent.
- Directorate's temporal precedence and Guild embeddedness near Chorus Node absent.
- ARBITER temporal position (§9.3) absent.
- The Witness register: "observational" quality and "for posterity" nuance dropped.
- No pointer to Art 07 §9 for full register guide.
- Design Principle 5: positive instruction ("should read as one") absent; only the prohibition is carried.

---

## Agent 6 — ref_taxonomy.md vs Art 04b §4 / §5.1

### High Severity
- **Layer × Function validity matrix entirely absent:** The 6×10 matrix (§5.1) is the primary tool for checking card taxonomy legality. Without it a ref user cannot determine if a proposed Layer × Function combination is valid. Three forbidden Corrupt combinations (Territory|Corrupt, Resolution|Corrupt, Standing|Corrupt — all excluded because no written values exist in those domains) are absent as a result.
- **§4.2 citation wrong:** Ref header `## Layer Vocabulary (§4.2)` — §4.2 does not exist in Art 04b. Headers jump from no §4.2 to §4.4. Correct citation is §5.1 (Column Definitions).
- **Duration types binary:** Ref construction rule 8 says "immediate (this Quarter) or permanent (rest of session)." Art 04b §4.7 defines four types: Immediate (resolved at beat), Transient (removed at Month-end), Seasonal (removed at Quarter-end / Phase 21), Permanent (rest of session). Transient and Seasonal are entirely absent.
- **§4.15 Reveal as stake, not compulsion — absent:** Every Information|Reveal card must be structured so the holder chooses and the card sets the stake. "Any card where the Reveal effect fires without the holder's choice is a 10.1 violation regardless of framing." Absent from ref.
- **§4.16 GR 9.1 income protection — absent:** No card may directly modify a faction's income generation. Distinguishes Economy|Remove|NativeResource (permissible) from income suppression at Upkeep (prohibited). Absent from ref.
- **§4.8 ARBITER-reveal carveout — absent:** ARBITER surfacing information from its own domain is outside GR 10.1. Faction Reveal = creates a stake (§4.15); ARBITER Reveal = game function (§4.8). The distinction governs all ARBITER-domain cards.

### Medium Severity
- **Submission scope truncated:** Missing boundary clause "Cards that affect whether and how an action reaches resolution — before the dice roll." Without this, Submission/Resolution boundary is undefined in the ref.
- **Resolution scope truncated:** "Battlefield Strength" absent from scope list. Missing boundary clause "Cards that alter how the queue resolves — at or during the dice roll, not the submission."
- **Redirect missing subsumption note:** "Convert" (Territory—Redirect ownership change) and "Transfer" (Economy—Redirect cross-faction resource) are not noted as subsumed vocabulary. Relevant for designers familiar with older terminology.
- **Conceal in primitive table without full retirement reasoning:** The §5.1 prohibition rationale (7.2a, structural attribution default) is absent from the primitive table entry.
- **§4.9 cited in source but unresolvable:** Art 04b §5.1 cites §4.9 for three Corrupt exclusions (Territory, Resolution, Standing), but §4.9 does not exist as a section header in Art 04b. This is a source artifact gap; the ref cannot cite what doesn't resolve.

### Low Severity
- Territory scope: "control flags" in ref vs. "Dominant markers" in source (§5.1).
- Recover retirement rationale: ref says "reducible to Add + React context" — §4.14 says committed board state finality. The ref's rationale is a synthesis, not a citation.
- §4.13 is a dangling cross-reference in the source artifact itself (not a ref issue).

---

## Notes for Session Application

**Blocking issues to resolve before applying ref updates:**
1. PA Dispatch Token cost (ref_resources.md Finding 11) — genuine ambiguity between PM02 L146 and Art 02 movement_path. Needs Andy decision and Art 03 clarification before the ref can be corrected.
2. §4.9 in Art 04b (ref_taxonomy.md Finding 17) — source artifact has a section reference that doesn't resolve. Ref cannot be blamed; Art 04b needs the fix first.

**Ref files with heaviest fix burden (ranked):**
1. ref_design_pillars.md — 9 missing pillars/corollaries (4.6b through 4.8d)
2. ref_taxonomy.md — 6 high-severity gaps including the missing matrix
3. ref_card_types.md — 8 high-severity gaps; structural source attribution error
4. ref_world_narrative.md — 2 high, 7 medium
5. ref_resources.md — 3 high; 1 requires prior design decision
6. ref_board_narrative.md — 2 high; both straightforward additions
