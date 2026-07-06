# CA/PA Design Review — Working Notes

Working doc for PM05 **09-16 step 2** (design review pass), CA/PA phase. Delete once this content is migrated into card entries / PM02 / PM05 (per Whiteboard convention — scratch, not canonical).

**Plan (Andy, S140):** separate session for CA review, separate session for PA review — don't try to do both (or all of CA) in one sitting. This file is what the next session reads to pick up where S140 left off.

---

## 1. Why this review is happening now, and in this order

`09-16` step 2 (design review pass) already closed for all three Modifier subclasses (ModAction S139, ModBattle S140, ModReact S138) — see PM02 L267–L269. CA/PA is the remaining step-2 scope: "the non-modifier action-space."

**Sequencing decision (PM02 L273, S140):** CA/PA review runs *before* finishing the remaining item-#3 whole-set schema decisions (04-n178 cost/value_rating model, `schema_cleanup_log.md` #2 stack behavior, #5 firing-window overlap). Reasoning: the modifier-card review pass kept surfacing schema-level findings as it went (04-n177 scaffolding gaps, the outcome_type/acquisition/generating_card corpus-wide gap, the Overture taxonomy correction) — deciding the whole-set schema items before CA/PA review has had its say would be premature. Do CA/PA first; let it feed the schema decisions, not the other way around.

---

## 2. The standard: re-derive, don't trust

This is the load-bearing instruction for this whole pass. Memory: `feedback_design_review_verification.md` (reinforced hard at S140 — read it before starting).

**Do not treat any of the following as ground truth without checking it directly:**
- A checklist row marked ✓
- `design_pass=1` / `structure_pass=1` in `card_status`
- A "Signed off ✓ S(n)" in the Status table
- A cross-card comparison in the card's own Design Rationale ("unlike GD-01," "matches Redline's pattern," "no standard card duplicates it") — **open the other card and check.** This caught a factually-backwards claim on STD.MOD.1 Overture (S140).
- A taxonomy assignment as stated — **verify against `Whiteboard/ref_taxonomy.md` directly**, not the card's own assertion.
- Freshly-written content from earlier in the same session. Andy explicitly asked "do the other 7 need the same scrutiny" after 7 fossil cards were authored fresh in S140 — they did; audit found a real gap (see §4 below).

**What re-deriving does NOT mean:** don't re-prose every row of every card from scratch. Verify each row against source; only rewrite the ones that fail. 114 cards' worth of unnecessary rewriting is not the goal — 114 cards' worth of *checked* claims is.

---

## 3. Concrete lookfor list (proven to find real defects this session)

Check these, in this order, on every card:

