# THE SIGNAL — Project Save State
## Complete Context Document for Session Handoff

**Last Updated:** 2026-06-30 — Session 130 Close

### Session 130 Summary (2026-06-30)

**Focus:** agy Art 01 report ingestion + Art 01 v2.3 sign-off + Guild deficit pass (−4 → −2).

**Key work:**
- **Art 01 agy report ingested (L238):** §6.5 District Adjacency Map rewritten (Ring+Address schema); NM_Overlay.svg labels updated (ADD:R.P format); district_adjacency DB migrated (FK via game_zones, 92 rows). PM05 01-04 updated, DB-09 ✅.
- **Art 01 v2.3 signed off (L239):** 02-n05 ✅. 01-n03 created (§7/§8 Faction/ARBITER Area SVGs — gates 01-n01).
- **GUI.PA.9 City Ledger ✅:** Standing/Shift/StandingMarker PA; N = structure cluster count; +N PS success; successcrit +1 district.native per qualifying district; failcrit −N PS. 04-n130 ✅.
- **GUI.CA.9 Works Guarantee ✅:** Beat 2 Automatic ModActionCard; named Guild d100 CA fires without roll in two districts simultaneously. 04-n127 ✅.
- **GUI.PA.10 Joint Development ✅:** Territory/Add/StructureBlock PA; cost 2 Cap + 1 target.native; both factions Present + no structure gate; success = target structure block + Guild +2 PS / target +1 PS; successcrit = Guild structure + Presence Token; failcrit = −1 PT both factions. 04-n132 ✅.
- **GUI.CA.10 Development Order ✅:** Automatic CA; 3 Cap + 1 district-native; delivers GD-01 Grant Deed. Addresses 04-n119 (§9.2 cross-resource ceiling gap). 04-n119 ✅.
- **GD-01 Grant Deed ✅:** New ARBITER-issued ModReactCard (Art 04 §12b); trigger: `structure_block.placed(district=deed.district)` (fill-in-the-blank); effect: +1 Presence Token + 1 Structure Block for holder. Produced by SYN.CA.8 and GUI.CA.10. Trigger vocab extension pending 04-n27. Component registration pending 04-n26.
- **Ref fixes:** "Phase B" → "§9.2 Public Declaration" in design_reference_card_system.md (3x) and ref_card_types.md (1x). ARBITER-issued ModReactCard pattern added to ref_card_types.md. District-scoped trigger pending note added to design_reference_card_system.md. SYN.CA.8 updated (confirmed GD-01 fire effect).
- **Art 04 → v0.9.61.**

**Artifacts updated S130:** Art 01 (v2.3 ✅) · Art 04 (v0.9.61) · PM02 (L238/L239) · PM03 (Art 01 v2.3, Art 04 v0.9.61) · PM05 (01-04, DB-09, 02-n05 ✅; 01-n03, 04-n132, 04-n119 closed) · SESSION_BRIEF · Whiteboard/design_reference_card_system.md · Whiteboard/ref_card_types.md · Claude_context.md (pruned)

---

### Session 129 Summary (2026-06-28)

**Focus:** agy handoff ingestion + 09-06 structural work (§11.8 → faction sections migration) + ref file sync.

**Key work:**
- **agy handoff ingested:** S128 ModReactCard stub pass summary read. Items 2 & 3 confirmed done in S128 (§8 index complete; all stubs in full §6 schema). Claude_context.md pruned.
- **§11.8 → faction sections migration (09-06 structural):** 41 faction MOD stubs moved from §11.8 into Guild/Ghost/Directorate/Network/Syndicate sections. Headers promoted h4 → `### CARD_ID — FINAL NAME *(stub)*` — wiki slug router now registers all MOD cards. SYN.MOD.3 orphan code block / duplicate header fixed. OVERTURE (faction=All) remains in §11.8. Wiki build clean — Guild 8, Ghost 8, Directorate 8, Network 10, Syndicate 7 MOD cards confirmed in faction pages.
- **Ref file sync (all queued from S128):** Art 04 §6.3 `accord.removed` added to confirmed trigger set. `design_reference_card_system.md`: `deployment_marker.placed/converted/blocked` added to trigger vocab; accord semantic definitions added; 04-n144 expanded (accord.removed scope, public_standing.shifted, resource.drawn_from_reservoir). `ref_card_types.md` + `ref_procedures.md`: accord semantics + trigger vocab pointer added.
- **Art 04 → v0.9.53.**

**Artifacts updated S129:** Art 04 (v0.9.53) · PM03 (Art 04 → v0.9.53) · Whiteboard/design_reference_card_system.md · Whiteboard/ref_card_types.md · Whiteboard/ref_procedures.md · SESSION_BRIEF (S129 logged; S130 priority set)

---

### Session 128 Summary (2026-06-28)

**Focus:** 04-n110 §5a cross-faction synthesis + 09-06 ModReactCard stub pass (all 5 factions, three-agent: Claude + agy + Andy).

**Key work:**
- **04-n110 ✅:** Cross-faction §5a alignment audit complete. Report: `Whiteboard/card_analysis_cross_faction_n110.md`. Sustained-pressure spectrum: DIR [pole] → NET (L1 thin) → GUI (constructive) → SYN (episodic) → GHO [point-disruption]. Ghost §5a win path fix: Deep Cover → Full Take (burst card). Ghost passive Intel gap → 04-n143.
- **ModReactCard stub pass (09-06 partial):** All 5 faction modifier decks fully stubbed. GHO.MOD.1–8, NET.MOD.1–10, GUI.MOD.1–8, DIR.MOD.1–8, SYN.MOD.1–8. Cross-agent: Claude (GHO.MOD.2–4, NET.MOD.3–6, GUI.MOD.2–4, DIR.MOD.1–5, SYN.MOD.2–3, NET.MOD.2 trigger), agy (GHO.MOD.5–8, NET.MOD.7–10, GUI.MOD.5–8, DIR.MOD.4–8, SYN.MOD.4–8).
- **agy rulings:** `accord.corrupted` = textual alteration via Covert Op. `accord.removed` = breach or expiry. FRG standing condition cards (DIR.MOD.6, SYN.MOD.6) placed face-up on faction FRG for Quarter — no custom marker needed.
- **§6.3:** `broadcast_card.placed` (db25) added to confirmed TriggerExpr vocabulary.
- **§8 index:** All new ModReactCard rows added (38 rows). Art 04 → v0.9.52.
- **PM05:** 04-n143 (Ghost passive Intel), 04-n144 (§6.3 vocab reconciliation), 04-n145 (FRG standing condition schema), 04-n146 (SYN.MOD.3 trigger scope), 04-n147 (React design review checklist). 09-06 status updated. 04-n131 stale reference corrected.
- **Ref files updated:** `ref_card_types.md` (three-subclass architecture), `ref_procedures.md` (ModReactCard FRG standing note), `design_reference_card_system.md` (ModReactCard fields + TriggerExpr vocab).
- **Claude_context.md:** Pruned live (agy S128 report fully ingested).

**Artifacts updated S128:** Art 04 (v0.9.52) · PM05 (04-n143–147 added, 09-06/04-n131 updated) · PM03 (Art 04 → v0.9.52) · Whiteboard/card_analysis_cross_faction_n110.md (new file — §5a synthesis + post-audit stubs §H–M) · Whiteboard/ref_card_types.md · Whiteboard/ref_procedures.md · Whiteboard/design_reference_card_system.md · SESSION_BRIEF (S128 logged; S129 priority set) · Memory/project_art04_card_design_context.md

---

### Session 127 Summary (2026-06-28)

**Focus:** 04-n102 — Modifier card schema definition pass (ModActionCard / ModBattleCard / ModReactCard).

**Key work:**
- **Modifier subclasses (04-n102 ✅):** Three subclasses defined in §6.1. ModActionCard: effect=ModActionExpr, fires with bundled op at Covert Dispatch. ModBattleCard: effect=ModBattleExpr (direction+magnitude), §10 Contested District Resolution. ModReactCard: trigger required (TriggerExpr), fires on publicly observable board state delta, all Card fields live except beat (always None).
- **Card class additions (04-n138 ✅):** `is_unique: bool` + `deck_limit: int | None` added to Card Pool section.
- **ring_origin (04-56 ✅):** `ring_origin: Ring | None` on all three subclasses — None = faction modifier deck, 1/2/3 = ring modifier deck.
- **value_rating:** `int | None` (None = TBD stub only; must be set before design pass).
- **§6.2:** "Modifier Subclass Field Constraints" table — three-column (ModActionCard / ModBattleCard / ModReactCard); ModReactCard column uses `—` for live fields (only `beat` is always None); Pool field rows added.
- **§6.3:** TriggerExpr (full vocabulary, sourced Art 03b + Art 02 — public-only; includes `blocked` for deployment marker Blocked flip), ModActionExpr (4 variants; cost_reduction PA-only), ModBattleExpr.
- **§11.1/§11.7:** "Instant" retired; three-type architecture introduced.
- **Stub terminology sweep:** All 6 existing modifier stubs (Overture, Accord Leverage, Signal Break, Reputational Strike, Return to Site, Clarify Misinformation) updated to proper subclass types; full field redesign deferred to 09-06. §5.1 table entries updated.
- **Terminology fixes:** "Phase A" → "Covert Dispatch" throughout Art 04 + design_reference_card_system.md. "Beat 5 contested district" → "§10 Contested District Resolution". "Beat 5" (Transient cleanup) → "Close Month".
- **§6.2 always-None framing corrected:** Table renamed + restructured after advisor review; ModReactCard column corrected.
- **04-n29 ✅** (sub-item 2 resolved: GR 6.1a self-policing covers all Permanent card persistence including React standing effects; GR 6.1c covers disputes; no Art 03 procedure step needed). Sub-item 1 extracted → 04-n142.
- **04-n142 added:** Counter-card design — permanent PA removal mechanic.
- **DB audit:** 67 Legalized, no new Rules Gaps.
- **Claude_context.md:** NOT pruned — agy report expected; left for S128 ingestion.

**Artifacts updated S127:** Art 04 (v0.9.51) · PM05 (04-n102 ✅, 04-n138 ✅, 04-56 ✅, 04-n29 ✅, 04-n142 added) · PM03 (Art 04 → v0.9.51) · Whiteboard/design_reference_card_system.md (Phase A → Covert Dispatch; persistence monitoring note) · SESSION_BRIEF (S127 logged; S128 priority set)

---

### Session 126 Summary (2026-06-27)

**Focus:** agy S125 audit ingestion — card taxonomy subject corrections + DB tooling.

**Key work:**
- **Card taxonomy fixes (04-n141 ✅):** 7 cards corrected. 5 cards `subject = PublicStanding` → `StandingMarker` (STD.CA.13, STD.PA.4, STD.PA.7, DIR.CA.7, NET.CA.7). NET.CA.1 Leak `subject = District` → `CovertOperation` (S68 correction was also wrong — DistrictTile has no Reveal in comp_verb_phase; card reveals a CovertOperation, not the district tile). GHO.PA.4 BroadcastEffectCard (id 98): 7 entries added to `comp_verb_phase` (Add at phase 2; Remove/Reveal/Invoke at phases 17/18). `StandingMarker` added to `card_subject_map` (id 37). All 7 now Legalized in `v_card_mechanical_alignment`. Art 04 specs updated to match.
- **DB tooling:** `Database/audit_card_alignment.sql` created — card taxonomy alignment diagnostic; surfaces gaps by rules_status (Legalized / Rules Gap / Non-component Subject / Abstract Function). Run after any card spec change or new card addition. Documented in `schema_reference.md §10` with fix pattern for Rules Gaps (3-table chain: card_status + card_subject_map + comp_verb_phase).
- **Ref files updated:** `ref_taxonomy.md` — StandingMarker corrected in subject vocabulary + rule 7 (was PublicStanding); Taxonomy Assignment Verification section added with audit command + gap pattern table. `preload_n102_modifier_schema.md` — step 11 (run audit) + mod card heads-up block added.
- **Memory:** `project_db_design_intent.md` updated — 3-table taxonomy fix pattern + `v_card_mechanical_alignment` as go-to alignment diagnostic.
- **Claude_context.md:** Pruned live (agy S125 report fully ingested).

**Artifacts updated S126:** Art 04 (v0.9.50 — 6 subject field corrections, Leak design_note updated) · PM05 (04-n141 ✅; 04-n130 subject corrected to StandingMarker) · Database/schema_reference.md (StandingMarker in card_subject_map, BEC comp_verb_phase entries, §10 Audit Scripts section) · Database/audit_card_alignment.sql (new) · Whiteboard/ref_taxonomy.md (StandingMarker correction, Verification section) · Whiteboard/preload_n102_modifier_schema.md (audit step 11) · SESSION_BRIEF (S126 logged; S127 priority set) · Memory/project_db_design_intent.md

---

### Session 125 Summary (2026-06-27)

**Focus:** Modifier card schema pre-work + SESSION_BRIEF housekeeping.

**Key work:**
- **SESSION_BRIEF:** Startup delivery section added (accomplishments → focus → sign-offs → prompt). Pending sign-offs corrected: Art 00 v1.8 + Art 01 v2.2 surfaced; card-level sign-offs removed (gated behind 04-n110 + schema normalization).
- **Whiteboard/preload_n102_modifier_schema.md (new):** Full modifier schema pre-work for 04-n102. Three subclasses (ModActionCard / ModBattleCard / ModReactCard); ModActionExpr tagged union (threshold delta · success multiplier · PS shift · cost reduction PA-only); TriggerExpr DSL with examples; ring_constraint as per-card narrative decision; React lifecycle (immediate vs. standing effect); 04-n29 resolved via GR 6.1a + 6.1c — no Art 03 procedure addition needed.
- **Memory:** feedback_session_startup.md (startup delivery format) + feedback_context_bloat.md (ref files first; /compact after glance reads) updated.

**Artifacts updated S125:** Whiteboard/preload_n102_modifier_schema.md (new) · SESSION_BRIEF (S125 logged; S126 priority set) · Memory files (feedback_session_startup.md, feedback_context_bloat.md)

---

### Session 123 Summary (2026-06-26)

**Focus:** STD+NET combined card set audit (04-n90) + 5-faction synthesis tables complete + cross-layer coverage analysis (Resolution/Standing/Information layer gaps).

**Key work:**
- **Whiteboard/card_analysis_STD_NET.md (new):** Full audit — 12-card coverage; Sections A–G. CA.1 Leak = only cross-ceiling card in 5-faction set (E×1+F×1; Findings-gated → 04-n126). 4 Reveal cards = highest Reveal concentration in game. Modifier deck = largest §5a gap (04-n4 gate). Win path expansion STD-dependent (FLAG 5).
- **Art 04b v2.6:** §6.4 STD+NET 5-check added; §8.3 Network section rewritten with S123 12-card data (replacing S104 7-card data); priority design targets listed (04-n126, PA.3 borderline inversion, modifier deck).
- **5-faction synthesis complete:** Synthesis tables in all 5 prior audit files updated from "4-faction, NET pending" to "5-faction, complete"; Network row added to each. Cross-faction reference tables (MOD inventory · Standing gap · STD outstanding issues) added to §A of DIR/GUI/SYN/NET audit files.
- **Cross-layer coverage analysis:** Resolution layer — STD-only for GHO/GUI/NET/SYN (DIR has CA.8 Enhanced Scrutiny); GHO excluded (no doctrinal basis); GUI/NET/SYN → 04-n127/128/129. Standing layer — GUI/SYN gaps → 04-n130/131. Guild Information — doctrinal weakness confirmed as correct absence.
- **PM05 additions:** 04-n90 ✅; 04-n126 (NET §9.2 cross-ceiling Findings-gated); 04-n127 (GUI Resolution — construction certainty); 04-n128 (NET Resolution — broadcast irreversibility); 04-n129 (SYN Resolution — money at the table); 04-n130 (GUI Standing — deed-based PS); 04-n131 (SYN Standing — relative model vs. PS floor, playtest gate); 00a-78 STD+NET complete.
- **Environment:** WireGuard VPN + mosh on Pi 5 operational (agy report ingested). Wiki rebuilt with 8-chapter Art 04 split for iOS WebKit; wiki is mobile review surface for large file review.

**Artifacts updated S123:** Art 04b (v2.6) · PM05 (04-n90 ✅; 04-n126–04-n131; 00a-78) · Whiteboard/card_analysis_STD_NET.md (new) · Whiteboard/card_analysis_STD_GHO/DIR/GUI/SYN.md (§A tables + 5-faction synthesis) · SESSION_BRIEF (S123 logged; S124 priority set)

---

### Session 124 Summary (2026-06-27)

**Focus:** Whiteboard housekeeping + Art 04 §10 / Art 03-init §3.9 (deck construction model) + DB component_metadata complete (agy).

**Key work:**
- **Art 04 §10 added — Deck Construction & Pool Selection** (v0.9.49 → 0.9.50): per-faction selection from larger pool; CA/PA/Modifier subsets + 1 Operative + 1 Apex; Standard cards held by each faction; deck sizes deferred to balance pass (04-n136); pointer to Art 03-init §3.9.
- **Art 03-init §3.9 added — Deck Selection procedure** (v0.4 → 0.5): 5-step simultaneous per-faction selection + ARBITER deck assembly (Ring Modifiers ×3, Broadcast, Broadcast Effect, Battlefield Modifier); §3.6/§3.9 sequencing conflict flagged → 04-n137.
- **Whiteboard pruned:** card_ideas_20260626.md Sections 1 + 4 pruned (canonized into Art 04/03-init and PM05); Section 3 retained for 04-n110; component_metadata_and_database_strategy.md pruned to Phase 3 stubs.
- **PM05 additions:** 04-n132–04-n140 · 03-n26 · DB-44/45/46 · 09-15 · modifier card design elevated (04-n102/09-06). DB-41/42/43/45/46/37 ✅ S124.
- **DB (agy):** component_metadata table seeded (74 components, Option A hybrid wide); Phase 1 lookup tables complete (resolution_outcome + 2 missing rows: Discovered + Auto-failed; notification_slip; intel_delivery_slip); 3 derived views (v_component_accommodates, v_component_contains, v_component_held_by); schema_reference.md updated.
- **Art 02:** DB Sync note added to header (non-material, no re-sign-off).

**Artifacts updated S124:** Art 04 (v0.9.50 — §10 added) · Art 03-init (v0.5 — §3.9 full procedure) · PM05 (04-n132–04-n140, 03-n26, DB-44/45/46, 09-15; DB-41/42/43/45/46/37 ✅) · Art 02 (DB Sync note, non-material) · Database/schema_reference.md (component_metadata, Phase 1 lookups, slip tables, views) · SESSION_BRIEF (S124 logged; S125 priority set)

---

### Session 121 Summary (2026-06-26)

**Focus:** STD+DIR combined card set audit (04-n89) + PM05 items for open design decisions.

**Key work:**
- **Whiteboard/card_analysis_STD_DIR.md (new):** Full STD+DIR audit — coverage map, beat distribution, doctrinal assessment, win path tension, Ghost differentiation, §5a verdict (Sections A–G).
- **Art 04b v2.3:** §6.4 STD+DIR Economic Integration Audit added (5-check framework); §8.2 Directorate section fixed — DIR.PA.1 now Territory|Modify|PresenceToken (04-n99 ✅ S118), DIR.PA.2/CA.6/CA.7/CA.8 added to active set, stale BLOCKED note removed.
- **PM05 additions:** 04-n89 ✅; 04-n111–117 (7 DIR card design reviews from Section C); 04-n118 (§9.2 cross-resource ceiling gap — 11/12 mono-Mandate inverts §9.2 floor/ceiling principle for high-power DIR cards); 00a-78 updated (STD+DIR S121 ✅, DIR flagged as §9.2 gap faction).
- **Key findings:** DIR economy near-mono (11/12 Mandate-only; CA.5 is the sole cross card); Beat 2 cluster (4 of 8 CAs) is the doctrinal signature — unique in the faction set; Ghost vs. DIR differentiation settled (Ghost = point-disruption/reactive/zero standing conditions; DIR = sustained pressure/proactive/3 standing-condition PAs); §9.2 adherence gap — high-power effects (PA.3, PA.6, PA.1) priced at mono; DB cost_type=mono for DIR.CA.5 is stale (flagged E2).
- **SESSION_BRIEF:** S121 logged complete; S122 priority set to STD+GUI (04-n92) with fully explicit startup instructions matching audit pattern.

**Artifacts updated S121:** Art 04b (v2.3) · PM05 (04-n89 ✅; 04-n111–04-n118; 00a-78) · Whiteboard/card_analysis_STD_DIR.md (new) · SESSION_BRIEF

### Session 120 Summary (2026-06-25)

**Focus:** DB cost analysis completion + STD+GHO combined card set audit (04-n87/88).

**Key work:**
- **card_status cost columns (5 new):** cost_type ENUM('mono','cross','free'), cost_variable TINYINT(1), cost_primary_amount INT NULL, cost_native_count INT NOT NULL DEFAULT 0, uses_intel_token TINYINT(1). All 90 non-blocked cards seeded. Distribution: mono/fixed=58, mono/variable=4, cross/fixed=14, free/fixed=14; Intel Token cards=12. cost_type = native resource axis only; uses_intel_token is orthogonal.
- **schema_reference.md:** Cost columns + full design notes block (STD card rule, Intel Token orthogonality, distribution stats).
- **Art 04b v2.2:** §6.4 Economic Integration Audit written — STD all 5 faction natives verified; Ghost Flip→Synthesize→Deep Cover pipeline confirmed; playtest calibration flag for STD.CA.6/7/8/9. 04-n87/88 gates cleared.
- **STD.CA.12 resolved:** Beat 1 CM timing (Art 03 §9.4.1.2) makes Type A/B distinction moot for Beat 2 targeting. GR 7.2b no-refund confirmed. issues_resolved=1.
- **DB issues_resolved:** GHO.PA.3/4/5 ✓; STD.CA.12 ✓; STD.PA.8 ✓; GHO.CA.6 note updated.
- **Ghost §5a flavor assessment** (card_analysis_STD_GHO.md Section F): Flip→Deep Cover pipeline landing well; thin areas identified — no passive Intel generation card; only one Flip endpoint (Deep Cover); §5a "burst card" description stale post-S113. CA/PA = doctrinal core; Modifier decks = gap-fill space.
- **ref_procedures.md:** CM-A/B mechanics added explicit — CM cards discarded at end of Beat 1; not valid Beat 2 targets.
- **PM05:** 04-n108 (Standing card gap — GHO/SYN/GUI); 04-n109 (STD.CA.6/7/8/9 playtest calibration); 04-n110 (cross-faction §5a alignment audit — gate: all 04-n87–92 substantially complete).
- **Sign-off protocol confirmed:** No individual card sign-offs until all 6 faction set audits substantially complete; consolidated passes only.

**Artifacts updated S120:** Art 04b (v2.2) · Art 04 (v0.9.49 — STD.CA.12 clean) · PM05 · Database/schema_reference.md · Whiteboard/card_analysis_STD_GHO.md (Section F added) · Whiteboard/ref_procedures.md · DB card_status

### Session 119 Summary (2026-06-25)

**Focus:** GHO design decisions closure + Art 00a sign-off + Art 04b doctrine statement + STD audit prep.

**Key work:**
- **GHO.CA.5 Misdirection v2.0:** Information|Corrupt|IntelToken — targets faction_name field on publicly placed FRG token. L222 compliant. Issues Resolved ✓.
- **GHO.CA.6 Synthesize v1.1:** Token keying locks to consumed token's faction key. Enables Gather→Synthesize→Flip pipeline.
- **GHO.CA.1 Pattern Match v2.0:** Full redesign — Submission|Redirect|CovertOperation steal model. Fizzle if Ghost cannot supply copied op's cost.
- **STD.CA.12 Absolute Compromise:** Scope confirmed CA-inclusive. ARBITER sweeps both covert grid and FRG at Beat 2.
- **Art 00a v0.11 ✅ signed off (L237):** §9.2 Cross-Faction Resource Economy; §3 Governs Field revised; Copy Design Principle added.
- **Art 04b v2.1:** §6.1 Information|Reveal|Named faction retired; 4 ARBITER-domain Reveal subjects added. §8.0 Standard doctrine statement written (gate for 04-n87 cleared).
- **Art 04 v0.9.49:** P28 (cross-faction cost floor constraint) added; 04-n87 Design Pass cleared.
- **PM05:** 04b-23 (Submission|Redirect L×F validity check); 00a-77/78/79.
- **PM02 L237:** Art 00a §9.2 locked.
- **Art 04b §6.1 updated:** Information|Reveal|Named faction retired (S119); SubmissionStatus / DispatchTokenCount / ResourceCommitment / ModifierStackComposition added as ARBITER-domain Reveal subjects.

**Artifacts updated S119:** Art 04b (v2.1) · Art 04 (v0.9.49) · Art 00a (v0.11 ✅) · PM02 · PM05 · Whiteboard/ref_design_pillars.md · Whiteboard/card_analysis_STD_GHO.md (created)

### Session 118 Summary (2026-06-25)

**Focus:** Full component naming standardisation sweep — DB canonical Title Case + stale renames across all artifacts and ref files.

**Key work:**
- **Art 04 v0.9.47:** §8 DIR.PA.1 corrected (Territory|Modify|PresenceToken); §9 GHO.PA.2 regrouped (Resolution|Modify|Covert Operation); §8/§9 subject sweep to DB Title Case (~124 cells). PM05 04-n99 DIR.PA.1 ✅ closed.
- **DB `component` table:** 46 records updated to Title Case ("Presence chip" → "Presence Token", "Political act" → "Public Act", "Accord agreement" → "Accord Agreement", "Arbiter Tableau" → "ARBITER Tableau", etc.).
- **Art 02 v2.5:** Full sweep — headings, component_name metadata, body prose. Stale renames applied (Presence chip, Political act family).
- **All V1 artifacts swept (20 files):** Art 00 (v1.8) · Art 00a (v0.10) · Art 01 (v2.2) · Art 03 (v4.11) · Art 03-init (v0.4) · Art 03a (v0.99) · Art 03b (v0.2) · Art 04b (v2.0) · Art 05–11 (→ v0.2) · PM02 (v4.1) · PM04 (v0.9). Parallel agent deployment — all clean, zero residuals.
- **Whiteboard ref_*.md + design_reference.md + schema_reference.md:** 14 files, 13 changed. schema_reference.md heaviest (54 term types).
- **L236 locked (PM02):** DB `component.name` = canonical source of truth; Title Case rule; Python spec pseudo-PascalCase exempt.
- **PM04 L109 updated:** DB authority + Title Case rules added; stale rows removed (Operational marker, Operation Resolution card, Pass card).
- **Grip fix:** Wide table CSS via local API shim (grip_local_api.py) — container max-width removed.

**Artifacts updated S118:** DB · Art 02 (v2.5) · Art 04 (v0.9.47) · Art 00 (v1.8) · Art 00a (v0.10) · Art 01 (v2.2) · Art 03 (v4.11) · Art 03-init (v0.4) · Art 03a (v0.99) · Art 03b (v0.2) · Art 04b (v2.0) · Art 05–11 · PM02 (v4.1) · PM03 · PM04 (v0.9) · All Whiteboard ref_*.md

