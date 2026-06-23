# Ref File Audit Results — S113
*Apply in next session. All findings are READ-ONLY reports from audit agents.*

---

## ref_tracking.md — COMPLETE

### Material inaccuracies (fix immediately)
- **Portrait band score ranges** presented as canonical in ref; Art 02 explicitly says "TBD pending Art 07 Portrait design (PM05 07-13)." Remove or flag the specific numeric boundaries.
- **"Portrait drives initiative"** — not present in Art 02 or Art 00a §5. Source unknown; remove or find citation.
- **"First action immediately exits Ambiguous"** rule — not in Art 02 or Art 00a §5. Remove or cite source.

### Missing content
- **IntelToken Blank state** — Art 02 lists 4 states: Blank / Fresh / Stale / Expired. Ref covers only 3 (starts at creation, skips Blank pre-creation state).
- **Movement path lifecycle** — Art 02 distinguishes covert spend vs. public spend as distinct paths. Ref conflates under "Use."
- **§10.1 scope** — rule applies to ALL private components (hand cards, modifier cards, directives, etc.), not only IntelTokens. Ref scopes it only to IntelTokens.
- **§10.1a precision** — ref says "without a specific game action"; source (Art 00a §10.1a) says "without a Reveal effect." Tighten to Reveal effect.
- **§10.2 gap** — covers tokens spent via action resolution as well as discarded. Ref only covers voluntary discard.
- **§10.3 gaps** — (a) holding limits (max 2 / Ghost max 4) are flagged as "balance decisions subject to playtesting" in Art 00a; ref presents them as locked; (b) limits are not mechanically enforced — ARBITER handles called violations per Art 07; ref omits this.
- **§5.1c** — Portrait scoring fires at Resolution (act or outcome); not mentioned in ref at all.
- **"Faction Resolution Grid = only valid cross-faction IntelToken target"** — this is a ref-synthesized rule not explicitly stated in Art 00a §10 or Art 02. If this is normative design (and it is), it needs to become a named governing rule in Art 00a §10, not just ref-asserted.

### Precision gaps
- §10.1a: "specific game action" → "Reveal effect"
- Beat 3/Beat 4 timing claim for IntelToken targeting has no cited source in Art 00a or Art 02 (likely Art 03 §9.4).
- Age tier values (Fresh 0–1 / Stale 2–3 / Expired 4+) attributed in ref as if canonical; Art 02 delegates to Art 03 §13.6.

---

## ref_components.md — COMPLETE

### Critical finding: ref is almost entirely empty
**66 of 70 components have zero coverage.** The ref covers lifecycle notes for 4 components (Dispatch Case, NS-xx, IS-xx, Broadcast Card pair) — none completely. No component has full field coverage.

### Stale "not yet designed" entries (these ARE designed in Art 02)
- **CC-xx / Countermeasure card (DB:52)** — fully signed off. CM-A / CM-B model, 15 total, full schema. Ref says "not yet designed."
- **ER-xx / Emergency Response card (DB:97)** — fully signed off. Ref says "not yet designed."
- **NS-xx / IS-xx / CA-xx** — all have full Art 02 schema entries. Ref flags all as "schema pending."
- **VS-xx** — not a component. Visibility is a field on each component, not a registered component type. Stale ref artifact; remove.

### Stale/incorrect content
- **NS-xx delivery condition:** Ref says "on covert op fail conditions." Art 02 says delivery condition is being targeted by a covert op — not a fail outcome. May be a substantive difference.
- **Dispatch Case "per Quarter" framing:** Same physical object cycles; it resets, not replaces. "One per Faction Player" is correct; "per Quarter" is wrong framing.

### Legality and targeting rules: zero coverage
Art 02 delegates legality to Art 03 §22; ref does not bridge this gap or point card designers there. Key targeting facts missing from ref:
- Presence chip: max 6/district/faction; verbs Add/Remove/Move only
- Structure block: max 1/faction/district; removed on Absence; verbs Add/Remove/Move only
- Intel token: 4 states (Blank/Fresh/Stale/Expired); Corrupt verb applicable; faction-to-faction trade path
- Target Profile (DB:48): Corrupt verb applicable — declared parameters can be altered; entirely absent from ref
- Modifier token (DB:47): Flip verb changes sign (positive/negative); absent from ref
- Modifier card (DB:11): 4 play modes with distinct paths; removed from game on use; absent from ref
- Countermeasure card (DB:52): CM-A blocks all actions; CM-B adds modifier; covert play path differs from standard dispatch; absent from ref
- Grant Deed (DB:113): React card, mutable owner field, consumed on fire; entirely absent from ref
- Boost Marker (DB:104) / Visibility Marker (DB:103): ARBITER-only resolution markers; absent from ref

### Priority components with zero ref coverage (most relevant to card design)
Intel token · Modifier card · Modifier token · Boost Marker · Visibility Marker · Countermeasure card · Grant Deed · Target Profile · Structure block · Presence chip

---

## ref_procedures.md — COMPLETE

### Critical errors (fix first)
- **"Beats 0–5" is wrong.** Art 03 §9.4 has Beat 0 / Beat 1 / Beats 2–3 / Beat 4 / Close Month (§9.4.4). Highest numbered beat is Beat 4. No Beat 5 exists.
- **"Phase B" stale terminology.** Beat 4 step uses "Phase B declaration" — Art 03 never uses Phase A/B/C. Canonical term: §9.2 Public Declaration.
- **"Auto-fail" is incorrect for zero-payment cards.** Art 03 §9.4.3.1.0.3: zero payment → ARBITER announces invalid → card flipped face-down → advance directly to Step 4 (cleanup). The fail outcome steps are also skipped. Not "auto-fail" — the card simply doesn't resolve.