1. **Status-row internal consistency.** Does "Signed off ✓ S(n)" coexist with a blank Design Pass or open (⚠) checklist rows? That's a fast contradiction signal — but not automatically a bug: if the sign-off predates a tracking item like 04-n70 (data schema sweep) or 04-n79 (card narrative sweep) even existing as a concept, the ⚠ rows may just be later-added flags, not evidence the sign-off itself was premature. Note which case it is; don't assume either way.
2. **Checklist format completeness.** Count the rows present against the canonical 17-row Art 04 §5 list (Action fit → Resource cost positioning — see Part1_Core.md ~line 263). CA/PA do **not** get the 5-row ModReactCard addendum (Trigger frequency/Firing window/Automatic vs d100/Stack behavior/Ring constraint) — that's ModReactCard-only. An old card (S60s-vintage, like the Standard CA set) may be missing rows entirely, the way STD.MOD.1 Overture was missing 10 of 22 before this session caught it.
3. **Cross-card precedent claims** — open the cited card, confirm the comparison holds.
4. **Taxonomy** — check Layer/Function/Subject against `ref_taxonomy.md` §5.1 (verb definitions) and §5.2 (subject vocabulary) directly. Watch especially for verb ambiguity (e.g. Remove vs. Corrupt — "component exits play" vs. "a recorded value is altered" are genuinely different things; don't default to whichever verb avoids taxonomy overlap with a sibling card, that reasoning doesn't actually settle anything per 04-n158's own logic).
5. **✓ marks vs. actual field state** — Voice fit ✓ with `perspectives={}`/empty is wrong (should be ⚠); Data schema validation ✓ with required fields simply absent from the code block is wrong.

---

## 4. Schema scope for CA/PA specifically — don't chase the modifier-card gaps here

Confirmed by reading Part1_Core.md §6.1 directly this session:

- `CovertOperation` and `PublicAct` are **`CardType` enum values on the base `Card` class**, not separate subclasses (unlike `ModActionCard`/`ModBattleCard`/`ModReactCard`, which each have their own `class X(Card):` block with extra fields).
- **`acquisition`, `generating_card`, `value_rating`, `ring_constraint`, `ring_origin` are Modifier-subclass-only fields** (defined only inside the `ModActionCard`/`ModBattleCard`/`ModReactCard` class blocks, ~Part1_Core.md lines 513–544). They are **correctly absent** on CA/PA cards — do not add them. (This is the opposite instinct from the modifier-card fossil work, where those fields WERE required — don't carry that muscle memory over blindly.)
- **`ps_framing` and `boost`** are base-`Card`-class fields (§6.1) and are the already-tracked 04-n177 gap ("easy to miss required fields... omitting them is a schema error") — expect them to be commonly absent on older CA/PA cards too. Confirmed absent on STD.CA.1. Not a new finding when you hit it again; just note and scaffold (`= None`) same as the modifier-card fix.
- **`outcome_type`** is a base-`Card`-class field, confirmed present and correctly `None` on the Standard CA cards checked so far (STD.CA.1/13/14/15). Per §6.2's data dictionary: `outcome_type | Metadata | OutcomeType | Public act resolution process type; None for covert operations`. **This means every PublicAct card should carry a real, non-None `OutcomeType` value** — this is the single highest-yield schema check to run once the PA batch starts. **Look up the `OutcomeType` enum definition (Part1_Core.md) before starting the PA session** and verify each PA sets it correctly; this was flagged by the advisor as the most likely place an old card silently gets it wrong, and hasn't been checked yet.
- `is_unique` / `deck_limit` are Pool-level metadata scoped to Operative/Apex cards per their own field definitions — their absence on ordinary CA/PA cards is expected, not a gap.

---

## 5. STD.CA.1 (Build Structure) — pattern-setter review, SCAFFOLDED S141 (scope corrected: scaffold + flag, not fix)

Read in full (`V1/04___Card_System___Part2_Standard.md` lines 29–116). This is the oldest CA card in the system (Guild-affinity territorial-foundation card, signed off S63) — picked as the pattern-setter specifically because "oldest/most legacy" is where stale format is most likely to surface (same logic that made Overture worth checking).

**Scope correction (Andy, S141):** this review pass scaffolds missing checklist rows and flags issues found — it does not resolve or redesign anything in place. Schema/data findings (like the cost bug below) get logged to `Whiteboard/schema_cleanup_log.md`, not fixed here. See `feedback_review_pass_scope.md`.

**Confirmed real defect — flagged in schema_cleanup_log.md #22, NOT fixed in file:**
- `cost = resource.faction(acting) * 1 + resource.district(native) * 1` — the first term has **no resource-type attribute**. Design Rationale states "dual cost (1 faction native + 1 district native)"; every other cost expression in the corpus specifies a type (compare STD.CA.13: `resource.faction(acting).native * 2`). Likely correction: `resource.faction(acting).native * 1` — left as a flag on the card's new "Resource cost positioning" row and in the whiteboard log, pending a later fix pass.

**Sign-off row question — resolved, not a contradiction:**
- Status row: `Design Pass` blank → now ✓ (checklist scaffolding complete), `Issues Resolved ✓`, `Signed off ✓ S63` — 2 rows (`Data schema validation`, `Card narrative`) still ⚠. Checked: 04-n69/70 (Data schema validation row) landed S94–95; 04-n78/79 (Card narrative row) landed S94. S63 predates both by ~30 sessions — the ⚠ rows are tracking concepts that didn't exist at sign-off time, not evidence the sign-off was premature. No further action; not a genuine process gap.

**Confirmed correct on direct check — no action needed:**
- Territory/Add/StructureBlock taxonomy verifies directly against `ref_taxonomy.md` §5.2 ("Structure Block | Territory").
- Missing `ps_framing`/`boost` — expected, per §4 above (04-n177 scope), not new.

**Scaffolded this pass:** Added the two entirely-missing checklist rows — `Outcome determinacy` (✓, Automatic/single deterministic outcome) and `Resource cost positioning` (⚠, flagged per the cost bug above, tier assessment blocked until fixed).

**Not yet checked:** the Guild affinity clause's `cost.resource.district(native) = 0` uses flat assignment (`=`) rather than the delta style (`-=`/`+=`) seen elsewhere (e.g. STD.CA.13's `threshold += 10`). May be stylistic, may be worth normalizing — low priority, noted for completeness, not a blocker.

**Checklist format confirmed (S141):** CA/PA = plain 17-row Art 04 §5 list, no ModReactCard addendum — confirmed by direct read of §5. **Pattern locked for replication across the rest of the Standard CA set:** scaffold missing rows, flag issues (don't fix), log schema findings to `schema_cleanup_log.md`.

---

## 5a. Standard CA set (STD.CA.1–16) — SCAFFOLDED S141, batch complete

All 16 Standard CA cards now carry the full 17-row checklist (Outcome determinacy + Resource cost positioning added where missing — was 15/17 on all of them) and `Design Pass ✓` in both the .md Status table and `card_status` DB. No content was rewritten; issues found were flagged in place and/or logged to `schema_cleanup_log.md`.

**Findings, in addition to STD.CA.1's cost bug (§5 above):**
- **Same cost-typing gap on STD.CA.2/3/4 and STD.CA.5** — `resource.faction(acting)` missing a resource-type attribute, identical shape to STD.CA.1. Confirmed corpus-wide across CA.1–5 only; CA.6–16 are all correctly typed (`.exposure`, `.capital`, `.mandate`, `.native`). Logged: schema_cleanup_log.md #22 (expanded).
- **STD.CA.12 Absolute Compromise** costs `IntelToken(any) * 1` — a second confirmed instance of the open "Intel Token as fungible cost?" question (first was DIR.MOD.9). Logged: schema_cleanup_log.md #10 (expanded).
- **STD.CA.10 Protect** — Status shows `Issues Resolved ✓` while its own Outstanding Issues section lists a real, undefined Art 03 procedural gap (threshold-reduction marker placement). Unlike CA.1's ⚠ rows, this doesn't predate any tracking concept — it's a live inconsistency in the same authoring era. Flagged in the card itself; status flag left as-is (not resolved).
- **STD.CA.13–16 header/variable format** (already noted in §6 below) — old-style `### STANDARD — [NAME]` headers and `C_*` Python variable names instead of `### STD.CA.n —` / `STD.CA.n =`. Not touched this pass (would be a normalization edit, not scaffolding); still a low-stakes fix-in-place candidate for a future sweep.
- **card_status DB note:** STD.CA.12's DB `issues_resolved=1` doesn't match the .md Status table's blank Issues Resolved cell (left blank this pass since a new issue — the IntelToken cost flag — was surfaced). Pre-existing MD/DB drift, not introduced this session; not reconciled, just noted.

**Outcome determinacy:** clean across all 16 — no card uses `game.choose_one()` or conditional player choice in any resolution tier.

**Resource cost positioning:** mono-resource on most of the set (Capital, Exposure, Mandate, or native, each single-typed); STD.CA.1/11 use genuine cross-faction-resource (dual-typed) costs; STD.CA.8 flagged as mono-resource paired with the highest Standard-CA cost (P28's explicit watch case, not confirmed as a mismatch).

---

## 5b. Re-derivation pass (S141) — the pre-existing 15 rows, not just the 2 scaffolded ones

Andy's correction: the standing "re-derive, don't trust" instruction (§2 above) wasn't retired by the scaffold-vs-fix scope split — it still applies to the whole pass. §5/5a above only checked the 2 newly-added rows plus whatever surfaced incidentally. This section covers direct re-verification of the pre-existing 15 rows against source, across all 16 Standard CA cards, done via cross-cutting batch checks rather than card-by-card prose review (more efficient, equally direct):

- **Taxonomy fit:** checked `v_card_mechanical_alignment` (DB) — all 16 show `Legalized` or the expected `Abstract Function` flag on Modify/Protect/Block cards (CA.6/7/10/12), which `ref_taxonomy.md`'s own gap-pattern table documents as "known design gap — not a card error." Also checked all 16 against the Layer × Function Validity Matrix (`ref_taxonomy.md` §Layer×Function) directly — every assignment is in a valid cell. STD.CA.5's Information/Add/IntelToken is literally the worked example in `ref_taxonomy.md`'s own Construction Logic rule 2. **All 16 confirmed clean, no mis-assignments.**
- **Portrait validity:** grepped all `PortraitEntry(...)` calls in the CA section — every single one uses `submitter=` only; zero uses `flat=` (the target-faction-flat pattern flagged as an open question elsewhere, schema_cleanup_log #7, doesn't recur here). Also grepped for direct `.portrait` mutation in effect fields — zero hits, confirming "no direct Portrait track shift in effect fields" holds across the whole set.
- **Card type fit:** grepped `type=/subtype=/faction=` fields — all 16 are `CovertOperation, Standard, All`, matching every card's claim.
- **Cross-card/math claims:** spot-checked ~8 (CA.5/8 Ghost/Syndicate effective-threshold arithmetic, CA.9's stacked Neighbor+Syndicate threshold, CA.4's "same dual cost as CA.3," CA.8's "+2 presence, superior to CA.3's +1," CA.10's −45/−25 protection split) — all checked out exactly against the code.
- **Doctrine alignment / Voice fit:** cross-checked the five factions' recurring doctrinal claims (Guild=permanence/builders, Network=transparency/broadcasters, Syndicate=capital/positioning, Directorate=institutional control, Ghost=epistemic caution) against Art 00 §7.2–7.6 directly (not just internal-corpus consistency) — broadly consistent.

**One substantive open question surfaced, not resolved:** Art 00 §7.5 states plainly: *"The Guild is also the only faction at The Table that cannot operate covertly. Planetary-scale infrastructure cannot be classified. To build the response is to expose it."* Yet Guild has full `faction=All` access to every Standard CovertOperation card, including several where the acting faction's identity is genuinely hidden (not just "intent" — STD.CA.9 Fund is an anonymous transfer; STD.CA.11 Tort Interference is filed with "neither party knows who filed it"; STD.CA.14/15/16 are blind, unattributed draws). STD.CA.1's own rationale resolves this for itself specifically ("construction is publicly visible — the covert element is intent, not the act"), but that reconciliation isn't stated as a general rule anywhere, and doesn't obviously extend to the identity-hidden cards. Art 00 §13 ("no engagement [with doctrine] is required... a player who acts against their stated doctrine simply produces a Chronicle that reflects the contradiction") suggests this may be intentional — doctrine is narrative flavor a player can act against, not a mechanical restriction — which would mean this isn't a bug at all. Not resolved either way this pass; flagging for Andy's read given Design Pillar 6's narrative-precedence standard. Applies to the CA set broadly, not one card — worth keeping in mind through Directorate/Ghost/Guild/Network/Syndicate CA review too.

**Andy's read (S141):** Confirms the mechanism — Portrait likely captures this already. A faction submitting a card that runs against its own doctrine (e.g. Guild playing a genuinely identity-hidden covert card) would be expected to carry `submitter=-1` for that faction on the card's portrait entry, the same way STD.CA.2/STD.CA.4 already give Guild `submitter=-1` for demolition/undermining (against Guild's "we build, we do not unmake" doctrine).

**Checked against the 5 identity-hidden cards this framing was raised about (already have the data from this pass):**
- **STD.CA.15/CA.16** — Guild already carries `submitter=-1` (rationale given: "taking what others gathered/built conflicts with earned-value principle"). Consistent with the off-doctrine-penalty framing, though the stated reason is about *acquisition-from-others*, not *identity concealment* specifically — plausibly the same doctrinal violation read two ways, not confirmed as such.
- **STD.CA.9 Fund** — no Guild portrait entry at all.
- **STD.CA.14 Disprove** — no Guild portrait entry at all.
- **STD.CA.11 Tort Interference** — `portrait = {}`, no faction has an entry (Standard-all-access, no doctrinal signal captured for anyone, not just Guild).

So the mechanism only actually covers 2 of the 5 cards that prompted the question. Whether CA.9/CA.11/CA.14's Guild-silence is itself fine (per Design Rationale's own absence-justification convention — e.g. "no doctrinal stake" reasoning already used elsewhere) or is a gap this framing exposes, is Andy's call — not re-resolved here, just laid out with the concrete data.

**Andy (S141): might be a gap across the whole card corpus**, not just these 3 — logged as its own open category: `schema_cleanup_log.md` #23. Watch for more "faction acting against its own doctrine, no portrait entry present" instances through the rest of the CA/PA review (Directorate onward) rather than deciding this from the 3 Standard-set candidates alone.

---

## 5c. Directorate CA set (DIR.CA.1–8) — SCAFFOLDED + RE-DERIVED S141

Andy's follow-up instruction before starting Directorate: load full reference context (components, procedures, narrative/world, resources, card types, design pillars) so checklist rows can actually be checked against source, not just taxonomy/portrait. Loaded: `ref_components.md`, `ref_procedures.md`, `ref_card_types.md`, `ref_resources.md`, `ref_world_narrative.md`, `ref_board_narrative.md`, `ref_special_district_and_ring_rules.md`, `design_reference.md`, `design_reference_card_system.md` (full Art 04 §6 schema + governing rules). This paid off immediately — several concrete findings below wouldn't have surfaced from taxonomy/portrait checks alone.

All 8 cards (DIR.CA.1–8) scaffolded (Outcome determinacy + Resource cost positioning, all 8 were missing both) and Design Pass ✓ set in `.md` + DB. Nothing fixed — findings logged to `schema_cleanup_log.md` per scope.

**New findings this batch (all logged to schema_cleanup_log.md):**
- **#22 (cost-typing bug) extends beyond Standard:** DIR.CA.5 Sanctioned Raid has the identical untyped `resource.faction(acting) * 1` in both `cost` and `boost` — 6th confirmed instance, first outside the Standard set.
- **#25 (new):** `function = Move` on DIR.CA.2/DIR.CA.4 isn't a valid Function per `ref_taxonomy.md`'s Function Vocabulary (Move is a physical-verb primitive, not a Function — Redirect/Shift are the Functions built on it). DIR.CA.2's own note says this was a deliberate S107 "correction" from the valid `Remove` — a real regression, not fresh drift. Third instance found in Part4d_Network, out of scope this session.
- **#10 (Intel Token as cost) — third instance:** DIR.CA.5's cost includes an IntelToken component alongside typed resources.
- **#26 (new):** DIR.CA.6/7's `game.active_permanents(faction=, ring=)` mechanism — grepped the whole corpus, found nowhere else. Their own "existing permanent card procedure" claim doesn't hold up; this reads as new ARBITER-facing behavior never formalized as a general Art 03/07 procedure (Governing Rule 6.1 / Design Pillar 4.7b territory).
- **#27 (new):** DIR.CA.8's subject `Difficulty` is DB-flagged `Non-component Subject` — a genuine registration gap, distinct from the expected/known "Abstract Function" pattern its Modify/Block/Protect siblings correctly show.
- **DIR.CA.7 checklist prose** still says "PublicStanding" (retired term, corrected S126) though the code already correctly uses `StandingMarker` — flagged in place, not edited.
- **Missing required fields:** DIR.CA.1–4 (oldest, "S59 scaffold") omit `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely; DIR.CA.5–8 (S79/S106) declare `doctrine_mod=None` but still omit `card_id`/`boost`/`ps_framing`. Same vintage-correlates-with-drift shape as the rest of the corpus (schema_cleanup_log #20A) — not a new category, folded into #24.

**Confirmed clean:** no `game.choose_one()` anywhere in the section; all portrait entries use `submitter=` only (no `flat=`); IntelDeliverySlip usage on DIR.CA.3 matches `ref_components.md`'s own description exactly.

---

## 5d. Ghost CA set (GHO.CA.1–15, + Backdate/Field Verification) — SCAFFOLDED + RE-DERIVED S141

15 active cards (GHO.CA.1–15 per `card_status`) plus 2 explicitly-BLOCKED, no-ID stub concepts (Backdate, Field Verification — GR 7.2b, already thoroughly self-documented, reviewed for consistency only, no new issues, not part of active scope). This set is noticeably more mature than Standard/Directorate — several cards already carry real `Data schema validation ✓ 04-n70 ✅ S95` content instead of the generic placeholder, and Card Story blocks are frequently already written.

**Scaffolded:** GHO.CA.1–12 (the 12 non-stub cards) were all missing Outcome determinacy + Resource cost positioning — added, Design Pass ✓ set in `.md` + DB. GHO.CA.13–15 (stubs) already carried the full blank 17-row skeleton — no row-scaffolding needed, left as stubs (not Design-Pass-ready).

**New findings (all logged to schema_cleanup_log.md):**
- **#10 (Intel Token as cost) — massively strengthened:** 5 new instances in this one faction's CA set alone (GHO.CA.2/6/9/10/11), bringing the corpus total to 8. GHO.CA.9/10 pay in IntelToken *alone*, no fungible resource at all — the starkest form yet. This looks less like scattered drift and more like Ghost's actual design intent (Intel Token as real currency) outrunning the schema's fungible-resources-only cost definition.
- **#27 (unregistered Subject) — second instance:** GHO.CA.15's `subject = TargetProfile` is also DB-flagged `Non-component Subject`, alongside DIR.CA.8's "Difficulty." Unlike Difficulty, TargetProfile is a well-established component elsewhere (DB:48) — this reads as a pure `card_subject_map` registration gap.
- **#28 (new):** GHO.CA.8 Full Take implements a variable-cost/boost mechanic with a bare undeclared `n` instead of the schema's actual `boost` field — DIR.CA.5 (reviewed same session) shows the correct pattern for the identical shape.
- **#29 (new):** GHO.CA.13/14/15 (all stubs) have bare string-literal `success` fields — same defect shape as the already-closed 04-n174 fossil sweep, but new instances that sweep didn't cover. All three are also missing nearly every base-Card field.
- **GHO.CA.11 Signals Analysis:** still shows `id=TBD` in its own spec despite `card_status` having assigned it `GHO.CA.11` — DB assignment never written back. Also functionally BLOCKED (same as Backdate/Field Verification per its own Outstanding Issues) but doesn't carry their "🚫 BLOCKED" header/Status treatment — inconsistent handling of the same category. One of its self-flagged Outstanding Issues (ClassifiedDirective component registration) is actually already resolved — DB confirms `Legalized` — noted so it isn't re-litigated as open.

**Confirmed clean:** no `game.choose_one()`, no `flat=` portrait entries, no untyped-cost-attribute bug (schema_cleanup_log #22) anywhere in this set.

---

## 5e. Guild CA set (GUI.CA.1–10) — SCAFFOLDED + RE-DERIVED S141

10 cards (GUI.CA.1–10 per `card_status`). GUI.CA.1–6, 9, 10 scaffolded (Outcome determinacy + Resource cost positioning); GUI.CA.7/8 are stubs with the full blank 17-row skeleton already present, so only flagged, not scaffolded — same treatment as the Ghost stub batch. Design Pass ✓ set (.md + DB) for the 8 non-stub cards.

**New findings (all logged to schema_cleanup_log.md):**
- **#25 extended:** GUI.CA.4's `function = RemoveRestriction` isn't in the Function Vocabulary either — a second invalid Function value alongside `Move`, same underlying category (author reaching outside the confirmed 10-value list). 4 confirmed invalid-Function instances total now.
- **#27 extended:** GUI.CA.9's `subject = Difficulty` is the *second* card using that exact unregistered subject (after DIR.CA.8) — both are threshold/difficulty-modifying cards, suggesting "Difficulty" is a real recurring concept needing a `card_subject_map` home, not one-off drift.
- **#29 extended:** GUI.CA.7/8 (both stubs) have the same bare string-literal `success` field defect as GHO.CA.13/14/15 — now 5 instances, all on stub-marked cards. Looks like a property of the stub-authoring convention itself, not scattered lapses.
- **New (#30):** GUI.CA.10's code has correct, valid Territory/Add/StructureBlock taxonomy, but `card_status` (DB) shows all three fields `NULL` — a DB/MD sync gap, not a card defect. Worth a quick DB sweep for other silently-desynced cards at some point.
- **GUI.CA.9 Works Guarantee** introduces `target_ca = ca.guild.beat3.d100` — a targeting field not in the documented Targeting field group (`target_district`/`target_faction`/`target_object`/`target_taxonomy`/`declared_params`). Card's own checklist already flags its "double-fire" *procedure* as new/unconfirmed; this is a companion finding about the *field* itself — whether it needs schema confirmation or should route through the existing `declared_params` mechanism instead.
- **GUI.CA.6 Labor Contract** is missing `persistence`/`persistence_condition`/`persistence_effect` entirely — not just unset, absent from the code block, unlike every sibling card in this set.

**Confirmed clean:** no `game.choose_one()`, no `flat=` portrait entries, no untyped-cost-attribute bug (#22) anywhere in this set.

---

## 5f. Network CA set (NET.CA.1–8) — SCAFFOLDED + RE-DERIVED S141

8 cards (NET.CA.1–8 per `card_status`). NET.CA.1–7 scaffolded (Outcome determinacy + Resource cost positioning, all 7 missing both); NET.CA.8 is a stub with the full blank 17-row skeleton already present — flagged only, not scaffolded, same treatment as the other factions' stub cards. Design Pass ✓ set (.md + DB) for the 7 non-stub cards.

**New findings (all logged to schema_cleanup_log.md):**
- **#25 confirmed directly:** NET.CA.8's `function = Move` is the third confirmed invalid-Function instance — this one was anticipated from a corpus grep during the Directorate pass, now confirmed by direct card review.
- **New (#31):** NET.CA.4 Network Cascade's Design Rationale *and* Balance row both independently state "Exposure×2," but the code's actual cost is Exposure×1 + Findings×1. Unlike the stale-prose findings elsewhere (DIR.CA.7/NET.CA.7's "PublicStanding," where the code was right and the label was outdated), here two independent prose locations agree with each other and disagree with the code — genuinely unclear which is correct, not just an annotation lag.
- **NET.CA.7 checklist prose** also says "PublicStanding" (retired term) while the code already correctly uses `StandingMarker` — second occurrence of the exact DIR.CA.7 pattern, flagged not corrected.
- **NET.CA.4** also uses a legacy `C06` sequential-number variable reference to STD.CA.6 — same low-priority non-material notation gap already flagged on GUI.CA.2.

**Confirmed clean:** no `game.choose_one()` in any live card spec (one *mention* of it exists, in a historical note explaining why NET.CA.3's predecessor was retired and split — a prior violation that was already caught and fixed, not a live one); no `flat=` portrait entries; no untyped-cost-attribute bug (#22) anywhere in this set.

---

## 5g. Syndicate CA set (SYN.CA.1–12) — SCAFFOLDED + RE-DERIVED S141 — richest findings batch this session

12 cards (SYN.CA.1–12 per `card_status`). Also present in this section: "The Fixer" (Accord Leverage, placeholder name) — a `ModReactCard`, not a CovertOperation, already flagged for redesign (04-n158) and correctly excluded from `card_status`'s CA numbering; not touched, out of scope.

**Scaffolded:** SYN.CA.1–9 were all missing Outcome determinacy + Resource cost positioning (added). SYN.CA.10/11 already had both rows physically present but Resource cost positioning was filled with raw template text, not a real assessment (see #33 below) — corrected as scaffolding; SYN.CA.10 was also missing a Trigger validity row entirely. SYN.CA.12 is a stub with the full blank skeleton — flagged only. Design Pass ✓ set (.md + DB) for the 11 non-stub cards.

**New findings — this batch surfaced more than any prior faction, several extending existing items substantially:**
- **#31 quadrupled:** SYN.CA.3 ("Capital×5" prose vs. Capital×3+Findings+Exposure code), SYN.CA.5 ("Capital×3" vs. Capital×2+Exposure), and SYN.CA.9 ("Capital×4+Intel" vs. Capital×3+Mandate×2, no Intel in cost at all) all show the same prose-overstates-pure-resource-amount pattern as NET.CA.4. Four independent cards now — this reads like a systematic authoring habit, not scattered typos.
- **#10 (Intel Token as cost) — 9th instance:** SYN.CA.7, cost is IntelToken alone.
- **#7 (Portrait flat on non-agentive factions) — massively strengthened:** 4 new confirmed instances in one faction (SYN.CA.7/10/11/12), all using `flat=` for the *submitter's own* entry where `submitter=` seems to be the semantically correct field — a different angle on item #7 than the original target-faction question. SYN.CA.10/11 also apply `flat=-1` to Network/Directorate, who never acted at all.
- **#22 extended — a third cost-notation style found:** SYN.CA.10/11/12 all use bare `Capital(n)`/`Mandate(n)` (no `resource.faction()` wrapper, no explicit faction binding) — distinct from both the majority dotted-notation and the bare-IntelToken notation already tracked.
- **New (#33):** SYN.CA.10/11's "Resource cost positioning" rows existed but contained the raw guidance template question verbatim, no real assessment — a checklist-completeness failure mode distinct from a missing row. Grepped the corpus for the same template string: one more hit, **GHO.PA.5** (Ghost PA, out of scope — flagged for the PA session).
- **SYN.CA.4's design_note** has a dangling "Cost reasoning: Exposure and Findings..." sentence that doesn't match its actual Capital-only cost — likely a copy-paste fragment from a different card, never corrected.
- **SYN.CA.6** is missing `fail`/`failcrit` fields entirely (not `None` — undeclared), the only card in the set with this gap.
- **SYN.CA.1's `boost` field and SYN.CA.7's `on_accept`/`on_decline` (ElectPlayer)** are both used *correctly* — good positive-confirmation examples against the GHO.CA.8 bug (#28) and worth citing as the right pattern.
- Two more legacy sequential-ID references (`C11` on SYN.CA.3) — same low-priority category as GUI.CA.2/NET.CA.4's existing notes.
- Two more unregistered-Subject instances (#27): SYN.CA.5's "NamedActionType" and SYN.CA.12's "AccordForm" — DB-confirmed `Non-component Subject`, bringing that item to 5 total distinct subject strings across 5 cards.

**Confirmed clean:** no untyped-cost-attribute bug (#22's original form) in this set; the one `choose_one` mention is historical (SYN.CA.7's predecessor was split S70 specifically because of a `choose_one` violation — another already-caught-and-fixed prior instance, not live).

**This completes all 5 factions' CA sets** (Standard, Directorate, Ghost, Guild, Network, Syndicate). PA review (Standard + all 5 factions) is a separate session per the original S140 plan — do not start it as a continuation of this one.

---

## 6. Full CA corpus synthesis (S141) — read this before starting PA review

Cross-cutting patterns across all 69 CA cards, visible only now that all 6 sets are done: logged in full as `schema_cleanup_log.md` item **#34**. Headlines:
- Every recurring defect category (invalid Functions, unregistered Subjects, `flat=` misuse, prose/code cost mismatches) is FactionSpecific-only — Standard has none of them.
- The prose/code cost mismatch (#31) clusters on cards with comparative cost framing ("cheaper than X," "vs. Y's cost") — candidate for a targeted grep sweep rather than assuming 4 instances is exhaustive.
- Newer cards (S111+) don't have fewer defects than older ones — they have *different* ones (new notation styles, imprecise Portrait fields) instead of missing fields and wrong taxonomy terms.
- Intel Token as cost (#10, 9 instances) is the strongest single candidate in this whole log for "formalize as a real cost category" rather than "flag every instance."
- Item #23 (doctrine-vs-portrait tension) never got re-checked against Directorate/Ghost/Network/Syndicate's own doctrines — still a 3-card, Standard-only evidence base, not closed.

Read `schema_cleanup_log.md` #34 in full before the PA session — several of its hypotheses (B, C) suggest specific things to grep for early in PA rather than waiting for them to surface card-by-card again.

---

## 5h. Standard PA set (STD.PA.1–8) — SCAFFOLDED + RE-DERIVED S142 — PA phase begins

Andy confirmed PA review scope before starting: identical to CA (scaffold + flag, re-derive, log don't fix). Faction order confirmed: Standard → Directorate → Ghost → Guild → Network → Syndicate, same as CA. Full reference context reloaded before starting (`ref_components.md`, `ref_procedures.md`, `ref_card_types.md`, `ref_resources.md`, `ref_world_narrative.md`, `ref_board_narrative.md`, `ref_special_district_and_ring_rules.md`, `design_reference.md`, `design_reference_card_system.md`) per the S141 lesson — do not start narrow.

All 8 STD.PA cards were missing the same 2 rows as the CA set (Outcome determinacy + Resource cost positioning) — 15/17 on all of them, identical shape to Standard CA. Scaffolded and Design Pass ✓ set (.md + DB) for all 8.

**§4's flagged high-priority check confirmed clean:** every one of the 8 cards carries a real, non-`None` `outcome_type` (7× `Unilateral`, 1× `BilateralAgreement` on STD.PA.8) — no PA in this set silently omits it. This was the single highest-yield check anticipated going into the PA phase; it did not surface a defect here, but is worth re-running on every subsequent faction's PA set rather than assuming it stays clean.

**New findings (all logged to schema_cleanup_log.md):**
- **#22 (untyped cost attribute) massively extended:** all 8/8 Standard PA cards show the identical untyped `resource.faction(acting)` shape — not confined to "old CA.1–5," it's the default convention across the whole PA set regardless of card ID. This breaks the earlier "clusters at the low card-ID end" read and item #34-A's "Standard is clean of all FactionSpecific-only defects" framing, once PA is folded into the CA-only corpus that synthesis was built on.
- **#10 (Intel Token as cost) — 10th instance, first in PA phase:** STD.PA.5 On the Record, paired with a typed resource (not pure), using a 4th distinct cost-notation variant not seen elsewhere in the corpus.
- **New (#35):** Two of STD.PA.1–3's three "public counterpart to STD.CA.n" claims, checked directly per the standing re-derive standard, are **false** — STD.PA.1 claims same cost as STD.CA.3 (actually different resource shape), STD.PA.2 claims same cost + "45 vs 40" threshold vs STD.CA.4 (actual STD.CA.4 threshold is 50, and PA.2's 45 is worse, not better). STD.PA.3's claim against STD.CA.1 checked true. This is the Overture-pattern failure mode recurring in the *Standard* set specifically, undermining #34-A's "Standard is clean" framing further.
- **Retired term "PublicStanding" in checklist prose (item 4-F pattern):** 2 more instances (STD.PA.4, STD.PA.7) — code correctly uses `StandingMarker` in both, prose didn't get swept forward. Now confirmed in Standard, not just Directorate/Network faction sets.

**Confirmed clean:** no `game.choose_one()` in any of the 8 (Outcome determinacy all ✓); no `flat=` portrait entries — all use `submitter=` only; taxonomy (Layer/Function/Subject) checked against `ref_taxonomy.md` and DB `card_status` — all 8 valid, no mis-assignments.

**Not yet checked:** STD.PA.3's design_note references forward to DIR.PA.1 (Regulatory Override) and GUI.PA.1 (Civic Works Mandate) as a cost-prerequisite/counter-play pair — out of scope this pass, worth confirming when Directorate and Guild PA sets are reached.

---

## 5i. Directorate PA set (DIR.PA.1–11) — SCAFFOLDED + RE-DERIVED S142

**Scope correction mid-set (Andy):** scaffolding applies to every card reviewed regardless of content maturity — "Design Review TRUE" means the review work (checklist assessed, spec fields completed) was done, not that the card is clean. Issues Resolved / open ⚠ rows record what was *found*, not whether review happened. This corrected an initial misstep on DIR.PA.7/8 (see below) and now governs the rest of the PA phase.

**11 cards, all scaffolded, all Design Pass ✓ (.md + DB).** STD.PA.3's forward-reference to DIR.PA.1 (raises presence-placement cost, prerequisite gate on Guild's build chain) checked directly against DIR.PA.1's actual code — confirmed accurate.

**"(stub)" label was unreliable — checked directly, not trusted:** 5 of 7 stub-tagged cards (DIR.PA.4/5/9/10/11) turned out to carry complete, schema-conformant content — real S131 redesigns closing specific named PM05 gaps (04-n104 BLOCKED-status fix, 04-n89 win-path gap, 04-n108 PS-card gap, 04-n142 counter-card gap, the 54-card floor). Only DIR.PA.7/8 are genuinely thin (bare prose-string `success`, most fields absent). All 9 non-thin cards got full checklists; DIR.PA.7/8 got full checklists too, assessing what the thin content actually supports rather than a blank template (schema_cleanup_log.md #40).

**Spec-level scaffolding performed this pass (not just checklist):** all 11 cards now carry `card_id`, `boost`, `ps_framing` explicitly (previously silently absent on 6 of 11 — DIR.PA.1/2/3/6/7/8). DIR.PA.7/8 additionally had their full deterministic field set scaffolded (`ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`/targeting fields/`portrait={}`/`narrative`/`perspectives`/`arbiter_note`, all `None` or the deterministic enum match) — `success` itself was left untouched since fixing it is content work, not scaffolding.

**New findings (all logged to schema_cleanup_log.md):**
- **#22 contrast confirmed:** all 11 Directorate PA costs are correctly typed (including two triple/cross-resource costs) — confirms the untyped-cost bug is Standard-specific, not a general corpus habit.
- **#10 (Intel Token as cost) — 11th instance:** DIR.PA.8, a 5th distinct notation variant.
- **#26 (unconfirmed `game.active_permanents` procedure) — 3rd instance:** DIR.PA.9, cross-card claim checked and confirmed true this time (unlike DIR.PA.10's looser version, below).
- **#29 (bare string-literal `success`) — 2 more instances, first in PA phase:** DIR.PA.7, DIR.PA.8.
- **New #36:** dangling "Cost reasoning: [wrong resource]" design_note fragments — DIR.PA.1, DIR.PA.2 (2 more instances alongside SYN.CA.4; DIR.PA.2's fragment names a different card entirely, confirming these are copy-paste artifacts).
- **New #37:** `resolution_type = "Permanent public act"` — not in the confirmed 2-value vocabulary. 3 instances (DIR.PA.5, DIR.PA.6, DIR.PA.11), all Permanent card-as-condition PAs — may be a genuine missing 3rd vocabulary value rather than an error.
- **New #38:** the PA-phase's flagged highest-priority check (`outcome_type` should never be `None` on a real PA) caught 3 confirmed defects here — DIR.PA.10 explicitly `None` despite a fully structured d100 resolution, DIR.PA.7/8 missing the field entirely. Standard PA's clean 8/8 result did not generalize.
- **New #39:** `narrative`/`perspectives` entirely absent (not sparse — explicitly `None`) on all 5 of the S131 mislabeled-stub cluster (DIR.PA.4/5/9/10/11) — uniform across one authoring batch, distinct from the Card-Story-pending placeholder every card carries.
- **New #40:** the "(stub)" mislabeling itself, plus a second DB/MD desync shape — DIR.PA.4/5 showed `design_pass=1` in `card_status` prior to this session despite a fully blank .md Status table (distinct from item #30's NULL-taxonomy desync).
- **DIR.PA.10's cross-card claim** ("same counting mechanism CA.6/CA.7 use for Permanents") checked directly and found **imprecise, not false**: DIR.PA.10 actually counts districts at Established+ tier, not active Permanent cards — a different count than CA.6/7's. Shared property ("no ARBITER judgment call, simple tally") holds; the specific mechanism claim doesn't. Noted as a softer version of the Overture-pattern check.
- **Legacy header/variable-naming pattern extends into Directorate PA:** DIR.PA.3 (`EntryExitControls`) and DIR.PA.6 (`P_StandingInjunction`) both use old-style headers with no card ID and non-standard Python variable names, plus "—" placeholders in the section TOC instead of proper anchors.

**Confirmed clean:** no `game.choose_one()` anywhere in the 9 fully-checkable cards; no `flat=` portrait entries; taxonomy (Layer/Function/Subject) checked against DB and `ref_taxonomy.md` — all 11 valid.

---

## 5j. Ghost PA set (GHO.PA.1–5) — SCAFFOLDED + RE-DERIVED S142

Smallest PA set (5 cards), notably more mature than Standard/Directorate — GHO.PA.3/4/5 already carried real Card Story blocks and "Data schema validation ✓"/"Card narrative ✓" checklist rows instead of the generic placeholders, matching the Ghost CA set's similar maturity noted in §5d.

**All 5 scaffolded, all Design Pass ✓ (.md + DB).** GHO.PA.1/2/3/4 were missing the two universal rows (15-row format, same shape as every other set); GHO.PA.5 already had both rows present but its **Resource cost positioning row contained the raw guidance-template text verbatim** — the second confirmed instance of that exact defect (schema_cleanup_log.md #33), previously flagged for this session back in S141's Syndicate review and now fixed with a real assessment (mono-resource, Findings × 1).

**Spec-level scaffolding:** all 5 cards got `card_id` added (previously absent on all 5, only GHO.PA.5 even mentioned it — as a stray sentence inside its own design_note prose rather than a real field); all 5 got `ps_framing = None` added; GHO.PA.1/2 got `boost = None` added (GHO.PA.3/4/5 already had real `boost` fields).

**New findings (all logged to schema_cleanup_log.md):**
- **#10 (Intel Token as cost) — 2 more instances, 6th notation variant:** GHO.PA.1 (2 tokens, one per target faction, same `intel_token(target=faction(X))` notation as STD.PA.5) and GHO.PA.3 (`boost = intel_token(holder=Ghost, status=Expired)` — a genuinely new `holder=`/`status=` keyed variant). Ghost now accounts for 8 of 13 total corpus instances.
- **#36 (dangling "Cost reasoning" fragment) — important contrast case:** GHO.PA.4 carries the same sentence template as the 3 mismatched instances (SYN.CA.4, DIR.PA.1, DIR.PA.2), but here it's **correct** — Exposure genuinely is part of GHO.PA.4's cost. Confirms the template recurs across a wider authoring habit than previously evidenced, and that each instance still needs a direct check rather than an assumption either way.
- **Extends the DB/MD desync family (schema_cleanup_log.md #40):** GHO.PA.3/4/5 all show `issues_resolved=1` in `card_status` despite fully blank .md Status tables — a third field/shape of the same underlying drift pattern (after DIR.PA.4/5's `design_pass` desync and GUI.CA.10/STD.CA.12's taxonomy desync).
- **#22 contrast holds:** all 5 Ghost PA costs are correctly typed (Findings, and one deliberate cross-faction Findings+Exposure cost on GHO.PA.4) — Ghost joins Directorate as clean on this pattern.

**Notable non-defect:** GHO.PA.4's cost pays partly in Exposure (Network's native resource, not Ghost's) — a deliberate cross-faction cost, explained coherently by its own design_note ("Exposure represents the deliberate unmasking of the threat to the public"). Confirmed intentional, not flagged as an error.

**Confirmed clean:** no `game.choose_one()` across all 5; no `flat=` portrait entries; all `outcome_type` values present and non-`None` (all `Unilateral`) — Ghost passes the PA-phase's flagged highest-priority check cleanly, unlike Directorate; taxonomy checked against DB — all 5 valid.

---

## 5k. Guild PA set (GUI.PA.1–10) — SCAFFOLDED + RE-DERIVED S142

Largest PA set reviewed after Directorate. **6 of 10 cards (GUI.PA.3/4/5/6/7/8) are `*(stub)*`-tagged and genuinely thin** — unlike Directorate's mostly-mislabeled cluster, these really are undeveloped: bare-string effect fields, most base-Card fields absent. Only GUI.PA.1/2/9/10 are fully developed. All 10 scaffolded, all Design Pass ✓ (.md + DB), per the scaffold-all standard now governing this review.

**New sub-variants of the bare-string defect (schema_cleanup_log.md #29, now 12 corpus instances):**
- **GUI.PA.6/GUI.PA.7:** the bare-string shape isn't confined to `success` — both cards' `restriction` field is also a bare string (with English `AND` instead of Python `and`), the first confirmed instance on a non-`success` field.
- **GUI.PA.4:** its `success` string reads as syntactically-valid Python left inside quotes, distinct from the plain-English-prose shape everywhere else — suggests at least two different authoring failure modes produce the same symptom (never structured, vs. structured-then-accidentally-stringified).
- **GUI.PA.3/GUI.PA.8:** both describe a Card-as-Condition standing effect in prose inside `success`, missing the required `persistence_condition`/`persistence_effect` structured fields — same gap as DIR.PA.7 Curfew.

**Other new findings (all logged to schema_cleanup_log.md):**
- **#30 (NULL-taxonomy DB desync) — 2nd confirmed instance:** GUI.PA.10 shows the identical pattern as GUI.CA.10 (valid code, `NULL` in `card_status`) — both confirmed instances are Guild-set cards, worth watching as a possible faction-specific DB sync gap.
- **#36 (dangling "Cost reasoning" fragment) — 4 more correct instances:** GUI.PA.1/3/4/5 all carry the recurring sentence template, all four check out correct against their actual costs. Template now stands at 5 confirmed-correct vs. 3 confirmed-mismatched — a genuine mixed bag, not a reliable defect signal either way.
- **#38 (`outcome_type` gap) — 6 more instances:** the entire thin-stub cluster (GUI.PA.3/4/5/6/7/8) had the field absent, now scaffolded explicit `None`. GUI.PA.1/2/9/10 all pass clean. Confirms the check's yield tracks content maturity, not faction.
- **Duplicated Outstanding Issues bullet on GUI.PA.2:** an identical bullet appeared twice verbatim — deduplicated as mechanical cleanup (not a content decision).
- **Doctrine tension flagged, not resolved:** GUI.PA.6 Asset Transfer's checklist notes a real doctrinal question its design_note doesn't address — giving up a Structure Block (Guild's core permanence asset) for resources cuts against "permanence through building," and nothing in the card's own text reconciles this.

**Confirmed clean:** no `game.choose_one()` on any of the 4 non-stub cards; no `flat=` portrait entries anywhere; taxonomy (Layer/Function/Subject) valid against `ref_taxonomy.md` on all 10 (GUI.PA.5's bare `subject = District` flagged as worth confirming against the registered Subject vocabulary, though not DB-flagged as invalid); GUI.PA.10 notably already carries real `ps_framing` content — the first card in the entire CA/PA review to do so rather than `None`.

---

## 5l. Network PA set (NET.PA.1–6) — SCAFFOLDED + RE-DERIVED S142

**Missed-then-caught finding, corrected retroactively:** NET.PA.1's `resolution_type = "Contested"` prompted a full corpus grep, revealing **9 distinct `resolution_type` values in active use against a documented vocabulary of 2** (schema_cleanup_log.md #41, which supersedes the narrower #37). Critically, this same `"Contested"` value had already passed through the Standard PA review (§5h: STD.PA.2/4/5/6) unflagged — corrected after the fact once the pattern was spotted here. This connects to an already-open PM05 item (04-25, "rationalize resolution_type taxonomy after full card set") whose trigger condition — the full CA+PA corpus being reviewed — is essentially met by this session.

**3 of 6 cards (NET.PA.4/5/6) are `*(stub)*`-tagged and genuinely thin**, matching Guild's pattern rather than Directorate's. NET.PA.3 (Live Coverage) uses a legacy header/TOC-anchor style (no card ID) matching DIR.PA.3/6, but is unusually self-aware — its own Outstanding Issues section already names its missing `card_id`. All 6 scaffolded, all Design Pass ✓ (.md + DB).

**New findings (all logged to schema_cleanup_log.md):**
- **#41 (resolution_type vocabulary sprawl)** — the headline finding this set surfaced; see above.
- **New #43:** NET.PA.5's cost draws partly from the *target* faction's own resource pool (`resource.faction(target_faction).native * 1`), not the acting faction's — a genuinely new schema shape (blurs cost/effect distinction), not just a typing question. Confirmed deliberate per its own design_note, not an authoring slip.
- **#29 (bare-string effects) extended to two more fields:** NET.PA.3's `persistence_condition` and `persistence_effect` (in addition to `restriction`) are all bare strings rather than structured expressions — the first confirmed instance of the defect spreading to persistence fields specifically.
- **#10 (Intel Token as cost) — 14th instance, 7th notation:** NET.PA.1's `intel_token(target=faction(target)).all_held` (spends every held token naming the target, not a fixed count).
- **New cost-notation form:** NET.PA.4's `district_native(target_district)` — a bare function-call style distinct from the corpus's usual `resource.district(native)` wrapper, semantically equivalent but syntactically new.
- **New threshold pattern:** NET.PA.1's `threshold = 30 + (10 * count(...))` is a computed formula rather than a flat int — the first instance of a dynamically-scaling threshold field in the corpus (distinct from ring_mod/doctrine_mod additive modifiers, which are separate fields).

**Confirmed clean:** no `game.choose_one()` on the 3 non-stub cards; no `flat=` portrait entries; taxonomy valid against DB for all 6.

---

## 5m. Syndicate PA set (SYN.PA.1–5) — SCAFFOLDED + RE-DERIVED S142 — final PA set, phase complete

Smallest remaining set. 2 of 5 (SYN.PA.4/5) are genuinely thin stubs; SYN.PA.1/2/3 are fully developed. All 5 scaffolded, all Design Pass ✓ (.md + DB).

**Confirmed a third instance of the raw-template-text defect (schema_cleanup_log.md #33):** SYN.PA.3's Resource cost positioning row contained the guidance template verbatim — fixed with a real assessment (mono-resource, Capital × 1). All 3 sightings of this exact defect (SYN.CA.10/11, GHO.PA.5, SYN.PA.3) are now resolved with real content.

**New findings (all logged to schema_cleanup_log.md):**
- **#7 (`flat=` portrait misuse) — 5th confirmed instance, new angle:** SYN.PA.3 uses `flat=` on all three of its portrait entries, including Syndicate's own — but unlike hypothesis C's "public-effect/covert-actor" framing, this card's actor is fully public (a loud table demand), so the pattern here is purely "flat on the submitter's own entry" plus "flat on factions who only reacted narratively, never acted." Confirms the pattern isn't confined to the covert-actor shape.
- **#22 (untyped/nonstandard cost notation) — 4th instance of the bare `Type(n)` style:** SYN.PA.3's `cost = Capital(1)` matches SYN.CA.10/11/12 exactly — all four instances are Syndicate cards, both CA and PA.
- **New #44:** `persistence = Transient` paired with prose describing an effect lasting "until Quarter+1" — SYN.PA.5 is the second confirmed instance of this tension (after DIR.PA.7), both on thin stubs, both using the identical phrasing. Worth checking whether "Quarter+1" has an established, non-violating meaning before treating this as a genuine rule conflict.
- **Confirmed correct:** SYN.PA.1's `outcome_type = ElectPlayer` is properly structured with `on_accept`/`on_decline` populated and `success`/`successcrit`/`fail`/`failcrit` correctly `None` — a clean positive example of the ElectPlayer pattern.

**Confirmed clean:** no `game.choose_one()` on the 3 non-stub cards; taxonomy valid against DB for all 5; no untyped-cost-attribute bug (#22's original form) anywhere in the set.

---

## PA phase complete — all 45 cards across 6 sets scaffolded and re-derived (S142)

Standard (8) → Directorate (11) → Ghost (5) → Guild (10) → Network (6) → Syndicate (5) = 45 PA cards, matching the CA phase's structure. Full cross-cutting synthesis: `schema_cleanup_log.md` item **#45** (mirrors item #34's treatment of the CA phase). Headlines:
- Item #34-A's "Standard is clean of all defect categories" claim did not survive — Standard PA is 8/8 on the untyped-cost bug and produced 2 of 3 false cross-card claims, both defects the CA-only synthesis had marked Standard-clean.
- `resolution_type` vocabulary sprawl (9 values in use, 2 documented) is the single most consequential finding — it directly triggers an already-open PM05 item (04-25).
- Intel Token as cost grew from 10→14 instances and 4→7 distinct notations across the full corpus — the strongest formalization candidate in the whole log.
- `flat=` portrait misuse stayed genuinely Syndicate-only across all 5 confirmed instances (both CA and PA) — the one pattern that held up as truly faction-specific rather than collapsing under full-corpus scrutiny.
- `card_status` DB/MD desync recurred across 3 factions and 3 different fields this session alone — reads as a systemic sync gap, not isolated incidents.

**114 CA/PA cards total, both phases now fully scaffolded, re-derived, and Design Pass ✓ in .md + DB.** This closes PM05 09-16 step 2's non-modifier action-space scope (see `ca_pa_review_notes.md` §1). Full history: this file §5a–§5m, `schema_cleanup_log.md` items 1–45, PM02 L267–L274+.

---

## 6. Scope inventory (from `card_status`, pulled S140)

```sql
SELECT
  CASE WHEN card_id LIKE '%.CA.%' THEN 'CA' WHEN card_id LIKE '%.PA.%' THEN 'PA' ELSE 'other' END AS card_kind,
  CASE WHEN card_id LIKE 'STD.%' THEN 'Standard' WHEN card_id LIKE 'DIR.%' THEN 'Directorate' WHEN card_id LIKE 'GHO.%' THEN 'Ghost' WHEN card_id LIKE 'GUI.%' THEN 'Guild' WHEN card_id LIKE 'NET.%' THEN 'Network' WHEN card_id LIKE 'SYN.%' THEN 'Syndicate' ELSE 'other' END AS faction,
  COUNT(*) AS total, SUM(design_pass=1) AS design_passed
FROM card_status WHERE card_id LIKE '%.CA.%' OR card_id LIKE '%.PA.%'
GROUP BY card_kind, faction ORDER BY faction, card_kind;
```

| Faction | CA total | PA total |
|---|---|---|
| Standard | 16 | 8 |
| Directorate | 8 | 11 |
| Ghost | 15 | 5 |
| Guild | 10 | 10 |
| Network | 8 | 6 |
| Syndicate | 12 | 5 |
| **Total** | **69** | **45** |

**114 CA/PA cards total.** A handful already show `design_pass=1` in the DB (Directorate PA ×2, Guild CA ×2, Guild PA ×2) — per §2 above, these get checked with exactly the same rigor as everything else, not skipped.

**Order confirmed (Andy, S140):** Standard/Ring first, then presumably Directorate → Ghost → Guild → Network → Syndicate (matching the modifier-card review convention), but re-confirm faction order with Andy at the start of the CA session — it wasn't explicitly locked beyond "Standard first."

**Standard CA set (16 cards):** STD.CA.1–12 have proper `### STD.CA.n —` headers in `Part2_Standard.md`. STD.CA.13–16 (Disinformation Campaign, Disprove, Intel Extraction, Modifier Raid) exist but use `### STANDARD — [NAME]` headers instead (no card ID in the header) and old-style Python variable names (`C_DisinformationCampaign` instead of matching the card ID) — worth normalizing header format while in there, low-stakes fix-in-place candidate.

---

## 7. Relevant history / where to look for more context

- PM02 **L267–L273** — full modifier-subclass review history + the Overture re-verification + the 7-fossil re-audit + this sequencing decision.
- PM05 **04-n174** (fossil re-authoring, closed S140), **04-n177** (scaffolding gap, scope expanded S140), **04-n158** (SYN.MOD.1 redesign, closed S140), **09-16** (master roadmap item).
- Memory `feedback_design_review_verification.md` — the standard itself, read before starting.
- Memory `feedback_ring_voice_parity.md` — if Standard/Ring CA/PA content touches Ring-specific voice, same "3 distinct cultures" standard applies as it did for Ring modifier cards.