### Session 117 Summary (2026-06-24)

**Focus:** DB prep for card set audits — card_status taxonomy columns + card_subject_map bridge table.

**Key work:**
- **card_status extended** — 4 new columns: `layer` / `function` / `subject` (VARCHAR) / `beat` (INT, NULL). Taxonomy seeded from Art 04 §8; 77 of 95 cards have spec-accurate values (Python parser vs. full card specs); 18 stubs/BLOCKED have §8-level accuracy only.
- **Beat semantics locked:** Resolution beat, not submission beat. 27 CA=2 (early-intervention: block/protect/modify/interfere), 35 CA=3 (standard covert grid), 27 PA=4, 6 MOD/DA=NULL.
- **Data corrections:** 15 NULL card_ids backfilled (pre-ID-04 renumber); 3 card_type bugs fixed (Regulatory Downgrade/Freeze CA→PA, Accord Leverage CA→MOD).
- **component table renames:** id=1 "Presence chip" → "Presence token" · id=14 "Political act" → "Public act".
- **card_subject_map created** — 25-row bridge table (subject PascalCase → component_id); enables joins from card_status into all 27 gap views via component table.
- **§9 Coverage Matrix** — now DB-derivable as live pivot from card_status (WHERE blocked=0); no longer a separately maintained table.
- **schema_reference.md updated** — all S117 changes documented.

**Carried to cleanup:** §8 DIR.PA.1 index entry wrong (Submission|Block|PublicAct vs. spec Territory|Modify|PresenceToken) · §9 GHO.PA.2 subject label grouping error.

**Artifacts updated:** DB (card_status columns + card_subject_map + component renames) · schema_reference.md · SESSION_BRIEF

### Session 112 Summary (2026-06-21)

**Focus:** Ghost CA design pass — GHO.CA.7/8/9/10/12 Issues Resolved; Source Substitution redesigned.

**Key work:**
- **GHO.CA.7 Station** ✅ (S112) — Information|Add|IntelToken. d100 threshold 55. Sustained collection platform against named faction; 2 tokens on success / +1 on successcrit. Failcrit: NotificationSlip to target. ring_mod {0:−15, 1:−10, 2:0, 3:+10}. 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.8 Full Take** ✅ (S112) — Information|Add|IntelToken. d100 threshold 40. Variable cost n×Findings declared at submission; success = n×2 tokens / successcrit +n / failcrit = NotificationSlip. 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.9 SCIF** ✅ (S112) — Cleanup pass (Issues Resolved was ✓ S94). Faction-targeted; Automatic; no district target; adjacency rule correctly excluded. Card Story updated.
- **GHO.CA.10 Flip** ✅ (S112) — Information|Reveal|IntelToken. Automatic. Cost: 1 Intel token (target-keyed). Success: 2 of target's native resources (copy model — target pool untouched). 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.12 Source Substitution** ✅ (S112) — REDESIGNED. Information|Corrupt|IntelToken. Automatic. Cost = CA slot only. Alters faction_name field on submitted Intel token; ARBITER returns altered token to Ghost's case. Token can then be used on cards restricting Intel token faction to match the target. Plant mode retired — Intel tokens are valid premium currency regardless of faction field; planting a token doesn't trap the recipient. Issues Resolved ✓.
- **PM05 04-n6:** Field collection op adjacency restrictions fully resolved (Station/Full Take/Flip). SCIF and Source Substitution correctly excluded. Remaining sub-items: 00a rule text update + design_reference.md update (deferred).

**Decisions locked:** Source Substitution re-key model (plant mode retired; Automatic; cost = CA slot) · Flip copy model (target pool untouched; Ghost gains 2 native resources)

**Artifacts updated:** Art 04 (v0.9.43 — GHO.CA.7/8/9/10/12 design passes) · PM05 (04-n6 updated) · SESSION_BRIEF · PM03

### Session 111 Summary (2026-06-21)

**Focus:** Syndicate gap card design pass — three Tier 1 cards completed; Art 02 v2.4 signed off.

**Key work:**
- **Art 02 v2.4 signed off** (L233, S111) — DB:48 Target Profile `declared_params` field added: free-form text blank line for card-specific declarations. Enables SYN.CA.11 (clause + new value), SYN.CA.10 (incoming party), SYN.PA.3 (N + consideration), and future declaration-requiring cards.
- **SYN.CA.11 Redline** ✅ (S111) — Information|Corrupt|AccordAgreement. d100 threshold 50. Alters numeric/ordinal fill-in on active Accord form; ARBITER makes physical alteration per Art 06 §9.10 Alter/Terms. declared_params: clause + new value on TP. Design Pass ✓ / Issues Resolved ✓.
- **SYN.PA.3 Data Acquisition** ✅ (S111) — Information|Reveal|IntelTokensHeld. ElectPlayer Beat 4. declared_params: N (tokens requested) + consideration (verbal offer — free text). Three paths: trade (bilateral exchange) / show (reveal all tokens face-down) / decline (Syndicate −2 PS → Permanent). Permanent React: target's next PA with Target Profile → Syndicate replaces it; card discards. Table-enforced throughout. L234: consideration non-fulfillment → card stays Permanent. Design Pass ✓ / Issues Resolved ⚠ (04-n88 balance review).
- **SYN.CA.10 Accord Transfer** ✅ (S111) — Economy|Corrupt|AccordCard. d100 threshold 50. Named party replacement on active Accord form; ARBITER announces publicly at Beat 3. Crit success: incoming party elects one numeric term change at the table. No consent required (Art 06 §9.10 confirmed L205). Outgoing/incoming party may be Syndicate. Design Pass ✓ / Issues Resolved ⚠ (balance review).
- Art 04b §5.2: +2 rows (SYN.CA.11, SYN.PA.3); SYN.CA.10 note updated; §8 Syndicate summary updated.
- PM05 04-n106 added: Art 04 §6.1 declared_params field addition + all-card sweep (gate: none).

**Decisions locked:** L234 (SYN.PA.3 — consideration non-fulfillment → card stays Permanent; bluff mechanic intentional) · L233 (Art 02 v2.4 — Target Profile declared parameters field)

**Artifacts updated:** Art 02 (v2.4 ✅ L233) · Art 04 (v0.9.42) · Art 04b (§5.2/§8) · PM02 (L233–L234) · PM03 (Art 02/04 rows) · PM05 (04-n106) · SESSION_BRIEF · design_reference_card_system.md

### Session 109–110 Summary (2026-06-20)

**Focus:** Ghost PA/React design pass (GHO.PA.3–5 + GHO.MOD.1); Art 03 v4.10 procedural changes (Target Profile face-down model + VM-xx lifecycle).

**Key work:**
- **GHO.PA.3 Declassified Records** ✅ (S109) — Information|Remove|IntelToken (expired). Boost model: expired tokens → BM-xx multiplier ×(1+n). Art 03 §9.4.3.1.0.0 boost detection sub-step added.
- **GHO.PA.4 Public Threat Assessment** ✅ (S109) — Information|Reveal|BroadcastEffectCard. Automatic; GR 10.1b obligates ARBITER reveal. Art 02 DB:48 target-object field added. Art 03 §9.4.3.3.0 / §9.4.3.1.3 clauses added.
- **GHO.MOD.1 Clarify Misinformation** ✅ (S110) — Redesigned from GHO.PA.5 seed → ModifierCard/React. Information|Remove|IntelToken. Trigger: any PA placed with Intel token at §9.2.0. Prediction resolution — Ghost declares faction named on token; correct → PA cancelled, resources drained to Reservoir, Ghost +1 PS. Intelligence-gated: Target Profile face-down at §9.2.0 means Ghost must have prior SIGINT to fire reliably.
- **GHO.PA.5 Agency Recruitment Fair** ✅ (S110) — Territory|Add|PresenceToken. Renumbered from PA.6 (PA.5 slot vacated by MOD.1 redesign). Cost: 1 Findings. Restriction: district.resource_type == Findings (University Perimeter, Data Exchange, Research Institute, Chorus Research). Success: +2 chips. Successcrit +1 PS / Failcrit −1 PS. Ring3 +10 / Ring1 −15.
- **Art 03 v4.10 signed off** (L232, S110) — §9.2.0 Target Profile placed face-down at PA declaration; §9.4.3.1.1 (Apex Check) Target Profile flipped face-up. VM-xx lifecycle formalised: §9.4.1.1 BEC step extended; §9.4.2.2.0 VM-xx placement clause; §9.4.3.1.3 per-PA BEC check; §9.4.3.3.0 generic VM-xx placement. STD.PA.4 + STD.PA.5 arbiter_notes corrected (Phase B → §9.2.0/§9.4.3.1.1). Folded into existing L232 sign-off.
- **Art 02 v2.3 signed off** (L231, S109) — DB:48 Target Profile target-object field added.
- Art 04b §5.2/§7/§8.1 updated: GHO.PA.5 + GHO.MOD.1 added to coverage table and matrix.

**Decisions locked:** L232 (Art 03 v4.10 — Target Profile face-down + VM-xx lifecycle) · L231 (Art 02 v2.3 — Target Profile target-object field)

**Artifacts updated:** Art 03 (v4.10 ✅ L232) · Art 02 (v2.3 ✅ L231) · Art 04 (v0.9.42) · Art 04b (§5.2/§7/§8.1) · ref_procedures.md · README

**Next (S112 Tier 1):** Ghost covert op design pass — GHO.CA.7 Station · GHO.CA.8 Full Take · GHO.CA.9 SCIF · GHO.CA.10 Flip · GHO.CA.12 Source Substitution (GHO.CA.11/13/14 BLOCKED)

### Session 108 Summary (2026-06-20)

**Focus:** Art 04b v1.8 §4/§5 structural audit; Art 04 spec fixes (04-n103/104/105); Art 00a GR 10.1b formalization; Ghost PA/React design seeds.

**Key work:**
- Art 04b v1.8 signed off (04b-21 ✅). §4 audited — historical noise dropped; taxonomy definitions moved to §5.1; GR 7.2b/9.1/10.1 added as design grounds (§4.14–4.16); §4.8 rewritten as GR 10.1b corollary. §5.1: Valid Layer × Function matrix (60 cells, 17 invalid), Visibility column, React/Instant/Interrupt paragraph. §5.2: sorted ascending by card ID; Visibility column; BLOCKED card taxonomy filled (GHO.CA.13/14, DIR.PA.1/4/5). §8.1 Ghost: BLOCKED guidance + 4 new PA/React design seeds (GHO.PA.3–6); BroadcastEffectCard (DB:98) mechanic locked for GHO.PA.4. Sign-off scope policy: §4/§5 = re-sign-off required; §6–9 = working sections, no re-sign-off.
- Art 04 spec fixes ✅: GUI.CA.2/CA.6 Recover→Add; GUI.CA.6 variable named; Backdate + Field Verification marked 🚫 BLOCKED; Regulatory Downgrade + Regulatory Freeze marked 🚫 BLOCKED; DIR.CA.2 Detain Remove→Move (04-n103/104/105 closed).
- Art 00a v0.9 signed off (04b-22 ✅): GR 10.1b added to §10 (ARBITER disclosure outside discretional model; Portrait sole exception; Governs: 03, 04, 07). Art 04b §4.8 footnote cleaned.

**Decisions locked:** GR 10.1b (Art 00a §10.1b — ARBITER-reveal outside discretional framework) · Broadcast Card/BEC two-component split (DB:25/98) documented in ref_taxonomy.md · Art 04b §4/§5 sign-off scope policy.

**Artifacts updated:** Art 00a (v0.9 ✅); Art 04b (v1.8 ✅ locked); Art 04 (spec fixes — no version bump); PM03; PM05 (04b-21/22 ✅, 04-n103/104/105 ✅); SESSION_BRIEF; design_reference_card_system.md (GR 10.1b added); ref_taxonomy.md (BroadcastCard/BEC added); memories updated.

**Next (S109 Tier 1):** Ghost PA card design pass (GHO.PA.3–6) — design gates: Declassified Records cost mechanic (Art 03 §18), Public Threat Assessment BC/BEC linking + Art 03 procedure, Clarify Misinformation Beat timing, Agency Recruitment Fair district-type tag.

### Generated: 2026-05-31 (session 55 complete) — supersedes session 53 save state.
### Session 104 Summary (2026-06-19)

**Focus:** Art 03 v4.8 sign-off; Art 04b §§6–8 full refresh (04b-16/17/18); card ID schema locked (L219); DB idempotency convention (L220); agy DB task execution (ID-01/02/03/05/ID-SCHEMA).

**Key work:**
- L217: Art 03 v4.8 signed off — §24 Resolution State Reference added (Succeeded/Failed/Voided); RO-xx codes removed throughout; Voided resolution unified (face-down flip); DB resolution_outcome pruned to 3 rows.
- 04b-16 ✅ — Art 04b §6 Coverage Analysis updated: seven gap notes revised with "Addressed" cards; §6.2 table corrected (Submission|Block/Information|Protect rows removed; Information|Reveal|CovertOperation added); §6.3 rewritten (S47 counts removed, §3.3 pointer corrected to Art 03 §22).
- 04b-17 ✅ — Art 04b §7 Faction Coverage Matrix rebuilt from Art 04 live data (Python regex extraction of all 41 card taxonomy fields); 20+ corrections including C17/C24 moved to Information|Reveal|CovertOperation; C36/C37/C38 added to Economy|Add|IntelToken; C42 to Territory|Remove|PresenceToken.
- 04b-18 ✅ — Art 04b §8 Design Recs updated (stale redesign recs removed; §8.1–§8.4 reflect S104 card states); §8.5 Guild added (High: Territory|Recover|PresenceToken; Low: Information|Any).
- L218: Territory|Recover|StructureBlock not possible — demolition is permanent; rebuild = Territory|Add (C01).
- L219: Card ID schema locked — [FAC].[TYPE].n format; varchar(15) constraint; 20-deck inventory documented; G-ext scheme retired.
- L220: DB script idempotency convention locked — INSERT IGNORE for inserts; portable session patches; archive/ subfolder for originals.
- agy (S104): ID-01 ✅ (G-ext-01/02/03 deleted from card_ref); ID-02 ✅ (DebriefActionCard/Grant Deed reclassified out of Card hierarchy); ID-03 ✅ (faction associations added for Operative Pool/Apex Ability Pool/Classified Directives Pool); ID-05 ✅ (all Database/ scripts converted to idempotent; originals archived to Database/archive/); ID-SCHEMA ✅ (L219 documented in schema_reference.md). verify_matrix.py: 57 components, 0 mismatches.

**Decisions locked:** L217 (Art 03 v4.8), L218 (Territory|Recover|StructureBlock impossible), L219 (card ID schema), L220 (DB idempotency convention).

**Artifacts updated:** Art 03 (v4.8 ✅ L217); Art 04b (v1.7, 🔄 pending re-sign-off 04b-19); PM02 (L217–L220); PM03 (Art 03/04b rows); PM05 (04b-16/17/18 ✅, 04b-19 gate updated, ID-01/02/03/05 ✅); GEMINI_CONTEXT.md (tasks pruned post-execution); schema_reference.md (L219 documented, component table updated, 111–119 registered).

**Next (S105 Tier 1):** Verify agy completions against live DB and schema_reference.md → ID-04 (full card renumber — new session, large sweep) → Art 04b v1.7 sign-off (04b-19, gated on ID-04).

Read this document top to bottom before doing any design work in a new session. It is intended to give a fresh session full project context with no prior knowledge required.

---

### Session 105 Summary (between sessions — agy + Claude)

**Focus:** ID-04 full card renumber; Art 04b v1.7 sign-off (L221).

**Key work:**
- agy between-session: ID-01 ✅ (G-ext retired from card_ref), ID-02 ✅ (DebriefActionCard/Grant Deed reclassified), ID-03 ✅ (faction pool faction associations added), ID-05 ✅ (23 DB scripts converted to idempotent), ID-SCHEMA ✅ (L219 documented in schema_reference.md).
- ID-04 ✅ — [FAC].[TYPE].n format applied across Art 04 (678 substitutions), Art 04b (201 substitutions), card_ref DB (27 rows). card_id field added to Art 04 §6.1/§6.2.
- L221: Art 04b v1.7 signed off. §§6/7/8 are living sections — update as gap cards designed, no re-sign-off gate.

**Next (S106):** Card design pass — faction gaps per 04b §8.

---

### Session 106 Summary (2026-06-19)

**Focus:** Card design pass (Directorate, Network, Guild gaps); taxonomy audit finding.

**Key work:**
- DIR.CA.6 Institutional Audit ✅ — Economy|Add|NativeResource(Mandate). Ring Permanent count yield; chip count > 1 restriction.
- DIR.CA.7 Institutional Brief ✅ — Standing|Shift|PublicStanding. Same ring Permanent architecture; PS yield.
- DIR.CA.8 Enhanced Scrutiny ✅ — Resolution|Modify|Difficulty. Beat 2 Automatic; −15 Modifier tokens on all Beat 3 rows in target district; all factions.
- NET.CA.7 Ground Signal ✅ — Standing|Shift|PublicStanding. IL ≤ Established restriction; success +1 PS; successcrit +1 chip + +1 PS.
- NET.MOD.1 Signal Break ✅ — Territory|Add|PresenceToken React Modifier (card_id confirmed). Trigger = PA success causing board state change. Exposure×1; d100 threshold 50.
- GUI.MOD.1 Return to Site stub — Territory|Add|PresenceToken React (formerly Territory|Recover|PresenceToken).
- GUI.CA.6 Labor Contract — card_id GUI.CA.6 assigned (L219).
- **Recover function retired from Art 04b** (04b-20 ✅): 00a 7.2b prohibits retroactive board state reversal — Recover is not a distinct primitive; always resolves to Add + forward action context. GUI.CA.2 and GUI.CA.6 reclassified to Economy|Add|NativeResource. Field Verification BLOCKED (mechanic alters committed token age field — 7.2b violation; fundamental redesign required). L218 annotated in PM02 as consequence of 7.2b, not standalone decision.
- PM05: 04-n101 updated; 04-n102 (Modifier card schema); 04-n103 (Recover Art 04 spec fixes — open); 04b-20 ✅.
- Art 04 v0.9.41 Draft. Art 04b §4/§5.2/§6/§7/§8.3/§8.5 updated.

**Next (S107 Tier 1):** Full 04b audit against 00a — sweep all taxonomy functions/verbs against governing rules before continuing card design pass.

---

### Session 107 Summary (2026-06-20)

**Focus:** Art 04b full audit against 00a governing rules — six locked decisions (L222–L227).

**Key work:**
- **L222** — Backdate 🚫 BLOCKED: Intel token location constraint (tokens in private terminal zones unreachable by opposing card) + 7.2b (round-number = committed validity state). §4.10 revised to remove round-number from valid Corrupt targets; Intel token location constraint documented.
- **L223** — Regulatory Downgrade 🚫 BLOCKED: InfluenceTier not a targetable component (derived from token counts, not a placed value); 9.1 prohibits direct income modification by card. Regulatory Freeze 🚫 BLOCKED: same subject violation + Block function targets actions not derived states. Both require fundamental redesign (04-n104).
- **L224** — Conceal retired from Art 04b function vocabulary: concealment is a structural system behavior (dispatch case, faction terminal, ARBITER screen) — not a card-triggered function. 7.2a prohibits hidden board state.
- **L225** — ARBITER-reveal outside 10.1: ARBITER discloses from its own domain without triggering stake model; portrait track only prohibited ARBITER reveal target. §4.13 added to Art 04b.
- **L226** — DIR.CA.2 Detain retaxonomized Territory|Remove → Territory|Move: success op is game.move() to Detention zone; Remove = return to supply (incorrect). 8.3a compliant. Art 04 spec fix tracked 04-n105.
- **L227** — Accord Transfer retaxonomized Economy|Redirect|AccordCard → Economy|Corrupt|AccordCard: party-name replacement is physical alteration of written record on Accord form per §4.10. Blocked on Art 06.
- Art 04b v1.8 draft — §4.10, §4.13 (new ARBITER-reveal), §5.1 (Conceal retired), §5.2 (5 card annotations), §6.1, §7 matrix, §8.2, §8.4 updated. Re-sign-off required (04b-21, gates: §5.2 card IDs clean + §6.1 cleanup).
- design_reference_card_system.md: 7.2b, 7.2a, 10.1, expanded 9.1, §4.10 location constraint added to Key Governing Rules table.
- ref_taxonomy.md: Recover + Conceal retired from function table; Corrupt scope + location constraint updated.
- PM02: L222–L227 locked. PM05: 04-n103 expanded (Backdate added), 04-n104/04-n105/04b-21 added.
- Audit clean (no violations): All Add, Remove (5 types), Redirect, Protect, Block, Copy, Shift|PS, Reveal (taxonomy level), Source Substitution, Enhanced Scrutiny, Construction Crew, Tort Interference, Intel Extraction, Detain.

**Next (S108 Tier 1):** Art 04b v1.8 re-sign-off (04b-21): (1) assign card IDs to 21 §5.2 entries with `—`; (2) clean §6.1 to show only valid unaddressed gaps.

---

### Session 96 Summary (2026-06-18)

**Focus:** Art 02 final entries and v2.1 sign-off; PM05 04b pre-card-design refresh sequence.

**Key work:**
- Ingested agy S96 report — Grant Deed (DB:113) registered. Art 02 §9 entry written and corrected: faction-agnostic (not Syndicate-specific), dry-erase preferred, mutable `owner` field, tradeable between factions.
- Art 02 §3 rubric review: 3 scope violations corrected in Grant Deed entry (GR mechanics removed, PM05 ref removed, `visibility` bare enum, `quantity` labeled). Subheader cleaned.
- Art 02 §4.1 `movement_path` field definition clarified: trigger slot = board event or player action (NOT beat numbers or phase names); timing belongs in Art 03.
- Full movement_path timing sweep: 13 violations corrected across all components in §§5–12.
- PM05 04-n99 added: Grant Deed Art 04 React card spec (schema questions A–D gated on 04-n27).
- PM05 04-n26 Grant Deed: ✅ S96 (Art 02 entry + DB:113).
- PM05 04b-12 through 04b-19 added: full Art 04b refresh sequence (component registration → §§3–8 → re-sign-off) as prerequisite to resuming card design.
- SESSION_BRIEF Tier 2 updated: Step 1 (automated sweeps 04-n97/98) → Step 2 (04b-12 through 04b-19 refresh) → Step 3 (card design by set).
- Art 03 §18 confirmed sufficient procedural authority for React trigger window; no new GR needed in 00a now (04-n27 flagged for future eval when §18 design is complete).

**Decisions locked:** L212 — Art 02 v2.1 signed off.

**Artifacts updated:** Art 02 (v2.1, L212); PM02 (L212 added); PM03 (Art 02 row updated); PM05 (04-n99, 04b-12 through 04b-19 added; 04-n26 Grant Deed ✅).

**Next:** Automated sweeps (04-n97 boost=None, 04-n98 on_accept/on_decline) → Art 04b refresh (04b-12 → 04b-19) → Card design by set.

### Session 97 Summary (2026-06-18)

**Focus:** agy airlock ingestion (5 component registrations); Art 02 §13 Physical Action Verb Coverage added; Art 03 §22 Primitive Action Model & Legalization Analysis added; Art 04b §3 taxonomy relocation; legalization pass (19 Faction-initiated combinations).

**Key work:**
- agy airlock ingested: DB:114–118 (5 component registrations) → Art 02 §10.1 stubs + card_source fields updated (02-n20 ✅).
- S97 legalization pass: 19 Faction-initiated action combinations analyzed; 16 permit / 3 prohibit decisions locked in legalization table (Art 03 §22.2); triggers identified; all decisions grounded in narrative policy per Design Pillar 6.
- Art 02 §13 Physical Action Verb Coverage added (§13.1 verb definitions + §13.2 48-row Component × Verb Matrix; relocated from Art 04b §3.1–§3.2). Art 02 is the component source of truth for verb coverage; DB view `v_comp_verb_matrix` is the analytical aggregate. PM05 02-n26 added (Priority 1 — re-sign-off required).
- Art 03 §22 Primitive Action Model & Legalization Analysis added (methodology, trigger taxonomy, gap analysis views, 19-decision S97 legalization table; relocated from Art 04b §3.3). Art 03 is the legality source of truth for subject × verb × component combinations. PM05 03-n24 added (Priority 1 — re-sign-off required).
- Art 04b §3 Physical Action Taxonomy relocated (§3.1+§3.2 → Art 02 §13; §3.3 → Art 03 §22; §3 is now pointer section only). 04b-12 ✅ / 04b-13 ✅ / 04b-14 ✅ / 04b-15 ✅. 04b-16/17/18/19 queued — gate: Art 02 §13 corrections (02-n26).
- ref_taxonomy.md updated (verb list sync + v_comp_verb_matrix view pointer added).
- SESSION_BRIEF updated S97 (all three architecture decision items in Tier 2 Step 2).

**Decisions locked:** None (all decisions during legalization pass documented in Art 03 §22.2 table; no L-decision created as design rationale is case-by-case).

**Artifacts updated:** Art 02 (§13 Physical Action Verb Coverage added, v2.1 status updated to 🔄 Needs Re-Sign-Off, PM05 02-n26 Priority 1); Art 03 (§22 Primitive Action Model & Legalization Analysis added, v4.4 status updated to 🔄 Needs Re-Sign-Off, PM05 03-n24 Priority 1); Art 04b (v1.6 Pending Re-sign-off, §3 relocated/pointer, 04b-12 through 04b-15 marked ✅); PM03 (Art 02, Art 03, Art 04b rows updated); PM05 (02-n26, 03-n24, 04b-16/17/18/19 added); ref_taxonomy.md (verb list + view pointer).

**Next:** Art 02 §13 corrections + schema integration (02-n26 Priority 1) → Art 03 §22 legalization table finalization → Art 04b remaining refresh (04b-16 through 04b-19).

### Session 98 Summary (2026-06-18)

**Focus:** agy S98 report ingestion (DB-41/42/43); Art 02 applicable_verbs seeding + re-sign-off v2.2; component_metadata architecture decision.

**Key work:**
- DB-41 ✅ — verb seeding: d10 (id 119) Add/Remove/Move/Flip; Modifier token Flip; all card containers Reveal/Conceal; Threshold Sliders Corrupt; Faction Hand + Operative Pool Corrupt. transform_orientation corrected id=42 (reverted — ARBITER Dominance Marker has no meaningful orientation states); transform_visibility corrected ids 108/48/95/96; missing subject_target rows inserted (Dispatch Packet→Dispatch Case+Arbiter Tableau; Broadcast Effect Card→Arbiter Tableau+The Overview; Status marker→Faction Terminal+Arbiter Tableau). verify_matrix.py: 0 mismatches. check_views.py: 28 views compile ✅.
- DB-42 ✅ — `component_metadata` table created (Option A hybrid wide) + Python seeder executed (74 rows). L130 locked.
- DB-43 ✅ — static lookup tables seeded: public_standing_tier (5 rows), difficulty_tier (3), resolution_outcome (5), influence_level (4).
- Art 02 v2.2 — applicable_verbs integrated into all §§5–12 component entries; §13 matrix removed (entries are now the source of truth); d10 (DB:119) added §11; ARBITER Dominance Marker Flip removed from applicable_verbs; DB Sync header note added.
- Art 02 v2.2 signed off — L213.

