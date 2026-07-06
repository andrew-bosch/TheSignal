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
