# PM03 — MASTER ARTIFACT INDEX
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.6  
**Status:** 🔄 Updated — Active  
**Last Updated:** 2026-06-15 (S91)  
**Supersedes:** THE_SIGNAL_P1___Master_Artifact_Index v1.1  
**Sign-off status:** See Design Artifact Registry below for individual artifact status

---

## 1. Design Standards & Terminology

→ All design standards and conventions are maintained in PM04 §2: narrative language convention (mechanical → in-world term mapping), voice and typography, code block standard, terminology sequencing principle, and cross-artifact reference convention.

---

## 2. Cross-Artifact Reference Convention

→ See PM04 §2 for the full cross-artifact reference convention. Summary: **[Artifact ID].[Section].[Subsection]** — example: `Artifact 04 §8`, `PM02 §2b`.

---

## 3. Design Artifact Registry

### Core Rules Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 00 | Factions & World | 1.9 | ✅ Signed Off — S134 (L255) | Factions, world, narrative context, ARBITER nature, timescale perspectives. Design Pillar 6 (§5), four-register system (§9), §14 Narrative Anchors incorporated. S33: ring renames. S34: re-sign-off. S38: Dispatch Token anchor §14. S39: §5 Pillar 1 revised ("The Overview is Truth"); §8 MIRROR origin narrative, holographic projection metaphor, Terminal definition; 00-04 closed (Quarter fix). S40: 00-07 multicultural texture (§6 Chorus Node first team, §8 season/cycle, §7 Guild generational building); §11 + §14 Faction Representative (L155). S54: §7 Doctrinal Alignment Pentagram rewritten (L174 — clockwise arrangement, 10 pairs, pentagram geometry). S57: §7 redesigned — shape language removed (header → "Inter-Faction Doctrinal Alignment"), three faction doctrine inserts (Guild/Syndicate/Directorate), Missing Author Vacuum paragraph added; re-signed off v1.6. S91: §8.1 added (faction private/public boundary narrative — grounds Faction Screen, Faction Terminal, Faction Resolution Grid); §9.6 "What The Table Sees" added (ARBITER's processing/revealing threshold — grounds ARBITER Screen, Arbiter Tableau; MIRROR as ARBITER's eyes). PM02 L209. S99: §14.10 Integration added (human-awareness-level narrative anchor; return channel framing; TrueState §11 open question on ARBITER's true perspective). S131: §15 Appendix added — 32-entry Master Reference Curriculum, per-entry creator/reason/filter. S134: §6.7 "Ring Character" added (PM02 L253/L254) — narrative anchor for Core/Mid/Baryo lived culture and history, model section for 00-15's eventual full-artifact refactor; §15 curriculum extended with Pine Gap (Institutional Insularity & Compartmentalization — Core workplace texture). **v1.9 signed off S134 (L255)** — bundles all three material additions since v1.8 (S99 §14.10, S131 §15, S134 §6.7 + Pine Gap curriculum entry). Open: 00-09 (World Conditions panel); 00-13 (three faction doctrine inserts, not yet written); 00-14 (Missing Author Vacuum design rule, not yet written); 00-15 (full narrative revision — now has a model section in §6.7). |
| 00a | Governing Rules & Design Policy | 0.13 | ✅ Signed Off — S150 | S150: §7.2c added (Triggering Conditions Are Exhausted on Resolution — a board-state condition qualifying a reactive effect is consumed the instant any effect resolves against it, corollary of §7.2; PM02 L341). S148: §10.4 added (Covert Attribution Remains Untraceable — a Covert Operation's effect may be public, its attribution to the acting faction may not be; PM02 L324). S108: GR 10.1b added to §10 (ARBITER disclosure outside discretional model; Governs: 03, 04, 07). 46 rules (R01–R40 + R06a, R13a, R13b, R29a, R29b, R40a). S67: Governing Rule 6.1 added (L187); Governing Rule 7.2b + Governing Rule 6.1a added (L188); Governing Rule 6.1 relocated §9→§3. S68: Governing Principle — ARBITER Cognitive Efficiency added to §1 (parent of Governing Rule 6.1 and Governing Rule 6.1a; design question: how can this narrative function be implemented while impacting ARBITER as lightly as possible?); Governing Rule 6.1 + Governing Rule 6.1a source references updated. Pending re-sign-off. S38: Governing Rule 7.3c (Dispatch Tokens). S40: stale migration notes removed; §11 Punch List removed; findings decay rule fix. S57: Governing Rule 10.1 added (Missing Author Vacuum; L177). S61: Art 04 §5 P19 updated (4-type duration taxonomy — Immediate/Transient/Seasonal/Permanent); Art 04 §5 P20 rewritten (partial payment model — full/partial/zero thresholds); Governing Rule 10.1a added (Missing Author Vacuum — renamed/renumbered from duplicate Governing Rule 10.1); Governing Rule 7.3c revised (covers both covert ops and public acts). Signed off v0.4 (L182). |
| 00b | Analysis Readiness | 0.3 | ✅ Signed Off — S83 | Restructured S83: document now tracks DB migration status to enable deep game analysis and computational balance work. DB is authoritative for migrated entities (see Database/schema_reference.md). Retains: L108 pointer (→ 00a §11), lookup tables for 5 non-DB entities (DT-xx, RO-xx, IL-xx, PS-xx, PB-xx), migration punchlist (16 entities — 1 ready to model, 7 pending migration/schema, 8 pending design), component_positions spec, derivation architecture note (unconfirmed — verify before DB-13). L108 standard migrated to 00a §11 (v0.8). |
| 00c | Economy Manifest | 0.7 | ⚠️ Future Analysis Stub — Not Canonical | S162: **§5 and §8 relocated to the new Art 04c — Card System Cost Model (PM02 L378); PM05 00c-03 CLOSED by Andy's ruling.** The header's *"do not cite 00c"* prohibition was unenforceable because §5 was authored content, not an index entry, and was cited as authority by Art 04 §6.1 and by a Reference file the header forbids — that exception is now gone and the prohibition holds without exception. §5 is a pointer stub; the §2 Index row is retained. **Opened in the same pass: 00c-04.** An S162 spot-check of the remaining index sections found the *values* largely current but systematically **mis-provenanced** — §3 cites Art 02 §7 (real home Art 03-init §2.6, an artifact absent from the "Depends on" line), §4 cites Art 02 §7 (real home Art 03 §20), §6 cites Art 03 §14 (now *Apex Activation*; real home §13) — and found one genuine content miss: §4 carries no Resource Type rule (Art 03 §20, S150), which makes §3's derived "Round 1 Totals" table wrong, and omits the Network/University Perimeter virtual structure. Source-versions stamp reads 03 v1.7 / 04 v0.9.91 against actual v4.15 / v0.9.100; the stamp now carries a ⚠ warning. v0.7. Prior — S160: §5 now states **what `value_rating` means** — gross effect delivered (Andy, PM02 L376) — which the artifact had never recorded anywhere; that omission is what allowed a net-of-payments measure to be wired into the tier at S160 before being reverted. Tier counts re-derived (113/49/21/22 over 205 priced cards, was 114/49/23/19) and a stale "201-card" figure corrected six lines below an existing "205". **Two of the three known open modeling gaps are now CLOSED** — self-cost vs delivered-value (the axis exists as `v_card_value_to_acting`, deliberately outside the tier) and Add-vs-Redirect mis-tagging (all 85 Add cards swept, one retag). The third, variable-count flooring, is re-scoped and cross-referenced to 04-n235. **The header conflict is now worse, not better:** §5 is cited by Art 04 §6.2 as authority for `value_rating` *and* is now the canonical home of its definition, while this artifact's own header still says not to cite it — unresolved, needs Andy. Prior — S159: |
| 01 | Game Board — New Meridian | 2.3 | ✅ Signed Off — v2.3 S130 | Complete physical zone hierarchy (40 zones): Table → P1–P6 → Central Area (8 sub-zones) → City → Ring 0–3 → 21 districts. District tiles with hex resource colors. District adjacency map (101 rows). Starting Configuration (Fixed Setup / Faction Starting Tokens / Track Starting Values). §9–§10 Faction Player/ARBITER Tableau stubs (Art 08). S44: §4 Narrative Function added (component anchors: District Tiles/Civic Grid, Influence Level Marker, Tension Markers, Session Timeline, Initiative Strip, Chorus Activity Track/The Seismograph, Accord Documents, Situation Reports); §6 Physical Environment — Zones and Components (renamed from [NEW]); §7–§12 renumbered; all component narrative cross-refs resolved; forward procedure refs removed (01-08 ✅). Open: DB-09 (district_adjacency); 00b-05 (live_state schema, L156). S90: §4 Narrative Function (8 component subsections) migrated to Art 02 §4; §6 Physical Forms table migrated to Art 02 §13; stale Art 02a/02b refs updated; Art 01 now geography/zone-only with pointers to Art 02 (PM05 02-n05). S114 (agy): DB-driven geography metadata blocks added, procedural content offloaded to Whiteboard/ref_special_district_and_ring_rules.md, Art 03a §setup refs updated to 03-init — pending review and re-sign-off (02-n05). |
| 02 | Components | 2.5 | ✅ Signed Off — S149 (PM02 L326) | S149: Target Profile amendment (S148, PM05 04-n197) reviewed and confirmed by Andy as-is, no changes requested — 04-n197 closed. S148: §8 Target Profile Gameplay Requirements amended — Target Profile confirmed as the sole CA/PA target-declaration mechanism, multi-target handling via the free-form declared-parameters line, ModReactCard exclusion (PM02 L317). Made without following the signed-off-artifact draft/confirm protocol; flagged retroactively, pending Andy's formal re-sign-off (PM05 04-n197). S118: Component name Title Case sweep — 43 renames across all headings and component_name fields; L235 Public Act cascade (Political act deck/discard/card set → Public Act Deck/Discard/Card Set); Presence chip → Presence Token; Arbiter Tableau → ARBITER Tableau. v2.5. S111: DB:48 Target Profile `recorded_fields` + Gameplay Requirements expanded — declared parameters (free-form text blank line) added for card-specific declarations; enables SYN.CA.11 Redline and future declaration-requiring cards. S109: DB:48 Target Profile `recorded_fields` + Gameplay Requirements expanded — target object (named component) added as valid field type; enables GHO.PA.4 and future object-targeting PAs. Prior: S98 (L213) — `applicable_verbs` seeded §§5–12; §13 matrix removed; d10 added; DB-42 seeded. Open PM05: 02-n17, 02-n21, 02-n22, 02-n25. | S88 merge from 02a v1.6 + 02b v1.5. S89: §13 comprehensive stub pass (44 rows, all 104 DB-registered components). S90: full scope rewrite v2.0 — 8-section taxonomy (§§5–12); all entries: Design Function + Narrative Anchor + Gameplay Requirements + Physical Form table; orphaned rules → Whiteboard/art02_orphaned_content.md (02-n08). S91 (02-n02 in progress): §§5–12 rubric pass complete. Art 00 §8.1 + §9.6 added (L209) to ground faction private/public boundary and ARBITER threshold components. Scope discipline sweep: all "Full design: Art 03" and "Full design: Art 00b" cross-refs removed (Art 03 = procedure only; Art 00b = DB punch list). DB:47 Modifier token Design Function written; DB:48 target district field added; DB:17/44/100/108 active narrative anchors written. New PM05: 02-n10 through 02-n13, 00-16. S92 (02-n02 complete): §§11–12 rubric pass + GR validation (Resolution Tools · Tracking Systems). Key decisions: DB:47 denominations (5/10/15; obverse/reverse color-keyed); DB:50 single physical strip (5 parallel tracks; behind ARBITER screen); DB:36 renamed Escalation marker (DB-38); DB:23 restructured (8Q × 3M); DB:106/107 sliders (0–100 × 5, crit zones). L210. | Component enumeration by function (§§5–12): Playing Surface · Faction Influence · Resources · Covert Messaging System · Intel & Information · Card Systems · Resolution Tools · Tracking Systems. DB component table is canonical completeness anchor. Design Principles: Scarcity is intentional; Disclosure is designed, not assumed. |
| 02a | Resource Systems: Board State | 1.6 | ⛔ Superseded — S88 by Art 02 v1.0. Moved to Retired/Paper/ S90. | Presence, influence, structures, resource generation — all publicly visible board state. Session 22: Control flag, Established marker, ARBITER Dominance Marker confirmed. Session 38: §8a Dispatch Tokens & The Backlog added — component definition, spend rules (one token per covert op, pass/political exempt), Ghost asymmetry (4 vs 3), The Backlog as named physical token pool distinct from Reservoir. Session 41: §4 Reservoir narrative anchor added; §8a Dispatch Token narrative intro added (executive authorization framing). Session 42: terminology sweep (Quarter, Baryo/The Mid, Deployment marker, Dispatch Case); §8a Narrative Anchor subheader; Art 01 Supply stub resolved; "Round 1" → "Quarter 1" in starting resources table. |
| 02b | Resource Systems: Tracking | 1.5 | ⛔ Superseded — S88 by Art 02 v1.0. Moved to Retired/Paper/ S90. | Chorus Portrait, Public Standing, Intel Tokens — tracking systems alongside the board. Cross-reference audit with 04 pending (PM02 D04-11) |
| 03-init | Game Initialization | 0.5 | 🟡 In progress — S124: §3.9 Deck Selection procedure added (per-faction pool selection + ARBITER deck assembly); §3.6 sequencing conflict open (04-n137). Remaining: Operative sequencing resolution (04-n137), Classified Directives (Art 06.x). Prior: §2.8 Broadcast Deck/Effect Deck rows; §3.9 deck list stub. |
| 03 | while session(true): Round Structure | 4.15 | ✅ Signed Off — S150 (PM02 L340, L341): §7.4 restructured (§7.4.0 Calculate District Income → §7.4.0.0 Apply Affinity Bonus/§7.4.0.1 Collect District Income; §7.4.1 Calculate Structure Block Income → §7.4.1.0 Declare/§7.4.1.1 Collect; §7.4.2 Collect Passive Generation), new Resource Type rule (district income pays in the district's own Resource Type, not the collecting faction's Native Resource); §18.1/§18.1.0 refined (a faction holding 2+ eligible React cards for one event chooses which to present; tied announcements resolve by initiative order). Prior: S149 (PM02 L332): §18.2.2 added — React cards are permanently removed from the game by default once resolved, unless card text states otherwise (previously unstated anywhere in Art 03; schema_cleanup_log #19, PM05 04-n195). Prior: S146 (PM02 L292): §9.4.3.1.0.3 Route — zero-payment Public Act invalidation now carries a Public Standing −1 ("failed commitment") consequence, closing a gap left when Art 04's old §14.3 language was retired without carrying its PS penalty into the unified Principle 20 payment model (PM05 04-n169). Prior: S132 (L243). S132: §10.1.2 Battlefield Strength redesigned (Boost/Hinder, face-down commit/reveal, any faction may commit, Intel Token −2 Hinder); §10.1.4.0/0.2/1 sequential + cleanup relocated. Resolves 04-n152. Prior: S110 (L232). §9.2.0 Target Profile placed face-down at PA declaration; §9.4.3.1.1 Target Profile revealed at Apex Check step (gates GHO.MOD.1 intelligence test). VM-xx lifecycle formalised: §9.4.1.1 VM-xx check added to BEC step; §9.4.2.2.0 VM-xx placement clause; §9.4.3.0.1 renamed Initiative Loop (BEC application moved to per-PA step); §9.4.3.1.3 Apply BEC Modifiers added (new — mirrors §9.4.1.1); §9.4.3.1.4 Base Difficulty (renumbered from 1.3); §9.4.3.3.0 generic VM-xx placement clause; specific BEC reveal clause removed (superseded by VM-xx model). Prior: S104 (L217) v4.8 — §24 Resolution State Reference (03-n25 ✅): three states Succeeded/Failed/Voided; Discovered as resolution effect alongside Failed; RO-xx codes removed from Art 03; targeting restriction → face-down model (§9.4.1.0 → §9.4.2.0 Step 0 unified Voided handler). Open PM05: 03a-n01. Prior: S102 (L216) v4.7 — § Primitive Action Model appendix restructured: governing principle surfaced; S97/S101 decision tables removed (DB is source of truth); coherent section flow. Index anchor fixed. v_unlegislated_primitives pass: 6 ❌ prohibit, 4 ✅ permit, 14 seeding gaps — agy task queued. Prior: S101 (L215) v4.6 — 03-n24 Primitive Action Model legality table (26 decisions). S101 (L214) v4.5 — 02-n08 migration. Prior — S97: §22 Primitive Action Model & Legalization Analysis added. Art 03 is the legality source of truth for subject × verb × component combinations. Prior: S88 (L207). | S60: L180 architecture applied — monthly A/B/C/D structure; all factions 4 Dispatch Tokens; face-down = void (Voided Resolution Card component retired); Phase C/D labels removed; Beat 2 renamed "Conditions Set"; §17 = Contested District Resolution; §18 = Month 3 Quarter Notes; §20 = End of Quarter; §21 = The Operation System; Beat 3 Step 12 = Dispatch Case Return (Month 3 only); Beat 4 Step 2 = board state validation; Pass cards removed; Contested/Failed TBD blocks removed. PM05: XA-43 (pass card sweep), XA-44 (Voided Resolution Card sweep), 04-n9 (deployment marker blocking flag) added. S61: Beat 3 Step 12 label "(Month 3 only)" and flavor line removed; Beat 4 Submit Payment promoted to Step 1, steps renumbered 1–13; Gameplay Procedure and Reference Material section breaks added in index and body. Duration taxonomy 5→4 types (Tripwire collapsed into Permanent). Signed off v3.0 (L181). S65: Beat 0 Retained validation; Beat 2 Golden Parachute bribe procedure; Beat 3 partial payment marker source. Signed off v3.1 (L185). S66: Beat 2 pre_loss_calc block removed (schema addition predated sign-off). Signed off v3.2 (L186). S67: §5 Design Principle 6 added (ARBITER Cognitive Load — Governing Rule 6.1); pending re-sign-off (L187). S68: §19 Debrief Actions step added (DebriefActionCard type); §25 updated to cross-reference §28; §28 React Card Rules added (interrupt model, Governing Rule 7.2a compliant). Signed off v3.3 (L189). S81: Beat 2 d100 resolution block added (after Automatic cards; queue order; 8-step procedure; additive crits per §21); Beat 2 header updated (C17/C28 listed; Automatic-first order noted); Beat 3 Step 1 item 4 added (VM-xx → public resolution: announce before Step 2, visible roll at Step 5, announce result at Step 6, remove at Step 8 cleanup). S82: Beat 0 Boost Detection procedure added (floor division; no refunds); Beat 3 Step 3 BM-xx threshold modifier clause; Beat 3 Step 7 all-effects multiply (1+n) / single NS-xx regardless of n; Beat 3 Step 8 BM-xx cleanup; Discovery (Step 7b.i) defined as public reveal — ARBITER announces acting faction + op name + target; Step 7b rewritten (ARBITER applies); Step 7b.i rewritten (faction player applies own board changes); Start of Month 1/2/3 "Active PA Obligations" blocks added (§9/§12/§15 — generalizable; cross-Quarter compatible). v3.4 pending re-sign-off. S83: §§12–16 unified into §9; §9.4.4 Beat 4 + §9.4.5 Close Month written; §10 Resolve District Tension; §11 Quarterly Debrief; §12 Quarter Close; reference sections §13–§19. v4.0 structural sign-off S83. S84/S85: entry/exit all §6 sections; §9.4.0–§9.4.1 restructured; Broadcast Card/Deck/Effect Card/Deck naming; Target Profile sweep; 03-init updated. v4.2. S87: §5 P7 (Step 0 convention); §9.4.2.6.1.0/1.1 (Target Profile return + case contents); §9.4.3.4 item 5 (Beat 4 Target Profile cleanup); §§11–12 restructured (Debrief/Quarter Close §11.0–§12.4); §13 modifier table rebuilt (M-06/M-07 merged, M-11 all/both beats, §13.6 Intel Age table); §14 renamed Apex Activation (flat Steps 0–4); §§15–17 rubric clean; §18 React Rules restructured (§18.0–§18.3); §19 Reserved; §20–21 new reference sections; § Examples rewritten/flagged. Grip review complete. v4.3. Sign-off pending PM05 03-n18 (lifecycle sweep). |
| 03b | Component Lifecycle Register | 0.2 | 🔄 In Progress — S88 initial formalization from Whiteboard. Living document — update when any component entry/exit changes in Art 03. All S88 lifecycle gaps resolved. Open: 03-n06 (Dispatch Packet), 03-n11/12 (sliders), 03-n16 (Target Profile physical design), XA-07 (Status Marker distribution), DB-14/15 (pending agy). |
| 03a | Game Engine Specification | 0.99 | 🔄 In Progress — Tiers 1–3 complete; Tier 4 stub | Code-lite technical companion to Art 03. Tier 1 (State Model): formal game state at each beat boundary using 00b entity IDs. Tier 2 (Phase & Beat Procedures): Quarter_Flow(); Phase_1()–Phase_7() with explicit state mutations for all phases; Beat_0()–Beat_5() for Phase 6 detail (modifier stack summation formula, resolution inequality). Tier 3 (Decision Tables): DT-01–DT-09; Apex_Activation() procedure. Tier 4 stub (modifier balance analysis) — blocked on Art 04 card definitions. |
| 04 | Card System | 0.9.101 | 🔄 In Progress | S162 (PM02 L380): **four of five S160 gate items closed.** GD-01 step 4 now gated on step 3 (04-n230, Andy) so the card never resolves as a bare Remove — applied to §12b.2, the `success` guard and the `design_note`; cost unchanged (12.0000), no rating tiered from it. **GD-01 added to the §8 Card Taxonomy Index** (04-n231) — `Territory \| Public \| Redirect \| Structure Block \| Move`, 📝; the framing question was answered by corpus practice (STD.MOD.1 and SYN.MOD.1, the only other Issued cards, were already indexed), §8 now 349 rows. **04-n233's three defects fixed, two worse than logged:** GHO.PA.5 was the corpus's only presence placement lacking `faction=` *and* its only `game.add(PresenceToken, …)` — normalised, which corrected `card_effect_component.target` from `district` to `acting` with `total_pair_cost` unchanged at 4.1140; three stale Grant Deed passages (not two) rewritten to include step 4; GD-01's own `design_note` mis-numbered the removal as Step 3. **04-n232 closed as no defect** — both tags correct, discriminator now in Art 04b §5.1. **04-n235 rehomed to 04c-01** (a pricing convention, not a punch-list item). Opened: 04-n237 (47 stale §8 rows), DB-50 (sync ordering — `card_effect_component` was one sync behind, drift guard evaluated stale rows; fixed). Prior — S160: **Add-vs-Redirect mis-tag sweep complete (Art 00c gap #2 closed) and the `target`-field audit + rewrite complete (gap #1 closed).** All 85 `Function=Add` cards audited — wider than 00c's Territory framing because Art 04b §5.1 defines Redirect as subsuming cross-faction resource movement in Economy too. One mis-tag: **GD-01 Grant Deed → `Territory/Redirect/StructureBlock`** (v0.4→v0.5), verified sole instance across every effect field. Toll/cut family ruled mechanics-win (Andy): STD.MOD.104/105/116/117/128/129 narrated a transfer their code never performs — six Card Stories, taglines and `narrative` fields rewritten, and three renamed (Toll Collected → **Freight Booked**, Informal Toll → **Side Work**, Cut of the Action → **Rents Adjust**). GHO.CA.10 Flip carried three narrative surfaces asserting a Redirect its copy model does not do; all corrected, taxonomy untouched. **`card_effect_component.target` rewritten** to name the entity whose holdings a row changes — it had been answering "which entity is mentioned first" and disagreed on **108 of 355 rows**; all four defect classes fixed, distribution 106→221 `acting`, 73→17 `other`. **04-n229 closed** — `v_card_pair_uvm_cost` was billing a Redirect's two halves as two operations, and inconsistently by effect category; an `xfer` CTE collapses them, moving exactly 3 of 205 cards (all ModReactCards, so no CA/PA rating shifted). **`value_rating` DEFINED (Andy, L376): gross effect delivered** — how much of the game a card moves, with `cost` recording separately what is paid. The definition had never been written down, and that silence let a signed net-of-payments measure be wired into the tier mid-session; it rated pay-to-impose cards as floor-tier and was reverted, restoring NET.CA.6 to 3 and GUI.PA.10 to 4. Now governing in Art 00c §5 and `design_reference_card_system.md`; the signed axis survives outside the tier as `v_card_value_to_acting`. **Parser fixes (04-n235 partial):** `find_magnitude` now reads `.native * N`, `IntelToken(...) * N` and `min(N, ...)` — 7 magnitudes recovered, SYN.CA.3 corrected 20.13→7.63, and GHO.CA.10 1→3, GHO.CA.6 1→3, GUI.CA.7 3→4 re-rated. **Corpus now reads zero drift.** Two infrastructure defects found by the work and fixed: `v_card_pair_uvm_cost` was defined nowhere on disk (now `Database/view_card_pair_uvm_cost.sql`), and the sync's drift guard excluded MOD cards by a `card_id` string test that leaked GD-01 into the CA/PA audit (now keyed on `card_type`). Opened: 04-n230/231/232/233/235, all gating; closed: 04-n229, 04-n234, 04-n236. Detail: PM02 L370–L376. Prior — S159: **`schema_cleanup_log` #64 and #65 both CLOSED — every Art 04 schema gate is now clear.** #64: all 72 non-React `Automatic` card bodies re-derived against the `PositionalWager` definition; corpus 13 → 21 (GHO.CA.1, DIR.CA.1, GHO.CA.3, DIR.CA.3, GHO.CA.5, STD.CA.12, NET.CA.1, NET.CA.4 recategorised; Design Pass reset on all 8 per 04-n225). Two boundary rulings from Andy now written into §6.3 as specification: a contingency carried by persistence or a delivered instrument leaves the card `Transactional`, and the unrevealed slate need not belong to a later beat. GHO.CA.1 reversed item #41's logged ruling, with its Design Rationale rewritten and approved first, plus Andy's clarification that a stolen operation card returns to its owner's case once resolved. #65: §6 swept of all provenance citations and audit vocabulary — zero `schema_cleanup_log`/PM05/PM02/session references and zero uses of "confirmed" remain; corpus analysis removed; the 14 "Displayed" TBDs kept and registered against the §7 / Art 09 gate. Four factual defects fixed in passing (the `beat` range, §6.1 contradicting §6.2 on `value_rating`, a false `None` qualifier, DIR.PA.1 mislabelled Permanent). Detail: PM02 L368/L369. S158: `persistence_effect` counts toward `total_pair_cost` (Andy) — not an inference: the pre-rebuild backup carries five `[persistence_effect]`-prefixed rows, and the S145 ratings on DIR.PA.3/5/6/11 + DIR.MOD.9 reconcile only with inclusion. Verified by rebuilding the view's inner logic as a CTE across three regimes; include-mode reproduces `v_card_pair_uvm_cost` row-for-row on all 199 shared cards, and the old-vs-new encoding is tier-neutral corpus-wide. **Three S157 claims overturned:** SYN.MOD.6 computes tier 4 in every regime and is a MOD card never subject to UVM tiering (the choice gated one card, SYN.PA.3); there are **five** bare-prose PAs not four (NET.PA.6 found); drift is 16 not 14 (6 MOD, out of scope). S157's enumeration of the 10 re-derivable cards was exactly right and all 10 are applied — STD.CA.14 2→1, GHO.CA.6 3→1, GHO.CA.10 3→1, SYN.PA.3 1→2, DIR.CA.4 1→2, STD.CA.7 1→2, DIR.PA.8 2→3, GUI.CA.8 2→3, GUI.CA.7 2→3, NET.PA.1 3→4 — each spot-verified against `uvm_pair_assumptions` (no fallbacks, all rates `validated`). `sync_card_db.sh` reports ✓ no drift; its check was split so bare-prose cards no longer register as permanent false-positive drift. **The S157 blanket provisional-`value_rating` caveat is lifted**, except the five bare-prose PAs which hold pending 04-n218/n220. v0.9.97. Prior — S157: **PM05 09-17 triage COMPLETE — the second and last original sign-off gate (PM02 L358).** All 27 S156 audit findings triaged; every `[verify]` finding re-derived against primary source, overturning four conclusions and correcting five claims. §9.2 grouping fails against corpus data (cross-cost share flat: GUI 50/SYN 43/DIR 41/NET 40/GHO 23 %) → 04-n223. SYS-1 reframed as a symptom of the undesigned sub-6-player configuration → 00a-80 (explicitly deferred from gating Art 04). §5a Directorate adjacency modifier-draw cut as unbuildable at stated scale; §5a Guild passive-income rewritten to the React lane as built (04-n2 closed superseded); DIR-4 "costs Portrait" ruled doctrinally backwards → 04-n222. **Schema:** #59 `resolution_type` populated on all 46 cards lacking it + §6.3 rewritten specification-only (L359); #60 `value_rating` — two coexisting derivation conventions documented for the first time, 9 cards re-tiered (L361); #61 `NamedActionType` retired, **SYN.CA.5 rescoped to v2.0** with a `faction != acting` self-exemption (L362); #62 NET.MOD.3 → v1.0 boost mechanic, exposing that Art 03 §18 has no React cost-payment step at all (26 cards) → folded into 04-n221 (L363); #63 GUI.CA.2/GUI.CA.6 live payout defect corrected (L364); §6.1 retired `PortraitEntry.flat` removed (L365). **#66:** `card_effect_component` — the substrate of every `value_rating` — had no extractor and was a month stale; `tools/extract_card_effects.py` built and wired into the new `tools/sync_card_db.sh`, 18 of 205 cards change tier, **not applied** pending 04-n228 (L366). All `value_rating` values are provisional until that lands. v0.9.96. Prior — S156:
| 04a | Card Reference Table | — | ⬜ Not Started | Condensed tabular view of all cards — one row per card, columns: Card ID, Card Name, Card Type, Card Subtype, Card Faction, Beat, Primary Cost, Difficulty, Taxonomy — Category / Function / Subject, Portrait. Full card data stays in Artifact 04; 04a is the lookup and cross-reference layer. Populated after all card reviews complete. Blocked by 04 completion. (Scope confirmed L83.) |
| 04b | Action Taxonomy & Design Analysis | 2.7 | ✅ Signed Off — S108 | S162 (PM02 L380): **two material §5.1 corrections, signed off in session.** (1) The blanket *"Modifier Cards are excluded from Layer — Function — Subject taxonomy"* scoped to **ModActionCard and ModBattleCard only** — ModReactCard carries real taxonomy on **91 of 93** cards; the retired wording still survives on 47 Art 04 §8 rows (PM05 04-n237). (2) **Add vs. Redirect discriminator added** to the Function vocabulary: *does one and the same element change hands?* — yes → Redirect (ownership change, verb Move); payment consumed and a different element created → Add. Worked pair STD.CA.9 / GUI.PA.2, both correct as tagged, which closed 04-n232 as no defect. v2.7. Prior — S123: §6.4 STD+NET 5-check added; §8.3 Network section rewritten (12-card S123 data); PM05 04-n126 added (Findings-gated cross-ceiling). v2.6. S122: §6.4 STD+GUI Economic Integration Audit added; §8.5 Guild section updated (card list current, design targets refreshed). v2.4. S121: §6.4 STD+DIR Economic Integration Audit added; §8.2 Directorate section fixed (DIR.PA.1 active, S106 cards added, stale BLOCKED removed). v2.3. S120: §6.4 STD+GHO Economic Integration Audit added; 04-n87/88 gates cleared. v2.2. S119: §6.1 Information|Reveal|Named faction retired; 4 ARBITER-domain Reveal subjects added; §8.0 Standard doctrine statement written (gate for 04-n87). v2.1. S108: §4 audit (GRs 7.2b/9.1/10.1 added as §4.14-16; §4.8 rewritten as GR 10.1b corollary); §5.1 Valid L×F matrix + Visibility + React/Instant/Interrupt; §5.2 sorted + Visibility + BLOCKED taxonomy filled; §8.1 Ghost design seeds (GHO.PA.3–6) + BEC mechanic; §8.2 Directorate BLOCKED guidance; 04b-21/22 closed. Sign-off scope: §4/§5 material = re-sign-off; §6–9 working sections = no re-sign-off. Companion to 04. Six-layer system locked S48 (Territory / Economy / Information / Submission / Resolution / Standing). §4 rewritten; §5–§10 swept for layer terminology; §6.1 rebuilt grouped-by-layer with Layer/Function definitions; §9 design principles moved to Art 04 §5 P1–P6. Agent (04b-07) and Beat (04b-08) dimensions deferred to future pass. S55: §4.2/§4.4 updated — Economy narrowed to capital flow only (L175); IntelToken generation classified as Information layer. §5.2 table updated (C05, C24: Economy→Information). S56: §4.6 C27 Source Protection row removed (04-63 ✅ — C27 is now Disclosure Loop, not a Protect card). S64: §5.2 +5 rows (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid) — material addition; pending re-sign-off. S107: Full audit against 00a governing rules. Locked decisions: L222 (Backdate BLOCKED—Intel location constraint), L223 (Regulatory Downgrade/Freeze BLOCKED—InfluenceTier not targetable), L224 (Conceal retired—not card-triggerable), L225 (ARBITER-reveal outside 10.1), L226 (Detain retaxonomized Territory|Move), L227 (Accord Transfer retaxonomized Economy|Corrupt). §4.10 revisions (round-number removed, location constraint documented); §4.13 added (ARBITER-reveal); §5.1/§5.2 (Conceal retired; 5 card annotations); §6.1/§7/§8.2/§8.4 updated. Audit clean: all taxonomy functions verified against 00a. v1.8 draft — re-sign-off pending (04b-21). |
| 04c | Card System Cost Model | 2.0 | ✅ Signed Off — S162 (initial version; revisit before Art 04 sign-off) | **S162 (PM02 L379) — rewritten from v1.0's section transplant into the artifact its title promises.** Two halves: **what cards charge** (§3 Principle 15 · §4 cost vocabulary incl. what may *not* be a cost · §5 cost by card type · §6 cross-resource costs · §7 Intel Tokens) and **how effects are priced** (§8 `value_rating` = gross effect delivered · §9 UVM + ⚠ governing caveat · §10 tier boundaries 113/49/21/22 over 205 priced cards · §11 model limits). **Art 00c §8 Derived Cost Analysis absorbed as §12** — still blocked on Art 04 sign-off; stale framing corrected on the way (it cited Art 04 §8 as *critical effects*; §8 is the Card Taxonomy Index, and the worked example used the retired C01/P01 ID scheme). **Established here for the first time: no cost magnitude rule is locked for any card type.** Principle 15 is a principle; the Balance checklist calls cost *best-effort*; §12 is the analysis that would fix it and is gated. The ⚠ caveat cannot be lifted until it exists. **ModReactCard is the only Modifier subclass that charges resources** (27/93 — ModAction folds into its host packet, ModBattle is schema-locked to None); its cost convention is recorded as **observed, explicitly not a rule** (Andy), with four named departures, at PM05 **04c-01**. Review caught two drafting errors before the artifact stood (an invented economic rationale for ModBattleCard's `cost=None` where the record gives a procedural one; a resource table conflating faction-native with district-native) and declined to reproduce a third inherited from 00c §8 (a formula treating a d100 threshold as a probability). **PM05 DB-49 opened:** `card_status`'s `cost_*` columns are stale and were not used — all figures here come from `card_body`. **18 cards take an Intel Token as cost** (10 CA, 4 PA, 4 ModReact) — a discrete-object category, not a fungible quantity, with no defined exchange rate to resources and none to be inferred. Session/decision provenance stripped from prose per the S146 hygiene rule; standing qualifications (⚠ caveat, five bare-prose PAs, MOD/React UVM exemption) kept. **Signed off S162 as an initial version** — sound as an account of where card economics stands, explicitly not a finished model; the open questions it records (no locked magnitude rule, ModReact convention descriptive not governing, ⚠ caveat unliftable until §12 is buildable) are to be worked as Art 04 approaches sign-off. Prior — S162 v1.0: relocated from Art 00c §5 (PM02 L378, closing PM05 00c-03), filed in the 04 series because the cost model is only ever about the card system. |
| 05 | Operative & Apex System | 0.2 | 🔄 Draft — Placeholder | Placeholder file created. System structure, operative data format, Apex procedure, Founding Figure slots per faction. Blocked by 04 completion — no card content finalized. |
| 06 | Messaging System | 0.5 | ✅ §9 Signed Off — S83 (L205) | S83: §9 re-signed off (L205) — §9.3 clause vocabulary complete (6 types: +Duration); §9.5 board state as sole compliance basis; §9.8 ACCORD DISSOLVED added to form; §9.10 Transfer collapsed into Alter (Named Party subtype; four alteration types). Form rendering fixed (em dash blanks). S80: §9.3 Accord clause vocabulary written (5 types); §9.4 PS formation mechanic redesigned. S77: §9.4 Formation re-signed off (L198) — blank AccordForm delivery model; cross-Quarter persistence; Debrief-only physical alterations. S69: §9.1–§9.10 Accord governance (L190/L191). §§1–8, 10–13 non-canonical stubs. |
| 07 | ARBITER Toolkit | 0.2 | 🔄 Draft — Placeholder | Placeholder file created. Portrait board tracking, Debrief reward system, resolution beats, four narrative registers (The Record / The Observation / The Reckoning / The Witness — updated session 11), Chronicle, ARBITER script pack. |
| 08 | Player Toolkit | 0.2 | 🔄 Draft — Placeholder | Placeholder file created. Faction board layout, starting assets (provisional), deck selection, classified directives, faction reference card, player setup procedure. |

### Reference Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 09 | Card Production Spec | 0.2 | ⬜ Placeholder | Placeholder. Production-only — no design content (L115). All content blocked pending 04 completion. |
| 10 | Game Manuals | 0.2 | 🔄 Draft — Placeholder | Placeholder file created. Player Guide, ARBITER Guide (incl. Translation script table), Setup Guide, Components List (provisional quantities). Pending all upstream sign-offs. |
| 10a | Victory System | 0.2 | ⬜ Placeholder | Placeholder file created. VP source categories, Portrait conversion (design decision required), scoring sequence, vote mechanic, tiebreakers. |
| 11 | Visual Design System | 0.2 | ⬜ Placeholder | Placeholder file created. Faction colors per Artifact 00 §7. Three narrative registers framework. Component standards. V01–V19 priority table. Ghost/Network color adjacency flagged. |

### Project Management Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| PM01 | Project Charter & Work Breakdown | 1.7 | 🔄 Active | S161: **WBS 4 — World Engine (Canon Tooling) added** (8 deliverables; build gated on Art 04 sign-off, lev cleared for 4.02 groundwork only; PM02 L377, constraints in PM05 WE-01). §6 exclusion clarified to agent-generated narrative *during a session* — agent-authored design artifacts under project-lead review are not excluded; AI as ARBITER logged as PM02 FD-07. Scope, deliverables, WBS (with production cost estimates), documentation standards, governance rules, reference convention. §§10–12: Playtest Readiness Checklist, Risk Register, Go/No-Go Framework for V2. §2: Replayability core assumption; S3/S4/S6 extended. WBS 2: 40 components (2.01–2.40), $115–270 est. |
| PM02 | Decision Log & Validation Tracker | 4.1 | 🔄 Active | Locked decisions (L01–L150). S37: L145–L150 (Double Case Pass, Dispatch Tokens, Ghost token gate, Intel universal currency, Intel decay, Month canon term). §2b punch list archived — live version in PM05. |
| PM03 | Master Artifact Index (this document) | 2.4 | 🔄 Active | Artifact registry, standard artifact template, dependency map, retired artifacts index (/Retired/). Design standards and conventions moved to PM04 §2. |
| PM04 | Glossary & Data Dictionary | 0.9 | 🔄 Updated — Active | Single source of truth for all terminology and design conventions. §1: In-World Data Dictionary — Component Physical Glossary added (S34); Asset token removed. §2: Design Terminology — Category column pattern (S34), L109 Component Terminology Standard (S34) added alongside existing conventions. |
| PM04b | Future Phases — Parking Lot | — | ⬜ Not Started | Post-Tier 1 design concepts, tier roadmap, electronic version considerations, ARBITER role redesign, Tier 5 faction vision. Companion to PM04 — not yet created. |
| PM05 | Active Punch List | 3.2 | 🔄 Active | Living action queue of all pending changes across all artifacts. S50: DB-22–26 ✅ (agy), DB-27–28 ✅ (agy), DB-29 ✅ (schema_reference.md populated), WEB-01 added (deferred), 04b-11 added (Inspect verb). S89: full cross-ref sweep — all 02a/02b/02x refs → Art 02; all stale Art 03 section numbers updated; 04-n95 added. DB-35/36 ✅, 02-n03, 02-n04 ✅, 03-n21, 03-n22 ✅, 04-n96 added. S92 (agy): DB-33 ✅ (beat→quarter_phase rename + 28 views recompiled), DB-32 ✅ (component hierarchy + component_dim + component_type tables), DB-38 ✅ (Escalation marker rename), DB-S92-01 ✅ (id=109 Broadcast Discard), DB-S92-02 ✅ (id=110 Broadcast Effect Discard), DB-S92-03 ✅ (id=101 SCIFRecord de-registered). S93: PM05 updated with closures; PM02 Change Log updated. |
| PM (Audit) | Cross-Artifact Inconsistency Audit | 1.0 | ✅ Retired — session 10 | All 24 items migrated to PM05 punch list. File deleted. |

### Visual Artifacts (Interactive HTML)

| ID | Title | Status | Notes |
|----|-------|--------|-------|
| V01 | Game Mat / Table Layout | 🔄 Draft | |
| V02 | Public Standing Track | ⬜ Not Started | |
| V03 | Round Phase Slider | ⬜ Not Started | |
| V04 | World Condition Tracks | 🔄 Draft | |
| V05 | Situation Report (World Event) Layout | 🔄 Draft | |
| V06 | Accord Document Layout | ⬜ Not Started | |
| V07 | Card Layouts — all types | 🔄 Draft | Requires 04 completion and 11 Visual Design System |
| V08 | District Hex Layout | ⬜ Not Started | |
| V09 | Player Tools Visual Layouts | ⬜ Not Started | |
| V10 | ARBITER Tools Visual Layouts | ⬜ Not Started | |
| V11 | Dispatch Case / Messaging Layout | ⬜ Not Started | |
| V12 | Quick Reference — Round Phases | ⬜ Not Started | |
| V13 | Quick Reference — Card Types | ⬜ Not Started | |
| V14 | Quick Reference — Difficulty | ⬜ Not Started | |
| V15 | Quick Reference — Covert Operations | ⬜ Not Started | |
| V16 | Quick Reference — Political Acts | ⬜ Not Started | |
| V17 | Quick Reference — Intelligence Tokens | ⬜ Not Started | |
| V18 | Quick Reference — Public Standing | ⬜ Not Started | |
| V19 | Intelligence Token Layout | ⬜ Not Started | |

---

## 4. Standard Artifact Template

Every text-based design artifact (IDs 00–11) follows this structure unless the artifact's nature requires deviation (noted in the artifact itself). Section names are fixed — do not rename them.

```
# [ID] — [TITLE]
## THE SIGNAL P1 — Paper Prototype

Version | Status | Last Updated | Supersedes

---

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Rules & Constraints
7. Component Description
8. Special Conditions & Gameplay Impacts
9. Examples & Exceptions
```

**Reference convention within artifacts:** `[Artifact ID].[Section].[Subsection]` — see §2 above.

**Card data structure** (Artifact 04 and 09): Cards use a separate 20-field data structure defined in Artifact 04 §6. The standard template above applies to artifact prose sections, not individual card definitions.

---

## 5. Artifact Dependency Map

Reading order reflects dependency — no artifact references a concept not yet introduced in a prior artifact.

```
00 (World & Factions)
 ├─ 00a (Governing Rules & Design Policy — companion, no new mechanics)
 └─ 01 (Game Board)
     └─ 02 (Components)
         └─ 03 (Round Structure)
                 └─ 04 (Card System)
                 │   └─ 04b (Taxonomy — reference only)
                 └─ 05 (Operative & Apex System)
                     └─ 06 (Messaging System)
                         └─ 07 (ARBITER Toolkit)
                         └─ 08 (Player Toolkit)
                             └─ 09 (Card Production Spec)
                             └─ 10 (Game Manuals)
                             │   └─ 10a (Victory System)
                             └─ 11 (Visual Design System)
                                 └─ V01–V19 (Visual Artifacts)
```

PM01, PM02, PM03, PM04 are parallel to this chain — they govern the project but do not introduce game mechanics.

---

## 6. Retired Artifacts

The following artifacts from the working design phase are superseded by the current baseline set. They should not be edited further. Content has been redistributed into the numbered artifact set.

| Former Artifact | Content Moved To |
|----------------|-----------------|
| game_overview | 10 — Game Manuals |
| components | 10 — Game Manuals |
| round_structure | 03 — Round Structure |
| hidden_objectives | 02b — Resource Systems: Tracking, 05 — Operative System |
| card_designs | 09 — Card Production Spec |
| arbiter_guide | 07 — ARBITER Toolkit, 10 — Game Manuals |
| player_guide | 08 — Player Toolkit, 10 — Game Manuals |
| reference_sheets | V12–V18 Visual Quick References |
| setup_guide | 10 — Game Manuals |
| event_card_system | 01 — Game Board, 09 — Card Production Spec |
| l1_generation | 02a — Resource Systems: Board State |
| action_redesign | 04 — Card System (superseded) |
| apex_system | 05 — Operative & Apex System |
| debrief_rewards | 07 — ARBITER Toolkit |
| prototype_to_tech | PM04 — Future Phases |
| influence_system | 02a — Resource Systems: Board State |
| l1_operatives | 05 — Operative & Apex System |
| ghost_actions | 04 — Card System |
| layer_roadmap | PM04 — Future Phases |
| arbiter_role_redesign | 07 — ARBITER Toolkit (player-ARBITER mechanics); PM04 — Future Phases (Tier 5 faction vision) |
| popularity_redesign | 02b — Resource Systems: Tracking |
| THE_SIGNAL_P1___Master_Artifact_Index | PM03 — Master Artifact Index (this document) |

---

### Legacy Folder Archive — /Retired

Two generations of pre-V1 design documents are archived in `/TheSignal/Retired/`, organized into subfolders as of 2026-05-16. (Folder was `/Old/` prior to 2026-05-16 reorganization.) These files are read-only reference — content has been redistributed into the V1 artifact set. Do not edit.

**`/Retired/Electronic/`** — 20 files — Original electronic brainstorming suite (pre-code design phase). Document numbering: 00–20. Uses old faction names (Architect, Warden, Signal). Includes TypeScript game state schema, hardware specifications, network architecture, audio system, website architecture, and full game design documents.

| File | Contents |
|------|----------|
| old__00_PROJECT_INDEX.md | Master index for the electronic design suite |
| old__01_WORLD_AND_NARRATIVE.md | Setting, factions, ARBITER, The Chorus, legacy structure |
| old__02_GAME_RULES.md | Complete formal rulebook written in ARBITER's voice |
| old__03_FACTIONS_AND_OPERATORS.md | All 5 factions, 20 operators, abilities, unlock conditions |
| old__04_CITY_OF_NEW_MERIDIAN.md | Board design, district history, layer system |
| old__05_ECONOMY_AND_RESOURCES.md | All 6 resources, generation rates, costs, trade rules |
| old__06_CARD_SYSTEM.md | Card types, NFC/QR system, production, legacy evolution |
| old__07_ARBITER_SYSTEM.md | ARBITER design, AI integration, voice, stage evolution |
| old__08_DATA_MODEL.md | TypeScript game state schema v0.2 |
| old__09_ACTION_RESOLUTION.md | Resolution pipeline, priority tiers, conflict handling |
| old__10_INFORMATION_HIERARCHY.md | Visibility rules — all game information (ARBITER_ONLY through WEBSITE_PRIVATE) |
| old__11_HARDWARE_SPECIFICATION.md | ESP32 terminals, ARBITER Raspberry Pi unit, laser projector, mat, full BOM |
| old__12_AUDIO_SYSTEM.md | Soundtrack, state cues, ARBITER voice, haptics |
| old__13_NETWORK_ARCHITECTURE.md | Protocol spec (WebSocket), failure modes, OTA updates |
| old__14_WEBSITE_ARCHITECTURE.md | Open Network, Secure Archive, between-session web content |
| old__15_DESIGN_GAPS.md | Remaining design decisions before development — pre-code checklist |
| old__16_DEVELOPMENT_ROADMAP.md | Incremental build sequence, milestone structure |
| old__18_ECONOMY_BALANCE_NOTES.md | Starting resource values, faction economic arcs, balance rationale |
| old__19_PAPER_PROTOTYPE_CORE_DESIGN.md | Paper prototype design philosophy and core requirements |
| old__20_ROUND_WALKTHROUGH_AND_PRODUCTION.md | Complete Round 4 walkthrough for 5-player paper prototype session |

**`/Retired/Paper/`** — 6 files + 1 zip — 1st generation Paper (pre-V1) design suite. Uses current V1 naming convention and current faction names. Early versions of V1 artifacts before the current baseline was established.

| File | Contents |
|------|----------|
| old__THE_SIGNAL_P1___Master_Artifact_Index.md | P1 Master Artifact Index v1.1 — superseded by PM03 |
| old__00___Factions_World_Narrative_Context.md | Artifact 00 v1.3 — superseded by current V1/00 |
| old__01___Game_Board_New_Meridian.md | Artifact 01 — superseded by current V1/01 |
| old__02a___Resource_Systems_Board_State.md | Artifact 02a — superseded by current V1/02a |
| old__02b___Resource_Systems_Tracking.md | Artifact 02b — superseded by current V1/02b |
| old__04b___Action_Taxonomy_Design_Analysis.md | Artifact 04b — superseded by current V1/04b |
| files.zip | Snapshot archive of V1 P1 artifacts as of 2026-05-15: PM01, PM02, PM03, 00, 01, 02a, 02b, 03, 04, 04b |

**`/Retired/backup.zip`** — Complete backup of the /Retired folder prior to reorganization. Contains all 26 files from both the Electronic and Paper generations.

---

## 7. Creative Content Directory

**`/Creative/`** — World-building source material: characters, vignettes, stories, and quotes generated to deepen the world of THE SIGNAL and provide possible source material for Artifact 00 and player-facing flavor copy.

This directory is **not part of the design artifact set.** Content here is evaluated, not assumed canonical. The brief for writers and AI agents lives at `Creative/CREATIVE_BRIEF.md`. Submission tracking lives at `Creative/README.md`.

| Subdirectory | Contents |
|-------------|---------|
| `Creative/Characters/` | Character profiles, histories, voice sketches |
| `Creative/Vignettes/` | Short scenes (100–600 words) |
| `Creative/Stories/` | Longer narratives (600+ words) |
| `Creative/Quotes/` | Standalone voiced moments (1–5 sentences, attributed) |

**Evaluation to canon:** Canon decisions are recorded in PM02. Flavor copy is tagged with a target artifact location in `Creative/README.md`.

---

*End of PM03 — Master Artifact Index v2.2*
