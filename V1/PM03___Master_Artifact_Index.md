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
| 00 | Factions & World | 1.7 | 🔄 Needs Re-Sign-Off — S99: §14.10 Integration added (material — new narrative anchor). Prior: ✅ S93 (L211) | Factions, world, narrative context, ARBITER nature, timescale perspectives. Design Pillar 6 (§5), four-register system (§9), §14 Narrative Anchors incorporated. S33: ring renames. S34: re-sign-off. S38: Dispatch Token anchor §14. S39: §5 Pillar 1 revised ("The Overview is Truth"); §8 MIRROR origin narrative, holographic projection metaphor, Terminal definition; 00-04 closed (Quarter fix). S40: 00-07 multicultural texture (§6 Chorus Node first team, §8 season/cycle, §7 Guild generational building); §11 + §14 Faction Representative (L155). S54: §7 Doctrinal Alignment Pentagram rewritten (L174 — clockwise arrangement, 10 pairs, pentagram geometry). S57: §7 redesigned — shape language removed (header → "Inter-Faction Doctrinal Alignment"), three faction doctrine inserts (Guild/Syndicate/Directorate), Missing Author Vacuum paragraph added; re-signed off v1.6. S91: §8.1 added (faction private/public boundary narrative — grounds Faction Screen, Faction Terminal, Faction Resolution Grid); §9.6 "What The Table Sees" added (ARBITER's processing/revealing threshold — grounds ARBITER Screen, Arbiter Tableau; MIRROR as ARBITER's eyes). PM02 L209. S99: §14.10 Integration added (human-awareness-level narrative anchor; return channel framing; TrueState §11 open question on ARBITER's true perspective). Material change — re-sign-off required. Open: 00-09 (World Conditions panel); 00-15 (full narrative revision). |
| 00a | Governing Rules & Design Policy | 0.8 | ✅ Signed Off — S83 | 46 rules (R01–R40 + R06a, R13a, R13b, R29a, R29b, R40a). S67: Governing Rule 6.1 added (L187); Governing Rule 7.2b + Governing Rule 6.1a added (L188); Governing Rule 6.1 relocated §9→§3. S68: Governing Principle — ARBITER Cognitive Efficiency added to §1 (parent of Governing Rule 6.1 and Governing Rule 6.1a; design question: how can this narrative function be implemented while impacting ARBITER as lightly as possible?); Governing Rule 6.1 + Governing Rule 6.1a source references updated. Pending re-sign-off. S38: Governing Rule 7.3c (Dispatch Tokens). S40: stale migration notes removed; §11 Punch List removed; findings decay rule fix. S57: Governing Rule 10.1 added (Missing Author Vacuum; L177). S61: Art 04 §5 P19 updated (4-type duration taxonomy — Immediate/Transient/Seasonal/Permanent); Art 04 §5 P20 rewritten (partial payment model — full/partial/zero thresholds); Governing Rule 10.1a added (Missing Author Vacuum — renamed/renumbered from duplicate Governing Rule 10.1); Governing Rule 7.3c revised (covers both covert ops and public acts). Signed off v0.4 (L182). |
| 00b | Analysis Readiness | 0.3 | ✅ Signed Off — S83 | Restructured S83: document now tracks DB migration status to enable deep game analysis and computational balance work. DB is authoritative for migrated entities (see Database/schema_reference.md). Retains: L108 pointer (→ 00a §11), lookup tables for 5 non-DB entities (DT-xx, RO-xx, IL-xx, PS-xx, PB-xx), migration punchlist (16 entities — 1 ready to model, 7 pending migration/schema, 8 pending design), component_positions spec, derivation architecture note (unconfirmed — verify before DB-13). L108 standard migrated to 00a §11 (v0.8). |
| 00c | Economy Manifest | 0.4 | 🔄 Partially Populated — Active Reference | Calibration reference aggregating from 02a v1.4, 02b v1.5, 03 v1.7. §3 Starting Assets (resources, components, tracking scales), §4 Resource Generation Rates (district base values, level modifiers, affinity bonus, structure bonus, passive generation, Findings decay, Public Standing drift, Translation rates, Guild Portrait bonus, Residential Quarter multiplier), §6 Operation System (M-01–M-12 modifier table, base difficulty thresholds, critical bands, Public Standing roll reference), §8 Derived Cost Analysis stub (formula and column spec in place; data blocked on Art 04 completion). §9 Round Income Analysis stub (min-income table in place; expected values require probability model — home TBD, see PM05 00c-02). §5 Card Costs blocked pending Art 04 completion. |
| 01 | Game Board — New Meridian | 2.1 | 🔄 Needs Re-Sign-Off — v2.1 S90 | Complete physical zone hierarchy (40 zones): Table → P1–P6 → Central Area (8 sub-zones) → City → Ring 0–3 → 21 districts. District tiles with hex resource colors. District adjacency map (101 rows). Starting Configuration (Fixed Setup / Faction Starting Tokens / Track Starting Values). §9–§10 Faction Player/ARBITER Tableau stubs (Art 08). S44: §4 Narrative Function added (component anchors: District Tiles/Civic Grid, Influence Level Marker, Tension Markers, Session Timeline, Initiative Strip, Chorus Activity Track/The Seismograph, Accord Documents, Situation Reports); §6 Physical Environment — Zones and Components (renamed from [NEW]); §7–§12 renumbered; all component narrative cross-refs resolved; forward procedure refs removed (01-08 ✅). Open: DB-09 (district_adjacency); 00b-05 (live_state schema, L156). S90: §4 Narrative Function (8 component subsections) migrated to Art 02 §4; §6 Physical Forms table migrated to Art 02 §13; stale Art 02a/02b refs updated; Art 01 now geography/zone-only with pointers to Art 02 (PM05 02-n05). |
| 02 | Components | 2.2 | ✅ Signed Off — S98 (L213) | S97–S98: `applicable_verbs` seeded into all §§5–12 entries; §13 matrix removed — entries are now the source of truth; d10 (DB:119) added to §11; ARBITER Dominance Marker Flip corrected; DB flag corrections + component_metadata seeded (74 rows, DB-42). Open PM05: 02-n17, 02-n21, 02-n22, 02-n25. 02-n07 ✅ S99. Prior: S96 (L212) — Grant Deed (DB:113) added §9; movement_path corrections. | S88 merge from 02a v1.6 + 02b v1.5. S89: §13 comprehensive stub pass (44 rows, all 104 DB-registered components). S90: full scope rewrite v2.0 — 8-section taxonomy (§§5–12); all entries: Design Function + Narrative Anchor + Gameplay Requirements + Physical Form table; orphaned rules → Whiteboard/art02_orphaned_content.md (02-n08). S91 (02-n02 in progress): §§5–12 rubric pass complete. Art 00 §8.1 + §9.6 added (L209) to ground faction private/public boundary and ARBITER threshold components. Scope discipline sweep: all "Full design: Art 03" and "Full design: Art 00b" cross-refs removed (Art 03 = procedure only; Art 00b = DB punch list). DB:47 Modifier token Design Function written; DB:48 target district field added; DB:17/44/100/108 active narrative anchors written. New PM05: 02-n10 through 02-n13, 00-16. S92 (02-n02 complete): §§11–12 rubric pass + GR validation (Resolution Tools · Tracking Systems). Key decisions: DB:47 denominations (5/10/15; obverse/reverse color-keyed); DB:50 single physical strip (5 parallel tracks; behind ARBITER screen); DB:36 renamed Escalation marker (DB-38); DB:23 restructured (8Q × 3M); DB:106/107 sliders (0–100 × 5, crit zones). L210. | Component enumeration by function (§§5–12): Playing Surface · Faction Influence · Resources · Covert Messaging System · Intel & Information · Card Systems · Resolution Tools · Tracking Systems. DB component table is canonical completeness anchor. Design Principles: Scarcity is intentional; Disclosure is designed, not assumed. |
| 02a | Resource Systems: Board State | 1.6 | ⛔ Superseded — S88 by Art 02 v1.0. Moved to Retired/Paper/ S90. | Presence, influence, structures, resource generation — all publicly visible board state. Session 22: Control flag, Established marker, ARBITER Dominance Marker confirmed. Session 38: §8a Dispatch Tokens & The Backlog added — component definition, spend rules (one token per covert op, pass/political exempt), Ghost asymmetry (4 vs 3), The Backlog as named physical token pool distinct from Reservoir. Session 41: §4 Reservoir narrative anchor added; §8a Dispatch Token narrative intro added (executive authorization framing). Session 42: terminology sweep (Quarter, Baryo/The Mid, Deployment marker, Dispatch Case); §8a Narrative Anchor subheader; Art 01 Supply stub resolved; "Round 1" → "Quarter 1" in starting resources table. |
| 02b | Resource Systems: Tracking | 1.5 | ⛔ Superseded — S88 by Art 02 v1.0. Moved to Retired/Paper/ S90. | Chorus Portrait, Public Standing, Intel Tokens — tracking systems alongside the board. Cross-reference audit with 04 pending (PM02 D04-11) |
| 03-init | Game Initialization | 0.3 | 🟡 In progress — §2.8 Broadcast Deck/Effect Deck rows added; §3.9 deck list updated. Remaining: card decks (Art 04 §12), Classified Directives (Art 06.x). |
| 03 | while session(true): Round Structure | 4.8 | ✅ Signed Off — S104 (L217). §24 Resolution State Reference (03-n25 ✅): three states Succeeded/Failed/Voided; Discovered as resolution effect alongside Failed; RO-xx codes removed from Art 03; targeting restriction → face-down model (§9.4.1.0 → §9.4.2.0 Step 0 unified Voided handler). Open PM05: 03a-n01. Prior: S102 (L216) v4.7 — § Primitive Action Model appendix restructured: governing principle surfaced; S97/S101 decision tables removed (DB is source of truth); coherent section flow. Index anchor fixed. v_unlegislated_primitives pass: 6 ❌ prohibit, 4 ✅ permit, 14 seeding gaps — agy task queued. Prior: S101 (L215) v4.6 — 03-n24 Primitive Action Model legality table (26 decisions). S101 (L214) v4.5 — 02-n08 migration. Prior — S97: §22 Primitive Action Model & Legalization Analysis added. Art 03 is the legality source of truth for subject × verb × component combinations. Prior: S88 (L207). | S60: L180 architecture applied — monthly A/B/C/D structure; all factions 4 Dispatch Tokens; face-down = void (Voided Resolution Card component retired); Phase C/D labels removed; Beat 2 renamed "Conditions Set"; §17 = Contested District Resolution; §18 = Month 3 Quarter Notes; §20 = End of Quarter; §21 = The Operation System; Beat 3 Step 12 = Dispatch Case Return (Month 3 only); Beat 4 Step 2 = board state validation; Pass cards removed; Contested/Failed TBD blocks removed. PM05: XA-43 (pass card sweep), XA-44 (Voided Resolution Card sweep), 04-n9 (deployment marker blocking flag) added. S61: Beat 3 Step 12 label "(Month 3 only)" and flavor line removed; Beat 4 Submit Payment promoted to Step 1, steps renumbered 1–13; Gameplay Procedure and Reference Material section breaks added in index and body. Duration taxonomy 5→4 types (Tripwire collapsed into Permanent). Signed off v3.0 (L181). S65: Beat 0 Retained validation; Beat 2 Golden Parachute bribe procedure; Beat 3 partial payment marker source. Signed off v3.1 (L185). S66: Beat 2 pre_loss_calc block removed (schema addition predated sign-off). Signed off v3.2 (L186). S67: §5 Design Principle 6 added (ARBITER Cognitive Load — Governing Rule 6.1); pending re-sign-off (L187). S68: §19 Debrief Actions step added (DebriefActionCard type); §25 updated to cross-reference §28; §28 React Card Rules added (interrupt model, Governing Rule 7.2a compliant). Signed off v3.3 (L189). S81: Beat 2 d100 resolution block added (after Automatic cards; queue order; 8-step procedure; additive crits per §21); Beat 2 header updated (C17/C28 listed; Automatic-first order noted); Beat 3 Step 1 item 4 added (VM-xx → public resolution: announce before Step 2, visible roll at Step 5, announce result at Step 6, remove at Step 8 cleanup). S82: Beat 0 Boost Detection procedure added (floor division; no refunds); Beat 3 Step 3 BM-xx threshold modifier clause; Beat 3 Step 7 all-effects multiply (1+n) / single NS-xx regardless of n; Beat 3 Step 8 BM-xx cleanup; Discovery (Step 7b.i) defined as public reveal — ARBITER announces acting faction + op name + target; Step 7b rewritten (ARBITER applies); Step 7b.i rewritten (faction player applies own board changes); Start of Month 1/2/3 "Active PA Obligations" blocks added (§9/§12/§15 — generalizable; cross-Quarter compatible). v3.4 pending re-sign-off. S83: §§12–16 unified into §9; §9.4.4 Beat 4 + §9.4.5 Close Month written; §10 Resolve District Tension; §11 Quarterly Debrief; §12 Quarter Close; reference sections §13–§19. v4.0 structural sign-off S83. S84/S85: entry/exit all §6 sections; §9.4.0–§9.4.1 restructured; Broadcast Card/Deck/Effect Card/Deck naming; Target Profile sweep; 03-init updated. v4.2. S87: §5 P7 (Step 0 convention); §9.4.2.6.1.0/1.1 (Target Profile return + case contents); §9.4.3.4 item 5 (Beat 4 Target Profile cleanup); §§11–12 restructured (Debrief/Quarter Close §11.0–§12.4); §13 modifier table rebuilt (M-06/M-07 merged, M-11 all/both beats, §13.6 Intel Age table); §14 renamed Apex Activation (flat Steps 0–4); §§15–17 rubric clean; §18 React Rules restructured (§18.0–§18.3); §19 Reserved; §20–21 new reference sections; § Examples rewritten/flagged. Grip review complete. v4.3. Sign-off pending PM05 03-n18 (lifecycle sweep). |
| 03b | Component Lifecycle Register | 0.1 | 🔄 In Progress — S88 initial formalization from Whiteboard. Living document — update when any component entry/exit changes in Art 03. All S88 lifecycle gaps resolved. Open: 03-n06 (Dispatch Packet), 03-n11/12 (sliders), 03-n16 (Target Profile physical design), XA-07 (Status Marker distribution), DB-14/15 (pending agy). |
| 03a | Game Engine Specification | 0.98 | 🔄 In Progress — Tiers 1–3 complete; Tier 4 stub | Code-lite technical companion to Art 03. Tier 1 (State Model): formal game state at each beat boundary using 00b entity IDs. Tier 2 (Phase & Beat Procedures): Quarter_Flow(); Phase_1()–Phase_7() with explicit state mutations for all phases; Beat_0()–Beat_5() for Phase 6 detail (modifier stack summation formula, resolution inequality). Tier 3 (Decision Tables): DT-01–DT-09; Apex_Activation() procedure. Tier 4 stub (modifier balance analysis) — blocked on Art 04 card definitions. |
| 04 | Card System | 0.9.41 | 🔄 In Progress | S71: C31 v1.4 (2:1 cost; boost field; Issues Resolved ✓). C40A stub → §11.8. C41A v2.0 (ElectPlayer covert choice; target_district). C41B v1.0 (ModifierCard; Accord Leverage; Lock manipulation). C42 v2.0 (block-bypass removed; modifier clearing; variable threshold 75−10n). §5 14th checklist row (data schema validation; 04-n68 ✅). §6 boost: BoostExpr | None field added; 04-34/36 superseded. C17 ⚠ re-sign-off pending (04-n50). Signals Analysis BLOCKED (Art 06.x). S70: C17 v1.1 (beat=2 correction; re-sign-off pending 04-n50). C31 v1.1 (Immediate delivery). C40 retired/split (Card A React stub; Card B PA stub). C41 v1.1 split (Card A spec; Card B stub). C42 block-bypass deferral. Signals Analysis blocked (Art 06.x). 04-n48 substantially complete. S75: §5 P19–P25 added (card design constraints from 00a §7 — XA-47 ✅). XA-46 rule ID sweep applied. v0.9.34. S77: Overture full spec written (§11.8; Modifier/Instant/All; outcome addition). §11.7 Outcome addition formalized. P08/P10/C09 updated to blank AccordForm model. S78: P26 locked L199 (Card Narrative Test). Card Story block added §5 (between Design Rationale and Design Checklist). 15th checklist row added. C28 "Breaking News" v2.0 (Network CovertOp; Beat 2 d100; VM-xx visibility marker). C40B "Live Coverage" v1.0 (Network PA; Seasonal; comply/resist hand-visibility model). v0.9.35. S79: C42 v2.2 (boost model; base cost faction×1+native×1+IntelToken; threshold 65−10×n_boost; additive PS scaling). S81: P08 cost → 1 native flat, affinity removed (L200); P10 cost → 1 Capacity + 2 native delivered to target (L201); C09 unchanged — two-action Accord route documented. v0.9.36. S89: C28 Breaking News — Issues Resolved ✓ (04-n75/76 confirmed closed; taxonomy subject soft flag; sign-off pending set-level gates). C40B Live Coverage — Issues Resolved ✓ (04-n77 found in Art 03 §9.0 — missed sweep ref corrected; sign-off pending set-level gates). C01/C03 "Supported by game procedure" checklist cleanup — stale §20 ref removed. 04-n95 added. S95: 04-n70 schema validation fix pass complete — 8 categories: schema violations (C39/C23 faction=All; C36/C42/C38/C41 affinity=None; P05/P13 threshold; C16 resolution=Automatic), 9 missing persistence triples, spec/checklist fixes, notation (C37 public_standing→standing; Overture perspectives={}), structural (C41/P15 ElectPlayer→on_accept/on_decline), EntryExitControls persistence_effect added, P16 DividendMarker world_condition formalized. §6.1 Card class: on_accept/on_decline fields added (ElectPlayer only). §6.2 updated. PM05 04-n98 added (on_accept/on_decline sweep). v0.9.37. | S35: L144 locked (1NF + snowflake schema). C15 signed off. C16 signed off. C16–C20 schema uplift complete (§6 schema, section headers, ring modifier fields — 4 per card). pool_copies deprecated (04-40). Effects normalization queued (04-39). Ring modifier formula working (XA-32). C18/C19 redesign flagged (D-04-02). C20 not yet reviewed. S37: Intel economy cards C36–C42 drafted (04-47 schema pass queued). C17 sign-off unblocked (04-41 closed). C37 SACRIFICE: direct PS track step cost confirmed (develop at 04-47). S49: §5 P1–P15 signed off (C17) — P2 updated, P6 rewritten, P8 new (multiple voices in tension). §11.1 modifier card canonical definition expanded. Taxonomy sweep C01–P18 (Category→Layer; six-layer values). Cross-faction narrative voices C11–C15. Art 04b §5.2 C17 row corrected. S51: C18→Dossier Breach (Information — Reveal — Card hand), C25→Tactical Redirection (Territory — Move — Presence token), C27→Disclosure Loop (Economy — Add — Exposure). Full schema pass C01–C35 — Ring 0–3 modifier fields (C17 canonical format); C13 resolution type fix; C22/C32/C33 resolution fields corrected. S54: doctrine_mod field added to schema (L173); all C01–C17 doctrine_mod populated. L174 doctrinal pentagram locked. S55: L175 taxonomy (C05/C24 Economy→Information). C01–C17 full 12-row checklist sweep (04-60/04-61 ✅). Outstanding Issues documented per card — C09/C10/C11/C13/C15/C16/C17 open. S58: §5a Faction Playstyle Reference added; gap analysis complete — 12 new cards identified. S59: Full covert op design pass complete — all C01–C42 baseline drafted. Design rationale scaffold added C18–C35. C36–C42 migrated from §8 Intel Economy appendix to canonical faction sections (Python spec). New faction cards: Ghost (Station, Full Take, SCIF, Flip, Signals Analysis), Guild (Labor Contract), Directorate (Regulatory Downgrade, Regulatory Freeze), Syndicate (Land Title, Hostile Takeover, Accord Transfer); Standard (Absolute Compromise=C39). Entry/Exit Controls (Directorate PA) written to §10. New components pending Art 02 registration: SCIFRecordCard, TierPenaltyMarker, TierFreezeMarker, EntryControlMarker, LandTitleMarker, ParasiticMarker. PM05 04-n7 closed. S61: §5a Narrative Anchor section added (faction doctrine→mechanic table; pentagram alignment reference); Faction Goals reordered (Anchor first); Ghost goal corrected (Delay — no premature answer to the Chorus); playstyle summaries reformatted to bullet lists. XA-40 (Political→Public Act sweep) ✅. XA-42 (design_reference.md L180 sweep) ✅. C22 Detain updated (L183 — detention zone on Directorate public tableau; Governing Rule 8.3a compliant; NotificationSlip removed; arbiter_note updated). C42 Sanctioned Raid v1.1 (Mandate×2 raised from ×1; PS −1 on success added; design_note updated). C32 Short the Market flagged for redesign (04-n14 — "applied silently" paper prototype incompatible; tagline/code conflict). PM05: 04-n10 (Ghost↔Guild pentagram gap), 04-n11 (Guild↔Network pentagram gap), 04-n12 (Terminal unique zones), 04-n13 (Network modifier/C42 response), 04-n14 (C32 redesign) added. Next: P-series PA pass (P01–P18); Outstanding Issues C13/C15/C16/C17; C32 redesign; 04-n10/n11 pentagram gaps. S63: Checklist template → 13 rows (Persistence added as row 8). `persistence = Immediate` added to 35 C-series Python specs; 9 C-series sign-offs cleared to n/a. P01–P08 design pass complete: Design Pass ✓/Issues Resolved ✓ (P08 Art 06 gaps). P09–P18 design pass complete: Design Pass ✓/Issues Resolved pending 04-n23 (aligned + opposed perspectives). `tmp_card_review.line_start` recalculated for all 75 cards. P05 Expired excluded, P06 floor clause, P07 → Standing/Shift, P08 on-decline intentional. 04-n23 added. Next: 04-n23; C-series re-sign-off; 04-n18. S64: gap card specs complete (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid). Art 04b §5.2 +5 rows. S65: §6.2 cost field redefined (fungible only). §6.6 Expression Parameters added (pre_loss_calc). C37 Sacrifice v1.1 (cost=None; PS in success). C34 Golden Parachute v2.0 (bribe mechanic; retained payment). v0.9.27. S66: Entry/Exit Controls redesigned v2.0 (district target; permanent deployment marker block; persistence_condition). §6.6 removed. persistence_condition added to §6.1/§6.2. C37 affinity=None. 04-n25 closed. 04-n29 + 04-n30 added. v0.9.28. S67 cont.: Regulatory Freeze redesigned v2.0 (PublicAct; card-as-condition; no TierFreezeMarker; self-policing per Governing Rule 6.1a; Issues Resolved ✓). Standing Injunction redesigned v2.0 (PublicAct; card-as-condition; Permanent with dual clearing — trigger OR Phase 21; target_taxonomy field; Issues Resolved ✓). target_taxonomy field added §6.1/§6.2 (L188). Governing Rule 7.2b + Governing Rule 6.1a added to Art 00a (L188). 04-n32 added (target_taxonomy sweep). v0.9.30. S68 pre-compact: C19 Deep Cover v1.1, C23 Tort Interference v2.0 (ex Evidence Preservation; Standard; Accord lock), C26 Leak v1.1 (pre-execution cancel; highest-cost target; cross-resource cost). S68 post-compact: C18 Dossier Breach v1.1 (SIGINT tap / DispatchReport model). C28 Open Channel retired to L2. C24 Surveillance Placement mechanics invalidated (narrative-first rethink pending 04-n41). PM05 04-n38–04-n41 added. v0.9.31. |
| 04a | Card Reference Table | — | ⬜ Not Started | Condensed tabular view of all cards — one row per card, columns: Card ID, Card Name, Card Type, Card Subtype, Card Faction, Beat, Primary Cost, Difficulty, Taxonomy — Category / Function / Subject, Portrait. Full card data stays in Artifact 04; 04a is the lookup and cross-reference layer. Populated after all card reviews complete. Blocked by 04 completion. (Scope confirmed L83.) |
| 04b | Action Taxonomy & Design Analysis | 1.8 | 📝 Draft — S107 audit (L222–L227); re-sign-off required (04b-21, gates: §5.2 card IDs clean + §6.1 cleanup) | Companion to 04. Six-layer system locked S48 (Territory / Economy / Information / Submission / Resolution / Standing). §4 rewritten; §5–§10 swept for layer terminology; §6.1 rebuilt grouped-by-layer with Layer/Function definitions; §9 design principles moved to Art 04 §5 P1–P6. Agent (04b-07) and Beat (04b-08) dimensions deferred to future pass. S55: §4.2/§4.4 updated — Economy narrowed to capital flow only (L175); IntelToken generation classified as Information layer. §5.2 table updated (C05, C24: Economy→Information). S56: §4.6 C27 Source Protection row removed (04-63 ✅ — C27 is now Disclosure Loop, not a Protect card). S64: §5.2 +5 rows (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid) — material addition; pending re-sign-off. S107: Full audit against 00a governing rules. Locked decisions: L222 (Backdate BLOCKED—Intel location constraint), L223 (Regulatory Downgrade/Freeze BLOCKED—InfluenceTier not targetable), L224 (Conceal retired—not card-triggerable), L225 (ARBITER-reveal outside 10.1), L226 (Detain retaxonomized Territory|Move), L227 (Accord Transfer retaxonomized Economy|Corrupt). §4.10 revisions (round-number removed, location constraint documented); §4.13 added (ARBITER-reveal); §5.1/§5.2 (Conceal retired; 5 card annotations); §6.1/§7/§8.2/§8.4 updated. Audit clean: all taxonomy functions verified against 00a. v1.8 draft — re-sign-off pending (04b-21). |
| 05 | Operative & Apex System | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. System structure, operative data format, Apex procedure, Founding Figure slots per faction. Blocked by 04 completion — no card content finalized. |
| 06 | Messaging System | 0.4 | ✅ §9 Signed Off — S83 (L205) | S83: §9 re-signed off (L205) — §9.3 clause vocabulary complete (6 types: +Duration); §9.5 board state as sole compliance basis; §9.8 ACCORD DISSOLVED added to form; §9.10 Transfer collapsed into Alter (Named Party subtype; four alteration types). Form rendering fixed (em dash blanks). S80: §9.3 Accord clause vocabulary written (5 types); §9.4 PS formation mechanic redesigned. S77: §9.4 Formation re-signed off (L198) — blank AccordForm delivery model; cross-Quarter persistence; Debrief-only physical alterations. S69: §9.1–§9.10 Accord governance (L190/L191). §§1–8, 10–13 non-canonical stubs. |
| 07 | ARBITER Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Portrait board tracking, Debrief reward system, resolution beats, four narrative registers (The Record / The Observation / The Reckoning / The Witness — updated session 11), Chronicle, ARBITER script pack. |
| 08 | Player Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Faction board layout, starting assets (provisional), deck selection, classified directives, faction reference card, player setup procedure. |

### Reference Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 09 | Card Production Spec | 0.1 | ⬜ Placeholder | Placeholder. Production-only — no design content (L115). All content blocked pending 04 completion. |
| 10 | Game Manuals | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Player Guide, ARBITER Guide (incl. Translation script table), Setup Guide, Components List (provisional quantities). Pending all upstream sign-offs. |
| 10a | Victory System | 0.1 | ⬜ Placeholder | Placeholder file created. VP source categories, Portrait conversion (design decision required), scoring sequence, vote mechanic, tiebreakers. |
| 11 | Visual Design System | 0.1 | ⬜ Placeholder | Placeholder file created. Faction colors per Artifact 00 §7. Three narrative registers framework. Component standards. V01–V19 priority table. Ghost/Network color adjacency flagged. |

### Project Management Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| PM01 | Project Charter & Work Breakdown | 1.6 | 🔄 Active | Scope, deliverables, WBS (with production cost estimates), documentation standards, governance rules, reference convention. §§10–12: Playtest Readiness Checklist, Risk Register, Go/No-Go Framework for V2. §2: Replayability core assumption; S3/S4/S6 extended. WBS 2: 40 components (2.01–2.40), $115–270 est. |
| PM02 | Decision Log & Validation Tracker | 4.0 | 🔄 Active | Locked decisions (L01–L150). S37: L145–L150 (Double Case Pass, Dispatch Tokens, Ghost token gate, Intel universal currency, Intel decay, Month canon term). §2b punch list archived — live version in PM05. |
| PM03 | Master Artifact Index (this document) | 2.4 | 🔄 Active | Artifact registry, standard artifact template, dependency map, retired artifacts index (/Retired/). Design standards and conventions moved to PM04 §2. |
| PM04 | Glossary & Data Dictionary | 0.7 | 🔄 Updated — Active | Single source of truth for all terminology and design conventions. §1: In-World Data Dictionary — Component Physical Glossary added (S34); Asset token removed. §2: Design Terminology — Category column pattern (S34), L109 Component Terminology Standard (S34) added alongside existing conventions. |
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