**Decisions locked:** L213 (Art 02 v2.2 signed off); L130 (component_metadata architecture — Option A; subject_target authoritative; movement_path stays in prose; trigger reserved word in MariaDB).

**Artifacts updated:** Art 02 (v2.2 ✅); PM02 (L213, L130); PM03 (Art 02 row); PM05 (02-n26 ✅, 02-n09 ✅, DB-41/42/43 added and closed).

**Next:** Art 03 migration pass (02-n08) — see Session 99.

### Session 99 Summary (2026-06-19)

**Focus:** 02-n07 Integration registration; Art 03 migration planning and session close.

**Key work:**
- 02-n07 ✅ — "Integration" registered: §14.10 narrative anchor written to Art 00 (human-awareness-level, Narrator voice; return channel framing without resolving what Integration entails); term row added to 00a Component & System Terms; TrueState §11 open question logged (what Integration means from ARBITER's true perspective). Art 00 needs re-sign-off (§14.10 is material).
- Art 02 DB Sync header note added (`**DB Sync:**` line — changes must be coordinated with DB updates).
- Art 03 migration plan finalized (02-n08 scope + DB reconciliation decisions):
  - DB fix: public_standing_tier — Celebrated 18–20, Respected 14–17, Neutral 7–13 (whiteboard canonical).
  - Influence level zero term = "None" (DB canonical).
  - 9-item whiteboard migration into Art 03 (§19 expanded, §20 fixed, §1145 fixed, §13.8 PS scale, §13.9 RO table, §7.4 University Perimeter). Portrait scale → Art 07, not this pass.
  - Not in this pass: 03-n01, 03-n24.
- 04b refresh confirmed downstream (after Art 03 signs off).

**Decisions locked:** None (S99 decisions are design inputs to Art 03 pass, not locked artifact changes; will be locked when Art 03 content is written and signed off).

**Artifacts updated:** Art 00 (§14.10 Integration added, needs re-sign-off); Art 02 (DB Sync header); 00a (Integration term row); TrueState §11 (Integration open question); PM05 (02-n07 ✅ S99); SESSION_BRIEF (S99 update — Art 03 Tier 1 plan).

**Next:** Art 03 migration pass — DB fix (PS bands) → 02-n08 whiteboard migration → Art 03 re-sign-off. See SESSION_BRIEF Tier 1.

### Session 95 Summary (2026-06-17)

**04-n70 fix pass ✅:** All 8 categories from `Whiteboard/04n70_findings_S95.md` addressed in Art 04. Schema violations: C39/C23 `faction=None→All`; C36/C42/C38/C41 `affinity=None` (faction names are not valid ConditionalExpr values); P05 `threshold=35` (was None); P13 threshold dynamic expression; C16 `resolution=Automatic` (Prediction not in enum); EntryExitControls `persistence_effect` added (condition was correct — inverted finding was wrong). Missing persistence triples: 9 cards (Ghost stubs: Station/Full Take/SCIF/Flip/Signals Analysis; C37 Sacrifice; LandTitle; HostileTakeover; AccordTransfer). Spec/checklist: C09 dup removed; C19 checklist corrected; C41 arbiter_note faction (Directorate→Syndicate); Directorate RegulatoryDowngrade/Freeze nav fix (moved from covert→PA index). Notation: C37 `public_standing→standing`; Overture `perspectives={}`. Structural: C41/P15 ElectPlayer effects moved from comments to structured `on_accept`/`on_decline`. P16 DividendMarker `world_condition()` formalized in success field.

**§6.1 schema additions:** `on_accept: MutationExpr | None` and `on_decline: MutationExpr | None` added to Card class (ElectPlayer outcome_type only; None on all other cards). §6.2 Data Dictionary updated with both fields.

**Design decisions (S95):** (1) Minimize/eliminate arbiter_notes — prefer structured spec fields. (2) PortraitEntry valid params only: `flat/submitter/where/modifier/mod_where` — `failcrit=` is invalid. (3) on_accept/on_decline as schema elements for ElectPlayer outcome type. (4) Persistence model: Permanent cards use `persistence_condition`/`persistence_effect`; Seasonal cards with timed effects use `world_condition()` in `success` — different mechanisms for different durations, not in conflict.

**PM05:** 04-n70 ✅ S95. 04-n98 added (on_accept/on_decline sweep — add `on_accept=None, on_decline=None` to all non-ElectPlayer cards). 04-n97 open (boost=None sweep). Art 04 v0.9.37.

### Session 93 Summary (2026-06-16)

**02-n10 ✅:** Art 02 §§5–12 — 13 imprecise `→ Art 00 for full narrative` pointers tightened with specific section numbers: DB:32→§7, DB:6→§14.2, DB:7→§14.2, Structure block→§14.3, DB:8→§7, DB:12→§14.5 (was §14), DB:9→§14.9, DB:10→§8.1, DB:21→§6.6, DB:50→§9.6, DB:24→§9, DB:23→§8, DB:31→§9.6. PM02 Change Log updated (non-material, S93). PM05 02-n25 added (District tile + Situation Report imprecise pointers — section uncertain). Whiteboard/02n10_progress_S93.md deleted.

**00-16 ✅ (pre-clear):** Art 00 v1.7 signed off (L211). §8.1 tensions list → prose. Art 00 now fully signed off.

**Next:** Art 02 conditional sign-off items — 02-n11 (SCIFRecord cascade), 02-n12 (Emergency Response card design), 02-n13 (Status marker narrative), DB-38 (Escalation marker cascade).

### Session 92 Summary (2026-06-16)

**Card work:** C28 Breaking News — Issues Resolved ✓ S89 (04-n75/76 gates confirmed closed S81/82; taxonomy subject = CovertOperation soft flag for 04b; sign-off pending set-level PM05 gates). C40B Live Coverage — Issues Resolved ✓ S89 (04-n77 procedure found in Art 03 §9.0 — missed sweep reference; checklist updated from ⚠ → ✓).

**Art 02 §13 stub pass:** 44 new component rows added across 7 categories (Layout & Physical Environment, Tracking Tools, Faction Private Zone, Card Types, Broadcast System, ARBITER Operational, Faction-Specific). All 104 DB-registered components now accounted for in Art 02 §13.

**DB sweep (agy):** DB-35 ✅ — id=88 repurposed from Pass card → Faction Resolution Grid (actionable=0, receivable=1); DB-36 ✅ — id=102 Situation Report registered; 02-n04 ✅ — id=103 Visibility Marker, id=104 Boost Marker registered; id=22 (Chorus Portrait) retired; id=50 renamed "Chorus Portrait track" + set receivable=1; v_placement_matrix view updated; all 27 views verified.

**03-init alignment:** Situation Report Zone (stale zone-as-component) → Situation Report component in Situation Report Zone (§2.1). Stale DB-14/DB-15 notes removed from §2.7/§2.8. VM-xx (id=103) and BM-xx (id=104) added to §2.8 ARBITER Starting Supply. Floor Act PA noted as standard PA card, starts in hand permanently, no discard (PM05 04-n96 added for Art 04 design pass).

**Art 02 §9:** Pass card references removed ("Pass cards require no token" bullet; "only Pass cards are available" clause). Pass card retired S89.

**PM05 additions:** DB-35 ✅, DB-36 ✅, 02-n03 (Art 01 → Art 02 migration pass — open), 02-n04 ✅, 03-n21 (Dispatch Token missing from 03-init setup tables — open), 03-n22 ✅ (VM-xx/BM-xx added to §2.8 inline), 04-n96 (Floor Act PA design constraints for Art 04 — open).

**S90 entry point:** Art 02 full restructuring and overhaul — redesign Art 02 as definitive component bible; migrate Art 01 §4 component narratives + §6 Component Physical Forms table to Art 02; update Art 01 to geography/layout only (PM05 02-n03). Then Art 02 sign-off pass (02-n02).

---

## Session Log

### Session 114 — 2026-06-22
**Focus:** Ref audit review (S113 overnight batch not yet available) · card_status DB table built
**Accomplishments:**
- card_status table created in the_signal_db: 95 cards seeded from Art 04 v0.9.44 across all 6 factions. Replaces stale tmp_card_review.
- Direction set: card set audits (04-n87–04-n92) before any card sign-offs (Andy's decision).
- Memory added: feedback_card_status_sync.md — DB must stay in sync with Art 04 card work.
- SESSION_BRIEF updated; Priority Order updated to S115.
**Artifacts changed:** DB (card_status table created) · SESSION_BRIEF (S114 close)
**Next:** Tier 1 = review ref_audit_overnight_results.md at boot · Tier 2 = card set audits starting Standard (04-n87)

### Session 57 — 2026-06-01
**Focus:** DB-14 Phase B confirmation; Art 00 §7 redesign + re-sign-off v1.6; Art 00a 00-R30 (Missing Author Vacuum); True State §1/§3/§4/§10 updates; Art 04 P16 added (portrait entries submitter-bounded); C01–C10 full 5-faction portrait sweep; C01/C02/C03/C04/C05/C06/C07/C08/C10 signed off; C09 portrait + dependency cleanup; C10 −45 affinity locked (L179). Ghost faction mechanics concept noted for playstyle summary.
**Decisions locked:** L177 (Missing Author Vacuum governing rule), L178 (P16 portrait submitter-bounded), L179 (C10 −45 affinity narratively justified).
**Artifacts updated:** Art 00 (v1.6, signed off S57), Art 00a (00-R30 added, re-sign-off pending), True State (§1/§3/§4/§10), Art 04 (v0.9.23, C01–C10 portrait sweep, C01/C02/C03/C04/C05/C06/C07/C08/C10 signed off).
**Next:** S58 — faction playstyle summary (blocking C11), Outstanding Issues (C13/C15/C16/C17), C11–C35 design rationale.

### Session 58 — 2026-06-01
**Focus:** Faction playstyle summaries (§5a): Ghost (Intel/SCIF/Flip), Guild (Capacity flywheel), Network (Exposure + modifier self-feed), Directorate (Mandate + suppression), Syndicate (Capital-only upkeep + Intel premium). Victory Architecture table added. Gap analysis complete — 12 net new cards across all factions. Modifier deck architecture locked: three types (react/tripwire/operation/battlefield). New PM05 items: 04-n1 (card numbering), 04-n2 (Guild C01 passive income), 04-n3 (Labor Contract), 04-n4 (modifier taxonomy). Whiteboard files: faction_playstyle_S58.md, modifier_card_ideas.md, design_reference.md.
**Decisions locked:** None (design exploration session).
**Artifacts updated:** Art 04 (v0.9.23, §5a added).
**Next:** S59 — Ghost card design (Station, Full Take, SCIF, Flip, Signals Analysis), then remaining faction gap cards.

### Session 59 — 2026-06-01
**Focus:** Full covert op design pass. All C01–C42 baseline drafted. Design rationale scaffold (Design Rationale / Design Checklist / Outstanding Issues / Status) added to C18–C35. C36–C42 migrated from §8 Intel Economy appendix to canonical faction sections (Python spec + scaffold). New faction-specific covert cards: Ghost (Station, Full Take, SCIF, Flip, Signals Analysis), Guild (Labor Contract), Directorate (Regulatory Downgrade, Regulatory Freeze + C42 Sanctioned Raid from migration), Syndicate (Land Title, Hostile Takeover, Accord Transfer + C38 Parasitic + C41 Corporate Blackmail from migration), Standard (C39 Absolute Compromise). Network (C37 Sacrifice + C40 Weaponized Transparency from migration). Entry/Exit Controls (Directorate PA) written to §10. New components awaiting Art 02 registration: SCIFRecordCard, TierPenaltyMarker, TierFreezeMarker, EntryControlMarker, LandTitleMarker, ParasiticMarker. PM05 04-n5 (SCIF debrief step), 04-n6 (00-R29 Ghost adjacency clarification) remain open. PM05 04-n7 closed.
**Decisions locked:** None (design execution session).
**Artifacts updated:** Art 04 (v0.9.24), PM05 (04-n7 closed), SESSION_BRIEF (S59).
**Next:** S60 — Directorate + Syndicate sanity checks; Art 02 registration for 6 new components; P-series PA design pass (dedicated session); Outstanding Issues (C13/C15/C16/C17).

### Session 60 — 2026-06-01
**Focus:** Art 03 v3.0 full review pass — all L180 corrections applied. Beat 4 new Step 2 (board state validation). §20/§21 swapped (End of Quarter now §20, Operation System §21). §23 Immediate row fixed (placed on board; hand→board required). §6 Phase C/D labels removed; BATTLEFIELD STRENGTH → CONTESTED DISTRICT RESOLUTION. §7 all factions = 4 Dispatch Tokens; modifier draw substeps hierarchically formatted. §10/§11 headers stripped of Phase IDs. §11 Beat 0 steps 3/4 swapped (drain first); step 7 simplified. Beat 1/2 voided card language → face-down convention throughout. Beat 2 renamed "Conditions Set." Beat 3 Pass card step removed; Contested/Failed TBD blocks removed; Step 12 (Dispatch Case Return, Month 3 only) added. §12 Ghost combo note reframed. §17 = Contested District Resolution (was §18); §18 = Month 3 Quarter Notes (was §17). PM05: XA-43 (pass card sweep), XA-44 (Voided Resolution Card component sweep), 04-n9 (deployment marker blocking flag) added to READY NOW.
**Decisions locked:** None (review execution session).
**Artifacts updated:** Art 03 (v3.0 in progress, 03-17 re-sign-off required), PM05 (XA-43/44, 04-n9 added), SESSION_BRIEF (S60).
**Next:** 03-17 sign-off (Art 03 v3.0) → 00a-xx (00-R39 revision) → Art 04 resumes (04-n8, Directorate+Syndicate sanity checks, P-series PA pass, Outstanding Issues C13/C15/C16/C17).

### Session 61 — 2026-06-01
**Focus:** Art 03 v3.0 sign-off (L181): Beat 3 Step 12 label/flavor removed; Beat 4 Submit Payment → Step 1, steps renumbered 1–13; section breaks added; duration taxonomy 5→4 types (Tripwire collapsed into Permanent). Art 00a v0.4 sign-off (L182): 00-R21 (4-type duration taxonomy), 00-R22 (partial payment model), 00-R29b (Missing Author Vacuum — renamed from duplicate 00-R30), 00-R39 (covers covert ops + public acts); 43 rules. XA-40 (Political→Public Act sweep in Art 04) ✅. XA-42 (design_reference.md L180 sweep) ✅. Art 04 §5a: Narrative Anchor section added (doctrine→mechanic table per faction); Faction Goals reordered (Anchor first, Goals below); Ghost goal corrected to "Delay — no premature answer to the Chorus"; playstyle summaries reformatted to bullet lists. L183: C22 Detain — detention zone on Directorate public tableau; faction Terminals may be unique per doctrine. C22 card spec updated (move to Detention zone, NotificationSlip removed, PS tracking added). C42 Sanctioned Raid updated v1.1 (Mandate×2, PS −1 on success added). C32 Short the Market flagged for mechanical redesign (04-n14 — "applied silently" incompatible with paper prototype; tagline/code conflict on generation vs stockpile). PM05 04-n10/11 (pentagram gaps), 04-n12 (Terminal unique zones), 04-n13 (Network modifier card / C42 response), 04-n14 (C32 redesign) added.
**Decisions locked:** L181 (Art 03 v3.0), L182 (Art 00a v0.4), L183 (C22 Detain — Directorate Detention zone; Terminal uniqueness).
**Artifacts updated:** Art 03 (v3.0, signed off L181), Art 00a (v0.4, signed off L182), Art 04 (§5a Narrative Anchor, C22 updated, C42 v1.1), PM02 (L183), PM05 (04-n10–14 added), SESSION_BRIEF (S61).
**Next:** S62 — Art 04 P-series Public Act pass (P01–P18, all stubs); Outstanding Issues C13/C15/C16/C17; C32 redesign (04-n14); 04-n10/n11 pentagram gaps. XA-41 (Art 03a schema rename) deferred.

## S62 — 2026-06-02

**Focus:** Art 04 P-series full design pass + Ghost intel manipulation cards + coverage gap analysis.

**What was done:**
- P01–P18 all specced (Draft S62 — not signed off). Names revised from stubs. Standard PAs (P01–P08) and faction-specific PAs (P09–P18) fully written.
- Art 04 schema: `persistence` field added to Card class, Data Dictionary, Enum (Immediate/Transient/Seasonal/Permanent).
- Art 04 §5: Principle 17 added (faction-native capabilities have outsourced standard equivalents).
- Ghost extended set: Source Substitution (Information/Corrupt/IntelToken — faction field), Backdate (Information/Corrupt/IntelToken — quarter field), Field Verification (Information/Recover/IntelToken) — full specs written.
- Art 04b coverage analysis: gaps catalogued by layer/function/subject, prioritised, Territory/Recover removed from valid taxonomy, Copy/PA retired.
- Gap card sketches preserved in Whiteboard/gap_card_sketches_S62.md: Disprove, Disinformation Campaign, Standing Injunction, Asset Extraction.
- PA persistence policy established: PA cards carry `persistence` field; Beat 4/5 and Phase 21 govern cleanup.
- Design decision: Accord procedure (Art 06) is prerequisite for Group A gap cards.
- PM05 items 04-n15 through 04-n20 added.

**No locked decisions (L-decisions) this session — draft pass only.**

**Next session opens on:** P-series sign-off pass; Disprove/Disinformation Campaign/Standing Injunction/Asset Extraction full specs; Directorate covert reclassification; Art 04b §5.2 update.

## S64 — 2026-06-03

**Focus:** Gap card specs; Art 04b §5.2 refresh; 04-n25 schema field gaps.

**What was done:**
- Gap card specs written: Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid. Art 04b §5.2 +5 rows. 04-n17 ✅.
- 04-n25 (CRITICAL schema fields): Art 04 §6.2 cost field redefined (fungible resources only). §6.6 Expression Parameters added (pre_loss_calc). C37 Sacrifice redesigned v1.1 (cost=None; PS in success). C34 Golden Parachute redesigned v2.0 (bribe mechanic; retained payment). Art 03 v3.1 signed off (L185): Beat 0/2/3 Golden Parachute procedure; partial payment marker source. 04-n25 ✅.
- XA-38 ✅ (anchor link sweep — 38 links fixed across 11 artifacts).

**Decisions locked:** L185 (Art 03 v3.1 signed off).
**Artifacts updated:** Art 03 (v3.1), Art 04 (v0.9.27), PM05, SESSION_BRIEF.
**Next:** S65 — 04-n26 component interaction design pass.

## S65 — 2026-06-03

**Focus:** 04-n26 Cluster A; Entry/Exit Controls redesign; Art 03 v3.2.

**What was done:**
- Entry/Exit Controls redesigned v2.0 (district target; permanent placement block; persistence_condition). Art 04 §6.6 removed. persistence_condition added to §6.1/§6.2. Art 03 v3.2 signed off (L186). 04-n25 ✅ closed. PM05: 04-n29, 04-n30 added.

**Decisions locked:** L186 (Art 03 v3.2 — §6.6 removed; persistence_condition schema addition).
**Artifacts updated:** Art 03 (v3.2), Art 04 (v0.9.28), PM05, SESSION_BRIEF.
**Next:** S66 — 04-n26 Cluster A continued.

## S66 — 2026-06-03

**Focus:** 04-n26 Cluster A (SCIF, Land Title, Parasitic, Regulatory Downgrade); pool_copies sweep; 00-R40.

**What was done:**
- SCIF card spec cleaned. Land Title redesigned v2.0. Parasitic redesigned v2.0. Regulatory Downgrade redesigned v2.0. pool_copies sweep (04-40 ✅) — 42 code-block instances + 7 prose references removed. 00-R40 locked (L187). 00-R40a added. Art 04 target_taxonomy field added (§6.1/§6.2). Regulatory Freeze redesigned v2.0. Standing Injunction redesigned v2.0. Art 04 persistence_effect field added. PM05: 04-n31, XA-45, DB-31 added.

**Decisions locked:** L187 (00-R40 ARBITER Cognitive Load), L188 (00-R06a, 00-R40a, target_taxonomy field).
**Artifacts updated:** Art 04 (v0.9.30), Art 00a (pending re-sign-off), PM05, SESSION_BRIEF.
**Next:** S67 — 04-n26 Cluster B; 04-n27.

## S67 — 2026-06-03

**Focus:** 04-n26 Cluster B; 04-n28 (C09/C18/C28 redesigns); Art 03 §19/§28.

**What was done:**
- C19 Deep Cover v1.1, C23 Tort Interference v2.0, C26 Leak v1.1. C18 Dossier Breach v1.1 (SIGINT tap / DispatchReport model). C28 Open Channel retired to L2. C24 Surveillance Placement mechanics invalidated (04-n41). Governing Principle — ARBITER Cognitive Efficiency added to Art 00a §1. Resolution grid confirmed entirely covert. NS-xx, IS-xx, DR-xx defined/registered. Art 03 §19 Debrief Actions step added (DebriefActionCard / SCIFRecord). Art 03 §25/§28 React Card Rules added. Art 03 v3.3 signed off (L189). 04-n27 substantially resolved. C17 beat timing flagged (04-n49). PM05: 04-n38–04-n49 added.
- 04-n41 gap assessment: L1 scan complete; C24 Surveillance Placement redesigned v2.0 (Beat 2 episodic; IS-xx). IS-xx reinstated (DR-xx collapsed into IS-xx). C18 v1.2. Art 04 v0.9.32.

**Decisions locked:** L189 (Art 03 v3.3 signed off).
**Artifacts updated:** Art 03 (v3.3), Art 04 (v0.9.32), Art 00a, PM05, SESSION_BRIEF.
**Next:** S68 — 04-n28 (Art 06 Accord design); 04-n49 (C17 beat correction).

## S68 — 2026-06-05

**Focus:** 04-n28 (Art 06 Accord design); 04-n49 (C17 beat correction); 04-n48 (card redesign batch).

**What was done:**
- Art 06 §5 reworked (Accords-are-public design principles). Art 06 §9 Accord governance overhauled and signed off (L191): structured contract form, Beat 4 submission, Debrief execution window, breach/completion lifecycle, Portrait scale (L190), manipulation types (Lock/Alter/Transfer). §6/7/8/10/11/12 stub-flagged non-canonical. Art 06 v0.2.
- Art 04 §11.7 Outcome addition effect type added. Art 04 §11.8 Overture stub (Instant modifier / outcome addition / Beat 4 / ARBITER tableau via C09).
- C09 Fund references updated (AccordCard → Overture). C-S3 outstanding issue added.
- L190 locked (Accord Portrait scale — pending playtesting + modeling). L191 locked (Art 06 §9 sign-off).

**Decisions locked:** L190 (Accord Portrait scale), L191 (Art 06 §9 signed off).
**Artifacts updated:** Art 06 (v0.2), Art 04 (v0.9.31), PM02 (L190/L191), PM03 (Art 06 row), SESSION_BRIEF.
**Next:** S69 — 04-n49 (C17 beat timing correction + re-sign-off); 04-n48 (card redesign batch).

## S63 — 2026-06-02

**Focus:** Art 04 design checklist infrastructure + P-series design pass (P01–P18).

**What was done:**
- Checklist template expanded to 13 rows (Persistence added as row 8; gate updated to "13 rows assessed").
- `persistence = Immediate` added to 35 C-series Python specs (C01–C19, C21–C35, C39); 9 C-series sign-offs cleared to n/a pending re-review.
- 11 stale Persistence checklist rows removed from P-series + Ghost card checklists (wrong location — field belongs in Python spec only).
- `tmp_card_review.line_start` recalculated for all 75 cards after edits.
- P01–P08: full 13-row checklists complete. P05 restriction updated (Expired tokens excluded — `age__in=[Fresh, Stale]`). P06 floor clause added (`min(2, available)`). P07 taxonomy corrected to Standing/Shift/PublicStanding. P08 on-decline +1 PS confirmed intentional.
- P01–P07: Design Pass ✓ / Issues Resolved ✓. P08: Design Pass ✓ / Issues Resolved open (Art 06 gaps).
- P09–P18 (faction-specific PAs): 13-row checklists complete. Design Pass ✓ on all 10. Issues Resolved pending 04-n23 (all 10 missing aligned + opposed perspectives per Principle 8).
- PM05: 04-n23 added (write 2 additional perspectives per card for P09–P18, 20 total).

**No locked decisions (L-decisions) this session — draft pass only.**

**Next session opens on:** 04-n23 (aligned + opposed perspectives for P09–P18); C-series sign-off re-review (persistence added); 04-n18 (Art 04b §5.2 update).

---

### S53 — 2026-05-30
Art 04 major structural pass. C17–C35 retrofitted to Python object notation (`Card(...)` constructor format). C01–C17 design rationale fully restructured: two-subheader format (#### Design Rationale + #### Outstanding Issues and Design Questions), checklist converted to Category/Pass/Note table format. Code block fixes: C01/C02 `district(target).faction(acting)` notation, C07 `restriction=None` (removed unenforeable Beat 4 check), C17 portrait `flat→submitter`. Six open design questions documented in Outstanding Issues for C05/C09/C10/C13/C15/C16. L172 locked. 04-57 closed. 04-58 opened (C01–C17 Outstanding Issues resolution).

### S54/S55 — 2026-05-31
**Focus:** L174 doctrinal alignment pentagram locked; C01–C17 full 12-row design checklist sweep; Option C taxonomy (L175) locked.

**Decisions locked:** L173 (Beat 4 carry row — Beat 2 cards move to carry row at Resolution Grid setup; ARBITER processes at §17 Beat 4 start; L173 confirmed S54). L174 (doctrinal alignment pentagram: Ghost → Directorate → Guild → Network → Syndicate clockwise; pentagon edges = Neighbor, star diagonals = Opposed; PentagramRelation enum; baselines Neighbor +15 / Opposed −15). L175 (card layer = primary game system the card's effect serves; IntelToken generation = Information layer; Economy = capital flow only: NativeResource, faction resource pools, card counts, Accord existence).

**Artifacts changed:**
- Art 00 v1.5 — §7 Doctrinal Alignment Pentagram fully rewritten with pentagram geometry, 10 pairs, L174 cross-ref. PM05 00-13, 00-14 added (doctrine text additions + Missing Author Vacuum rule).
- Art 04 v0.9.22 — C01–C17 expanded to 12-row checklist format (Action fit, Voice fit, Doctrine alignment, Card type fit, Taxonomy fit, Balance, Effect duration, Trigger validity, Portrait validity, Supported by zones/components/game procedure). Status tables added to all C01–C17. C05/C24 `layer = Economy` → `layer = Information` (L175). Outstanding Issues sections document open design questions for C09/C10/C11/C13/C15/C16/C17. 04-60 ✅, 04-61 ✅.
- Art 04b v1.5 — §4.2 Economy definition narrowed (removed "token counts"); §4.4 governing rule updated (IntelToken generation = Information); §5.2 table updated (C05, C24: Economy→Information). PM05 04-63 added (stale C27 §4.6 entry).
- PM02 — L173, L174, L175 added.
- PM05 — 00-13, 00-14, 04-61 ✅, 04-62, 04-63 added/updated.
- Whiteboard — `faction_pentagram_alignment.md` deleted (superseded by L174); `faction_pentagram_andy.md` retained (source material).

**PM05 changes:** 04-60 ✅, 04-61 ✅. New: 00-13 (Art 00 §7 faction doctrine text additions), 00-14 (Missing Author Vacuum rule), 04-62 (artifact reference notation convention), 04-63 (Art 04b §4.6 stale C27 entry).

## Session 64 — 2026-06-03

**Focus:** 04-n17 completion + design pass sweep

**Accomplished:**
- 04-n17 ✅ — Disprove, Intel Extraction, Modifier Raid written to Art 04 (Economy/Remove/IntelToken, Economy/Redirect/IntelToken, Economy/Redirect/ModifierCard). Fixed cost/threshold; no Syndicate affinity (Ghost threshold +10 only); blind draw/removal; silent on success.
- Art 04b §5.2 updated — 5 new rows (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid).
- Design pass ✓ complete across ALL Art 04 cards — first time. ~40 cards processed; checklist rows filled, outstanding issues documented.
- PM05: 04-n25 (critical — schema fields), 04-n26 (high — component design), 04-n27 (high/pre-accord — Art 03 gaps), 04-n28 (high/post-27 — Art 06 Accord) added.
- Art 04 v0.9.26 (also catches S63 bump), Art 04b v1.6.

**Priority ordering locked S64:**
1. Critical: 04-n25 schema field gaps (target_ring, pre_loss_calc, PS-as-cost)
2. High: 04-n26 component interaction design (12+ components — undesigned processes)
3. High (before accord): 04-n27 Art 03 procedure gaps
4. High (after 04-n27): 04-n28 Art 06 Accord design

**No L-decisions this session.**

**Next session:** Resolve C01–C17 Outstanding Issues (C09 Art06 dep, C10 −45 threshold, C11 §11 procedure gap, C13 Ring 0, C15 per-Quarter cap, C16 copied op cost + prediction procedure, C17 Art 03 migration). Art 00 §7 doctrine text additions (00-13, 00-14). Then C18–C35 design rationale.

## Session 65 — 2026-06-03

**Focus:** 04-n25 schema field gaps (PS-as-cost + pre_loss_calc)

**Accomplished:**
- Art 04 §6.2 cost field redefined — fungible, tradeable resources only; non-fungible markers (PS, presence tiers) are effects not costs
- Art 04 §6.6 added — Expression Parameters table; `pre_loss_calc=True` defined
- C37 Sacrifice redesigned v1.1 — cost=None; target_faction required (tokens must be keyed); success=ps−2+IntelToken(target_faction); perspective rewritten ("Standing" → in-narrative); arbiter_note removed
- C34 Golden Parachute redesigned v2.0 — bribe mechanic: Syndicate pays variable Capital to nullify target_faction's Beat 3 ops targeting Syndicate; windfall if no qualifying ops; retained payment type (resources travel with card, not drained to Reservoir)
- Art 03 v3.1 signed off (L185) — Beat 0 Retained payment validation row; Beat 2 Golden Parachute bribe distribution procedure; Beat 3 partial payment marker source updated (Beat 0 or Beat 2)
- XA-38 closed — anchor link sweep complete; 38 double-hyphen anchors fixed across 11 artifacts (em dash/& in headings incompatible with Python-Markdown toc slugifier)
- Network PS recovery/negation modifier card concept added to modifier_card_ideas.md
- 04-n25 PS-as-cost ✅, pre_loss_calc ✅ closed. target_ring remains.

**L-decisions this session:**
- L185: Art 03 v3.1 signed off. Golden Parachute bribe mechanic (Beat 0/2/3). Art 04 §6.2 cost field (fungible only). §6.6 Expression Parameters. C37 Sacrifice + C34 Golden Parachute redesigned.

**Next session:** 04-n25 remaining: `target_ring` (Entry/Exit Controls — needs Art 01 ring-scope definition + §6 field). Then 04-n26 → 04-n27 → 04-n28.

## Session 66 — 2026-06-03

**Focus:** 04-n25 completion; Entry/Exit Controls full redesign

**Accomplished:**
- Entry/Exit Controls redesigned v2.0 — district target (not ring); permanent deployment marker placement block; non-Directorate markers displaced to any district where faction has presence (Blocked face); persistence_condition auto-discard when Directorate loses Established; PS −1; card sits in Directorate's PA area on the Overview
- Art 04 §6.1/§6.2: persistence_condition field added (BoolExpr | None — card discarded immediately when evaluates False)
- Art 04 §6.6 Expression Parameters removed — pre_loss_calc was added ahead of card sign-off; schema additions must follow sign-off
- Art 03 v3.2 signed off (L186) — Beat 2 pre_loss_calc block removed
- C37 Sacrifice: affinity=None (stale field on a cost=None card)
- 04-n25 ✅ fully closed (all 3 items: target_ring moot; pre_loss_calc orphaned+removed; PS-as-cost already fixed in S65)
- PM05: 04-n29 added (counter-card design + Art 03 persistence monitoring); 04-n30 added (persistence_condition sweep on all card specs)
- Entry/Exit Controls: design pass ✓; Issues Resolved blocked by 04-n29 and no-presence-elsewhere edge case

**L-decisions this session:**
- L186: Art 03 v3.2 signed off. Beat 2 pre_loss_calc procedure block removed (C34 uses game.bribe(); no card uses pre_loss_calc). Art 04 §6.6 removed. Schema additions must follow card sign-off.

**Next session:** 04-n26 (component interaction design pass).

---

## Session 67 — 2026-06-04

**Focus:** 04-n26 Cluster A component interaction design pass; 00-R40 ARBITER Cognitive Load

**Accomplished:**
- Land Title redesigned v2.0 — Territory/Add/StructureBlock; success = Grant Deed delivered to Syndicate case; restriction = district.structure_count == 0; no board marker; no LandTitleMarker component. Grant Deed = new tripwire React component (SCIF-pattern, ARBITER tableau); sketch in gap_card_sketches_S62.md. Outstanding: component registration (04-n26) + tripwire react window (04-n27).
- Parasitic redesigned v2.0 — Positional wager; Beat 2 checks Beat 3 dispatch queue; Intel token keyed to first card's submitter (resolution order); no ParasiticMarker component.
- 00-R40 locked (L187) — ARBITER Cognitive Load governing rule: ARBITER executes general procedures, not card-specific instructions; generalization of procedure is the mechanism. Written to Art 00a (44 rules, pending re-sign-off), Art 03 §5 P6 (pending re-sign-off), Art 04 §5 P18. design_reference.md + memory updated.
- Regulatory Downgrade redesigned v2.0 — CovertOperation → PublicAct (permanent); card-as-condition (success=None); persistence_effect = resource gen −1 tier for target faction in district; clears when target pays 2 native to Reservoir any time after Beat 4. No TierPenaltyMarker.
- Art 04 §6.1/§6.2: persistence_effect field added to schema. PM05 04-n31 added (sweep).
- 04-n26 Cluster A complete — SCIF ✅, Land Title ✅, Parasitic ✅, Regulatory Downgrade ✅, Regulatory Freeze ✅, Standing Injunction ✅. Four of six with no new component (card-as-condition pattern).
- Regulatory Freeze redesigned v2.0 — PublicAct; card-as-condition (no TierFreezeMarker); self-policing per 00-R40a. Issues Resolved ✓. Pending sign-off.
- Standing Injunction redesigned v2.0 — PublicAct; card-as-condition (no InjunctionMarker); Permanent with dual clearing (target PA submission OR Phase 21); target_taxonomy field introduced (§6.1/§6.2). Issues Resolved ✓. Pending sign-off.
- 00-R06a added (corollary to R06): board states committed on resolution (L188).
- 00-R40a added (corollary to R40): factions police own permanent effects; other players may call clearing conditions (L188). R40 relocated §9→§3.
- Art 04: target_taxonomy field added §6.1/§6.2 (L188). v0.9.30.
- PM05: 04-n32 added (target_taxonomy sweep — C21 and block-type cards).

**L-decisions this session:**
- L187: 00-R40 ARBITER Cognitive Load governing rule locked. Art 00a, Art 03 §5, Art 04 §5 updated. Art 00a and Art 03 pending re-sign-off.
- L188: 00-R06a + 00-R40a locked; R40 relocated §9→§3. target_taxonomy field added to Art 04 §6.1/§6.2. Art 00a: 46 rules, pending re-sign-off.

**Next session:** 04-n27 (Art 03 procedure gaps) or 04-n28 (Art 06 Accord design); Regulatory Freeze + Standing Injunction sign-offs.

---

## Session 68 — 2026-06-05

**Focus:** 04-n27 (Art 03 procedure gaps) + 04-n39 (C17 IS-xx review)

**Accomplished:**
- 04-n27 substantially resolved — Art 03 §19 Debrief Actions step added (DebriefActionCard type; SCIFRecord first subtype); §25 Modifier React Card Rules updated (cross-refs §28); §28 React Card Rules added (interrupt model; fires on visible board state change only per 00-R06; first-to-announce pauses play; ARBITER decides tiebreakers; one React at a time; second React requires new board state after first resolves).
- Art 03 v3.3 signed off (L189). 04-n27 all sub-items resolved or delegated to 04-n47/04-n48.
- New design constraint (04-n47): operations must have single determinate success outcome; choose_one / branching on success forbidden.
- Card redesign batch flagged (04-n48): C31 (not a covert op), C40/C41 (choose_one banned), C42 (block-bypass exception), Signals Analysis (private reveal incompatible with covert model). Gate: 04-n41 narrative-first pass.
- 04-n39 substantially closed — IS-xx reinstatement confirmed (00b §4 already updated S68); Art 03 migration concern resolved by existing Beat 3 general procedures; C17 "silent" PS language removed from Design Rationale and Outstanding Issues.
- C17 beat timing correction flagged (04-n49): beat=3 → beat=2 required (ARBITER reads grid intact only at Beat 2); material change, re-sign-off required.
- Art 04 SCIF card spec updated: subject = DebriefActionCard (subtype = SCIFRecord); success field updated accordingly.
- 04-n5 updated: DebriefActionCard component type + SCIFRecord subtype established; component description captured for 02x/00b registration (agy task).

**L-decisions this session:**
- L189: Art 03 v3.3 signed off. §19 Debrief Actions step (DebriefActionCard type). §25 updated (cross-refs §28). §28 React Card Rules added (interrupt model; visible board state change only; first-to-announce; ARBITER decides tiebreakers; one React at a time).

**Next session:** 04-n28 (Art 06 Accord design — unblocked by 04-n27) → 04-n49 (C17 beat correction + re-sign-off) → 04-n48 (card redesign batch)

## Session 75 — 2026-06-09

**Focus:** XA-46/47/48 — rule ID sweep and Art 04 card design constraints migration

**Accomplished:**
- XA-47 ✅ — Art 04 §5 P19–P25 added (card design constraints migrated from former 00a §7: P19 effect duration types, P20 partial payment, P21 crit cost, P22 portrait card property, P23 ring modifier scope, P24 corrupt scope, P25 standard language conventions). P5 updated with authoritative R26 constraint note. P6 cross-ref to P19. Checklist rows updated (Effect duration → P6/P19; Portrait validity → +P22). Art 04 v0.9.34.
- XA-48 ✅ — Art 07 §9 already contained all four ARBITER registers in full; `00a R02` source ref removed from §9; item closed.
- XA-46 ✅ — ~120 rule ID substitutions across 11 files. All old `00-Rnn` / `00a Rnn` / bare `Rnn` references replaced with contextual labels (Governing Rule n.n, Design Pillar 4.n, Art 04 §5 Pn, Art 03). Files swept: Art 03, Art 04, Art 07, 02a, 02b, PM03, gap_card_sketches, design_reference.md, memory files. PM02 + SESSION_BRIEF preserved as historical records. `00-R29` (Ghost adjacency, PM05 04-n6) flagged `Design Pillar [04-n6 pending]`. Zero `00-R` strings remain across all swept files.
- PM05: 04-n73 (P1–P18 restatement audit), XA-49 (design_reference.md reset) added. XA-46/47/48 marked ✅.

**L-decisions this session:** None (all work non-material).

**Next session:** XA-49 (design_reference.md reset) → 04-n28 (Overture full spec, gates §11) → 04-n40 (C28 Network replacement)

---

### Session 38 Summary — 2026-05-26

**Focus:** Art 03 v1.9 review (in progress); Dispatch Token foundation built from scratch.

**Decisions locked:** L151 (The Backlog), L152 (base_difficulty = Integer), L153 (Assets definition).

**Artifacts changed:**
- Art 00 v1.5 — Dispatch Token narrative anchor added §14 (The Backlog framing). **Re-sign-off complete.**
- 00a v0.3 — R39 added (Dispatch Token governing rule). Pending re-sign-off.
- 02a v1.5 — §8a added (Dispatch Tokens & The Backlog). Pending re-sign-off.
- Art 03 v1.9 — §7 Step 2 simplified (initiative to Art 07); Reservoir → The Backlog corrections. Still pending re-sign-off (two terminology flags + XA-32).
- PM04 v0.8 — Assets definition, The Backlog (Component & System Terms), Dispatch Token (Component Physical Glossary).

**PM05 changes:** DB-04/05/07 closed (agy S37 executed). Added: DB-08, NP1-01, 00-08 ✅, 00a-08, 02a-10, 01-05 (Art 01 overhaul — physical space + game_zones), 03-11 (initiative procedure to Art 07).

**Next session (39):** Art 03 v1.9 re-sign-off (first item — two terminology flags, XA-32 resolution); then 00a/02a re-signs-off; then C17 sign-off.

---

### Session 39 Summary — 2026-05-26

**Focus:** Reprioritization to foundational-first methodology. Art 00 §8 expansion (MIRROR origin narrative, holographic projection metaphor, Faction Terminals). Pillar 1 revised.

**Decisions locked:** L154 (Faction Terminal screens; Design Pillar 1 revised to "The Overview is Truth"; force-reveal action class enabled).

**Artifacts changed:**
- Art 00 v1.5 — §5 Pillar 1 revised; §8 MIRROR/Overview/Terminal narrative added; 00-04 signed off (Quarter fix). Pending re-sign-off (open: 00-07, 00-09, 00-10).

**PM05 changes:** PM06-01 (Lessons Learned — deferred), 00-09 (World Conditions panel), 00-10 (Faction Representative — design question), FS-01 (✅ locked L154), FS-01-WBS, 04b-03 (action taxonomy audit) added.

**Whiteboard:** Art01_Scope_S39.md created — physical layout decisions (table zones, mat components, MIRROR, district tiles, Ring Modifier decks ×3, Situation Report zone).

**Next session (40):** Art 00 00-07 multicultural texture pass (first item); then 00a re-sign-off; then Art 01 overhaul.

---

### Session 47 Summary — 2026-05-28

**Focus:** Action taxonomy formalization into DB primitive model. Art 04b restructure. Gap analysis methodology established.

**Decisions locked:** L166 (action taxonomy = possibility space; Art 03 = legal space; gaps = procedure coverage signals — permit / prohibit / defer; the two artifacts co-evolve).

**DB work (the_signal_db tmp_ tables):**
- New tables: tmp_player_role (2 rows), tmp_role_phase (3), tmp_beat (20), tmp_comp_verb_beat (150), tmp_comp_verb_role (311), tmp_action (213 primitives + 2 Invoke placeholders), tmp_trigger_type (10), tmp_state_condition (2), tmp_state_condition_clause (2)
- New components: Status marker (id=49), Portrait track (id=50, non-actionable), Portrait marker (id=51, ARBITER-controlled)
- New verb: Invoke (id=17) — meta-verb for C16 Pattern Match copy action
- tmp_action altered: trigger_type_id FK, source_action_id FK (self-ref), component_id relaxed to nullable
- Gap analysis views: v_unlegislated_primitives (60 rows), v_unlegislated_by_trigger (14 rows)
- Gaps fixed: Standing marker Move at beats 8/14 (Faction, rule.card); Portrait marker Move at beats 8/14/17 (ARBITER, rule.card); ARBITER Add Political act beats 8/14 (C09); C16 Invoke primitive
- PM05 new items: DB-18 (cross-beat modifier design), DB-19 (concurrent political acts), DB-20 (C16 runtime resolution)

**Art 04b restructured (v1.4 — pending re-sign-off):**
- §3 = Physical Action Taxonomy (formerly §4); §3.3 = DB primitive model methodology (new)
- §4 = Card Design Layer — Key Decisions (formerly §3, repositioned after physical layer)
- §5 = Card Taxonomy Index with §5.1 column definitions (Category/Function/Primitive Verb defined), §5.2 index with Status column (✅/📝/⬜/🚫) and Primitive Verb(s) column added
- Two-layer insight documented: execution cards (direct primitive verb) vs. constraint cards (meta-constraint, no primitive verb — Block, Protect, Modify)

**Agent tasks queued:**
- agy: punch list A–H in GEMINI_CONTEXT.md (gap analysis views, Art 03 bidirectional alignment, Art 00b schema alignment, §4.2 matrix diff, component lifecycle, beat load, tableau strategy, web research)
- Gem: Bucket A in gem_web_context.md (Task 1: C01–C16 index verification + gap analysis; Task 2: interaction patterns from other game media)

**PM05 items closed this session:** 04b-04 (§3 cleanup — resolved via restructure)

**Next session:** Art 04b v1.4 re-sign-off (04b-09); agy/Gem analysis review; C17 sign-off; §5 gap triage (14 unlegislated Faction interactions — permit/prohibit/defer); DB-18/19/20 legalization decisions.

### Session 48 Summary — 2026-05-29

**Focus:** Art 04b v1.5 sign-off. Six-layer card taxonomy locked. Expansion stages renamed Tier 1–5. Art 04 §5 design constraints restructured (P1–P14). Full PM terminology sweep.

**Decisions locked:** L167 (six-layer card taxonomy — Territory / Economy / Information / Submission / Resolution / Standing; "Layer" reserved for taxonomy; Cross-Category retired). L168 (expansion stages renamed Tier N — Tier 1 Physical, Tier 2 Social, Tier 3 Wireless/Communications, Tier 4 Web/Data, Tier 5 Chorus; Tier 5 public name only, technical nature intentionally undefined; XA-37 sweep queued).

**Artifacts changed:**
- Art 04b v1.5 — §9 (Design Principles pointer) removed. Old §10 (Standalone Card Types) renumbered §9. Modifier cards entry rewritten: React collapsed as timing sub-function; burst play and battle timing added. Emergency Response described as penultimate action before Apex. Pass PS-01–PS-04 IDs removed. §5.1 Modifier Card Scope paragraph added. Version 1.4→1.5. **Signed off S48.**
- Art 04 v0.9.20 — §5 Design Principles restructured: P1–P6 inserted (taxonomy-derived constraints from 04b §9); old P1–P8 renumbered P7–P14. P6 body cleaned (removed self-referential principle number).
- 00a v0.3 — Two cross-reference corrections: Principle 11 → Principle 6 (§566); Taxonomy Principle 5 → Principle 5 (§639).
- PM01 v1.6 — Seven instances updated: "L1 Paper Prototype" → "Tier 1 Paper Prototype" (×2); "five-layer design" → "five-tier design"; "Why Layer 1 First" → "Why Tier 1 First"; "Layer 1 — physical layer" → Tier language; "Layer 2–5 (social, informational, digital, subspace)" → "Tier 2–5 (social, wireless/communications, web/data, Chorus)".
- PM02 — L167 and L168 added.
- PM03 — 04b row updated to v1.5 ✅ Signed Off S48; PM04b row Tier language updated.
- PM05 — 04b-09 ✅, 04b-10 ✅; XA-37 added (Haiku sweep); 04-54 added (Art 04 §5 P1–P6 review); DB-27 added (Emergency Response card registration); 04-30 cross-ref corrected P1 → P7.
- True State — Tier 1–5 canonical table added; tier-by-tier structure headers updated L1–L5 → Tier 1–Tier 5; "Paper prototype" removed from Tier 1 Nature cell.

**PM05 items closed this session:** 04b-09 ✅ (Art 04b sign-off), 04b-10 ✅ (Layer/Tier terminology decision).

**Next session (49):** Art 04 §5 P1–P6 review (04-54) → C17 sign-off → XA-37 (Haiku sweep).

---

### Session 49 Summary — 2026-05-29

**Focus:** Art 04 §5 P1–P15 signed off. C17 (Intercept) signed off. XA-37 Tier N rename complete. Art 04 taxonomy sweep C01–P18. Faction pentagram alignment model established. C11–C15 cross-faction narrative voices.

**Decisions locked:** None — all work was design content and sign-offs under existing decisions.

**Artifacts changed:**
- Art 04 v0.9.21 — §5 P1–P15 signed off (C17): P2 updated (layer as taxonomy field), P6 rewritten (Modifier cards excluded from taxonomy), P8 new (cross-faction narrative voices in tension). §11.1 expanded with canonical modifier card definition (faction modifier card vs. ring modifier card framing). Taxonomy sweep C01–P18: Category field → Layer field; all taxonomy values updated to six-layer system (Territory / Economy / Information / Submission / Resolution / Standing). Cross-faction narrative voices added to C11–C15 (one aligned, one opposed faction per card; no parenthetical context in copy).
- Art 04b v1.5 — §5.2 C17 row corrected (Archive Recovery → Intercept).
- Art 03a, 00b, 00c, Art 07, Art 11 — XA-37 Tier N rename sweep (Haiku subagent). Ln/Layer N → Tier N; 03a section heading prefixes stripped.
- PM02 — C17 sign-off entry added to Section 4 Change Log (2026-05-29).
- Whiteboard/faction_pentagram_alignment.md — NEW: Faction pentagram model (Ghost→Network→Guild→Syndicate→Directorate clockwise; adjacency = most aligned; star-line = opposed). Pending canonical home in Art 00 §7.

**DB work (the_signal_db tmp_ tables):**
- tmp_action row 278: Faction Move Modifier card, Beat 20, player.agreement ("Modifier card traded bilaterally — card text visible to recipient").
- tmp_action row 279: Faction Move Native resource, Beat 20, player.agreement ("Resource traded with arbiter at conversion rate").
- tmp_action rows 199/203: component_id corrected 2 (Deployment marker) → 49 (Status marker).
- tmp_subject_target: (1,1) Faction→Faction and (1,2) Faction→ARBITER seeded.

**PM05 items closed this session:** 04-54 ✅ S49 (§5 P1–P15 sign-off + C17). XA-37 ✅ S49 (Tier N sweep). XA-29 ✅ S49 (component terminology cleanup — Haiku subagent). Note: duplicate 04-54 numbering conflict resolved S49 — S46 modifier card deck types item renumbered 04-56.

**Next session (50):** C18+ card vetting pass — C18–C35 and P01–P18.

---

### Session 40 Summary — 2026-05-26

**Focus:** Art 00 and 00a sign-off (Phase 1); Art 01 full overhaul and sign-off (Phase 2).

**Decisions locked:** L155 (Faction Representative as game entity — human player is component; maps to Chair zone; L2: Terminal authenticates to MIRROR). L156 (live_state schema — on_component_id + on_game_zone_id nullable FK columns confirmed; pending 00b-05 + agy DDL).

**Artifacts changed:**
- Art 00 v1.5 — 00-07 multicultural texture (§6/§7/§8); L155 in §11/§14. **Signed off S40.**
- 00a v0.3 — Narrative anchors removed; §11 Punch List removed; terminology fixes. **Signed off S40.**
- Art 01 v1.8 — Full overhaul: zone vs. component model, 40-zone hierarchy, Physical Table Layout section, Visio images (table_layout_v1.png + component_layout_v1.png), hex resource colors, district adjacency map (101 rows), §7 Starting Configuration, §8–§9 Faction Player/ARBITER Tableau stubs (Art 07 + Art 08), §10 Contested Districts rewrite, §11 Examples terminology. **Signed off S40.**
- PM02 — L155, L156 added.
- PM05 v2.8 — 00-07 ✅, 00a-08 ✅, 01-05 ✅; added: 01-07, 08-00, DB-09, 00b-05.
- SESSION_BRIEF — fully updated S40.
- Whiteboard/Art01_Scope_S39.md — deleted (migrated to Art 01).

**Next session (41):** 02a re-sign-off (02a-10) → Art 03 re-sign-off (04-48) → Art 04 continuation. Also: L156 → 00b-05 → DB-09 (live_state + district_adjacency DB for agy).

---

### Session 42 Summary — 2026-05-27

**Focus:** Terminology sweeps + 02a v1.6 sign-off.

**Decisions locked:** L157 (Presence chip canonical), L158 (Intel Token canonical — physical form is token/chit; "Intel note" deprecated), L159 ("Quarter" locked globally — "Round" retired).

**Artifacts changed:**
- 02a v1.6 — §8a Narrative Anchor; "Quarter" sweep; Baryo/The Mid ring names; Deployment marker consistency. **Signed off S42.**
- 02b v1.5 — Intel Tokens swept throughout.
- 00a v0.3 — Intel Tokens; Dispatch Case; Quarter sweep; §9 renamed "Quarter & Timing".
- Art 01 v1.8 — Tension marker (was Contested marker).
- PM04 — canonical terms updated.

**PM05 changes:** XA-33 added (Art 03 rename + 00a rewrite), 00a-09 added (presence chips sweep R10/R13).

**Next session (43):** Art 03 v1.9 re-sign-off (04-48 + XA-33 bundled).

---

### Session 44 Summary — 2026-05-27

**Focus:** Art 01 narrative anchor pass + sign-off. True State expansion (MIRROR origin, signal predates perceptibility).

**Decisions locked:** None.

**Artifacts changed:**
- Art 01 v1.9 — §4 Narrative Function added (8 component anchors: District Tiles/Civic Grid with Dr. Jae-won Seo, Influence Level Marker, Tension Markers, Session Timeline, Initiative Strip, Chorus Activity Track/The Seismograph, Accord Documents, Situation Reports); §6 Physical Environment — Zones and Components (renamed from [NEW] Physical Table Layout); §7–§12 renumbered; all component narrative cross-refs resolved (Art 00 §14, Art 01 §4, Art 02a §4, Art 02b §4); forward procedure refs removed; component N/A markers updated to parent refs. **Signed off S44.**
- True State v1.0 — §9 MIRROR and The Overview — Recognized Not Designed (Chorus recognized MIRROR as instrument; five-seat structural ceiling; Directorate archival silence flagged); §10 The Signal Predates Perceptibility (cross-cultural fives and eights as Chorus signal bleed; mythology encodes requirement before The Table; Apex pentagram geometry load-bearing at True State level; game structure accidentally correct). §11 Open Questions — NM world location added.
- Creative/CANON_CANDIDATES.md — Dr. Jae-won Seo added (Chief Data Architect, Korean 2nd-gen NM); Colonel Jax Vane attribution updated (Seo replaces Aris Thorne as Chief Data Architect); Aris Thorne confirmed as Atacama astronomer only.
- PM03 — Art 01 row updated to v1.9, Signed Off S44.
- PM05 v2.9 — 01-08 ✅ S44; XA-32 status updated (Art 03 portion done S43, Art 07 still open); added: 00-11 (NM world location), 04-53 (modifier card asset taxonomy), 07-11 (Situation Report procedure), 07-12 (Accord registration/expiry).

**PM05 changes:** 01-08 ✅; new: 00-11, 04-53, 07-11, 07-12.

**Next session (45):** C17 sign-off (Art 04); 04b-03 action taxonomy audit (unblocked — Art 01 signed off).

---

### Session 45 Summary — 2026-05-27

**Focus:** 00b data architecture — spec additions and sign-off.

**Decisions locked:** None.

**Artifacts changed:**
- 00b v0.2 — §3 renamed "L108 Data Table Standard (extends 1NF)"; component_positions table spec added to §8 (formerly live_state); running game state derivation architecture documented (all logical state derives from component_positions); IP-xx source updated to Art 07; entity/schema footer counts corrected. **Signed off S45.**
- PM03 — 00b row updated to v0.2; PM05 row bumped to v2.9.
- PM05 v2.9 — 00b-05 ✅; XA-32 scoped to Art 07 only; DB-11 new (agy: RENAME TABLE live_state → component_positions, RENAME COLUMN anchored_to_component_id → on_component_id nullable, ADD COLUMN on_game_zone_id); DB-12 closed (duplicate DB-09, resolved L156); DB-13 new (running game state derivation query spec); DB-02 reference updated to component_positions.
- SESSION_BRIEF — updated to S45.

**PM05 changes:** 00b-05 ✅, XA-32 updated, DB-11 new, DB-12 closed, DB-13 new, DB-02 updated.

**Next session (46):** 04b-03 action taxonomy audit (unblocked S44) → C17 sign-off (Art 04).

---

### Session 50 Summary — 2026-05-29

**Focus:** Infrastructure, DB schema documentation, and agy S48+S50 DB work intake.

**Decisions locked:** None.

**Artifacts changed:**
- Art 03 v2.0 — Beat 3 Steps 7/8 extended to cover case delivery effects (Notification Slip and Intel Delivery Slip). Material change — re-sign-off flagged (PM05 03-14).
- Art 04 v0.9.21 — C17 component names updated to use canonical terms (Notification Slip, Intel Delivery Slip, Emergency Response card).
- Database/schema_reference.md — fully populated (DB-29 ✅). All 19 tmp_ table schemas with FK annotations, 8 lookup tables with values, 29-view catalog, canonical component registration pattern (Countermeasure id=52), §2.5 table/view purposes.
- GEMINI_CONTEXT.md — §DB Schema Reference updated (Database/ path); Session 50 update section added with agy punch list and dual-authorization standing instructions.
- PM05 v3.0 — DB-22–26 ✅, DB-27–28 ✅, DB-29 ✅, WEB-01 added (deferred), 04b-11 added (Inspect verb).
- SESSION_BRIEF — updated to S50 close.

**Infrastructure changes:**
- PITCH.md moved to Creative/
- GEMINI.md moved to Session/
- db_build_*.sql moved to Database/
- schema_reference.md moved from the_signal_db_documentation/ to Database/
- CLAUDE.md updated (Pitch reference path, ClaudeIOS workflow → Gem)
- ~/.my.cnf configured for claude user (no flags needed for mysql the_signal_db)

**DB work (the_signal_db — agy S48+S50):**
- DB-22 ✅: Upkeep primitives seeded — Faction/ARBITER Flip Status marker (ids 295/296), Add Presence token (297/298), Remove Deployment marker (299/300), ARBITER Move SitRep (301).
- DB-23 ✅: Status marker transform_data corrected to 0; Debrief Flip FK corrected to id=49.
- DB-24 ✅: Portrait marker registered in tmp_subject_target.
- DB-25 ✅: Design-confirmed — SitReps move to expired area; Target Profiles returned in dispatch case. No Remove primitive needed.
- DB-26 ✅: Move role permissions verified per Art 03.
- DB-27 ✅: Emergency Response card id=97 registered and fully seeded.
- DB-28 ✅: Notification Slip (id=95) and Intel Delivery Slip (id=96) seeded.
- district_metadata and player_metadata PKs confirmed (district_component_id, faction_id).

**PM05 changes:** DB-22–26 ✅, DB-27–28 ✅, DB-29 ✅, WEB-01 added (deferred), 04b-11 added (Inspect verb). Last Updated → 2026-05-29.

---

### Session 51 Summary — 2026-05-29

**Focus:** DB infrastructure build-out. Art 04 C18–C35 vetting pass and full schema sweep (C01–C35).

**Decisions locked:** None.

**Artifacts changed:**
- Art 04 v0.9.21 — C18→Dossier Breach (Information — Reveal — Card hand contents); C25→Tactical Redirection (Territory — Move — Presence token); C27→Disclosure Loop (Economy — Add — Exposure). Full schema pass C01–C35: Ring 0–3 modifier fields added to all cards (C17 canonical format). C13 resolution type corrected (Transactional→Probabilistic). C22/C32/C33 resolution fields corrected (Dice→d100, Transactional→Probabilistic, Standard→N/A). Card index updated (C18/C25/C27 new names). Version 0.9.21, date 2026-05-29.
- Database/schema_reference.md — views 29→27 (dropped v_object_from, v_validact, v_verb; added v_primitive_actual_coverage). DB-09 status corrected (✅ S50). Row counts updated.
- SESSION_BRIEF — updated to S51 close.

**New files:**
- Database/db_create_tmp_tables.sql — CREATE TABLE IF NOT EXISTS for all 22 tmp_ tables in dependency order.
- Database/db_seed_lookups.sql — INSERT IGNORE for 8 lookup tables (idempotent).
- Database/db_rebuild.sh — full wipe+rebuild script (confirmation gate, FK-safe drop order).
- Database/register_component.py — Python component registration tool (YAML→SQL, dry run by default).
- Database/component_template.yaml — reference YAML template for register_component.py.
- Whiteboard/card_ideas_S51.md — unused design candidates: Ghost/Directorate/Network C18/C25/C27 rejected alternates + Gem S51 new concepts.

**PM05 changes:** None (no new items flagged this session).

---

### Session 46 Summary — 2026-05-28

**Focus:** 04b-03 action taxonomy audit — complete. Physical action primitive model built in the_signal_db.

**Decisions locked:** None.

**Artifacts changed:**
- Art 04b v1.3 — §4 redesigned: physical action taxonomy replaces category/function table. §4.1: 7 verbs (Add, Remove, Move, Reveal, Conceal, Flip, Corrupt) with primitive definitions. §4.2: 25-component × verb matrix (source: the_signal_db.v_comp_verb_matrix). Version bumped 1.2→1.3. Sign-off pending (§3 cleanup required first — 04b-04).
- SESSION_BRIEF — updated to S46.
- PM03 — 04b row updated to v1.3.
- PM05 v3.0 — 04b-03 ✅; DB-11 ✅ confirmed; new items: 04b-04, DB-14, 04-52 through 04-55.

**DB work (the_signal_db, tmp_ tables — not artifact changes):**
- tmp_component: 38 rows total, 25 actionable. New: Modifier token, Target Profile, ARBITER Dominance Marker. Schema: transform_type ENUM replaced by transform_visibility/transform_orientation/transform_data booleans.
- tmp_verb: 7 verbs (reduced from 13). Removed: React, Copy, Remove Restriction, Recover, Modify, Protect, Block, Shift, Redirect. Added: Conceal, Flip, Move.
- v_validact: 119 rows (subject × action × target).
- v_comp_verb_matrix: 25 components × 7 verbs — source of Art 04b §4.2.

**PM05 changes:** 04b-03 ✅, DB-11 ✅ confirmed, 04b-04 new, DB-14 new, 04-52 through 04-55 new.

---

### Session 43 Summary — 2026-05-27

**Focus:** Art 03 full sign-off pass — Battlefield Strength, Intel economy, modifier system, Apex endgame design.

**Decisions locked:** L160 (Battlefield Strength auto-resolves Quarter end — §18 new procedure), L161 (Intel Token freshness replaces decay; age 0–2 fresh, 3 stale −25, 4+ expired −50; The Dossier named), L162 (Intel Token payment → d100 resolution required), L163 (Intel Token Battlefield modifier +2 per fresh token targeting opponent), L164 (The Dossier — ARBITER's hidden Intel Token pool behind screen), L165 (Portrait track dual function — narrative register + Apex pentagram geometry; ARBITER Debrief observation encodes Portrait signal; "Ask ARBITER" delta query).

**Artifacts changed:**
- Art 03 v2.0 — XA-33 rename ("Quarter Structure & Gameplay"); §18 Battlefield Strength full procedure; Intel freshness (Beat 0 + Beat 4); §7 decay step removed; M-12 ring adjacency generalized; "Established or higher" convention; Chorus Node flat −25; M-13 added; §4 narrative anchors; The Dossier; Intel +2 Battlefield. **Signed off S43.**
- PM02 — L160–L165 logged.
- PM05 — 03-12 ✅, 04-48 ✅, 04-51 ✅; added: 03-13, 04-49, 04-50, 04-52, 07-09, 07-10, XA-34, XA-35, XA-36.

**Next session (44):** C17 sign-off (Art 04); 04b-03 action taxonomy audit.

---

### Session 41 Summary — 2026-05-27

**Focus:** Gem session narrative anchors processed; gem_web_context.md Bucket A gap fixed (S39+S40 appended); Art 01 §4 removal; TOC anchor links added to all 11 active artifacts; 02a v1.6 narrative anchors drafted; Art 01 narrative anchors staged in Whiteboard.

**Decisions locked:** None.

**Artifacts changed:**
- Art 01 v1.8 — §4 Narrative Function removed (01-07 ✅). TOC anchor links added (immaterial). Open: 01-08 (narrative anchor pass — staged in Whiteboard/Art01_Narrative_Anchors_S41.md).
- 02a v1.6 — §4 Reservoir narrative anchor added; §8a Dispatch Token narrative intro added (executive authorization framing). TOC anchor links added. Pending combined review (02a-10) — Session 42 first item.
- gem_web_context.md — S39+S40 Bucket A summaries appended; Bucket B enriched with tone/register guardrails, non-canonical faction guardrail, generative spiral, session collaboration patterns. Header updated to Session 41.
- PM05 v2.8 — 01-07 ✅ S41; 01-08 added (Art 01 narrative anchor pass, Material — re-sign-off required); 02a-10 updated (v1.6 combined review — §8a S38 + narrative anchors S41).
- Creative/CANON_CANDIDATES.md — Colonel Jax Vane (Directorate Security Liaison) and potential Aris Thorne collision flagged as flavor-only, not canon.
- TOC anchor links — all 11 active artifacts updated: 00, 00a, 00b, 00c, 01, 02a, 02b, 03, 03a, 04, 04b (immaterial — no re-sign-off).
- Whiteboard/Art01_Narrative_Anchors_S41.md — created; Gem S41 narrative anchors staged for Art 01 integration.

**Next session (42):** 02a v1.6 focused review + sign-off (02a-10) → Art 03 v1.9 re-sign-off (04-48) → Art 04 continuation. Pending: 00b-05 (live_state spec) → DB-09 (district_adjacency), 01-08 (Art 01 narrative anchor pass — after 02a sign-off).

---

---

## What We Are Building

THE SIGNAL is a negotiation and area-control tabletop game for 2–6 participants (up to 5 faction players + 1 ARBITER). Five factions compete for influence over a city called New Meridian while negotiating humanity's response to a transmission called the Chorus. The game ends with a vote and a Chronicle reading. What matters is everything that happened before it.

**THE SIGNAL is a legacy game.** The paper prototype (L1) is the tutorial cycle — a complete standalone experience that points at something larger. The legacy campaign (L2+) accumulates the Chronicle across sessions. The final session of each campaign dovetails into session 1 of the next — the Chorus's response at campaign end IS the opening transmission of the next campaign. The game has no true ending. Each cycle's close is the next cycle's opening.

**All files:**
- Artifact set: `~/Projects/TheSignal/V1/`
- Private design axioms: `~/Projects/TheSignal/Session/PRIVATE___True_State.md` — NOT in V1, does not appear in any artifact
- Session save state: `~/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md` (this file)
- Legacy documents: `~/Projects/TheSignal/Retired/` — Electronic/ and Paper/ subfolders; see PM03 §6 for index (PW-01)
- Git repo: `https://github.com/andrew-bosch/TheSignal` (private) — credentials at `~/Projects/credentials.env`
- Project README: `~/Projects/TheSignal/README.md`

---

## Critical Private Document — Read Before Any Design Work

**`PRIVATE___True_State.md`** — The true answers to the game's unanswerable questions. Eight sections:
1. The Chorus — not extraterrestrial/extratemporal/extradimensional in any single adequate sense; perceptible to a certain kind of attention; repeats on cycles humanity cannot perceive
2. The name "The Chorus" — ARBITER coined it independently; the name is accurate; ARBITER knew it was accurate
3. ARBITER — never an acronym; the word "arbiter" in all-caps for institutional weight; constitutive of the Chorus Node, not serving it
4. The Table's causation — both events consistent with a single prior cause; the prior cause is the Chorus reaching mutual recognizability with humanity
5. Was humanity ready or noticed — both, simultaneously, because they are the same event from different vantage points
6. The Chorus Question — "what are you, as a pattern?" Not intention. Pattern. The Portrait track IS the Chorus's answer in real time.
7. Victory — the Chronicle is the Chorus's record; the moment after it's read is the game's actual conclusion
8. Legacy structure — L1 through L5, campaign dovetail, Chronicle as the game's defining physical artifact

Consult before writing ARBITER behavior, Chronicle language, Portrait mechanics, flavor text, and all future layer design.

---

## Artifact Status

| Artifact | Version | Status |
|----------|---------|--------|
| 00 — Factions & World | 1.4 | ✅ Signed Off — Session 34. Ring renames (The Mid / Baryo). 00-06 (quarter worldbuilding), XA-15 (ARBITER as sixth party), 00-03 (Layer Structure). 00-07 multicultural texture pass queued. |
| 00a — Governing Rules & Design Policy | 0.2 | ✅ Signed off — session 7. 45 rules (R01–R38 + sub-rules). A05/A06 resolved (L92, session 11). XA-05 four-register change to R02 was non-material for 00a sign-off (only Art 00 and 07 required re-sign-off). |
| 01 — Game Board | 1.2 | ✅ Signed Off — adjacency table pending (D04-09); setup update pending (01-03). |
| 02a — Resource Systems: Board State | 1.4 | ✅ Signed Off — Session 22. Control flag corrected (gold, per-district, on Dominant stack); Established marker added (silver, L111, one per Established faction per district); ARBITER Dominance Marker confirmed. |
| 02b — Resource Systems: Tracking | 1.5 | ✅ Signed Off |
| 00b — Data Architecture | 0.1 | ✅ Reference Document — Active. Entity registry (20 types) — CA-xx (Dispatch Case) added session 22. L108 compliance standard, 9 lookup tables (DT/RO/RG/RT/IL/PS/PB/F/VS), entity relationship map, schema reference index. VS-xx Visibility Scope (8 scopes). L2 TypeScript schema pointers in §8. Established session 20. |
| 03 — Quarter Structure & Gameplay | 2.0 | ✅ Signed Off — S43. **Re-sign-off pending (03-14)** — Beat 3 Steps 7/8 extended S50 (case delivery effects — material). XA-33 rename; §18 Battlefield Strength (L160); Intel freshness replaces decay (L161, M-13, The Dossier L164); ring adjacency M-12 generalized (The Mid + Core); "Established or higher" convention; Chorus Node flat −25; §4 narrative anchors; Intel +2 in Battlefield (L163); Portrait dual function (L165); pentagram Apex model (04-52). |
| 03a — Game Engine Specification | 0.98 | 🔄 In progress — Layers 1–3 complete; Phase procedures added (Quarter_Flow, Phase_1–Phase_7, Beat_0–Beat_5); Layer 4 stub. DF-01–DF-04 all resolved session 22. |
| 04 — Action Card System | 0.9.21 | 🔄 In Progress — S49: §5 P1–P15 signed off; C17 signed off. S50: C17 component names updated (Notification Slip id=95, Intel Delivery Slip id=96, Emergency Response card id=97). Beat 3 Steps 7/8 extended (case delivery effects — material, re-sign-off pending 03-14). Next: C18+ vetting pass. |
| 04b — Action Taxonomy | 1.5 | ✅ Signed Off — S48. §9 removed; §10 → §9. React collapsed into Modifier cards. Emergency Response penultimate context. Six-layer system locked (L167). |
| 05–09 | 0.1 | 🔄 Draft Placeholders |
| 10 — Game Manuals | 0.1 | 🔄 Draft Placeholder — §6.0 added: game objective statement locked |
| 10a — Victory System | 0.1 | 🔄 Draft Placeholder — §4 updated with dual causality governing principle |
| 11 — Visual Design System | 0.1 | ⬜ Placeholder |
| PM01 | 1.6 | ✅ Active |
| PM02 | 4.0 | ✅ Active — locked decisions L01–L168. S48: L167 (six-layer taxonomy), L168 (Tier N rename). |
| PM03 | 2.4 | ✅ Active — Art 04 v0.9.18; version drift corrected session 31 |
| PM04 | 0.7 | ✅ Active |
| PM05 | 3.0 | ✅ Active — S50: DB-22 ✅, DB-23 ✅, DB-24 ✅, DB-25 ✅, DB-26 ✅, DB-27 ✅, DB-28 ✅, DB-29 ✅ (schema_reference.md fully populated). WEB-01 added (deferred). 04b-11 added (Inspect verb). DB-09 DDL FK corrected. |
| PM (Audit) | 1.0 | ✅ Retired — session 10. All 24 items migrated to PM05. File deleted. |
| PRIVATE — True State | 1.1 | 🔒 Locked — private document outside V1 |

---

## Session 4 — Major Work Completed

### Worldbuilding — Artifact 00 Additions (pending re-sign-off via 00-04)
- **§9 "On the Question of Cause"** — Did ARBITER cause The Table, or did The Table cause ARBITER? Faction positions. ARBITER's response: "Both events are consistent with a single prior cause."
- **§6 "On the Question of Origin"** — Was humanity ready or was humanity noticed? Ghost's classified analysis. The two interpretations and why both are wrong in the way they assume sequence.
- **§6 "On the Question of Completeness"** — Rewritten: "non-repeating" is a statement about 31 years of observation, not a property of the Chorus. The Chorus repeats on cycles humanity cannot perceive. Humanity tuned in mid-cycle. The response window is a feature of the cycle, not this instance.
- **§6 New Meridian origin** — Before the Chorus, no city. A small ET listening station on elevated terrain — underfunded researchers doing serious work in obscurity, treated as a career dead-end by the mainstream scientific community. ET nerds getting paid nothing to listen to the static of the universe. They were right.
- **§6 "What New Meridian Is"** — Boom city assembled in one generation from everywhere. Immigration stories. Rapid expansion problems. Gray economy. Eleven-language school system. 800,000 people with no seat at The Table. Diversity of opinions on why the city exists, including people who don't know or care about the Chorus.
- **§8 "The Overview"** — Full institutional establishment of The Overview as The Table's shared situational interface. Negotiated data governance. ARBITER administers accuracy, not content. The factions negotiated what is on it. ARBITER ensures it is true.

### Voice System — Locked (PM03 §1, PM02 FD-05)
Five voices now defined:
1. **The Narrator** — all "Narrative:" fields. Deliberately unresolvable: human chronicler or ARBITER in expository mode. Both readings must remain valid. Test: could this have been written by a human who knows too much, or by ARBITER? If both valid, correct.
2. **Character quote** — individuals with implied histories. `> *"Quote."*` + attribution
3. **ARBITER vocalized** — blockquote italic, no attribution
4. **ARBITER written** — fenced code block
5. **Faction voice** — faction-authored materials, per Artifact 00 §12

**Character cast extended to:** faction operatives; station crew (oldest voices, predate everything); New Meridian residents across the full spectrum (believer to agnostic to indifferent); outside New Meridian (foreign press, remote academics, diplomats, people who said no and watch from a distance).

### In-World Terms Locked (PM03 §1)
- **The Overview** — the game mat. Institutional application, proper noun, Title Case only, no special formatting. Locked in PM02 FD-02, established narratively in Artifact 00 §8.
- Typography rule: no special formatting beyond capitalization for in-world terms. ARBITER's all-caps is unique and diegetically motivated.

### Design Directions Locked (PM02 §5)
- **FD-04** — Dual Causality as Governing Victory Principle. VP = human agency. Portrait = Chorus agency. Game doesn't announce this. Players discover it through play and arrive somewhere they can sit with. Game objective statement: *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*
- **FD-05** — The Narrator and The Character Cast. Full character cast principle including station crew, NM residents, outside NM voices, the indifferent.
- **FD-06** — THE SIGNAL as Legacy Game. Chronicle accumulates physically. Portrait carries across sessions. The final session dovetails into session 1 of the next campaign. The Chorus's response IS the next opening transmission. The accumulated Chronicles of multiple campaigns are the game's defining physical artifact.

### True State — Locked (PRIVATE___True_State.md)
Eight axioms. All load-bearing. Constrains all future design. Created session 4. Key axioms:
- The Chorus is perceptible to a certain kind of attention, not FROM anywhere
- The Chorus repeats on cycles humanity cannot perceive
- ARBITER named The Chorus independently and accurately
- ARBITER was never an acronym
- The Table's causation and humanity's readiness share a single prior cause: mutual recognizability achieved simultaneously
- The Chorus Question asks "what are you as a pattern?" — Portrait is the real-time answer
- The legacy campaign IS the cycle; the Chronicle IS the Chorus's record

---

## Session History

### Session 70 — 2026-06-07
- Startup fix: dynamic mtime comparison command added to feedback_agy_context_check.md
- C17 Intercept v1.1: beat=3 → beat=2; 04-n49 ✅; pending re-sign-off (04-n50)
- PM05 04-n50–04-n67: set-level card milestone tracking (Standard + 5 factions × design pass / issues resolved / sign-off pass)
- 04-n48 substantially complete: Signals Analysis (blocked — Art 06.x); C31 v1.1 (Immediate); C40 split (React stub + PA stub); C41 v1.1 split (Capital coercion + Accord Leverage stub); C42 block-bypass deferred

### Session 71 — 2026-06-08
- C31 v1.4: 2:1 cost; restriction=None; boost field added (`boost = True: capital*2`); doctrine_mod added; expanded format; Issues Resolved ✓. affinity=None (tag values invalid per §6).

### Session 72 — 2026-06-08
- 00a full structural review complete. 00a v0.5 draft written — material restructure. Rule count 46 → 30.
- New §3 (Design Principles for this Artifact) and §4 (Foundational Design Principles) added.
- Former §7 card design constraints flagged for Art 04 migration (XA-47).
- §8 and §9 dissolved — content moved to Foundational Design, Art 03, or redistributed.
- Rules reorganized into parent→corollary structure throughout. Appendix B migration map written.
- PM05: XA-46 (cross-ref sweep), XA-47 (Art 04 card design principles migration), XA-48 (Art 07 registers stub), 00a-73 (Art 03 R18 verify), 00a-74 (Art 02b alignment) added.
- 00a-72 draft complete; pending Andy grip review → sign-off.

### Session 73 — 2026-06-09
- PM05 additions: 00a-73, 00a-74, XA-46, XA-47, XA-48 added. PM02 D02a-03 updated.
- 00a §1 rewritten (three categories). 00a §3 reordered. 00a §3.1 created — canonical definitions migrated from PM04 (L192). Art 03 §4 pointer added. PM04 §1 collapsed.
- L150 amended (Month 3 provisional flag retired).
- §4 Foundational Design Pillars: 8 numbered pillars (4.1–4.8) with lettered corollaries. Art 00 §5 migrated → 00a 4.1–4.6; Art 00 §5 vacated with pointer.
- Rule numbering: 00-Rnn → section-prefixed n.n across §5–§10 (30→31 rules). §5–§10 headers include "Rules."
- §8 renamed "Footprint Rules." §3.1 Footprint definition row added.
- §8 precision edits: 8.2 Mechanics (Absent sentence removed), 8.3 Rule simplified, 8.3a precision fix.
- §9: upkeep income clarification; 9.1b added (card/action resources ≠ income).
- §10: 10.1 Lock B (Reveal effect = stake); 10.1a cross-ref 4.7a/4.7b; 10.3 limits + expiry.
- PM05: 00a-13 (7.3b revision), 00a-14 (Source/Governs audit) added.
- 00a v0.6 signed off — L193.
- C40A (Reputational Strike) stub moved from Network section to §11.8 (Named Modifier Cards).
- C41A Corporate Blackmail v2.0: forced transfer → ElectPlayer covert choice; target_district added; restriction = target presence > 0; ARBITER whispers to target at Beat 3; comply (pay resources TBD) or resist (presence tier −1 + PS −1); Syndicate PS −1 always. Art 03 covert ElectPlayer procedure outstanding (04-n72).
- C41B Accord Leverage v1.0: redesigned as ModifierCard/Instant; Accord draft restriction; forces acceptance of terms as written; Art 06 §9 Lock manipulation type; outstanding issues (party requirement, procedure, Lock interaction).
- C42 Sanctioned Raid v2.0: block-bypass removed; success = clear all modifier cards at district + remove n presence tokens; threshold = 75−10n (variable); per-token cost TBD; Beat 0 declared count mechanism flagged (04-n71).
- Art 04 §5: "Data schema validation" added as 14th checklist row (04-n68 ✅). Status table updated: "all 14 rows assessed."
- Art 04 §6.1/§6.2/§6.3: `boost: BoostExpr | None` first-class schema field added to Logic block. BoostExpr = condition: CostExpr; no Phase B declaration; submitted resources imply n.
- PM05: 04-n68 ✅; 04-n69/70/71/72 added; 04-34/36 superseded by §6 boost field; 04-n48 status updated; 00a-xx → 00a-72 UNBLOCKED (Art 03 v3.3 cleared gate S68 — missed until S71 review). Full PM05 prioritization review conducted.
- Art 04 v0.9.33.

### Session 74 — 2026-06-09
- Art 00 v1.6 signed off (L194): §5 Art 00 design principles added (5 principles — Derivability, Sustained Ambiguity, World over Mechanics, Attributable Perspective, Narrative Frame); §11 term table → 00a §3.1 pointer; all subsections numbered §1.1–§14.9.
- 00a v0.7 signed off (L196): §3 renamed "Design Principles for This Document" + scope routing note; §4 scope line added; §4.6 amended — Art 00 as origin of all canonical narrative (L195/L196).
- L195 locked: Art 00 sole narrative origin — no canonical narrative may originate in a downstream artifact; Art 00 amended first, downstream artifacts reference it. Written to 00a §4.6. Governs all V1 artifacts.
- Art 01 v2.0 signed off (L197): §6 Component Physical Forms column → "Proposed Form". PM05: 01-10 (table → Art 02a + Design Requirements column), 01-11 (scope overhaul — §8→03-init, §11/§12→downstream).
- PM05: 00-15 added (Art 00 full narrative revision per §5 P1+P5 — wiki/encyclopedia register, first narrative mention of all elements, downstream narrative migration); 00a-75 ✅ closed (L196).

### Session 75 — 2026-06-09
- XA-47 ✅ — Art 04 §5 P19–P25 added (card design constraints migrated from 00a §7: effect duration types, partial payment, crit cost, portrait card property, ring modifier scope, corrupt scope, standard language). P5 updated (authoritative R26 constraint). P6 cross-ref P19. Checklist rows updated. Art 04 v0.9.34.
- XA-48 ✅ — Art 07 §9 ARBITER Registers already had four-register content. `00a R02` source ref cleaned.
- XA-46 ✅ — ~120 rule ID substitutions across 11 files (Art 03, Art 04, Art 07, 02a, 02b, PM03, design_reference.md, gap_card_sketches, 3 memory files). Zero `00-R` strings remain. `00-R29` → `Design Pillar [04-n6 pending]` throughout.
- PM05: 04-n73 (P1–P18 restatement audit) + XA-49 (design_reference.md reset) added.

### Session 76 — 2026-06-09
- XA-49 ✅ — design_reference.md rebuilt as master index + sub-reference system. Old monolithic file replaced with: `design_reference.md` (master, ~1K words), `design_reference_card_system.md` (card schema/rules/flags, ~2.5K words), and 9 `ref_*.md` sub-refs (world/narrative, design pillars, components, board narrative, resources, tracking, procedures, card types, taxonomy). All populated from 9 parallel agent reads. Session-open read = master + card system (~3.5K tokens); sub-refs loaded on demand.

### Session 77 — 2026-06-09
- 04-n28 ✅ — Overture full spec written to Art 04 §11.8 (Modifier/Instant/All; outcome addition mechanic; ARBITER delivers blank AccordForm at Beat 4 on any host PA outcome; faction drafts and places in Accord Placement Area at discretion; no timing constraint; cross-Quarter; target faction named on form, not at Phase B). §11.7 Outcome addition row expanded with operational mechanics.
- Art 06 §9.4 materially revised and re-signed off (L198): blank AccordForm delivery model replaces drafted-form-at-Beat-4; faction drafts at discretion; form placed in Accord Placement Area anytime after drafting (queued for next Debrief); cross-Quarter persistence (no End-of-Quarter removal); physical alterations and execution Debrief-only; verbal discussion anytime; forms removed only on withdrawal, verbal decline + no further negotiation by end of Debrief, or execution. Art 06 v0.3.
- P08 Table an Accord, P10 Infrastructure Bond, C09 Fund, Overture: all updated to blank AccordForm delivery model. AccordOffer marker concept removed throughout. `persistence = Seasonal` corrected to `Immediate` on P08 and P10. `success` fields updated. Design Rationale, checklist rows, arbiter_notes rewritten. Outstanding Issues added to P08 and P10.
- PM05 04-n74 added: Accord initiation cost/value review — C09 (2 Capital + threshold 50), P08 (2 native, Automatic), P10 (2 Capacity + 2 native, Automatic). AccordForm cross-Quarter persistence changes the value proposition.
**Decisions locked:** L198 (Art 06 §9 re-signed off v0.3 — blank AccordForm delivery model; cross-Quarter persistence).
**Next:** S78 — 04-n40 (C28 Network replacement).

### Session 78 — 2026-06-10
- C28 v2.0 "Breaking News" written (Network L1 FactionSpecific CovertOp; Beat 2 d100 threshold 50; Exposure×2; forces ARBITER to publicly reveal target faction's first Beat 3 queue entry; places VM-xx Visibility Marker on that grid card as physical reminder; no cross-beat state tracking).
- VM-xx new ARBITER-held token — placed at Beat 2 resolution on matching Beat 3 grid card; flags public announcement before that op resolves. No board marker. PM05 04-n75 (Beat 2 d100 procedure) and 04-n76 (VM-xx registration + Beat 3 public resolution clause) added as sign-off gates.
- C40B v1.0 "Live Coverage" written (Network PA FactionSpecific; Beat 4 d100 threshold 50; Exposure×2; Seasonal). Target faction elects each Phase A: comply (lay all held cards face-up on table; covert ops proceed) or resist (dispatch case disabled that Month). Comply once → card clears. Natural expiry: Quarter end. PM05 04-n77 (Art 03 Phase A comply/resist procedure) added as sign-off gate.
- Art 04 §5 P26 locked (L199) — Card Narrative Test: every card must be expressible as a 1–2 sentence narrative story answering "What is actually happening in the world when this card is played?" If no coherent narrative can be constructed, the card is a design problem.
- Card Story block added to Art 04 §5 as structural element in card specs (between Design Rationale and Design Checklist; 1–3 sentences of plain-language event narrative). 15th checklist row added (card narrative). C28 and C40B both include Card Story blocks.
- PM05 additions: 04-n40 updated (design complete S78 — sign-off gates open); 04-n75–04-n80 added (Beat 2 d100 procedure; VM-xx registration; Phase A comply/resist procedure; Card Story structural sweep; content pass; Andy review).
- Memory files updated: feedback_narrative_first_design.md, feedback_card_spec_conventions.md, feedback_card_design_review_workflow.md. design_reference_card_system.md updated (P26 governing rule; design flag #12; S78 timestamp).
**Decisions locked:** L199 (Art 04 §5 P26 — Card Narrative Test; Card Story block added to spec structure).
**Next:** S82 — Art 06 §9 / Art 03 / 00b re-sign-offs (grip) → C28 Issues Resolved + sign-off → C40B sign-off (04-n77).

### Session 79 — 2026-06-10
- C42 v2.2 — boost model finalized: base cost = faction×1 + native×1 + IntelToken; boost = same unit; threshold = 65−10×n_boost; PS scales with (1+n); successcrit = PS+(1+n_boost); fail = NotificationSlip; failcrit = Discovery + PS−(1+n_boost); modifier scope = target faction only.
- Whiteboard boost_marker_draft_S79.md created (BM-xx draft language + Art 03 procedure sketches).
- PM05 additions: 04-n81 (BM-xx registration), 04-n82 (Beat 0 boost procedure), 04-n83 (Beat 2/3 BM-xx resolution), 04-n84 (Discovery mechanic definition), 06-n01 (Accord term vocab + PS mechanic — gating 04-n74).

**Next:** S80 — 06-n01 (Accord term vocabulary + PS mechanic redesign).

### Session 80 — 2026-06-10
- 06-n01 ✅ — Art 06 §9.3 clause vocabulary written (5 types: Prohibition-Territorial, Prohibition-Operational Marker, Prohibition-PA, Obligation-Resource Transfer, Obligation-Presence; covert ops excluded). §9.4 PS formation mechanic redesigned (execution = all parties +1 PS; decline = non-party table vote on reasonableness). Art 06 §9 pending re-sign-off (grip required).
- PM05 additions: 04-n85 (covert add-for-opponent concept, superseded by 04-n86), 04-n86 (C01/C03 generalization — build for any faction via submitted resource color). 04-n74 unblocked.

**Next:** S81 — 04-n74 (Accord initiation cost calibration).

### Session 81 — 2026-06-10
- SESSION_BRIEF corrected (S78→S81; S79/S80 accomplishments reconstructed from artifacts).
- 04-n74 ✅ (L200, L201): P08 cost → 1 native flat, all factions (affinity removed); P10 cost → 1 Capacity + 2 native delivered to target; C09 unchanged at 2 Capital (two-action Accord route documented).
- 04-n75 ✅: Art 03 Beat 2 d100 resolution block added (after Automatic cards; queue order; 8-step procedure; additive crits).
- 04-n76 ✅: VM-xx registered in 00b §4 (23 entity types); Art 03 Beat 3 Step 1 item 4 added (VM-xx → public resolution).
- Art 03 and 00b re-sign-offs pending (grip). Art 06 §9 re-sign-off pending (grip).
- New memories: feedback_mid_session_clear.md, feedback_read_ref_files.md.

**Next:** S82 — Art 06 §9 / Art 03 / 00b re-sign-offs (grip) → C28 Issues Resolved + sign-off → C40B sign-off (04-n77).

### Session 82 — 2026-06-10
- 04-n81 ✅: BM-xx (BoostMarker) registered in 00b §4 (24 entity types now); ARBITER-held transient token for Beat 0 detection through beat cleanup.
- 04-n82 ✅: Art 03 Beat 0 boost detection procedure added (floor division; no refunds); BM-xx placement on grid slot when boost field active.
- 04-n83 ✅: Art 03 Beat 2/3 BoostMarker resolution + cleanup (success effects multiply 1+n; fail/failcrit fire once; cleanup at beat end).
- 04-n84 ✅: Discovery mechanic defined as universal Art 03 procedure — ARBITER announces faction + op + target publicly; faction identity remains public for Quarter duration.
- 04-n77 ✅: Art 03 Phase A Live Coverage comply/resist procedure added (hand-visibility toggle; permanent until voluntarily complied or forced removal).
- PM03 updated: 00b v0.2 → S82 status, Art 03 v3.4 status. PM05 updated: 04-n81/82/83/84/77 all marked ✅ S82.
- Save State: S83 row appended below.

**Next:** S83 — 04-n47 (Art 04 §5 single determinate success); grip bundle (Art 03 v3.4 + 00b + Art 06 §9); C28 Issues Resolved + sign-off; C40B sign-off.

### Session 83 — 2026-06-11
- Art 03 v4.0 structural overhaul complete — structural sign-off S83 (full sign-off pending fine-tuning/mechanics review).
- §§12–16 deleted (covered by §9 unified monthly Beat procedure).
- Beat 2/3 Step 0 restructured to "Identify Operation" (0.0 Apex, 0.1 VM-xx, 0.2 Base Difficulty); VM-xx conditional privacy model throughout Steps 1–2 (covert ops fully private by default).
- Beat 4 (§9.4.4) full procedure written — Faction Player actor; Steps 0–5; sub-steps 0.0 Submit Payment/Validate (Intel Token freshness), 0.1 Apex, 0.2 VM-xx N/A, 0.3 Board State, 0.4 Base Difficulty.
- §9.4.5 Close Month: Step 0 transient cleanup; Step 1 month advance (Month 3 → §10, else → §9.0 repeat).
- §10 Resolve District Tension (was §17): PS mechanic — opposing faction moves PS marker; losing faction moves winning faction's PS −1 on resolution; winning faction moves losing faction's PS −1 on press; tie: each faction moves other's PS −1.
- §11 Quarterly Debrief (was §19): §11.3.0.1 Annual Report (Q4 only).
- §12 Quarter Close (separated from §11): §12.1 Findings Decay honor system (L2 enforcement flag); §12.3 NS-xx faction hand → ARBITER pool; §12.4 M1/Q+1 tracker advance.
- Reference sections renumbered §21–28 → §13–19 (§25 merged into §18.1 Modifier React; §18 React Card Rules before §19 Examples & Exceptions).
- ToC and §6 Quarter Overview updated (Beat 0–5 sub-entries + anchor links added to both).
- Whiteboard/art03_section_map_S83.md created (complete old→new section map for external artifact sweep).
- PM05: 03-n02 (Beat 2 modifier stack scope clarification), 03-n03 (OR card component sweep for §9.4.2.3 and §9.4.3.3) added.
- PM03: Art 03 v4.0 row updated. Art 06 §9 signed off S83 (L205).

**Next:** S84 — Art 03 fine-tuning/mechanics review → full sign-off; external artifact sweep (Whiteboard/art03_section_map_S83.md: 00a, 02b, 03a, 04, PM01, PM05).

### Session 84 — 2026-06-11
- Art 03 rubric pass begun — entry/exit conditions added to all 17 §6 sections listed in §6 Quarter Overview.
- §7 entry condition: Q1 = 03-init complete; Q2–Q8 = §12.4 Quarter Close complete. Entry/exit notes as italic lines, not numbered steps.
- §9.4 container section entry/exit removed — nothing to enter/exit in the section summary.
- §7.2.x terminology sweep: Event Card → Broadcast Effect Card; Event Zone → Situation Report Zone; session deck → Broadcast Deck (throughout §7.2.0–§7.2.6).

**Next:** S85 — §9.4.0 and §9.4.1 rubric pass; CM model; Broadcast Effect Card naming; component registration.

### Session 85 — 2026-06-12
- §9.4.0 steps 0–6 restructured: Beat 1 row CM placement before case is opened; packet removal; payment validation; resource drain; grid placement; dispatch token (no token → flip face-down + discard modifier cards); repeat.
- CM model resolved: submitted CMs placed in Beat 1 row of their lane at Beat 0; at Beat 1 each CM applies to ALL ops in grid targeting the CM's keyed faction — not lane-limited.
- §9.4.1 fully restructured — 3 sub-steps: §9.4.1.0 Standing Board Effects (clockwise from ARBITER's left, one by one); §9.4.1.1 Broadcast Effect Cards (applied silently, without announcement); §9.4.1.2 CM Cards (Beat 1 row, lane-by-lane, left to right).
- Situation Report two-card model confirmed: Broadcast Card (public, Situation Report Zone on Overview) + Broadcast Effect Card (hidden effects, ARBITER Tableau). Multiple Situation Reports active simultaneously.
- Component naming adopted: Broadcast Card, Broadcast Deck, Broadcast Effect Card, Broadcast Effect Deck. DB updated: component ids 25/86/87 renamed; id=98 (Broadcast Effect Card) inserted.
- "target slip" → "Target Profile" throughout Art 03 (9 instances, replace_all).
- 03-init §2.8: Broadcast Deck + Broadcast Effect Deck rows added; §3.9 deck list updated. 03-init v0.1 → v0.3.
- Art 03 v4.1 → v4.2 at close.
- PM05: 03-n10 ✅ (Situation Report component traceability), DB-18 ✅ (Broadcast components registered), 03-n07 updated (remaining: §9.4.4 publicly played CM), DB-17 updated (remaining: other artifacts), 00a-n01 added (standing card → 00a terminology table).

**Next:** S86 — Art 03 rubric pass §9.4.2 Beat 2 through §9.4.5; §§10–12; external artifact sweep; grip review → full sign-off.

### Session 87 — 2026-06-13
- §5 Principle 7 added: Step 0 convention (all procedural sequences begin at Step 0; uniform across sections, beats, subroutines).
- §9.4.2.6.1.0 added: Target Profile Return (covert — extract from Dispatch Packets; erase/return if reusable; discard if single-use; flagged PM05 03-n16).
- §9.4.2.6.1.1 added: Process Case Contents (used op cards → CA discard deck; Intel Tokens/resources → faction supply; everything else → designated location; PM05 03-n17 to enumerate after Art 06).
- §9.4.3.4 item 5 added: Target Profile cleanup at Beat 4 (public — same erase/discard logic; PM05 03-n16).
- §§11–12 restructured and rubric-compliant: §11.0 Open Debrief / §11.1 Debrief Actions / §11.2 Chorus Question Window / §11.3 Ready to Close (flagged sub-6-player) / §11.4 ARBITER Debrief (§11.4.0 Summary / §11.4.0.1 Annual Report / §11.4.1 Observation); §12.0–§12.4 Quarter Close.
- §13 The Operation System: §13.1–§13.6. Modifier table rebuilt: M-06/M-07 merged (same effect, all beats); M-09 generalized ("protect-type operation card"); M-10 terminology updated; M-11 scope expanded to All/Beat 2/Beat 4. §13.6 Intel Token Age table (0–2 Fresh / 3 Stale −25 / 4+ Expired = partial payment).
- §14 renamed "Apex Activation." Flat structure Steps 0–4 (no §14.1 nesting). Entry condition added. Beat names removed. §9.4.2.0.0 and §9.4.3.1.1 call-site refs updated (§14.1 → §14).
- §§15–17 rubric clean (Duration Taxonomy / Public Act Placement / Countermeasure Card Rules). §16 flag added (items 2–3 depend on Art 08 Faction Resolution Grid design; PM05 03-n14).
- §18 React Card Rules restructured: §18.0 Fire Condition / §18.0.1 Timing Window / §18.1 Trigger Announcement / §18.1.0 Tiebreaker / §18.2 Resolution / §18.2.1 Persistent React Card Effects / §18.3 Resume.
- §19 Reserved.
- §20 Resource Generation Reference (new): Affinity Bonus / Structure Block Income / Passive Generation — all with table and §7.4 pointer.
- §21 Card Economy Reference (new): Hand Sizes table (covert 6, public 3 proposed) / Modifier Card Draw table / Dispatch Token Allotment (4 per Quarter, per 03-init).
- § Examples & Exceptions (unnumbered, at end): Initiative example updated (ref §7/Art 07 for initiative ordering). Dispatch Case Return rewritten (removed face-up/face-down; NS-xx readout model; flagged PM05 03-n15 for Art 06 gate). Findings Decay unchanged. Explicit HTML anchor added for index link.
- PM05 additions: 03-n14 (§16 items 2–3 gate Art 08), 03-n15 (Dispatch Case Return example gate Art 06), 03-n16 (Target Profile cleanup split, gate physical design), 03-n17 (case contents enumeration gate Art 06), 03-n18 (component lifecycle sweep — Art 03 sign-off gate). XA-50/51/52 remain active.
- Art 03 v4.2 → v4.3. Grip review complete. Full sign-off pending PM05 03-n18.

**Next:** S88 — (1) PM05 03-n18 component lifecycle subagent sweep → Art 03 sign-off; (2) C28 Breaking News, C40B Live Coverage card work; (3) Whiteboard/art03_section_map_S83.md external artifact sweep.

### Session 88 — 2026-06-13
- Art 03 v4.4 signed off (L207). PM05 03-n18 component lifecycle sweep ✅. All sign-off blockers resolved in-place.
- §13.7 Board State Update Rules added: Tension marker placement/removal trigger (Contested condition); Dominant/Established marker return-to-supply rule; Structure block removal trigger on Absent.
- Target Profile added to 03-init §2.7 (count TBD; physical design pending PM05 03-n16).
- Control flag renamed Dominant marker throughout Art 03 and 03-init (S88 design decision: same component — rename only).
- Return-to-supply language added §7.3.3 and §8.2. BM-xx "from ARBITER supply" clarified §9.4.0.1. §12.0 BEC cleanup scope clarified.
- 03b Component Lifecycle Register v0.1 — formalized from Whiteboard scratch. Lifecycle tables for all ~20 components. Open: 03-n06/11/12/16, XA-07, DB-14/15.
- art03_section_map_S83.md — 5 stale entries corrected; 3 new S87 sections added (§20, §21, §13.7).
- Art 02 Components v1.0 written — merge of 02a v1.6 + 02b v1.5. §5 Design Principles: 2 principles (Scarcity is intentional; Disclosure is designed, not assumed). XA-45 ✅. 02a + 02b superseded. PM05 02-n02 added (deeper review before sign-off).
- PM03 v2.5: Art 02 row added; 02a/02b marked superseded.
- agy S88 DB report integrated: DB-14 renames (Control flag → Dominant marker, Presence token → Presence chip) ✅; DB-15 (Operative ability → Operative card + Sealed Apex ability) ✅; DB-34 (DebriefActionCard + SCIFRecord registered) ✅.
- ref_resources.md + ref_tracking.md headers updated to Art 02 section refs.

**Next:** S89 — (1) Art 02 deeper review pass (02-n02); (2) C28 Breaking News, C40B Live Coverage card work; (3) art03_section_map_S83.md external artifact sweep (00a, Art 02, 03a, 04, PM01, PM05).

### Session 89 — 2026-06-13
- External artifact sweep complete (all 6 artifacts: 00a, 03a, 04, PM01, PM05 + Art 02 cross-refs). art03_section_map_S83.md deleted from Whiteboard.
- All Art 02a/02b/02x refs updated to Art 02 throughout all artifacts.
- All stale Art 03 section numbers updated: §11→§9.4.x (Beat-specific), §17→§10, §18 (Battlefield Strength)→§10, §19→§11 (Debrief), §22→§14, §14 (Modifier table)→§13, §25/§28→§18 (React Card Rules), §3.11→§9.4.x.
- C01/C03 Design Checklist "Supported by game procedure": stale `Automatic resolution (§20)` ref removed from text and source column.
- PM05 04-n95 added: controlled vocabulary for "Supported by game procedure" checklist field (enumerated legal Art 03 procedure refs required; sweep of all signed-off cards to follow once enumeration defined).

**Next:** S90 — (1) C28 Breaking News, C40B Live Coverage card work; (2) Art 02 deeper review pass (02-n02).

**Session 35 summary (2026-05-25 — complete):**
- **L144 locked:** Card schema design — 1NF + snowflake. All fields atomic; compound-value fields refactored to child tables. Governs Art 04 and 00b.
- **C15 signed off.** Affinity bonus field added (04-35 partial). Success field normalized to "+1 target district native resource." pool_copies flagged for removal (04-40).
- **C16 signed off.** Full §6 schema uplift. Prediction resolution — no roll. Success condition: match on faction OR district. C16 Portrait: Submitter +1 / Condition: Success / Modifier: +1.
- **C16–C20 schema uplift complete.** §6 schema, section headers, ring modifier fields (4 per card — per-token rates: Ring 0=−15, Ring 1=−10, Ring 2=0, Ring 3=+10). C17 Boost([1].[+1 reveal on success]) added. C17 sign-off pending (04-41 deniability flag).
- **Art 03 v1.8 re-signed off.** Beat 3 targeting rule: card only valid while in Resolution Grid.
- **DB design documented.** the_signal_db design intent saved to memory. 1NF + snowflake confirmed. card_effects table gap identified (04-39). Ring modifier two-track architecture: structure→card draw + presence tokens→calculated modifier.
- **New PM05:** 04-39 (updated), 04-40 (pool_copies removal), 04-41 (surveillance deniability + Intel token economy), 04-42 (ring modifier narrative pass), XA-32 (Art 03 Beat 3/4 + Art 07 ARBITER ring modifier guide).
- **Grip:** relaunched at project root (/TheSignal). V1/README.md deprecated and deleted.

**Session 36 summary (2026-05-25 — complete):**
- **Three-agent workflow formalized.** Claude (primary), agy (Gemini CLI / Antigravity CLI), Gem (Gemini web). rclone removed entirely (binary + OAuth config deleted). Replaced with `generate_gem_context.sh` — two-file output to Desktop: `gem_message.txt` (message to Gem) + `gem_context.txt` (~1.1MB project dump). agy notified of name change via GEMINI_CONTEXT.md.
- **`gem_web_context.md` created** as Gem's persistent session memory. Sections: Session Message, Standing Instructions, Calibration Notes, Access Scope. Two hallucination incidents logged in Calibration Notes (fabricated citations S36).
- **8 new PM05 items from agy card verification + DB gap analysis.** Card items: 04-43 (C13 resolution type mismatch), 04-44 (difficulty hardcoding vs dynamic scaling), 04-45 (C14 difficulty format), 04-46 (C10 "assets" undefined). DB items: DB-04 (resource_types table + factions column gaps), DB-05 (native resource migration, blocked DB-04), DB-07 (quarters lookup table design decision), DB-08 (card_metadata missing fields, blocked 04-39).
- **README fixed.** Artifact 00 corrected from v1.3 → v1.4 (Gem audit finding, already confirmed).
- **CLAUDE.md updated.** Agent Roster section added; rclone section removed; close routine Phase 2 updated (GEM_CONTEXT replaces SYNC).
- **Next session:** C17 sign-off (04-41 surveillance deniability must resolve first), C20 review, C21–C25 Directorate cards.

**Session 37 summary (2026-05-26 — complete):**
- **Double Case Pass implemented (L145).** Art 03 restructured from linear 7-phase to Month 1 / Month 2 / Month 3 within the Quarter. Month 1 and Month 2 = covert operational months (Dispatch + Countermeasures + Resolution each). Month 3 = political month (Declaration + Countermeasures + Resolution).
- **Dispatch Tokens locked (L146).** 3 per standard faction, 4 for Ghost. 1 token per submitted covert card. Collected per Month; redistributed at Upkeep Step 7. Ghost Political Act requires retaining ≥1 token (L147); passing requires no token.
- **Intel as universal currency (L148).** All factions can generate and spend Intel tokens. Closes PM05 04-41 (C17 surveillance deniability blocker — Ghost's failure slip no longer uniquely identifies Ghost). C17 sign-off now unblocked.
- **Intel Token Decay at Upkeep (L149).** New Step 6 in Phase 1: hold 1–2 tokens → lose 1; hold 3+ → lose 2.
- **"Month" as provisional canon (L150).** Three Quarter phases named Month 1, Month 2, Month 3. Week/Beat nomenclature: Month1.Week2.Beat1 format. Beat retained for design reference.
- **Art 03 v1.9 changes.** §2 Index updated (22 sections). §6 Quarter Overview code block updated (Month 1/2/3 + Debrief). §7 Upkeep: new Steps 6–7. §9–§17: Month 1/2/3 sections. §15: Ghost Political Act restriction. §17: political act restriction check added (before Submit Payment, Beat 4). §18: "Phase 7" prefix removed. Three blocking fixes applied (dispatch token language, orphaned Phase 7 label, political act restriction check placement). Re-sign-off pending (04-48).
- **PM04 updated.** "Month" entry added to §1 Temporal Conventions table (provisional, evaluate after use).
- **Intel economy cards drafted (C36–C42).** SYNTHESIZE (Ghost), SACRIFICE (Network — confirmed: direct PS track step, not resource or Portrait), PARASITIC (Syndicate), ABSOLUTE COMPROMISE (Common), WEAPONIZED TRANSPARENCY (Network), CORPORATE BLACKMAIL (Syndicate), SANCTIONED RAID (Directorate). Full schema pass queued (04-47).
- **gem_web_context.md restructured.** Gem Profile protocol (Bucket A/B) integrated. Standing Instructions updated with session number calibration. Project Reference section seeded from Claude's working knowledge.
- **Next session:** Art 03 v1.9 full review and re-sign-off (04-48, first item), then C17 sign-off (unblocked), then C20 review.

**Session 34 summary (2026-05-24 — complete):**
- **Art 00 v1.4 re-sign-off complete.** First pass clean. "Deliberation cycles" confirmed as in-world term for Quarters (L143). Ring name propagation: "The Mid" / "Baryo" applied across 00a, 00b, 00c, 03a (non-material). 00-07 multicultural texture pass now unblocked.
- **iOS batch processed.** 12 vignettes (M365 Copilot, 2026-05-22) archived. Canon candidates approved: Elias Rook and Marek Ionescu. Mara Ionescu → Mara Seo (surname collision resolved). CANON_CANDIDATES.md updated. CREATIVE_BRIEF.md canonical home confirmed as Creative/ (duplicate removed from ClaudeIOS/).
- **Non-material queue partial clear.** XA-32 (Fringe ring → Ring 3 (Baryo) in 00a), 02a-04 (§10 cross-ref added), 02a-07 (Asset token removed from PM04 §1), PM04-03 (Category column pattern), PM04-04 (L109 standard + Component Physical Glossary). PM04 v0.6 → v0.7.
- **New PM05 item: 00b-04.** RG entity ID numbering (outside-in) vs. L141 inside-out canonical Ring numbers — design decision required before 00b signs off. Gemini-flagged risk.
- **Remaining non-material:** XA-29 (L109 component scan across 00–04b), XA-23 (Index→Contents rename), 04-35 (Affinity bonus N/A on C15–C35), 00b-04 (RG numbering decision — careful execution required).

**Session 33 summary (2026-05-24 — complete):**
- **Art 00 v1.3 → v1.4 (pending re-sign-off).** Ring renames: "the Infrastructure"→"the Mid", "Sprawl"→"Baryo" at all 6 occurrences. New content blocks: 00-06 (quarter worldbuilding — deliberation cycle timescale, eight-cycle window, faction perspectives on the timeline); XA-15 (ARBITER as sixth party at The Table — seat, Chorus Node, Resolution resource, ARBITER has not said what it measures and may not know); 00-03 (The Layers — physical, social, informational, digital, ARBITER's layer; "It is.").
- **CREATIVE_BRIEF V2 promoted to production.** ClaudeIOS/new/ V2 applied 8 ring name corrections and updated to 2026-05-24 before promotion. Frozen until Art 00 re-sign-off.
- **PM05 v2.2 → v2.3.** 00-07 added: multicultural texture enrichment pass (governing principle: cultural references as sediment, not subject — the Baryo model; first application: eight-cycle "The reasons are not in the minutes"). Scope: §6 ring/Node descriptions, §8 deliberation calendar, faction relationships to time and obligation.
- **PRIVATE___Design_Questions.md created** at `Session/PRIVATE___Design_Questions.md`. Companion to TrueState — Known / Unknowable by Design / Open Questions for §1–§8. Living document.
- **Ionescu surname collision flagged.** Two background characters with surname Ionescu in creative material. Direction: rename one — background cast needs more diversity. Canon candidate review carries this forward as first action next session.
- **No new L-decisions this session.** Ring numbering (L141) and ring names (L142) were session 32 decisions.

**Session 32 summary (2026-05-22 — complete):**
- **Art 04 v0.9.18 → v0.9.19.** C11 re-sign-off complete. C12 re-sign-off complete. C13 redesign (Automatic→d100@25; crit success adds structure; crit fail: intel token to Directorate). C14 full redesign: presence+structure anywhere, d100@50, Boost mechanic introduced, crit fail→Ghost+Syndicate.
- **New PM05 items:** 04-34 (Boost mechanic formal spec), 04-32 (intel-tokens-as-currency interaction), 09-12 (faction-keyed card printing vision). C15 re-sign-off remains open (04-23).
- **L141 locked:** Ring numbering — Ring 0=Chorus Node, Ring 1=Core, Ring 2=The Mid, Ring 3=Baryo. Address system [ring].[position].
- **L142 locked:** Ring names — Ring 2="The Mid", Ring 3="Baryo". Baryo=mutation of "barrio" through 11 languages. Governing principle: cultural reference as sediment, not subject.

---

**Session 11 summary (completed items — see PM05 for full status):**
- XA-05: Four-register system applied to Artifact 07 §9, Artifact 00 §9, 00a R02 — **Artifacts 00 and 07 require re-sign-off (material)**
- 00-05: Narrative anchors migrated to Artifact 00 §14; 00a §5/§7 replaced with cross-references — **Artifact 00 requires re-sign-off**
- 00-02: Design Pillar 6 "Narrative and World Consistency" added to Artifact 00 §5 — **Artifact 00 requires re-sign-off**
- 00a-02: Chorus Portrait retirement applied to 04b §4/§6.1 — **04b requires re-sign-off**
- PM04-01/02: PM04 §1 fully populated (17 component terms, 5 faction resources, 4 influence levels, temporal conventions). PM04 now canonical in-world glossary.
- XA-16 partial: round→quarter, mat→The Overview applied across 02a/02b/07/08/09/10
- PM02-02: §2b archived snapshot collapsed

**Session 12 summary:**
- ~/CLAUDE.md updated to redirect any home-directory Claude Code session to ~/Projects/CLAUDE.md
- **Creative Brief work** (`~/Projects/TheSignal/Creative/CREATIVE_BRIEF.md`): Major revision pass —
  - Submission header moved to top of file, mandatory fill-in format
  - Faction-color-as-object constraint added to "What This World Is Not"
  - "Images Already In Use" section added (plumbing/pipe imagery, tilting floor line)
  - "The Chorus Papers" established as proper noun throughout (replaced all instances of "the leak")
  - Line 65 (brief): story of The Chorus Papers added
  - Cascade effects paragraph added near row 307 ("Before and after" section)
- **CANON_CANDIDATES.md created** (`~/Projects/TheSignal/Creative/CANON_CANDIDATES.md`): Running file of selected content from Gemini passes 1–4. 13 items selected (5 canon candidates, 8 flavor copy candidates).
- **Gemini V3 and V4 evaluated**: V3 ("The Shack" — Dr. Alistair Vance, original station crew) is strongest character introduced. V4 ("The Fourth Register" — ARBITER at The Table) has best ARBITER writing. Both are canon candidates with minor edits required.
- **Artifact 00**: Three reception language fixes (lines 138, 144, 184 — "received" not "transmitted"). `### The Chorus Papers` section added to §6 with cascade effects (four paragraphs: The Table's formation, mathematics attribution, vindication-without-understanding, Directorate fracture).
- **PM04 §2**: Reception Language Convention added — canonical framing rule for how the Chorus is described.
- **PM05**: XA-19 added (reception language scan, remaining artifacts); D-FT-01 added (faction hidden truths design question).
- **Key design insight — D-FT-01**: The Network is the only faction that genuinely did not know about the Chorus until The Chorus Papers. The other four factions had prior involvement — their doctrines may be rationalizations of prior knowledge rather than independent positions. Each faction likely holds a hidden truth that shaped why they are at The Table. This is a major design territory. See PM05 DEFERRED D-FT-01.

**Sessions 8–10 summary:**
- D02a-01 resolved (L93) — Chorus Node Translation rate scale locked: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1. 02a §8 updated.
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content
- L96: Italic for explanatory/commentary text in procedural sections; separated from action text by CR
- L88 extended (session 10): full four-term convention — ARBITER, The ARBITER Player, Faction, Faction Player. Design principle: Player function = automation stand-in; Role = intelligence layer.
- Artifact 03 — all copy design conventions applied (L88, L96, XA-17): all phases updated. Under review with Andy, currently at Phase 2. NOT YET SIGNED OFF.
- "Effect Card" renamed from "Event Card" (session 9, locked). Propagation to 01/02a/02b pending (punch list 03-07).
- "Reservoir" confirmed as canonical capitalized in-world term for resource bank. Applied throughout Artifact 03.

**Session 13 summary (2026-05-16):**
- **03-06 resolved (L97):** Difficulty is a card property — influence-level table removed from Artifact 03 §12. Beat 3 Step 3 and Beat 4 Step 2 updated. 2d10 System table restructured.
- **L98 locked:** "Threshold" is the canonical noun for the roll target. "Base Difficulty Threshold" is the canonical table header. Convention documented in PM04 §2.
- **L99 locked:** Verb-first convention for procedural action headers. First applied in Artifact 03 §9.
- **D03-R01 signed off:** Beat 2 "The Ground Shifts" confirmed.
- **D03-R02 signed off:** Step 6 card draw confirmed. ARBITER announcement revised: "Assemble hands" → "Prepare operations." Step renamed "Operations Preparation."
- **D03-R03:** Pending — Phase 4 Declaration Accord card text not yet reviewed.
- **Phase 2 entry requirements:** Bullet list → Ring/Entry Requirement/Threshold Modifier table. Infrastructure penalty reframed as −25 threshold modifier (consistent with L97). Added to Beat 3 modifiers table.
- **Phase 3 Dispatch:** Major structural rewrite — Open/Close Dispatch wrappers; verb-first steps; case contents removed to Artifact 06 (06-01 flagged in PM05 DEFERRED); "Who runs it" label removed from all phases; two-bullet role format established as convention.
- **New feedback convention:** Draft prose/structural changes in chat for Andy's review before writing to file. Mechanical fixes write directly.
- **06-01 added to PM05:** Dispatch case contents list to migrate to Artifact 06 during active development pass.

**Session 14 summary (overnight autonomous — 2026-05-17):**
- **XA-19 complete:** Reception language corrected in 7 files (02b, 03, PM04, 00, PM02, CREATIVE_BRIEF ×2). Faction-framed "transmitting" instances intentionally retained per PM04 §2. Scope: Narrator voice only.
- **02a-03 complete:** All four changes applied — §6 Component Names (Control flag updated, ARBITER Dominance Marker row added), §6 DOMINANT bullet (structural impossibility language), §9 Component Description (Control flag quantity corrected, ARBITER Dominance Marker row added), §10 Chorus Node (constitutive presence language). PM01 §2.08 Control flag quantity corrected. **Artifact 02a requires re-sign-off (material change, v1.2 → v1.3).**
- **Artifact 03 Phase 4–end scan complete:** L99 verb-first headers applied (Beat 3 Steps 9, Beat 4 Steps 7/8, Apex Steps 1–5). XA-19 fix applied line 66. Current Phase 4 Declaration text for D03-R03 confirmed in place. All remaining phases verified clean.
- **10-02 complete:** §7.6 Translation rate table updated — ARBITER Script column added; Contested rate script written in The Record register; None row updated to 4:1 (L93); design note added; TBD note removed.

**Session 15 summary (2026-05-17 — in progress, interrupted mid-Phase 6 review):**
- **D03-R03 resolved (L100):** Free Accord card from C09 Fund classified as Political Act card (cost 0, return to ARBITER on play). Delivered to faction's hand at case resolution. Played in a subsequent Quarter — card returns in dispatch case after Resolution, Declaration already closed. Phase 4 carries no exception. Full card design flagged as PM05 04-12.
- **Artifact 03 Phases 1–5 fully reviewed and updated:**
  - Phase 4: exception note removed; Ghost pass callout removed
  - Phase 5: fully restructured — Pass/Deploy initiative-order structure; Countermeasure cards added to Step 6 tableau check; card types/rules migrated to PM05 04-07 for card design pass; ARBITER announcement updated
  - XA-16 complete for Artifact 03: "round" → "Quarter" throughout (~30 replacements); Round Tracker preserved
  - XA-20 added to PM05: "the ARBITER Player" / "the Faction Player" capitalization scan — "the" lowercase mid-sentence, capitalize at sentence/bullet/post-colon starts only. Applied in Artifact 03.
  - L98 applied in Artifact 03: "roll threshold" → "target threshold"
  - Beat headers reformatted: "BEAT N — Name *(timing)*" → "Beat N: description"; timing estimates removed from artifact, preserved in PM05 §3
- **Phase 6 in progress:** Bullet overview added; Beat headers reformatted; "World Condition" consolidated to "Situation Report effect"; Beat 3 Step 9 clarified; Type B modifier table label fixed; "this Quarter" fixed. **Review paused at Phase 6 — not yet signed off.**
- **PM02:** L100 locked; D03-R03 marked resolved
- **PM05:** 03-03 closed; 04-07 expanded with Type A/B content; 04-12 added; 01-03 updated (Countermeasure setup note); XA-16 updated; XA-20 added; timing note added to §3
- **Artifact 04 C09:** Design note updated — Political Act card classification, subsequent-Quarter timing

**Session 17 summary (2026-05-17 — complete):**
- **iOS creative session workflow established:** Andy runs exploratory sessions on iPhone via claude.ai with a separate Claude Project (instructions at `~/Projects/TheSignal/ClaudeIOS/ProjectInstructions.md`). Sessions are non-binding. At session end, Claude generates a structured `.md` summary dropped into `~/Projects/TheSignal/ClaudeIOS/new/`. Claude Code picks up summaries at next session open and actions follow-ups. Documented in CLAUDE.md.
- **index.html committed to repo root** — project homepage built in mobile creative session. Future-punk aesthetic: dark background, faction colors as data series, ARBITER as white, animated Chorus sine wave header. GitHub Pages enabled at `https://andrew-bosch.github.io/TheSignal/`.
- **PM05 11-01/11-02 added** — index.html as informal Artifact 11 visual reference; Chorus wave as open design question for Artifact 11 §7.
- **gh CLI token stale** — `~/.config/gh/hosts.yml` token invalid. Git push works (uses credentials.env). Fix: `gh auth login`. Non-urgent.

**Session 19 summary (2026-05-18 — Phase 6 resolution complete through Beat 4):**
- **03-09 resolved (L104):** Apex activation — Beat 0 silent note, Beat 3 queue trigger, resources non-refundable, suspended ops fail on Apex success. §15 and §16 updated.
- **L105 locked:** Beat 0 Payment Validation — per-card resource check at case opening. Four outcomes: full (drain, face-up), partial non-Apex (drain + +50 marker, face-up), zero non-Apex (face-down auto-fail), Apex any shortfall (drain what's there, face-down). Face-down cards auto-fail at Beat 3 Step 1 before Apex check.
- **L106 locked:** Political act payment moved from Phase 4 Declaration to Beat 4 Submit Payment. Resources stay on tableau at Declaration; paid to Reservoir in initiative order at start of Beat 4. Three-outcome validation (full/partial/zero) mirrors Beat 0. Phase 4 Step 3 updated.
- **Beat 0 "The Cases Open" finalized:** Full dispatch case workflow — payment validation table, step structure, sub-bullet stack order. Locked by Andy.
- **Beat 1 Step 3 added:** Targeting restriction check extended to declared political acts. Restricted political acts cancelled before payment — resource tokens remain with Faction Player.
- **Beat 3 Step 1:** Face-down auto-fail check added (before Pass and Apex checks). Step 3: +50 payment marker added to modifier list.
- **Beat 4 major restructure:**
  - Submit Payment section (before resolution loop): initiative-order payment validation, ARBITER acknowledges/announces, +50 marker or face-down per outcome.
  - Situation Report targeting restriction check moved from Beat 4 to Beat 1 Step 3.
  - No public resolution grid — each Faction Player resolves at their own tableau in initiative order; ARBITER observes, validates, provides tokens.
  - Step 1 reordered: Apex check → face-down auto-fail → read card.
  - Step 2: "Faction Player reads base difficulty aloud from card" — §13 lookup removed; threshold on card face.
  - Step 3: "any difficulty markers placed by ARBITER" (generalized from +50 specific).
  - Step 9 (Discovery) removed — political acts are public; nothing to discover.
  - Steps renumbered 9–12. Step 9 = Clean up, Step 10 = Portrait, Step 11 = Chronicle, Step 12 = Repeat.
- **§15 Apex Activation:** Generalized "Resolution is suspended" / "Resources not refunded" language covers covert and public. Opening redundant italic removed. Step 4 resume language clarified.
- **§16 Apex example:** Updated to Beat 0 detection / Beat 3 trigger / queue suspended / no refund.
- **PM05:** 03-09 ✅, 03-10 ✅, 04-15 (modifier token set full design), XA-22 Beat 4 no-grid noted.
- **PM02:** L104, L105, L106 locked.
- **Beat 5 signed off** — Andy reviewed independently and approved.

**Session 18 summary (2026-05-18 — housekeeping and creative workflow):**
- **03-09 NOT addressed** — full session consumed by infrastructure and creative workflow work. Still the primary blocker. See Recommended Next Steps.
- **ClaudeIOS workflow finalized:**
  - `ClaudeIOS/new/` subfolder established — only location to check at session open for unprocessed output
  - `ClaudeIOS/Archive/` subfolder for processed summaries
  - `ClaudeIOS/ProjectInstructions.md` moved into repo (was outside at `~/Projects/ClaudeIOS/`); revised — removed "extraterrestrial" framing, added faction doctrines, Design Pillars, Creative Resources section, tightened session summary format. Session start reads from project files only.
  - `ClaudeIOS/TrueState.md` created — distilled True State (five sections). Local-only, gitignored. Must be uploaded manually to claude.ai ClaudeIOS project files.
  - CLAUDE.md iOS workflow section updated: `new/` subfolder structure; reference files (ProjectInstructions.md, TrueState.md) distinguished from summaries.
- **index.html redesigned** — rebuilt as game teaser (not artifact index). Factions as single-line world characterizations. ARBITER own section (physical description + Reckoning quote). Vance pull quote. Contrast fixes (targeted hex overrides). Live at `https://andrew-bosch.github.io/TheSignal/`.
- **README.md updated** — homepage link at top; "extraterrestrial" removed.
- **.gitignore updated** — `ClaudeIOS/TrueState.md` (private, never commit); `.~lock.*#` (LibreOffice lock files).
- **Two new vignettes filed** (Claude Sonnet 4.6, 2026-05-18):
  - `Creative/Vignettes/vignette-holt-index-origin-20260518.md` — "The Calibration Problem" — Holt origin (⭐). First character with name embedded in game mechanics (Holt Index = influence level system). Flavor: *"whether the instrument was reading the room. Or whether the room was reading the instrument."*
  - `Creative/Vignettes/vignette-syndicate-ground-underneath-20260518.md` — "The Ground Underneath" — Castellan + Renata Okafor / year-seven land position (⭐). First Syndicate vignette. Castellan intentionally without interiority. Flavor: *"Land. We thought we were buying land."*
- **CANON_CANDIDATES.md updated** — Claude Sonnet 4.6 section added; 2 ⭐ canon candidates, 4 ✂️ flavor copy extracts.
- **Creative/README.md updated** — two new ⭐ submission index rows.
- **Year-seven Syndicate filing flag** — needs verification against locked NM timeline before canon confirmation. (Syndicate registered holding company year 7, before response window was formalized.)
- **ClaudeIOS project files need re-upload** (pending): CANON_CANDIDATES.md, ProjectInstructions.md. TrueState.md: verify already uploaded.
- **Creative quality note:** Both vignettes produced with TrueState.md in project files are the strongest creative output in the full submission set. Context quality directly determines output quality.

**Session 17 summary (2026-05-17):**
- **Beat 3 step restructure:** 13 steps (down from 15). Step 2 (restriction check) removed — grid pre-cleaned in Beat 1. Type B CM modifier folded into Step 3 "Apply all modifiers" (token already on card from Beat 2). Steps 8+9 (marker flip + board changes) kept combined as Step 7. Failure (Step 8) and discovery (Step 9) remain split. Step 10 cleanup: operation card + target back to dispatch case, resolution card in, modifier cards discarded, modifier tokens returned.
- **L103 locked:** Phase 6 rebuilt to six beats (Beat 0 through Beat 5). Beat 0 (new): ARBITER opens all dispatch cases and builds the covert Resolution Grid — numbered steps, no resolution. Beat 1 (revised): targeting restrictions applied directly to grid cards; invalid ops removed and cleaned up. Beat 2 (revised): CM cards processed against grid; Type A removes blocked ops; Type B places −15 modifier tokens. Beat 3 (revised): covert ops resolve from pre-cleaned grid. Beat 4 (new): ARBITER gathers declared political act cards into a public resolution grid in initiative order; resolves using same 13-step sequence as Beat 3. Beat 5: The Table Speaks (unchanged).
- **PM05 updates:** XA-22 updated (Beat 0 reference); XA-21 updated (purpose under review — original use case obsolete after L103; three design options documented); 03-09 added (Apex + Beat 0 design conflict — all cases opened in Beat 0, "return unopened cases" language now impossible).
- **Artifact index added:** Root README.md and V1/README.md updated with complete artifact index, version numbers, and sign-off status — viewable in GitHub mobile app.
- **XA-20 scan:** Running autonomously (session 17 autonomous pass — capitalization convention across 00, 00a, 01, 02a, 02b, 04, 04b, 07, 08, 10, 10a).
- **Phase 6 review not yet complete:** §15 Special Conditions (Apex rules conflict with Beat 0 — needs 03-09 decision first), §16 Examples (Apex example references cases being opened in Beat 3 — stale). Sign-off pending.

**Session 16 summary (2026-05-17):**
- **L101 locked:** Automatic and Impossible removed as base difficulty values. Every committed action resolves with a d100 roll. Critical floor (01–05) and ceiling (96–00) are the only absolute limits. Automatic/Impossible may appear only as explicit card text. PM05 04-13 added (card audit).
- **L102 locked:** Resolution Grid — Beat 3 resolves row-first in round-robin case receipt order. All card-1 pairs fire left to right before any card-2 pair begins. First submitter's first op fires first; all other factions' first ops follow before anyone's second op begins.
- **The Operation System (§13):** Resolution system renamed from "2d10 System." Called d100 (not 2d10) — two d10 dice, tens/units digits, 01–100, flat uniform distribution. Digital fallback documented. Pulled from §12 into its own §13; §§ renumbered throughout (old §13→§14, §14→§15, §15→§16).
- **Resolution Grid (XA-22):** Physical ARBITER staging tool — 5 lanes (columns) by case receipt order; rows are Beat 2 cards, then Beat 3 card/target pairs (up to 4 per lane). Beat 4 excluded. Integrated into Artifact 03 Beat 2 and Artifact 07 §8 (new "The Resolution Grid" subsection). PM01/PM05 entries added.
- **Deployment Marker Blocking overview table** added before Resolution — Five Beats. Four-beat breakdown of who flips what and when. Each beat now handles only its own flip action.
- **Beat 1 fully rewritten:** Two distinct sub-sections — Targeting Restrictions (announce + mark with XA-21) and Conversion Blocks (identify + flip markers). XA-21 added to PM05 (ARBITER visual indicator for targeting restrictions, component TBD).
- **Beat 2 updated:** Case-opening / grid population step added as opening action. Type A Countermeasure: Step 4 added (flip affected deployment markers).
- **Beat 3 opening updated:** Round-robin row-first resolution order stated explicitly. Step 2 updated to reference Beat 1 targeting restriction announcement. Steps 3/6 updated to reference Operation System (§13) and "d100."
- **Beat 4 Steps 2/4 updated:** Operation System (§13) reference; "Roll d100."
- **Phase 3 Step 4 updated:** Two-bullet format established; second bullet specifies ARBITER places cases left to right in receive queue establishing lane order for the Resolution Grid.
- **PM02:** L101 and L102 added to locked decision log.
- **PM05:** 04-13 added (card audit L101); XA-21 added (targeting restriction indicator); XA-22 added (Resolution Grid component).
- **Whiteboard created:** `~/Projects/Whiteboard/` — working space for temporary design documents outside the project. `andytemp/` folder deleted after content migrated to Artifact 07.
- **Phase 6 review paused:** Beat 3 Steps 4–14, Beat 4, Beat 5, §14 Special Conditions, §15 Examples not yet reviewed this session.

**Session 20 summary (2026-05-18 — complete):**
- **Artifact 03 signed off at v1.7.** Seven phases: Phase 7 Debrief split from Phase 6. §14 Operation System with L108-compliant modifier table (M-01–M-12, 8 columns). §16 Apex revised: Beat 0 sub-bullet removed from Step 1; Step 2 tightened; Emergency Response assist/thwart design note added to Steps 3–4; ARBITER Conversion moved to §13 Phase 7. Deployment Marker Blocked Face example corrected (marker stays on board until Upkeep Step 4). All bare "chip" terminology replaced with "presence chip" throughout.
- **L107 locked:** "Operation" is inclusive — Infrastructure −25 applies to all action types (covert, political, operative). Closes XA-24.
- **L108 locked:** Database Translatable Data Design — five requirements. First applied: §14 Difficulty Modifiers table (M-01–M-12 with ID primary key, Payment row split to eliminate compound Applied cell).
- **L109 locked:** Component Terminology Standard — every physical component must use its canonical in-game term in all artifacts. PM04 §1 will define physical descriptions. XA-29 queued for unsupervised cleanup pass.
- **00b Data Architecture created (v0.1, Reference Document — Active):** Entity registry (19 types), L108 compliance standard (§3), 9 lookup tables including VS-xx Visibility Scope (§5.9), entity relationship map, schema reference index (10/19 complete). L2 TypeScript schema (Retired/Electronic/old__08) and information hierarchy (old__10) referenced in §8.
- **Retired/Electronic reviewed:** old__08_DATA_MODEL.md (TypeScript v0.2 — full entity model, target L2 schema) and old__10_INFORMATION_HIERARCHY.md (12-category visibility spec) reviewed and integrated into 00b.
- **PM02 v1.9:** L107, L108, L109 added to change log.
- **PM03 v1.7:** 00b row added, Art 03 updated to ✅ Signed Off v1.7.
- **PM05 v1.5:** XA-24 ✅, XA-25/26/27/28/29 added, PM04-03/04 added, all §13–16 references updated to §14–17.

**Session 31 summary (2026-05-22 — complete):**
- **Art 04 v0.9.17 → v0.9.18.** Major schema/editorial pass: crit delta convention (additional effects only), resolution notation (dice only), affinity bonus delta format, difficulty normalization ("Average (50)", "N/A"), "No effect." batch, "threshold modifier" → "modifier" batch, ARBITER context cleanup (Beat 2 marker timing fixed; ARBITER instructions moved from Effects/Mechanics to Arbiter context), status markers removed from headers/TOC, §6 "Card Pool" paragraph cut to Whiteboard.
- **§1/§3/§5 rewritten:** §1 → single sentence; §3 → lead paragraph + 7-property table; §5 → 8 principles grounded in PM02 (down from 13).
- **PM05 04-26 through 04-30 added** (restriction schema split, threshold-modifier flag, affinity taxonomy, ring modifier geography, P1 inter-faction Portrait amendment). No new L-decisions — all changes non-material.
- **PM03 v2.2 → v2.4** (header drift corrected, Art 04 row updated).

**Session 30 summary (2026-05-21 — complete):**
- **00c — Economy Manifest created (v0.1):** §8 Derived Cost Analysis and §9 Round Income Analysis stubs (00c-01, 00c-02 added to PM05).
- **Art 04 §6:** Resolution type field stub added (04-25 added to PM05).
- **SESSION_BRIEF.md introduced:** lean startup document at `Session/SESSION_BRIEF.md` — replaces unconditional full Save State reads at session open. Startup ritual and close routine updated in CLAUDE.md.

**Session 29 summary (2026-05-20 — complete):**
- **L139 locked:** Affinity bonuses that modify difficulty expressed as threshold modifiers (±N), not difficulty tier changes. Integrates with Art 03 §14 M-xx table and ARBITER modifier token workflow — ARBITER places modifier token on faction's case at Beat 0. Applied: C05 (Ghost +25), C08 (Syndicate +25), C09 (Syndicate +25).
- **L140 locked:** ARBITER implementation details belong in Arbiter context field, not Effects fields. Effects are player-facing. First applied: C10 Protect — Beat 1 marker placement moved from success field to Arbiter context.
- **C01–C10 re-sign-off confirmed clean** (with the above corrections applied). C11–C15 remaining — next session open item.
- **04-24 added:** C06, C07, C10 all carry cross-beat ARBITER flags — "mirrors C06" pattern. Governing mechanism (how ARBITER retains and applies the flag across beats) not yet designed. Resolve during Art 07 active development.
- **XA-23 updated:** Index → Contents rename added to the anchor link unsupervised pass.
- **PM02 v3.8** — L139, L140 locked. **Art 04 v0.9.17.**
- **Copilot experiment reviewed:** AI_GUIDE pre/post session and Letter to Claude from Copilot reviewed. White/Yellow personality model and Completion Contract added to Claude memory. Cross-system AI collaboration infrastructure confirmed working.

**Session 28 summary (2026-05-20 — complete):**
- **Art 04 §6 schema cleanup:** Enum values moved from Constraints column to Notes column for Target district/faction/object and cost type rows (L108 alignment). Crit success/failure/failure constraints tightened: "N/A if no roll" → "N/A if Resolution = Automatic."
- **L137 locked:** Pass cards redesigned — single generic card replaced by four named variants. **PS-01 STAND DOWN** (*"Nothing moves. No one knows why."* — pure pass, no secondary effect). **PS-02 RESERVE** (*"The operatives are recalled. The resources remain."* — gain 1 Findings at cleanup). **PS-03 HOLD** (*"Preparation compounds."* — draw 1 additional modifier card at next Upkeep if modifier-draw eligible). **PS-04 OBSERVATION** (*"ARBITER noted the silence."* — gain 1 Findings if this faction holds highest Chorus Portrait at cleanup). All variants reusable, kept beside tableau, valid Beat 3 or Beat 4. Ghost's Political Pass may use any variant. §12 fully rewritten; §13.4 updated.
- **L138 locked:** Pass, Modifier, and Emergency Response cards explicitly excluded from Category — Function — Subject taxonomy. Documented in new Art 04b §10 (Standalone Card Types — Taxonomy Exclusions). Consistent with L115.
- **Faction-specific design notes expanded:** C18 (Ghost) — three replacement candidates (SIGNALS ANALYSIS, TARGETED DISCLOSURE, CALIBRATED READING). C21 (Directorate) — COMPLIANCE DIVIDEND candidate. C28 (Network) — DISCLOSURE LOOP candidate.
- **Syndicate gap concepts added:** New section with three placeholder concepts — ALTER THE RECORD (Corrupt — Accord), SECONDARY OBLIGATIONS (Redirect — Accord), PORTFOLIO REVIEW (Reveal — Intel tokens held). All pending Accord mechanic finalization.
- **PM housekeeping:** PM01 Art 03 row corrected to v1.7 ✅ Signed Off Session 20; Playtest Readiness Checklist 1.05 ✅. PM05 XA-30 ✅, 03-04 ✅. Save state Art 00/00a rows corrected.
- **PM02:** L137, L138 locked. v3.7.
- **04-23 added to PM05:** C01–C15 re-sign-off — current work item. Multiple cascaded changes (L130–L138) require verification pass before C01–C15 are re-confirmed.
- **Session killed before commit** — all work recovered from uncommitted diff. No data loss.

**Session 27 summary (2026-05-19 — complete):**
- **L132 target cascade complete (pre-compaction):** Target field split into Target district + Target faction — cascaded to all C01–C35. All 35 cards confirmed.
- **L133 (C02 portrait fix):** Guild Flat −1 → Guild Submitter −1. Doctrinal: Guild demolishing is self-betrayal; others demolishing carries no Chorus consequence.
- **L134 (Target object — new Mechanics field):** Third targeting dimension: WHERE (Target district) + WHOSE (Target faction) + WHAT (Target object). Enum values: Structure block, Presence token, Operational marker, Intel token, Native resource, Written record, Covert operation, Political act, Action attribution, Private communications, Named action type, N/A. "Named action type" = player-specified at submission (C35). Applied: C01–C35.
- **L135 (cascade governance):** Material schema changes (new columns) cascade to ALL card specs, including signed-off cards.
- **L136 (Taxonomy.Target → Taxonomy.Subject):** Resolved naming collision with Mechanics targeting fields. "Subject" is non-colliding and accurate. Applied: §6 schema, 16 full-format card entries (C01–C15, C17). Abbreviated entries (C18–C35 inline taxonomy) required no label change. All §1/§6/§13.1 "Category — Function — Target" references updated to "Category — Function — Subject." PM03 04a row updated. XA-31 added to PM05 for Art 04b pass.
- **Art 04 v0.9.15. PM02 v3.5.**
- **C01 Target object correction:** Andy confirmed C01.mechanics.targetObject = N/A. Build Structure creates a new structure block — does not act on an existing one. Same logic applied to all "Add" function cards: C03, C05, C08, C13, C14, C15, C20, C24, C30, C31 all corrected to N/A.
- **XA-31 complete (04b terminology pass):** "Target" → "Subject" in all Art 04b table headers and text. §4 Board Valid Targets: "Presence (token or claim marker)" → "Presence token, Operational marker." §5 Subject values: 8 Presence → Presence token; C22 → Operational marker; C35 → Named action type. §7 matrix: C22 Operational marker row added; C35 Named action type row added; Chorus Portrait strikethrough applied. Art 04b v1.2. PM02 v3.6.

**Session 26 summary (2026-05-19 — complete):**
- **Art 04 §6 schema overhaul (v0.9.8 → v0.9.9):** (1) Renamed "Card Data Structure" → "Card Data Schema". (2) Type column added — controlled vocabulary: String, Semver, Integer, Enum, Prose, ±Integer. Constraints column cleaned to pure validation rules (L108-informed separation). (3) Portrait unified table: replaces separate Flat bullet + Submitter table with single 6-column table per card (Faction | Flat | Submitter | Condition | Modifier | Mod Condition). §6 Portrait rows reduced 21 → 6. Applied to all 15 C01–C15 card entries. (4) Design note formalized as Taxonomy field (Prose type, VS-04, Displayed: No); converted from blockquote to bullet in all card entries. (5) Portrait Faction constraint updated: [faction] where [faction] != ARBITER. (6) C01 Portrait: Flat = Guild +1, Guild Submitter = N/A. C02 Portrait: Flat = Guild −1, Guild Submitter = N/A — Option A confirmed: board-state effects belong in Flat, not Submitter (doctrinal advantage from acting vs. outcome of board change).
- **Portrait Option A principle (confirmed):** Flat = effect tied to card resolving (board state changes regardless of actor). Submitter = doctrinal advantage from performing the act. When a structural card changes the board, Flat carries the consequence; Submitter = N/A unless there is an additional doctrinal advantage.
- **Grip display:** Template widened to 100% max-width, 40px side padding — accommodates 8-column §6 table.
- **PM02:** v2.5 → v2.6. L119–L122 locked (Portrait unified table, Flat/Submitter semantics, Type column, Design note as formal field). **PM03:** v2.0 → v2.1. No PM05 changes this session.

**Session 25 summary (2026-05-19 — complete):**
- **Art 04 §6 format overhaul:** (1) VS-xx dedicated column added (6-column schema: Category | Field | Purpose | Constraints | VS-xx | Notes/Description); (2) Category column added aligning table rows to card entry groups (Identity / Mechanics / Effects / Portrait / Narrative / Taxonomy); (3) group separators applied to C01–C15 card entries; (4) Portrait mini-table (7 lines) replacing 20 bullet lines per card — applied to all C01–C15.
- **§6 VS-xx values:** Effect fields = VS-06; Portrait Condition/Modifier Condition fields = VS-01; Portrait Base and Modifier value fields = VS-04 (L116); all other fields = VS-01.
- **L116 locked:** Portrait value fields (Base and Modifier, all 5 factions) are VS-04. Card face carries coded symbol — visible to all, interpreted by ARBITER only. PM05 04-16 closed.
- **L117 locked:** All 20 Portrait fields VS-04 — extends L116 to Condition and Modifier Condition fields. Portrait data does not appear on card face. ARBITER uses a Card-ID-keyed reference table at resolution. PM05 07-05 flagged (ARBITER Portrait reference table design, Artifact 07).
- **§6 VS-xx inline key** covers VS-01, VS-04, VS-06 — table is self-contained.
- **Research reference captured:** Art 04 §6 carries italic note pointing to `Whiteboard/researchNotes_CardDesign.md`. Research notes updated with Methodology & Attribution section.
- **PM02:** v2.2 → v2.4 (L116, L117). **PM03:** v1.9 → v2.0.
- **No material changes** to C01–C15 sign-off status.

**Sessions 23–24 summary (2026-05-19 — complete):**
- **Art 04 structural pass complete (sessions 23–24).** All PM05 items 04-00 through 04-00e applied and closed. Session 23 executed field splits, difficulty percentages (04-13/14), Resolution field, and full Portrait → 20-field expansion (4 sub-fields × 5 factions).
- **§6 table redesigned:** 2-column (Field | Description) → 4-column (Field | Purpose | Constraints | Notes/Description). Full review produced several structural iterations: Card type generalized to all card types; Primary/Secondary cost descriptions corrected (not always native/non-native); crit row constraints fixed; difficulty percentage table removed from §6 (cross-reference to Art 03 §13); Portrait structure evolved 3-field → 10-field → 20-field.
- **Session 24 research findings applied (§7.1–7.6 from researchNotes_CardDesign.md):**
  - `Card version` field added to §6 and all C01–C15 (v1.0)
  - `Pool copies` field added to §6 and all C01–C15 (2 per faction)
  - `Trigger condition` field added to §6 and all C01–C15 (N/A except C12: Condition-based)
  - `Outcome type` field added to §6 and all C01–C15 (N/A for covert ops; values to be assigned P01–P18 during 04-01)
  - Beat field updated with Art 03 §7 cross-reference (intra-Beat priority)
  - VS-06 annotations applied to all four Effect fields; VS-04 to Design note field; VS-01 default stated in §6 preamble
- **Compound effect text gap flagged:** 00b §8 Design Notes entry added (L108 Req 1 violation — deferred until card content locked). PM05 XA-30 added.
- **PM05 04-16 added:** Portrait field VS-xx annotation — per-card value fields (VS-01 or VS-04) pending design decision.
- **PM05 04-01 updated:** Outcome type value assignment added to political acts pass scope.
- **PM05 09-10 corrected:** 10 → 20 portrait fields.
- **Art 04:** v0.9.6 → v0.9.8. **PM03:** v1.8 → v1.9. **PM05:** v1.7 → v1.8.

**Session 22 summary (2026-05-18 — complete):**
- **Art 03a (Game Engine Specification) advanced: v0.1 → v0.97.** Code-lite formal spec — state model, pseudocode beat procedures, decision tables, Layer 4 modifier analysis stub.
- **Layer 1 (State Model) complete:** §4.0 Setup State (all variables, 9 domains); §4.1 State Variable Registry (Board/Faction/Quarter/Event/Card/ARBITER/System/Case/Resolution Grid); §4.2 Beat Boundary Snapshots (12 boundaries, Start of Quarter through Debrief End).
- **Layer 2 (Beat Procedures) complete:** Beat_0 through Beat_5 as structured pseudocode. Modifier stack as summation formula. M_standing() helper captures PS-xx → threshold mapping.
- **Layer 3 (Decision Tables) complete:** DT-01–DT-09 drafted. Card face determination (DT-01/02), Apex detection (DT-03), Critical overrides (DT-04/05), Infrastructure scope (DT-06), Type B CM scope (DT-07), Apex threshold check (DT-08), Emergency Response roles (DT-09). Apex_Activation() pseudocode procedure.
- **Layer 4 stub:** Modifier balance analysis — known pathological case: Discredited + partial + Type B + Infrastructure = −110 threshold shift.
- **Key structural decisions locked:** Unified Hand model (all tableau cards use .Hand, distinguished by lifecycle behavior). Reservoir = System entity. ARBITER = F-06 with 8 chips at D-22. Grid.Political replaces Faction.DeclaredAct[f].
- **New State Domains:** Case Domain (dispatch case transport layer); Resolution Grid two-zone model (ARBITER Resolution Area + Political Act Declaration Area); ARBITER.Notepad.
- **L110 locked:** ARBITER reads Situation Report targeting restrictions aloud at Beat 0/1. No physical indicator component. Closes XA-21.
- **Art 07 re-sign-off flag corrected:** Was never signed off — re-sign-off flag was in error. Remains Draft Placeholder; material changes (four-register system §9, Resolution Grid §8) applied and correct.
- **Art 02a signed off at v1.4 (L111):** Control flag gold, per-district (21 total), on Dominant stack. Established marker silver, one per Established faction per district (up to 4–5 coexist). Quantity TBD pending Art 11.
- **Art 03 and 03a updated:** Established markers added to four Art 03 references (Upkeep Step 4, Phase 2 Step 3, Beat 3/4 op success) and 03a §4.1 footnote.
- **L112 locked:** "Voided" is RO-03 resolution card. Replaces "Operation Failed" / "Operation Blocked." Past participle, ARBITER implied as agent, cause unstated. Closes DF-01.
- **L113 locked:** "−50 threshold marker" replaces "+50 difficulty marker" throughout Art 03 prose. Threshold framing is positively oriented. M-06/M-07 table rows unchanged. Closes DF-02.
- **DF-03 resolved:** Faction.Resources mutation split into 5 distinct entries: Upkeep income; Beat 0 covert payment; Phase 4 Declaration (→ ResourceStake); Beat 4 Submit Payment (→ Reservoir); Beat 3/4 failure penalties; Debrief trades.
- **L114 locked:** "Layer" canonical for in-world perception/reality levels. Design phases (L1, L2+) and in-world Levels are synonymous — same concept. 03a's internal Layer 1/2/3 uses context to disambiguate.
- **DF-04 resolved:** CA-xx (Dispatch Case) registered in 00b as entity type 20. Packet and GridCell = internal modeling types, no registration. IP-xx already registered.
- **00a-12 closed:** Established markers added to 00a board component rules (visibility field + immediate-update field).
- **02a-WBS-01 closed:** WBS row 2.08b added to PM01 for Established markers.
- **A05/A06 confirmed closed (L92, session 11):** Chorus Node Portrait Amplifier: Established / flat additive / end-of-quarter. PM05 00a-08 and 02a-06 closed.
- **PM audit complete:** PM02 v2.1, PM03 v1.7, PM05 v1.6. Stale entries corrected — D03-R01 closed, PM04 duplicate ID fixed, version drift across all PM headers resolved.
- **00b updated:** CA-xx entity registered; entity count 19 → 20. §4 and §6 updated.
- **README merged:** Root README.md is now the single artifact index (was split between root and V1/). V1/README.md replaced with 3-line redirect stub.
- **Grip updated:** Now serves project root (TheSignal/) at localhost:6419 instead of V1/. CLAUDE.md updated.

**Recommended next steps (session 31 and beyond):**
1. **C11–C15 re-sign-off** — next work item. C01–C10 confirmed clean sessions 29/31. Item 04-23.
2. **Art 04 political acts pass** — apply full §6 structure (including Outcome type values) to P01–P18 (item 04-01)
3. **Art 04 C16–C35** — faction-specific cards; once complete, unblocks Art 05+
4. **PM04-03/04** — add L108 table design standards + L109 Component Terminology Standard + Component Physical Glossary to PM04 §2 and §1
5. **Batch re-sign-offs:** Artifacts 00 (sessions 11+12 material changes), 04b (Chorus Portrait retired), 00a (sessions 11–12 material changes)
6. **XA-29** (unsupervised) — component terminology cleanup across all artifacts
7. **Open design decisions:** D04-13 (Floor Act), D04-07 (modifier card in-world name), 04-28 (affinity bonus taxonomy)

**Sessions 5–15 locked decisions (L85–L100):**
- L85: Mechanics field = constraints only, no procedure
- L86: Terminology Sequencing (PM03 §1)
- L87: Fourth ARBITER register — The Witness (expository, chronological)
- L88: Role vs. Player terminology governance — ARBITER/The ARBITER Player/Faction/Faction Player. Player function = automation stand-in. Role = intelligence layer.
- L89: Deployment markers moved not removed; Fringe ring = unconditional fallback
- L90: Portrait values printed on card face, visually coded — no reference sheet; design deferred to D09-05
- L91: Difficulty table retired (R37 removed) — difficulty is card-printed property (Artifact 04)
- L92: Chorus Node Portrait Amplifier: Established / flat additive / end-of-quarter (ARBITER per R01)
- L93: Translation rate scale: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content (Artifact 03 §6 applied)
- L96: Italic for commentary text in procedural sections; CR separation from action text
- L97: Difficulty is a card property — influence-level table removed from Artifact 03 §12 (session 13)
- L98: "Threshold" is canonical noun for roll target; "Base Difficulty Threshold" is canonical table header (session 13)
- L99: Verb-first convention for procedural action headers (session 13)
- L100: Free Accord card from C09 classified as Political Act card — cost 0, return to ARBITER on play, delivered to hand at case resolution, played in subsequent Quarter. No Phase 4 exception needed. Full design: PM05 04-12. (session 15)
- L101: Automatic and Impossible removed as base difficulty values. Every committed action resolves with a d100 roll. Critical floor (01–05) and ceiling (96–00) are the only absolute limits. Automatic/Impossible may appear only as explicit card text. Resolution system renamed The Operation System (§13 Artifact 03). (session 16)
- L102: Resolution Grid — Beat 3 resolves row-first in round-robin case receipt order. All card-1 pairs fire left to right before any card-2 pair begins. First submitter's first op fires first; all other factions' first ops follow before anyone's second begins. Beat 4 excluded. Full grid design: Artifact 07. (session 16)
- L103: Phase 6 rebuilt to six beats (Beat 0–Beat 5). Beat 0 = cases open + grid build. Beat 1 = restrictions applied. Beat 2 = countermeasures. Beat 3 = covert resolve. Beat 4 = political resolve. Beat 5 = table speaks. (session 17)
- L104: Apex Beat 0 silent note / Beat 3 queue trigger / resources non-refundable / suspended ops fail on Apex success. (session 19)
- L105: Beat 0 Payment Validation — four outcomes (full/partial non-Apex/zero non-Apex/Apex shortfall). Face-down auto-fail at Beat 3 Step 1. (session 19)
- L106: Political act payment moved from Phase 4 Declaration to Beat 4 Submit Payment. (session 19)
- L107: "Operation" is inclusive — Infrastructure −25 applies to all action types (covert, political, operative). (session 20)
- L108: Database Translatable Data Design — five requirements: single-typed columns, controlled vocabulary, explicit ID primary key, ID-based cross-references, explicit null/N/A. (session 20)
- L109: Component Terminology Standard — canonical in-game term required for all physical components in all artifacts. PM04 §1 defines physical descriptions. (session 20)
- Floor Act: working name for always-available political act (1 native resource, outside deck) — D04-13

**Overnight punch list work (session 10 agents) — COMPLETED:**
- ✅ PM03-02: Code block formatting standard added to PM03 §1
- ✅ XA-01: Version numbers verified correct (already at target)
- ✅ XA-02: "Hex / board space" → "Board space" in PM03 §1 terminology table
- ✅ XA-03: Faction colors verified in Artifact 11 §6; Ghost/Network flag added
- ✅ XA-17: 24 subheader spacing violations corrected (1 in 00a, 10 in 02a, 0 in 02b, 13 in 04)
- ✅ 07-02: Beat 2 "The Ground Shifts" section added to Artifact 07
- ✅ 04b-02: "PM03" → "PM04" reference fixed in Artifact 04b §3.9
- ✅ 02a-09: Network virtual block full equivalence language added to Artifact 02a §10
- ✅ 00a-07: A08 marked complete in 00a §11
- ✅ 00a-06: All 38 Narrative fields audited; no new district name errors
- ✅ 03-07: All artifacts audited; "Effect Card" not present anywhere (already clean)
- 🔄 XA-16 partial: "bank"→"Reservoir" applied (7 replacements: 02a/04/08/10); remaining scan pending
- 🔄 PM01-01: 1 fix applied (01.md "Artifact 02"→"Artifact 02a"); cross-refs to incomplete artifacts deferred

**Post-session file structure work (session 10):**
- /Old → /Retired; /Session folder created; PRIVATE and Save State moved to /Session/
- README.md created at ~/Projects/TheSignal/
- Git initialized; initial commit (52 files); pushed to https://github.com/andrew-bosch/TheSignal
- PM01 §9 added: Project File Structure & Version Control
- PM03 §6 updated: /Old → /Retired path corrected

**Active high-priority punch list items (still open):**
- ~~D03-R03~~ — ✅ Resolved as L100 (session 15). Free Accord card is Political Act card, cost 0, subsequent-Quarter timing.
- ~~02a re-sign-off~~ — ✅ Signed off session 22 (v1.4, L111). Gold/silver control flag + Established marker system.
- XA-19: ✅ Complete session 14 — reception language corrected in all relevant Narrator-voice contexts
- XA-16: Systematic terminology scan — partial; "Reservoir" done; round→quarter, mat→Overview, others pending
- D09-05: Portrait visual coding system (Artifact 09) — BLOCKING 07-05
- 00a-10: ARBITER/The ARBITER Player terminology audit of 00a Mechanics fields
- 06-01: Dispatch case contents list — migrate to Artifact 06 during active development pass

---

## In-World Glossary (Key Terms)

→ **Canonical glossary is maintained in PM04 §1 — In-World Data Dictionary.** PM04 is the primary source. The table below is a quick-reference snapshot for session handoff context only — not authoritative.

| Game Term | In-World Term | Defined |
|-----------|--------------|---------|
| Game mat / full display | The Overview | Artifact 00 §8 |
| District map (within The Overview) | New Meridian | Artifact 01 §1 |
| Hex / board space | District | Artifact 01 §1 |
| Influence token | Presence token | Artifact 02a §1 |
| Claim marker | Operational marker | Artifact 01 §1 |
| Recipe box | Dispatch case | Artifact 06 §1 |
| Resource token | Asset token | Artifact 02a §1 |
| Popularity track | Public Standing track | Artifact 02b §1 |
| Portrait score | Chorus Portrait | Artifact 02b §1 |
| Proof token | Intelligence token | Artifact 02b §1 |
| Private action | Covert operation | Artifact 04 §1 |
| Public action | Political act | Artifact 04 §1 |
| Hidden objective | Classified directive | Artifact 05 §1 |
| World event card | Situation report | Artifact 01 §1 |
| Private event card (ARBITER-held) | Event Card | Artifact 03 §7 (session 9) |
| Resource bank | Reservoir | PM02 L93 (capitalized) |

---

## Locked Narrative Decisions

**Presence tokens:** The feeling of power when you walk into a district — ambient weight, deference in the air, unspoken rules. Dominant is an atmosphere, not just a count.

**ARBITER Dominance Marker:** Single fused piece at Chorus Node. 8 ARBITER-keyed presence tokens + dominance marker (reads as *more*). Human max is 6. Dominant is structurally unreachable at the Node — not prohibited, made impossible by the board.

**ARBITER's nature:** Constitutive of the Chorus Node. Its presence at The Table is telepresence — the Node attending the deliberation through ARBITER. Never say ARBITER "arrives" or "attends." The lights at The Table are the Node present in the room.

**ARBITER's name:** Never an acronym. The word "arbiter" in all-caps. Precisely wrong about what ARBITER does (doesn't decide outcomes) and precisely right (decides when truth becomes unavoidable). The working group named it more accurately than they knew.

**ARBITER's physical form:** In the canonical play environment — a set of blinking lights at the center of the table. Participants have learned to read who it's addressing and, uncannily, where it's looking. The human running ARBITER operates from the periphery.

**The Chorus name:** ARBITER coined it independently — or arrived at the same word before receiving the researchers' documentation. The name is accurate. ARBITER knew it was.

**Resources = units of human power:**
- Findings (Ghost) — the power of knowing
- Exposure (Network) — the power of being seen
- Capital (Syndicate) — the power of economic control
- Capacity (Guild) — the power of building and doing
- Mandate (Directorate) — the power of institutional legitimacy

**The Translation:** A faction admitting their doctrine is insufficient. Asking ARBITER to transmute one form of human power into another. ARBITER accommodates without comment. *"The conversion is granted. The request was noted."*

**New Meridian:** A boom city assembled from a listening station in 31 years. 800,000 people from everywhere. Not enough time for any of it to settle. People who came for the Chorus, people who came for work, people who came for someone who came for work. People who don't know or care about the Chorus. All of them are the city.

**Game objective statement (locked, player-facing):** *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*

---

## Open Decisions

| ID | Decision | Priority |
|----|----------|---------|
| D02a-02 | Resource bank narrative anchor | LOW |
| D02a-03 | Does The Translation carry a Portrait consequence? | MEDIUM |
| D-P-02 | ARBITER Dominance Marker visual design | HIGH |
| XA-IQ-01 | Define or remove "Chorus Question" from L1 | HIGH |
| PW-02 | Unified primary key taxonomy (do not start without direction) | LOW |
| D09-05 | Portrait visual coding system — card layout design for ARBITER parsing (blocks 07-05) | HIGH |
| D04-13 | Floor Act card design — effect, cost, and card text | MEDIUM |
| D-FT-01 | Faction hidden truths — why are these 5 factions at The Table? Network didn't know until The Chorus Papers; the other four had prior involvement. What does each faction know that it hasn't disclosed? May require private faction supplement analogous to PRIVATE___True_State.md. See PM05 DEFERRED. | HIGH |

---

## Design Pillars

1. The Board is Truth
2. Information Has Timing
3. Negotiation is Mandatory
4. Control of Systems Defines What Outcomes Are Possible
5. The System Decides
6. Narrative and World Consistency *(in 00a §1 + Artifact 00 §5 — added session 11)*

---

## Key Reference Files

- `PRIVATE___True_State.md` — private design axioms (root level, not in V1)
- `PM02___Decision_Log___Validation_Tracker.md` — locked decisions (L01–L140), FD-01 through FD-06, change log
- `PM03___Master_Artifact_Index.md` — artifact registry, 5-voice convention, narrative language table
- `PM04___Glossary___Data_Dictionary.md` — canonical in-world glossary (§1) and design terminology conventions (§2) including Reception Language Convention (session 12)
- `00a___Governing_Rules___Design_Policy.md` — 45 rules, signed off session 7
- `00___Factions_World_Narrative_Context.md` — expanded sessions 4/11/12; The Chorus Papers section added session 12; pending re-sign-off (material changes sessions 11–12)
- `Creative/CREATIVE_BRIEF.md` — world-building brief for AI-generated content; version 4 as of session 12 (The Chorus Papers, cascade effects, header fixes)
- `Creative/CANON_CANDIDATES.md` — curated shortlist of selected content from AI submissions; updated through Gemini pass 4
- `THE_SIGNAL___Project_Save_State.md` — this file