### Entirely absent sections (major gaps)
- §9.0 Start of Month (PA obligation check)
- §9.4.0 Beat 0 — grid-building procedure (the most referenced beat in card specs)
- §9.4.1 Beat 1 — Read Board State / SitRep / BEC application
- §9.4.2 Beats 2–3 step sequence (covert resolution loop, sub-case structure)
- §9.4.4 Close Month
- §7 Upkeep (8 sub-sections: initiative, SitRep, deployment conversion, resource collection, ops prep)
- §8 Placement
- §12 Quarter Close (Findings Decay, Debrief Reward, NS-xx return, Session Timeline advance)
- §14 Apex Activation (4-step subroutine; called from both covert and public resolution)
- §15 Duration Taxonomy (Immediate/Transient/Seasonal/Permanent with exact cleared behaviors)
- §17 Countermeasure Card Rules (6 rules including carry-forward, removal-on-use, full CM-A/CM-B ruleset)

### Missing rules within covered sections
- Beat 4: BEC Modifiers step (§9.4.3.1.3) absent from Beat 4 sequence
- Beat 4: Faction Threshold Slider / initiative loop mechanic absent
- Beat 4: VM-xx (Visibility Marker) check at §9.4.3.1.0 absent
- §9.3 CM Window: carry-forward rule (unused CMs carry to next Monthly window) absent
- §10 Battlefield Strength: PS marker penalty on winner (−1 PS from Battlefield win per §10.1.4.0) absent
- §13.5 Intel Token age: Expired = partial payment rule absent (ref covers Fresh/Stale/Expired tiers but not the partial payment consequence)

### Stale/incorrect details
- CM matching at "Beat 0 (§9.4.0.1)": placement at Beat 0 is correct; processing (application) is Beat 1. Ref conflates the two.
- Beat 4 step numbering is editorial summary — doesn't match Art 03's canonical step labels (§9.4.3.x).
- Battlefield Strength triggered "after Beat 5" — wrong; triggers after Month 3 §9.4.4 Close Month.

---

## design_reference_card_system.md — COMPLETE

### Critical errors (fix first)
- **`CardType` enum:** Ref says `PublicAct`; source §6.3 says `PoliticalAct`. Wrong enum value.
- **`resolution_type` field:** Missing from Metadata field table entirely. Present only in prose note. Type is `str | None`, feeds 00c §8.
- **16-row design checklist absent.** The ref's 13-item "Design Flags" list is a pre-design gate, not the §5 checklist. All 16 rows (with pass criteria) are missing. Most critical absent row: Outcome determinacy (P27 — no `game.choose_one()`, each tier resolves to exactly one outcome).
- **P27 entirely absent** — hard constraint prohibiting conditional branching within resolution tiers. Corresponds to missing checklist row.

### Missing enums (7 of 14 §6.3 vocabularies absent from ref)
- `Ring`: 0 (Chorus Node) | 1 (Core) | 2 (The Mid) | 3 (Baryo)
- `PentagramRelation`: Neighbor | Opposed
- `OutcomeType`: Binary | ElectPlayer | ElectDistrict | ElectFaction | BilateralAgreement | Unilateral ← only ElectPlayer mentioned in ref
- `PSFramingType`: probabilistic | fixed
- `PSFramingTrigger`: resolution | discovery | placement
- `PSTarget`: acting | target | both
- `BoostExpr`: composite expression (ARBITER detection at Beat 0, BM-xx placement, exact-multiple submission, threshold-scaling rules)

### Missing class definitions
- **`PSFraming` class** (6 fields: type, trigger, ps_target, threshold, on_success, on_fail) — entirely absent. Required to write any card with a PS effect.
- **`PSShift` class** (faction, delta) — entirely absent.

### Missing design principles (absent from ref)
P1 (one primary layer) · P2 (faction cards fill gaps not duplicate) · P3 (layer = system affected not physical verb) · P4 (Protect belongs to target layer) · P7 (faction exclusivity two-test: mechanical AND narrative) · P8 (perspective count: standard=5 voices, faction-specific=3) · P10 (narrative consistency with Art 00) · P11 (Portrait fires on action not outcome) · P12 (ARBITER sole mover of Portrait — no card Effect field may state direct Portrait shift) · P13 (flat Portrait prohibited on standard cards) · P14 (card entries contain only card-specific info) · P15 (cost equitable to success effect) · P17 (faction-native capabilities have accessible standard equivalents) · P22 (Portrait values are card properties, printed not computed) · P27 (outcome determinacy)

### Missing structural content
- Design Rationale block structure (5-part: role, cost/reward, resolution rationale, restriction/affinity rationale, paired card relationship)
- Card Story block structure (named section; 1–3 sentences; separate from Design Rationale)
- Status table format and gate conventions (Design Pass gate = all 16 rows; Issues Resolved; Signed off with session number)
- §6.4 Visibility Rules (VS-01/VS-04/VS-06 — visibility field encoding)
- §6.5 Modifier Baselines (ring_mod: −15/−10/0/+10; doctrine_mod: Neighbor +15 / Opposed −15)
- §5a Faction Playstyle Reference (faction goals, path to victory axes, per-faction summaries)

### PortraitEntry gaps
- `flat` restriction not noted: "faction-specific cards only (L131)"
- PortraitEntry field types not documented

### Header staleness
- Ref header says "Updated: S95" but body contains S108 content. Maintenance gap.

---
*Overnight batch (2:07am June 23): ref_card_types.md · ref_design_pillars.md · ref_resources.md · ref_board_narrative.md · ref_world_narrative.md · ref_taxonomy.md → results written to ref_audit_overnight_results.md*
