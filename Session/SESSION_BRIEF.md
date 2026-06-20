# THE SIGNAL — Session Brief
**Session 106 complete | S107 next | Updated: 2026-06-19**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

### Priority Order (S107) ← CURRENT

**Tier 1 — Art 04b full audit against 00a** (Andy: "we missed that audit")
- Full sweep of Art 04b taxonomy functions/verbs against 00a governing rules
- S106 found: Recover violates 7.2b. Full audit required before more card design.

**Tier 2 — Syndicate gaps** (deferred from S106)
- Information|Corrupt|AccordAgreement
- Information|Reveal|IntelTokensHeld
- Accord Transfer sign-off

**Tier 3 — Art 04 spec fixes (04-n103)**
- GUI.CA.2: function Recover → Add
- GUI.CA.6: function Recover → Add; card_id/variable assignment
- Field Verification: BLOCKED flag + G-ext id (7.2b violation)

---

### Priority Order (S106) ← PREV

**S106 accomplishments:**
- DIR.CA.6 Institutional Audit ✅ — Economy|Add|Mandate. Ring Permanent count yield; chip count > 1 restriction.
- DIR.CA.7 Institutional Brief ✅ — Standing|Shift|PublicStanding. Same ring Permanent count architecture as CA.6.
- DIR.CA.8 Enhanced Scrutiny ✅ — Resolution|Modify|Difficulty. Beat 2 Automatic; −15 Modifier tokens on all Beat 3 rows in target district.
- NET.CA.7 Ground Signal ✅ — Standing|Shift|PublicStanding. IL ≤ Established restriction; successcrit = +1 chip + +1 PS.
- NET.MOD.1 Signal Break ✅ — Territory|Add|PresenceToken React Modifier. Trigger = PA success causing board state change. Exposure×1; d100 threshold 50.
- GUI.MOD.1 Return to Site stub — Territory|Add|PresenceToken React (formerly Territory|Recover|PresenceToken).
- GUI.CA.6 Labor Contract — card_id GUI.CA.6 assigned (L219).
- **Recover function retired from Art 04b** (04b-20 ✅ — 00a 7.2b: committed board states cannot be nullified):
  - GUI.CA.2 Materials Acquisition: Recover → Add (taxonomy); Art 04 spec fix pending 04-n103
  - GUI.CA.6 Labor Contract: Recover → Add; Art 04 spec fix pending 04-n103
  - Field Verification: BLOCKED — arbiter.update(token.quarter) violates 7.2b; fundamental redesign required (04-n103)
  - L218 annotated in PM02 as consequence of 7.2b, not standalone decision
- PM05: 04-n102 (Modifier card schema), 04-n103 (Recover Art 04 spec fixes), 04b-20 ✅
- Art 04 v0.9.41 Draft. 04b §4/§5.2/§6/§7/§8.3/§8.5 updated.

**Tier 1 (S106) — Card design pass** (all gates cleared)
- Art 03 ✅ v4.8 (L217, S104) · 00a ✅ v0.8 (S83) · ID-04 ✅ (L221, S105)
- Card design pass: Standard → faction sets
- PM05: 04-n50–04-n67 (set-level milestones) · 04-n87–04-n92 (doctrine review)

**Tier 2+ — Deferred**
- 03-n01 (Beat 2 overhaul) — dedicated session
- 01-n02 (Art 01 overhaul)

### Priority Order (S105) ← PREV

**S105 accomplishments:**
- ID-01 through ID-05 + ID-SCHEMA ✅ — agy completed between sessions (reported in Claude_context.md)
- ID-04 ✅ — Full renumber complete: [FAC].[TYPE].n format applied across Art 04 (678 substitutions), Art 04b (201 substitutions), card_ref DB (27 rows), and ref_*.md / design_reference_card_system.md. 3 dot-ref lines in Art 04 preserved (L6286/L6950/L6979 — pseudocode variable refs). card_id field added to Art 04 §6.1/§6.2. Art 04b §9 Pass card entry removed (retired).
- Art 04b v1.7 ✅ signed off — L221. §§6/7/8 are living sections; updated as gap cards are designed, not a re-sign-off gate.
- Decision: Art 04 card set files remain monolithic until CA/PA design pass is complete; split to per-faction sub-files after design stabilizes.

### Priority Order (S104) ← PREV

**Tier 1 (S105) — Card renumber pass + 04b-19 sign-off**
1. Check Claude_context.md — verify agy completed ID-01/02/03, ID-05, ID-SCHEMA between sessions
2. ID-04: Full renumber — (a) add card ID taxonomy definition to Art 04 §6 data dictionary, (b) establish canonical ordering per deck type, (c) renumber all cards across Art 04, Art 04b §5.2/§7, and card_ref
3. 04b-19: Art 04b v1.7 sign-off (gated on ID-04 complete)

**Tier 2+ — Deferred**
- 03-n01 (Beat 2 overhaul) — dedicated session
- Card design pass (gate: 00a-72 + Art 03 stable + ID-04 complete)
- 01-n02 (Art 01 overhaul — gate: 00a-72 first)

**S104 accomplishments:**
- Art 03 v4.8 ✅ signed off (L217) — §24 Resolution State Reference (three states: Succeeded / Failed / Voided; Discovered fires alongside Failed, not parallel). RO-xx removed throughout Art 03. §9.4.1.0 targeting restriction updated to flip face-down (unifying all Voided cases under §9.4.2.0 Step 0 handler). Open: 03a-n01 (3 residual RO-xx refs in 03a, lines 1038/1363/1370 — non-material, separate artifact)
- Art 04b v1.7 content complete: 04b-16 ✅ (§6 refresh — gaps updated, §6.2 stale rows replaced, §6.3 stale counts removed / Art 03 §22 pointer corrected), 04b-17 ✅ (§7 matrix rebuilt from Art 04 data — STD.CA.2/DIR.CA.3 misclassification fixed, DIR.CA.5/DIR.CA.4/GHO.CA.6–SYN.CA.6/SYN.CA.7 added), 04b-18 ✅ (§8.1–§8.4 updated to current card states; §8.5 Guild added). 04b-19 sign-off gated on ID-04 (§7 IDs must be updated before Andy can validate)
- L218: Territory|Recover|StructureBlock not possible — demolition is permanent; rebuild = Territory|Add (STD.CA.1). §6.1 N/A; §8.5 Guild rec removed
- L219: Card ID schema locked — [FAC].[TYPE].n; varchar(15). 20-deck inventory; STD = 5 physical copies; ARB.BCAST/BCEV only ARBITER cards; ARB instruments not cards. Full schema in PM02
- L220: DB script idempotency convention locked — INSERT IGNORE, portable session patches, archive/ subfolder for originals
- ID-01 through ID-05 + ID-SCHEMA queued in PM05 and GEMINI_CONTEXT.md for agy between sessions

### Priority Order (S103) ← PREV

**Tier 1 — Art 04b refresh** (Art 03 stable ✅ — check 02-n26 gate status before starting)
- 04b-16 → 04b-17 → 04b-18 → 04b-19 (re-sign-off v1.7).

**Tier 2+ — Deferred**
- 03-n01 (Beat 2 overhaul) — dedicated session
- Card design pass (gate: 00a-72 + Art 03 stable)
- 01-n02 (Art 01 overhaul — gate: 00a-72 first)

*Note: Art 00 v1.7 needs re-sign-off (§14.10 Integration added S99). Art 02 v2.2 ✅ S98 (L213). Art 03 v4.8 — re-sign-off needed (S103 changes: §24 added, RO-xx removed, targeting restriction procedure updated).*

**S103 accomplishments (mid-session clear):**
- 03-n25 ✅ — §24 Resolution State Reference added to Art 03. Three states: Succeeded / Failed / Voided. Discovered defined as resolution effect (fires alongside Failed, not a parallel state). RO-xx codes removed from Art 03 and 03a throughout. Targeting restriction procedure (§9.4.1.0) updated to flip face-down in grid — unifying all Voided cases under single Beat 3 Step 1 handler. DB resolution_outcome pruned to 3 rows (Discovered and Auto-failed dropped). Art 03 v4.8.

### Priority Order (S102) ← PREV

**Tier 1 — Art 03 ✅ S102**
- Art 03 v4.7 ✅ (L216) — § Primitive Action Model appendix restructured (governing principle surfaced; S97/S101 decision tables removed; DB is source of truth). Index anchor fixed. Inline flags removed.
- agy task queued (GEMINI_CONTEXT.md): v_unlegislated_primitives pass — 6 ❌ prohibit (junction table cleanup), 4 ✅ permits, 14 seeding gaps.

**S102 accomplishments:**
- Art 03 § Primitive Action Model appendix restructured: governing principle surfaced, S97/S101 decision tables removed (DB is source of truth), coherent section flow. Index anchor fixed. Status block trimmed. Inline flag removed from § Examples.
- v_unlegislated_primitives legalization pass (52 rows): 6 ❌ prohibit, 4 ✅ permit, 14 seeding gaps, remainder §22 seeding tasks — agy task queued in GEMINI_CONTEXT.md.
- Art 03 v4.7 ✅ signed off (L216).

### Priority Order (S101) ← PREV

**Tier 1 — Art 03 ✅ S101**
- Art 03 v4.5 ✅ (L214) — 02-n08 migration. Art 03 v4.6 ✅ (L215) — 03-n24 Primitive Action Model legality table.
- agy seeding of 11 permitted combinations ✅ complete (Claude_context.md S101 report).
- 03-n25 queued.

**S100 accomplishments:**
- DB fix ✅ — `public_standing_tier`: Celebrated 18–20, Respected 14–17, Neutral 7–13.
- 02-n08 ✅ — Art 03 v4.5. `Whiteboard/art02_orphaned_content.md` deleted. Full structural pass:
  - §7.4: University Perimeter virtual structure definitional rule added.
  - §11.0/§1145: dead pointer → inline pointer to §19.1.
  - §13: trimmed to operation-system scope. §13.2 merged with former §13.4 (succeed/fail + crit in one table). §13.3–§13.5 renumbered. RO-01/02 in §13.2. Former §13.7/§13.8/§13.9 removed from §13.
  - §19 Influence Level Reference: §19.0 thresholds + §19.1 Chorus Node Benefits & The Translation (merged — single table with Benefits + Translation rate columns).
  - §20 Resource Generation Reference: ring base values + IL generation by level + affinity + structure + passive.
  - §22 Board State Update Rules (moved from §13.7).
  - §23 Public Standing Scale (moved from §13.8; band/range/drift table only; modifier → §13.4 ref).
  - Appendices section added; Primitive Action Model + Examples & Exceptions moved under it.
  - Index updated throughout.
- PM05: 02-n08 ✅, 02-n27 added (Residential Quarter PS multiplier — placement deferred), 03-n25 added (generalized resolution effects reference section — Discovered pattern).

### Priority Order (S99) ← PREV

**Tier 1 — Art 03 migration + re-sign-off**
- **DB fix first:** `UPDATE public_standing_tier` — set Celebrated 18–20, Respected 14–17, Neutral 7–13 (whiteboard canonical per S99 decision; three UPDATEs).
- **02-n08 migration** (whiteboard `art02_orphaned_content.md` → Art 03):
  - §19 "Reserved" → "Influence Level Reference" (IL thresholds, resource gen by IL, Chorus Node benefits table). "Absent" → "None" throughout.
  - §20 dead-pointer fix (ring base values + structure income fully written; remove "Art 02a §8" stub)
  - §1145 dead-pointer fix (translation rate table written inline)
  - New §13.8: Public Standing scale (bands 0–20 corrected values + drift table + full difficulty grid)
  - New §13.9: Resolution Outcome reference (RO-01–RO-05 + crit flag note)
  - §7.4 Resource Collection: University Perimeter virtual structure definitional rule added
  - Portrait scale (whiteboard §5) → Art 07, not Art 03 — skip this pass
  - Delete `Whiteboard/art02_orphaned_content.md` after migration
- **Not in this pass:** 03-n01 (Beat 2 overhaul — dedicated session), 03-n24 (§22 legality table — dedicated session)
- Art 03 version bump + re-sign-off after migration.

**Tier 2 — Art 04b refresh** (downstream — after Art 03 signs off)
- 04b-16 (§6 Coverage Analysis) → 04b-17 (§7 Faction Coverage Matrix) → 04b-18 (§8 Design Recs, incl. Guild) → 04b-19 (re-sign-off v1.7). Gate: 04b-15 ✅ S97. All unblocked.

**Tier 3+ — Deferred**
- 03-n01 (Beat 2 overhaul), 03-n24 (§22 legality table) — dedicated sessions each
- Card design pass — Standard → faction sets (gate: 00a-72 + Art 03 stable)
- 01-n02 (Art 01 overhaul — gate: 00a-72 first)

*Note: Art 02 v2.2 ✅ S98 (L213). 02-n07 ✅ S99. Art 00 §14.10 added S99 — re-sign-off needed.*

**S99 accomplishments:**
- 02-n07 ✅ — "Integration" registered: §14.10 narrative anchor written to Art 00; term row added to 00a Component & System Terms; TrueState §11 open question logged. Art 00 now needs re-sign-off (§14.10 is material).
- Art 02 DB sync header note added (`**DB Sync:**` line).
- Art 03 migration plan finalized: DB fix (PS bands) + 02-n08 whiteboard migration. See Tier 1 above.
- Design decisions: PS band boundary — whiteboard canonical (Neutral 7–13); influence level zero term = "None" (DB); 04b refresh downstream after Art 03 sign-off.

**S98 accomplishments:**
- DB-41 ✅ — verb seeding: d10 (id 119) Add/Remove/Move/Flip; Modifier token Flip; Threshold Sliders Corrupt; all card containers/decks Reveal/Conceal; Faction Hand + Operative Pool Corrupt. transform_orientation corrected id=42; transform_visibility corrected ids 108/48/95/96; missing subject_target rows inserted (Dispatch Packet, Broadcast Effect Card, Status marker).
- DB-42 ✅ — `component_metadata` table created (Option A hybrid wide) and seeded (74 rows via Python parser). L130 locked: subject_target authoritative for placement; movement_path stays in prose; `trigger` is a reserved word.
- DB-43 ✅ — static lookup tables seeded: public_standing_tier (5), difficulty_tier (3), resolution_outcome (5), influence_level (4).
- Art 02 v2.2 ✅ S98 (L213) — applicable_verbs seeded into all §§5–12 entries; §13 matrix removed (entries are now source of truth); d10 (DB:119) added §11; ARBITER Dominance Marker Flip corrected; ARBITER Dominance Marker transform_orientation reverted in DB.
- 02-n09 ✅, 02-n26 ✅ S98. DB-41/42/43 closed.

**S92 accomplishments (mid-session clear #1):**
- README.md — fixed two broken Art 03 anchor links.
- Art 02 02-n02 — Gameplay Requirements validation pass, 7 issues resolved (DB:2, 11, 10, 3, 50, 1, 13).
- Art 02 DB:4 — accommodation requirements and virtual structure block notation added.
- Art 02 §3 — "Calculation over count" and "Procedurally auditable structure" added.
- Art 02 §4 — per-group metadata schemas written for all 8 groups.
- 00b §4.5, Art 07 §6.5 — Portrait band updates.
- PM05: 00a-n04, 03-n23, 07-13 added.

**S92 accomplishments (mid-session clear #2 — this clear):**
- PM05 02-n14 added — District Tile per-faction zone layout (working assumption: organized lanes; virtual structure = faction-keyed filled square printed on tile; back-stream update pending visual design lock).
- Art 02 §4 fully redesigned → **§4.1 Universal Component Schema**: 17 fields (2 identity + 9 universal + 6 group-specific); Physical Form table replaced by Metadata block throughout; old per-group schemas replaced by Field Registry + Data Dictionary + Group Field Summary.
  - Key design decisions: all derivable fields dropped (lifecycle, held_by, custodian, created_by, play_beat/beat_active, economy_role, resource_source/sink, accommodates, contains, card_source) — derivable from placement_surface + movement_path + 03-init/03b; DB-37 covers view creation.
  - Three groups with no group-specific fields: Faction Influence, Resources, Covert Messaging.
  - `max_placement` split → `max_placement_count` (Integer) + `max_placement_ref` (ID Reference) — L108 Req 1 compliance.
  - `starting_position` renamed → `init_value` (scale value at setup only; geographic init = 03-init territory).
  - Type vocabulary: Prose · Integer · Enum · ID Reference · Expr (Expr flagged XA-53 for L123 extension).
  - `placement_surface`/`movement_path` typed as Prose with defined format; normalize to junction tables in DB (DB-37).
- Art 02 §3 Entry Rubric — updated to reference Metadata block (Physical Form table row replaced).
- Art 02 §5 Playing Surface — all 10 entries populated with Metadata blocks (DB:29, 4, 102, 26, 27, 88, 28, 30, 105, 43).
- PM05: DB-37 (derived component_metadata views — 6 views flagged), XA-53 (L123 Expr extension) added.

**S92 accomplishments (mid-session clear #3 — this clear):**
- Art 02 §4.1 schema: `display_component` field added (ID Reference | Playing Surface — semicolon-separated list of component.id values with dedicated labeled areas on this surface). `privacy_model` definition updated: flat surfaces = own visibility; physical dividers (screens) = privacy of concealed space.
- Art 02 §5 Playing Surface — full sign-off review complete (all 10 entries: DB:29, 4, 102, 26, 27, 88, 28, 30, 105, 43). display_component populated; max_placement_count/ref set on all entries.
- Art 02 §6 Faction Influence — full sign-off review complete (all 7 entries: DB:1, 2, 5, 6, 7, 3, 42).
- **DF vs GR rubric established (locked):** Design Function = what the component IS (1–2 sentences, no mechanics). Gameplay Requirements = everything else (triggers, effects, limits, removal, visual constraints).
- **Design decisions locked:** DB:30 = private workspace (not public-facing); DB:1, 3, 5, 6, 7 supply origin = Arbiter Tableau (DB:30); DB:5 = neutral silver shared supply (not faction-keyed); DB:7 Chorus Node trigger = 2+ chips (not 3+); DB:6 quantity = 20 (Chorus Node excluded); DB:5 quantity formula = (factions × (districts−1)) + 1 = 101; DB:7 quantity = 21.
- Narrative anchors locked: DB:2 Deployment marker ("Whatever the doctrine requires..."); DB:5 Established marker ("They are no longer noticed because they are no longer new..."); DB:30 Arbiter Tableau ("The inside of ARBITER's awareness...").
- PM05: 02-n16 (district metadata table DB design + Art 03 stub), 02-n17 (DB:102 Broadcast Card max placement TBD), 02-n18 (Broadcast Discard/Effect Discard registration — lifecycle gate) added; 02-n14 and 02-n15 updated.
- Handoff notes: `Whiteboard/art02_review_handoff_S92.md` (full correction patterns, rubric, progress, §§7–12 component list with line numbers).

**S92 accomplishments (mid-session clear #5 — this clear):**
- Art 02 §§7–10 sign-off review first pass complete:
  - §7 Resources: DB:8 (5-path movement incl. resource trade), DB:12 (copper, corrected paths), DB:32/33 moved to §5 with Playing Surface schema, DB:44/108/48/95/96/100 corrected.
  - §8 Covert Messaging: DB:44/108/48 corrected; DB:95/96/100/101 moved out; global "ARBITER Resolution Workspace" → "Arbiter Tableau (DB:30) — resolution workspace subzone" replacement applied.
  - §9 Intel & Information: DB:9/10 states/lifecycle/paths corrected; DB:95/96/100 added (recorded_fields schema); DB:48 recorded_fields corrected; DB:101 removed.
  - §10 Card Systems: restructured into subgroups + §10.1 Card Containers.
    - §10 main: **Operative** (DB:17, 15, 99, 97) → **Operations Resolution** (DB:13, 14, 11, 52) → **Broadcasts** (DB:25, 98).
    - §10.1 Card Containers: Faction Hand (DB:94) / Covert Operation (DB:92, 93) / Political Act (DB:90, 91) / Broadcast (DB:86, 87, 109, 110) / Modifier (DB:53/54/55, 89).
  - DB:109 (Broadcast Discard) + DB:110 (Broadcast Effect Discard) registered by agy; added to §10.1.
  - DB:101 (SCIFRecord) de-registered by agy; 02-n11 updated (DB step complete; cascade + Art 04 section still pending).
  - 02-n18 closed; 02-n19 added (resource exchange verification in Art 03).
  - DF vs GR pass applied to all §§7–10 entries.
- §10 review by Andy in Grip: pending (next after clear).

**S92 accomplishments (post-clear #6 — this clear):**
- Art 02 §§11–12 sign-off review complete (Resolution Tools + Tracking Systems).
  - DB:103 VM-xx, DB:104 BM-xx — movement paths corrected (AT → resolution workspace → DB:105 → AT); GR expanded.
  - DB:47 Modifier token — denominations 5/10/15; obverse positive (green) / reverse negative (red); static once placed; two placement paths (DB:105 covert / DB:88 PA).
  - DB:106/107 threshold sliders — 0–100 in increments of 5 (20 ticks); crit zones 1–5 (green) / 96–00 (red); set to base threshold then adjusted per Art 03 §13.5.
  - DB:50 Chorus Portrait track — single physical strip with 5 parallel faction-keyed tracks; behind ARBITER screen (not face-down).
  - DB:36 renamed Escalation marker (DB-38 cascade to DB + downstream pending).
  - DB:23 Session Timeline — restructured to 8Q × 3M (24 positions total).
  - DB:38 Faction order marker — physical form = Structure Block clone, faction-colored.
  - All markers ARBITER-managed except: PS (ARBITER or acting faction player), Status marker (faction player only).
- **Art 02 v2.0 signed off — L210.** Conditional on PM05: 00-16, 02-n10, 02-n11, 02-n12, 02-n13, DB-38.
- PM02 L210 locked. PM03 Art 02 status updated.

**S95 accomplishments:**
- 04-n70 fix pass ✅ — all 8 categories complete. Schema violations: C39/C23 `faction=None→All`; C36/C42/C38/C41 `affinity=None` (faction names were invalid); P05 `threshold=35`; P13 threshold dynamic; C16 `resolution=Automatic`. Missing persistence triples: 9 cards (Ghost stubs: Station/Full Take/SCIF/Flip/Signals Analysis; C37; LandTitle; HostileTakeover; AccordTransfer). Spec/checklist: C09 dup removed, C19 checklist corrected, C41 arbiter_note faction corrected, Directorate nav fixes (RegulatoryDowngrade/Freeze moved covert→PA index). Notation: C37 `public_standing→standing`, Overture `perspectives={}`. Structural: C41/P15 ElectPlayer effects moved from comments to structured `on_accept`/`on_decline`. EntryExitControls `persistence_effect` added (condition was correct, effect was absent). P16 DividendMarker `world_condition()` formalized.
- §6.1 Card class: `on_accept: MutationExpr | None` + `on_decline: MutationExpr | None` fields added (ElectPlayer outcome_type only; None on all other cards). §6.2 Data Dictionary updated.
- Design decisions (S95): (1) minimize/eliminate arbiter_notes — prefer structured spec fields; (2) PortraitEntry `failcrit=` is invalid — valid params only: `flat/submitter/where/modifier/mod_where`; (3) on_accept/on_decline as schema elements for ElectPlayer; (4) persistence model: Permanent cards use `persistence_condition`/`persistence_effect`; Seasonal cards with timed effects use `world_condition()` in `success` — different mechanisms for different durations, not in conflict.
- PM05: 04-n70 ✅ S95, 04-n98 added (on_accept/on_decline sweep — add `None` to all non-ElectPlayer cards).

**S94 accomplishments (pre-clear #3 — this clear):**
- 02-n11 (step 3) ✅ — Art 04 §12a Debrief Action Cards written. DA-xx identifier convention established; DA-01 SCIFRecord fields and Debrief procedure written. SCIF card checklist updated: Taxonomy fit and Supported by components updated (SR-xx → DA-01, registrations confirmed); Supported by game procedure → ✓ (Art 03 §11 present since S68); arbiter_note updated; Outstanding Issues reduced to balance playtest flag; Issues Resolved ✓ S94. PM05 02-n11 ✅ S94.

**S94 accomplishments (pre-clear #2 — this clear):**
- 02-n13 ✅ — Status marker (DB:49) Narrative Anchor corrected: `N/A — mechanical readiness indicator; no in-world narrative element.` (Art 03 is procedure, not narrative context; no Art 00 grounding warranted.)
- 03-n21 ✅ — Dispatch Token row added to 03-init §2.1: ×20 / Backlog / 4 per faction (Art 02 §7, Art 03 §21 authoritative). Note: PM05 stated 16 (Ghost:4; others:3 each) — stale; corrected in PM05.
- 02-n11 (step 2) ✅ — SR-xx cascade: stale `SR-xx subtype` parenthetical removed from Art 02 Arbiter Tableau (DB:30) Gameplay Requirements. Only outstanding: action (3) add Debrief Action Cards section to Art 04 (material).
- DB-31 (artifact sweep) ✅ — 00b: no tmp_component refs; XA-43/44 PM05 descriptions updated (tmp_component → `component` table; tmp_comp_verb_role/beat → comp_verb_phase); Art 04 A-04-05 assessment note updated. DB-side audit assigned to agy.
- SESSION_BRIEF: DB-38 corrected (was ✅ S92; stale in current focus list).

**S94 accomplishments (pre-clear #1):**
- PM05 sweep scan: identified 04-n30, 04-n31, 04-n78, 04-n69, NP1-01, 04-n35 as unsupervised candidates.
- NP1-01 ✅: threshold field already uses bare integers; resolved by Python spec redesign. PM05 closed.
- 04-n30 ✅ + 04-n31 ✅ + 04-n78 ✅ + 04-n69 ✅: Art 04 4-sweep via `tools/art04_sweep.py`. 7623 → 8142 lines (+519). 61 persistence pairs added; 79 Card Story blocks inserted (3 already present untouched); 79 Data schema validation rows added; 81 Card narrative rows added. PM05 all four closed.
- 04-n35 left as-is: correctly blocked — faction variant design pass, not a schema field issue.
- Remaining automated: 03-n21 (Dispatch Token in 03-init §2.1), DB-31 artifact side (tmp_component → component in 00b §4 + PM05).
- S94 design items still pending: 02-n11, 02-n12, 02-n13.

**S93 entry point:** ✅ S93 complete.

**S93 accomplishments (pre-clear):**
- agy S92 report ingested: DB-32/33/38/S92-01/02/03 all ✅ in PM02/PM03/PM05.
- Whiteboard migration: `~/Projects/Whiteboard/` → `~/Projects/TheSignal/Whiteboard/`; stale refs updated (PM05 04-55, Art 04 §6).
- 00-16 ✅: Art 00 v1.7 signed off (L211). §8.1 tensions list → prose. Unblocks Art 02 anchor sign-offs DB:27/88/28/30.

**S93 accomplishments (02-n10 complete):**
- 02-n10 ✅: Art 02 §§5–12 — 13 imprecise `→ Art 00 for full narrative` pointers tightened with specific section numbers: DB:32→§7, DB:6→§14.2, DB:7→§14.2, Structure block→§14.3, DB:8→§7, DB:12→§14.5 (was §14), DB:9→§14.9, DB:10→§8.1, DB:21→§6.6, DB:50→§9.6, DB:24→§9, DB:23→§8, DB:31→§9.6. PM02 Change Log updated (non-material). PM05 02-n25 added (District tile + Situation Report imprecise pointers — section uncertain). Whiteboard/02n10_progress_S93.md deleted.

**S65 accomplishments:** 04-n25 PS-as-cost ✅ and pre_loss_calc ✅ closed. Art 04 §6.2 cost field redefined (fungible resources only). Art 04 §6.6 added (Expression Parameters — pre_loss_calc). C37 Sacrifice redesigned v1.1 (cost=None; target_faction required; success=ps−2+IntelToken). C34 Golden Parachute redesigned v2.0 (bribe mechanic; variable cost; retained resources). Art 03 v3.1 signed off (L185) — Beat 0 Retained validation; Beat 2 Golden Parachute procedure; Beat 3 partial payment marker source. XA-38 closed (anchor link sweep — 38 links fixed across 11 artifacts). Network PS recovery/negation modifier card added to modifier_card_ideas.md.

**S66 accomplishments:** 04-n25 ✅ closed. Entry/Exit Controls redesigned v2.0 (district target; permanent placement block; `persistence_condition`). Art 03 v3.2 signed off (L186). Art 04 §6.6 removed. `persistence_condition` added to §6.1/§6.2. New PM05: 04-n29 (counter-card design + Art 03 persistence monitoring), 04-n30 (persistence_condition sweep).

**S67 accomplishments:**
- 04-n26 started: Cluster A in progress (SCIF complete; Land Title, Parasitic, Regulatory Downgrade complete)
- SCIF card: spec cleaned — `success = SCIFRecord(target=faction(target))`, tagline fixed (in-fiction), design_note doctrine-only, arbiter_note flagged ⚠ outstanding (04-n27), `target_district/target_object = None`. SR-xx registered in 00b §4 concept (agy task).
- pool_copies sweep: **04-40 ✅** — 42 code-block instances + 7 prose references removed from Art 04; Pool copies row removed from design_reference.md.
- PM05 additions: XA-45 (merge Art 02a + 02b → Art 02), DB-31 (update tmp_component refs → `component` table).
- IS-xx (Intel Delivery Slip): used by C17 Intercept (success) and C28 Open Channel (redirect scope). Art 03 §11 has one covering sentence; detailed steps not yet written (migration pending, overlaps 04-n27).
- Land Title redesigned v2.0 ✅: Territory/Add/StructureBlock; success = Grant Deed delivered to Syndicate case; no board marker; restriction = district.structure_count == 0. Grant Deed = new tripwire React component (SCIF-pattern, ARBITER tableau). Grant Deed sketch in gap_card_sketches_S62.md. Outstanding: Grant Deed component registration (04-n26), tripwire react window in Art 03 (04-n27).
- Parasitic redesigned v2.0 ✅: Positional wager. Beat 2 checks Beat 3 queue; Intel keyed to first card's submitter (resolution order). No component.
- **00-R40 locked (L187):** ARBITER Cognitive Load governing rule. Art 00a (44 rules, pending re-sign-off) + Art 03 §5 P6 + Art 04 §5 P18. design_reference.md + memory updated.
- Regulatory Downgrade redesigned v2.0 ✅: CovertOperation → PublicAct (permanent). Card-as-condition (success=None). persistence_effect = resource gen −1 tier. Clears: target pays 2 native to Reservoir any time after Beat 4. No TierPenaltyMarker.
- Art 04 §6.1/§6.2: `persistence_effect` field added to schema (S67). PM05 04-n31 added (sweep).
- Regulatory Freeze redesigned v2.0 ✅: PublicAct, card-as-condition (no TierFreezeMarker), self-policing enforcement per 00-R40a. Issues Resolved ✓. Pending sign-off.
- Standing Injunction redesigned v2.0 ✅: PublicAct, card-as-condition (no InjunctionMarker), Permanent with dual clearing (trigger OR Phase 21), target_taxonomy field introduced (§6.1/§6.2), Accords excluded, no operational restriction. Dispatch Token consumed on trigger per 00-R35. Issues Resolved ✓. Pending sign-off.
- Art 04 §6.1/§6.2: target_taxonomy field added to schema (S67).
- 00a: R06a added (corollary to R06 — board states committed on resolution; countering requires forward action).
- 00a: R40a added (corollary to R40 — factions police their own permanent effects; ARBITER adjudicates on call). R40 relocated from §9 to §3. Rule count: 44 → 46. Pending re-sign-off.

**S68 accomplishments (pre-compact):** 04-n26 Cluster B complete — C19 Deep Cover v1.1 (R40 fix; IntelToken physical target only), C23 Tort Interference v2.0 (Standard; any faction; Accord lock until game end or breach), C26 Leak v1.1 (pre-execution cancellation; highest-cost target; cross-resource cost 1 Exposure + 1 Findings). Cross-resource cost design principle established and locked to PM05 04-n34c. PM05 04-n34 split into 04-n34a/b/c. PM05 01-n01, 02-n01 added (zone/component design review items).

**S68 accomplishments (post-compact):** C18 Dossier Breach v1.1 — redesigned to SIGINT tap / DispatchReport model (Beat 2 submission; ARBITER delivers DispatchReport from Beat 0 grid data at beat3_pre_resolution). C28 Open Channel — retired to L2 (cross-beat ARBITER state required; R40 + cognitive efficiency violations; PM05 04-n40). C24 Surveillance Placement — mechanics invalidated; narrative-first rethink required (PM05 04-n41; gate for all covert intelligence card redesign). **Governing Principle — ARBITER Cognitive Efficiency** added to 00a §1 (parent of R40 and R40a — objective, not just rule; design question: "how can this narrative function be implemented while impacting ARBITER as lightly as possible?"). Resolution grid confirmed entirely covert — factions never see it; return deliveries only valid L1 intercept targets. NS-xx defined in 00b §4. IS-xx reinstated with tighter definition (R40 misdiagnosis corrected). DR-xx (DispatchReport) registered in 00b §4. PM05 04-n38–04-n41 added. C17 redesign flagged (PM05 04-n39).

**S68 accomplishments (S68+):** 04-n41 gap assessment complete — L1 scan confirmed no new execution problems beyond C17/C24/C28/C18; Beat 0 = payment validation only; Beat 1 = SitRep only; Beat 2 = first resolution opportunity. C24 Surveillance Placement redesigned v2.0 (Beat 2 episodic model; IntelDeliverySlip delivery; no board marker — R06 prohibits covert markers; op type only, no faction; 04-n42/43/44/45/46 added). DR-xx (DispatchReport) collapsed into IS-xx (IntelDeliverySlip) — IS-xx expanded to cover Beat 2/3, column reads (C18) and row reads (C24). C18 Dossier Breach updated v1.2 (subject=IntelDeliverySlip; delivery at Beat 2 resolution). PM03: 04b marked pending re-sign-off (S64 material addition missed). Art 04 v0.9.32. Session startup memory added (boot must be proactive + include summary).

**S68 accomplishments (session close):** 04-n27 substantially resolved — Art 03 §19 Debrief Actions step added (DebriefActionCard type; SCIFRecord first subtype); §25 Modifier React Card Rules updated to cross-reference §28; §28 React Card Rules added (interrupt model; fires on visible board state change only; first-to-announce pauses play; ARBITER decides tiebreakers). Art 03 v3.3 signed off (L189). 04-n39 substantially closed — IS-xx reinstatement confirmed; Art 03 migration concern closed; C17 "silent" PS language removed; beat timing correction flagged (04-n49). Art 04 SCIF card spec updated: DebriefActionCard (type) / SCIFRecord (subtype). PM05 04-n47 (no-branching design constraint), 04-n48 (card redesign batch: C31/C40/C41/C42/Signals Analysis), 04-n49 (C17 beat timing correction) added. 04-n27 sub-items all resolved or delegated.

**S69 accomplishments:** 04-n28 substantially complete. Art 06 §5 reworked (Accords-are-public; player-verified compliance; R40a does not apply). Art 06 §9 Accord governance overhauled and signed off (L191): §9.1–§9.10 — Accord form (mad-libs structured contract), terms, formation (Beat 4 submission; Debrief execution window; all Accord blanks as Beat 4 resolution outcomes), compliance monitoring, breach (form → ARBITER area; Portrait −4 breacher only), completion (Portrait +1/Quarter + +2 on completion), dissolution (Debrief only; no Portrait), Portrait scale (L190 — pending playtesting + modeling), manipulation types (Lock/Alter/Transfer). §6/7/8/10/11/12 stub-flagged non-canonical. Art 06 v0.2. C-S3 outstanding issue added (ARBITER record → physical Accord form). Art 04 §11.7 Outcome addition effect type added. Art 04 §11.8 Overture stub: Instant modifier / outcome addition / Beat 4 / delivers blank Accord form / from ARBITER tableau via C09 success / full spec pending §11 redesign. C09 Fund references updated (AccordCard → Overture). L190/L191 locked.

**S70 accomplishments:** Startup fix — dynamic mtime comparison command added to feedback_agy_context_check.md (prevents hardcoded timestamp false positives). C17 Intercept v1.1: beat=3 → beat=2; checklist/issues/code updated; 04-n49 ✅ closed; pending re-sign-off (04-n50). PM05: 04-n50 through 04-n67 added — set-level card milestone tracking for 6 sets (Standard + 5 factions), each with 3 items: design pass complete / issues resolved / sign-off pass; 04-n50 updated to gate on 04-n54 + 04-n55. 04-n48 substantially complete — all five cards written with outstanding issues: Signals Analysis (BLOCKED — Art 06.x Classified Directive procedure required); C31 Leveraged Acquisition v1.1 (timing=Upkeep removed; Immediate at Beat 3); C40 Weaponized Transparency retired/split → Card A Reputational Strike (React stub) + Card B Forced Disclosure (PA stub); C41 Corporate Blackmail v1.1 split → Card A spec (Capital coercion) + Card B stub (Accord Leverage, deferred); C42 Sanctioned Raid (block-bypass Art 03 rule deferred; issues clarified).

**S71 accomplishments:** C31 v1.4 — redesigned (2:1 cost, restriction=None, boost field added, Issues Resolved ✓). C40A (Reputational Strike) stub moved to §11.8. C41A Corporate Blackmail v2.0 — ElectPlayer covert choice redesign; target_district added; comply/resist model. C41B Accord Leverage v1.0 — modifier card spec (Instant; Accord draft restriction; Lock manipulation). C42 Sanctioned Raid v2.0 — block-bypass removed; modifier card clearing on success; variable threshold (75−10n); Beat 0 declared count mechanism flagged (04-n71). Art 04 §5: "Data schema validation" added as 14th checklist row (04-n68 ✅). Art 04 §6.1/§6.2/§6.3: `boost: BoostExpr | None` first-class schema field added; 04-34/04-36 superseded. PM05: 04-n69–04-n72 added; 00a-xx → 00a-72 (UNBLOCKED — Art 03 v3.3 cleared gate S68). PM05 full review and prioritization conducted. Signals Analysis still BLOCKED (Art 06.x). C40B and C42 per-token cost open.

**S72 accomplishments (partial — context limit, pending Andy grip review):** 00a full structural review complete. 00a v0.5 draft written — material restructure. Rule count 46 → 30. New §3 (Design Principles for this Artifact) and §4 (Foundational Design Principles) added. Former §7 card design constraints flagged for Art 04 migration. §8 and §9 dissolved — content moved to Foundational Design, Art 03, or redistributed into remaining sections. Rules reorganized into parent→corollary structure throughout. Appendix B migration map written (old ID → new ID sweep guide). 00a-72 status: draft complete, pending Andy review in grip → sign-off → L193.

**S73 accomplishments:** PM05 additions complete: 00a-73, 00a-74, XA-46, XA-47, XA-48 added. PM02 D02a-03 updated (00a §5 migration note on resolution; stale R05 ref → R40b). 00a §1 "What This Document Is Not" rewritten (three categories: §3 design principles / §4 foundational premises / §5–§10 governing rules). 00a §3 fully reordered (logical argument sequence); principles scoped to this document; "Time Convention" → "Copy Design Principle — In-Game Terms in Narrative Fields." 00a §3.1 created — all canonical definitions migrated from PM04 (temporal, component/system, physical forms, faction resources, influence levels); hardcoded values replaced with source artifact references. Art 03 §4 temporal framing removed, pointer to 00a §3.1 added. PM04 §1 collapsed to pointer; Purpose updated; §2 stale refs cleaned. L192 locked (source of truth migration — 00a §3.1 canonical for game definitions). L150 amended (Month 3 "political act phase" retired; all months carry both modes; "Provisional" flag retired). PM05 PM04-06 added (PM04 §2 review). §4 Foundational Design Pillars restructured — 8 numbered pillars (4.1–4.8) with lettered corollaries; subsections: Core Design Pillars (4.1–4.6b), ARBITER Design Principles (4.7–4.7b), Guaranteed Effects (4.8–4.8d). Art 00 §5 design principles (6 pillars) migrated to 00a 4.1–4.6; Art 00 §5 vacated with pointer. Rule numbering changed to section-prefixed n.n format across §5–§10. §5–§10 headers include "Rules." §8 renamed "Footprint Rules"; §3.1 Footprint definition row added. §8 precision edits: 8.2 Mechanics (Absent sentence removed — 8.2b owns it); 8.3 Rule simplified; 8.3a header/rule/mechanics precision fix (displaced markers are repositioned, not simply removed). §9: "upkeep income" clarification; 9.1b added (card/action resources ≠ income). §10: 10.1 Lock B (Reveal effect = stake not compulsion); 10.1a cross-ref 4.7a/4.7b; 10.3 header/rule/mechanics updated (limits + expiry). PM05: 00a-13 (7.3b revision), 00a-14 (Source/Governs audit). 31 rules. 00a v0.6 signed off — **L193**.

**S74 accomplishments:** Art 00 v1.6 signed off (L194) — §5 Art 00 design principles added (5 principles: Derivability, Sustained Ambiguity, World over Mechanics, Attributable Perspective, Narrative Frame); all subsections numbered throughout (§1.1–§14.9). 00a v0.7 signed off (L196) — §3 renamed "Design Principles for This Document" + scope routing note; §4 scope line added; §4.6 amended with Narrative Origin Principle: Art 00 as sole canonical narrative source (L195). Art 01 v2.0 signed off (L197) — Component Physical Forms column → "Proposed Form"; 01-10 (table → Art 02a, add Design Requirements column) and 01-11 (scope overhaul: §8→03-init, §11/§12→downstream) flagged. PM05: 00-15 (Art 00 full narrative revision per §5 P1+P5), 01-10, 01-11, 00a-75 added.

**S75 accomplishments:** XA-47 ✅ — Art 04 §5 P19–P25 added (R21–R28 migrated from former 00a §7); P5 updated (authoritative R26 constraint note); P6 cross-ref to P19; checklist rows updated (Effect duration → P6/P19; Portrait validity → +P22); Art 04 v0.9.34. XA-48 ✅ — Art 07 §9 already had four-register content; `00a R02` source ref removed. XA-46 ✅ — ~120 rule ID substitutions across 11 files (Art 03, Art 04, Art 07, 02a, 02b, PM03, design_reference.md, gap_card_sketches, 3 memory files); zero `00-R` strings remain; PM02 + SESSION_BRIEF preserved as historical records; `00-R29` → `Design Pillar [04-n6 pending]` throughout. PM05: 04-n73 (P1–P18 restatement audit) + XA-49 (design_reference.md reset) added.

**S76 accomplishments:** XA-49 ✅ — design_reference.md rebuilt as master index + sub-reference system. Old monolithic file replaced with: `design_reference.md` (master, ~1K words), `design_reference_card_system.md` (card schema/rules/flags, ~2.5K words), and 9 `ref_*.md` sub-refs (world/narrative, design pillars, components, board narrative, resources, tracking, procedures, card types, taxonomy). All populated from 9 parallel agent reads of Art 00, 00a, 00b, 01, 02a, 02b, 03, 04§1-6, 04b. Session open = master + card system (~3.5K tokens); sub-refs loaded on demand. Sub-refs treated as living documents — update in place when recurring gaps found.

**S77 accomplishments:** 04-n28 ✅ — Overture full spec written to Art 04 §11.8 (Modifier/Instant/All; outcome addition; ARBITER delivers blank AccordForm at Beat 4; faction drafts and places at discretion; no timing constraint; cross-Quarter). §11.7 Outcome addition formalized. Art 06 §9.4 materially revised and re-signed off (L198): blank AccordForm delivery model; faction drafts at discretion; form placed in Accord Placement Area anytime after drafting; cross-Quarter persistence; physical alterations and execution Debrief-only; verbal discussion anytime. P08, P10, C09, Overture all updated to blank AccordForm model; AccordOffer marker concept removed throughout. PM05 04-n74 added (Accord initiation cost/value review — C09/P08/P10).

**S78 accomplishments:** C28 v2.0 "Breaking News" (Network L1 FactionSpecific CovertOp; Beat 2 d100 threshold 50; Exposure×2; forces ARBITER to publicly reveal target faction's first Beat 3 queue entry + places VM-xx Visibility Marker on that grid card — physical reminder; no cross-beat cognitive state). VM-xx: new ARBITER-held token registered via PM05 04-n76. C40B v1.0 "Live Coverage" (Network PA FactionSpecific; Beat 4 d100 threshold 50; Exposure×2; Seasonal; target faction elects each Phase A: comply = hand face-up, ops proceed; resist = dispatch disabled that Month; comply once → card clears). Art 04 §5 P26 locked L199 — Card Narrative Test (every card expressible as 1–2 sentence narrative story; if not, design problem). Card Story block added to Art 04 §5 and card spec structure (between Design Rationale and Design Checklist; 1–3 sentences of plain-language event narrative). 15th checklist row added. PM05: 04-n40 updated (design complete S78); 04-n75–04-n80 added (Beat 2 d100 procedure, VM-xx registration, Phase A comply/resist procedure, Card Story structural sweep, content pass, Andy review). Memory + design_reference_card_system.md updated (S78).

**S79 accomplishments:** C42 v2.2 — boost model replaces per-token n-declaration. Base cost = faction×1 + native×1 + IntelToken (Mandate×2 removed); boost = same unit; threshold = 65−10×n_boost; PS scales with (1+n) in both directions; successcrit = PS+(1+n_boost) (public endorsement); fail = NotificationSlip; failcrit = Discovery + PS−(1+n_boost); modifier scope = target faction only. Whiteboard `boost_marker_draft_S79.md` created (BM-xx draft language + Art 03 procedure sketches). PM05 additions: 04-n81 (BM-xx registration), 04-n82 (Beat 0 boost procedure), 04-n83 (Beat 2/3 BM-xx resolution), 04-n84 (Discovery mechanic definition), 06-n01 (Accord term vocab + PS mechanic redesign — gating 04-n74).

**S80 accomplishments:** 06-n01 ✅ — Art 06 §9.3 clause vocabulary written (5 types: Prohibition-Territorial, Prohibition-Operational Marker, Prohibition-PA, Obligation-Resource Transfer, Obligation-Presence; covert ops excluded). §9.4 PS formation mechanic redesigned (execution = all parties +1 PS; decline = non-party table vote on reasonableness — majority reasonable: declining faction −1 PS; majority unreasonable: proposing faction −1 PS). Art 06 §9 pending re-sign-off (Andy working remotely; no grip access). PM05 additions: 04-n85 (covert add-for-opponent concept, superseded by 04-n86), 04-n86 (C01/C03 generalization — build for any faction via submitted resource color). 04-n74 unblocked.

**S81 accomplishments:** SESSION_BRIEF corrected (S78→S81; S79/S80 accomplishments reconstructed from artifacts). 04-n74 ✅ (L200, L201) — Accord initiation cost calibrated: P08 → 1 native flat (affinity removed; PA slot is the primary gate; 3 slots/Quarter, draw-dependent); P10 → 1 Capacity + 2 native delivered to target (form price equitable with P08; 2 native = sweetener enabling income clause); C09 → unchanged at 2 Capital (Overture is success bonus; effective Accord route costs 2 of 4 action slots). 04-n75 ✅ — Art 03 Beat 2 d100 resolution block added (after Automatic cards; queue order; 8-step procedure; additive crits per ref_procedures.md). 04-n76 ✅ — VM-xx registered in 00b §4; Art 03 Beat 3 Step 1 item 4 added (VM-xx present → public resolution: announce before Step 2, visible roll at Step 5, announce result at Step 6, remove at Step 8). Art 03 and 00b re-sign-offs pending (grip required). Art 06 §9 re-sign-off still pending (grip required — S80 material additions). PM05 04-n74/75/76 all ✅.

**S82 accomplishments:** PM05 split — 144 completed items archived to `PM05___Archive.md`; 2 all-done sections removed. Active PM05 now 559 lines / 251 open items. 04-n81 ✅ — BM-xx (BoostMarker) registered in 00b §4 (token marked "Boost"; VM-xx supply-size over-spec also removed). 04-n82 ✅ — Beat 0 Boost Detection procedure added to Art 03 (after Intel Token Freshness; floor division; no refunds). 04-n83 ✅ — BM-xx resolution added to Art 03 Beat 3: Step 3 threshold modifier clause; Step 7 all-effects multiply (1+n) / single NS-xx regardless of n; Step 8 BM-xx cleanup. 04-n84 ✅ — Discovery mechanic defined as public reveal (ARBITER announces acting faction + op name + declared target to all players); Step 7b rewritten (ARBITER applies); Step 7b.i rewritten (faction player applies own board changes as directed). 04-n77 ✅ — "Active PA Obligations" general procedure written; Start of Month 1/2/3 blocks added to §9/§12/§15 (generalizable; cross-Quarter compatible). Art 03 v3.4 additions complete — pending grip bundle re-sign-off.

**S83 accomplishments (pre-clear):** 04-n47 ✅ — P27 (single determinate outcome per resolution tier — success/successcrit/fail/failcrit each must specify exactly one outcome; no branching in any tier; successcrit/failcrit are additive not alternative) added to Art 04 §5; 16th checklist row "Outcome determinacy" added; Design Pass count updated to 16. PM05: 04-n87–92 added (set-level play and doctrine review, one per set — Standard/Ghost/Directorate/Network/Syndicate/Guild; gates on issues resolved for that set; each gates corresponding sign-off pass). 04-n50/53/58/61/64/67 gates updated to include doctrine review items. Session entry point corrected: card sign-offs gate on §5 stability — removed C28/C40B from S83 menu.

**S83 accomplishments (post-clear):** 00b ✅ signed off — restructured as Analysis Readiness (v0.3, L204); L108 standard migrated to 00a §11 (00a v0.8 signed off, L204). 00b filename renamed 00b___Data_Architecture.md → 00b___Analysis_Readiness.md; README + PM03 + 03a updated. L202 locked — crit is a boolean flag on RO-xx, not a standalone outcome type (§4.2.a). L203 locked — Contested is a boolean flag on IL-xx, not IL-04 (§4.3.a). 00b editorial pass: BM-xx placement timing corrected (after card situated in grid); RO Physical Component column removed; IS-xx/VM-xx/BM-xx procedural language trimmed (procedure → Art 03 §11); CA-xx L2+ note added; §3 updated to 3NF; PS-xx flagged ⭐ ready to model. PM02: L202, L203, L204. Art 03 v3.4 sign-off deferred — Beat 2 overhaul (03-n01) scheduled as separate session first.

**S83 accomplishments (Art 06 sign-off):** Art 06 §9 signed off (L205, v0.4). Index anchors fixed for python-markdown shim. §9.2 form: underscore blanks → em dashes (rendering fix), ACCORD DISSOLVED row added, parenthetical placeholders italicized. §9.3 Duration clause vocabulary added (6th type). §9.5 board state as sole compliance basis added. §9.10 Transfer collapsed into Alter as Named Party subtype (four alteration types); Lock last sentence removed; notification language removed from Alter and Transfer.

**S83 accomplishments (post-clear #3):** Art 03 structural overhaul v4.0 — structural sign-off S83 (full sign-off pending fine-tuning). §§12–16 deleted (unified into §9 monthly procedure). Beat 2/3 Step 0 restructured to "Identify Operation" (0.0 Apex, 0.1 VM-xx, 0.2 Base Difficulty); VM-xx conditional privacy model (covert ops fully private by default). Beat 4 (§9.4.4) full procedure written (Faction Player actor; Steps 0–5; Intel Token freshness check; Apex at 0.1; board state validation at 0.3). §9.4.5 Close Month (transient cleanup; month advance; Month 3 → §10). §10 Resolve District Tension (was §17): PS mechanic — opposing faction moves PS marker on resolution; losing faction moves winning faction's PS −1 on resolution; winning faction moves losing faction's PS −1 on press; tie: each faction moves other's PS −1. §11 Quarterly Debrief (was §19): §11.3.0.1 Annual Report (Q4 only). §12 Quarter Close (separated from §11): §12.1 Findings Decay honor system (L2 enforcement deferred); §12.3 NS-xx faction hand → ARBITER pool; §12.4 M1/Q+1 advance. Reference sections renumbered §21–28 → §13–19 (§25 merged into §18.1; §18 React Rules before §19 Examples). ToC and §6 Quarter Overview updated (Beat 0–5 sub-entries + anchor links). Whiteboard/art03_section_map_S83.md created (old→new section map for external sweep). PM05: 03-n02 (Beat 2 modifier stack scope), 03-n03 (OR card component sweep) added.

**S84/S85 accomplishments:** Art 03 rubric pass — entry/exit conditions added to all 17 §6 sections. §7 entry: Q1 = 03-init complete; Q2–Q8 = §12.4 Quarter Close complete. §9.4 container entry/exit removed. §7.2.x terminology sweep: Event Card → Broadcast Effect Card; Event Zone → Situation Report Zone; session deck → Broadcast Deck. §9.4.0 restructured steps 0–6 (CM in Beat 1 row; packet handling; payment validation; drain; grid placement; dispatch token model; repeat). CM model: submitted CMs placed in Beat 1 row at Beat 0; apply to all grid ops targeting keyed faction at Beat 1. §9.4.1 restructured — §9.4.1.0 Standing Board Effects (clockwise from ARBITER's left), §9.4.1.1 Broadcast Effect Cards (silent), §9.4.1.2 CM Cards. Situation Report two-card model confirmed: Broadcast Card (public, Situation Report Zone) + Broadcast Effect Card (hidden, ARBITER Tableau). Multiple Situation Reports active simultaneously. Component naming: Broadcast Card/Deck/Broadcast Effect Card/Deck adopted; DB updated (ids 25/86/87 renamed; id=98 inserted). "target slip" → "Target Profile" throughout Art 03 (9 instances). 03-init §2.8/§3.9 updated; v0.3. Art 03 v4.2 at close. PM05: 03-n10 ✅, DB-18 ✅, 03-n07/DB-17 updated, 00a-n01 added.

**S87 accomplishments:** Art 03 rubric and simplification pass complete. §5 P7 added (Step 0 convention — all procedural sequences begin at Step 0). §§9.4.2.6.1.0/1.1 added (Target Profile return + process case contents after dispatch case return). §9.4.3.4 item 5 added (Target Profile cleanup at Beat 4). §§11–12 restructured: §11.0–§11.4 (Debrief); §12.0–§12.4 (Quarter Close). §13 Operation System: modifier table rebuilt (M-06/M-07 merged, M-09 generalized, M-10 terminology, M-11 scope all/both beats); §13.6 Intel Token Age table (Fresh/Stale/Expired). §14 renamed Apex Activation (flat Steps 0–4, entry condition, beat names removed). §§15–17 rubric clean. §18 React Card Rules restructured (§18.0–§18.3; timing window at §18.0.1). §19 Reserved. §20–21 new reference sections (Resource Generation; Card Economy). §§9.4.2.6 and 9.4.3.4 hardcoded values replaced with table refs. § Examples & Exceptions (unnumbered end section): Initiative example updated (ref §7/Art 07); Dispatch Case Return rewritten + flagged (PM05 03-n15); Findings Decay unchanged. PM05: 03-n14–03-n18, XA-50–52 active. Grip review complete. Art 03 v4.3. Full sign-off pending PM05 03-n18 (component lifecycle sweep).

**S88 accomplishments:** Art 03 v4.4 signed off (L207). Component lifecycle sweep complete; 03b Component Lifecycle Register formalized (v0.1) — replaces Whiteboard scratch file. All sign-off blockers resolved in-place: §13.7 Board State Update Rules added (Tension marker placement trigger; Structure block removal + return; Dominant/Established marker return); Target Profile added to 03-init §2.7 (count TBD); Control flag renamed Dominant marker throughout Art 03 and 03-init (S88 design decision: same component); return-to-supply language added §7.3.3 and §8.2; BM-xx "from ARBITER supply" clarified §9.4.0.1; §12.0 BEC cleanup scope clarified. PM05: 03-n18 ✅, 03-n19 ✅, 03-n20 ✅, DB-14 updated, 03-n16 §2.7 gap closed. PM02 L207 locked. art03_section_map_S83.md stale entries corrected (5 fixes + 3 new sections added). Art 02 Components v1.0 written — merge of 02a v1.6 + 02b v1.5; 02a and 02b superseded; XA-45 ✅; PM05 02-n02 added (deep review before sign-off). Art 02 §5 Design Principles: 2 principles only (Scarcity is intentional; Disclosure is designed, not assumed). agy S88 DB report integrated: DB-14 renames ✅, DB-15 (Operative card split) ✅, DB-34 (DebriefActionCard + SCIFRecord) ✅. PM03 v2.5.

**S88 accomplishments (session close / S89):** External artifact sweep complete across all 6 artifacts (00a, 03a, 04, PM01, PM05, and Art 02 cross-ref cleanup). All Art 02a/02b/02x refs updated to Art 02 throughout. All stale Art 03 section numbers updated: old §11→§9.4.x, §17→§10, §18 (Battlefield)→§10, §19→§11, §22→§14, §14 (Modifier)→§13, §25/§28→§18. C01 and C03 "Supported by game procedure" checklists: stale `Automatic resolution (§20)` ref removed; PM05 04-n95 added (controlled vocabulary for checklist procedure field). art03_section_map_S83.md deleted.

**S89 accomplishments:** C28 Breaking News — Issues Resolved ✓ S89 (04-n75 ✅ S81, 04-n76 ✅ S81/82 confirmed; taxonomy subject soft flag; sign-off pending set-level gates). C40B Live Coverage — Issues Resolved ✓ S89 (04-n77 found in Art 03 §9.0 — missed sweep ref; checklist corrected). Art 02 §13 comprehensive stub pass — 44 new rows across 7 categories covering all 104 DB-registered components. DB completeness sweep (agy S89): id=88 → Faction Resolution Grid, id=102 Situation Report, id=103 VM-xx, id=104 BM-xx, id=22 retired, id=50 renamed "Chorus Portrait track"; all 27 views verified. 03-init alignment: Situation Report Zone → Situation Report component (§2.1); stale DB-14/DB-15 notes cleaned (§2.7/§2.8); VM-xx/BM-xx added to §2.8; Floor Act PA noted with constraints (standard PA, starts in hand, no discard — PM05 04-n96). Art 02 §9 pass card text removed. PM05 additions: DB-35/36 ✅, 02-n03, 02-n04 ✅, 03-n21, 03-n22 ✅, 04-n96.

**S90 accomplishments (continued):** Art 02 v2.0 — full scope rewrite complete. New scope: component enumeration (design function + physical requirements + gameplay requirements per component). DB `component` table is canonical completeness anchor; all 63 registered components covered. Out of scope stripped to correct homes: procedures → 03, starting positions → 03-init, rules → 00a. Orphaned rules content (9 items) parked in Whiteboard/art02_orphaned_content.md pending Art 03 migration (PM05 02-n08). L208 locked: Art 02 does not mirror DB schema flags (actionable/receivable/transformable). Dispatch token corrected to 4 per faction (20 total) — Art 03 §21 authoritative. PM05: 02-n08 added (Art 03 orphan migration, material — Art 03 re-sign-off required); 00a-n03 added ("Scarcity is intentional" design principle → 00a).

**S90 accomplishments:** 02-n03 ✅ — Art 02 restructuring complete. (1) Art 02 §4: 8 component narrative subsections added (District Tiles, Influence Level Marker, Tension Markers, Session Timeline, Initiative Strip, Chorus Activity Track, Accord Documents, Situation Reports — migrated verbatim from Art 01 §4; flagged as Art 00 migration candidates, PM05 02-n06; "Integration" flagged for PM04 registration, PM05 02-n07). (2) Art 02 §13: Physical Forms subsection added (migrated from Art 01 §6; 4 stale rows dropped — Pass card, Operational marker, Status marker, Operation Resolution card; Situation Report row reconciled to Broadcast Card + Broadcast Effect Card; Dispatch Token ref Art 02a §8a → Art 02 §9). (3) Art 01 v2.1: §4 condensed to pointer, §6 Physical Forms replaced with redirect stub, all stale Art 02a/02b/Art 01 §4 refs updated → Art 02 §4; status flagged for re-sign-off (PM05 02-n05). (4) Art 02a and 02b files moved to Retired/Paper/ — 02a namespace free. PM03 v2.6 (dependency tree updated: 01 → 02 → 03); README updated. Art 02 v1.1.

**S90 accomplishments (continued — S90 day 2):** Art 02 §§5-14 → §§5-12 restructured: 8-group taxonomy finalized (Playing Surface · Faction Influence · Resources · Covert Messaging System · Intel & Information · Card Systems · Resolution Tools · Tracking Systems). All entries converted to new schema: Design Function + Narrative Anchor (always present; N/A with justification if no content) + Gameplay Requirements + Physical Form table (Physical Form · Quantity labeled gameplay req vs. pre-production estimate · Visibility). Card Systems §10: 6 bold subgroups (Covert Operations · Countermeasures · Political Acts · Broadcasts · Classified Directives · Modifier); Faction hand + Sealed Apex ability ungrouped at top. Status marker moved to §12 ungrouped; Design Function corrected to quarter-end discussion state (active / ready). DB:105/106/107 enumerated in §5 (ARBITER CRG) and §11 (threshold sliders). Dispatch Packet DB:108 added to §8 Covert Messaging System (03-n06 steps 1+5 ✅); Dispatch case entry updated. PM05 housekeeping: DB-30 ✅ (Floor Act = PA card; Voided Resolution Card not needed), 03-n13 ✅ (Faction Resolution Grid already registered + enumerated). Art 02 now 68 components (all DB-registered), ready for 02-n02 sign-off review.

**S91 accomplishments:** Art 02 02-n02 sign-off pass — §5 full rubric pass: 8 narrative anchor corrections; Art 00 §8.1 + §9.6 material additions (PM02 L209); DB:29/26/27/88/28/30 anchors written; DB:105 ARBITER CRG scope discipline fix; DB:43 Human Player full rewrite; DB:4 District tile anchor corrected (resource generation framing + lead sentence restored). §§6–12 rubric pass complete: scope discipline sweep — all "Full design: Art 03" and "Full design: Art 00b" cross-refs removed throughout (Art 03 = procedure only; Art 00b = DB punch list, not design spec); DB:108 Dispatch Packet procedural sentences trimmed; DB:47 Modifier token Design Function written (threshold modification accumulator — holds modifier value on target operation while generating card exits queue); DB:48 Target Profile target district field added; DB:44/108 active anchors → Art 00 §14.5; DB:100 DebriefActionCard active anchor → Art 00 §9.6; DB:17 Classified Directives active anchor → Art 00 §14.7; Dispatch token / Backlog reordered (narrative-first). New PM05: 00-16 (Art 00 v1.7 re-sign-off — gates §5 anchor sign-offs for DB:27/88/28/30), 02-n10 (11 imprecise Art 00 section pointers across §§6–12), 02-n11 (SCIFRecord de-registration + cascade update), 02-n12 (Emergency Response card design TBD), 02-n13 (Status marker Art 00 narrative evaluation).

**S91 entry point:** ✅ S92 in progress — see S92 entry point above.

**Also pending:** 04-n40 (C28 sign-off — set-level gates); 04-n44/45/46 (IS-xx Art 03/00b updates — gate: C24 sign-off); 04-n71 (Art 03 Beat 0 boost procedure); 04-n72 (Art 03 covert ElectPlayer procedure); 04-n69/70 (schema sweep); 03-n21 (Dispatch Token in 03-init); Standing Injunction 5 open flags; agy DB-S63-01/02/03 check-in; 04b re-sign-off; 04-n73 (P1–P18 restatement audit).

---

## 04-n26 Component Analysis — Full Cluster Map
*Captured S67 mid-session. Read this before any n26 work.*

**Governing principle (Andy S67):** Walk each card individually — components are not automatically needed. Ask whether the card can be reworked to avoid a new component before committing to registration. Only SCIF Record (SR-xx) confirmed as new component so far.

### Cluster A — Process-blocked (new game procedures required)

| Component | Card | Status | Direction |
|-----------|------|--------|-----------|
| SCIFRecord (SR-xx) | Ghost SCIF | ✅ Component confirmed — 00b §4 registration (agy). Art 03 Debrief procedure outstanding (04-n27). | ARBITER slip, not board marker |
| GrantDeed | Syndicate Land Title | ✅ Spec written — registration pending | New component (SCIF-pattern). Blank card in ARBITER tableau; filled + dispatched to Syndicate case at Beat 3. Fields: `district \| owner`. Tracks under 04-n26. |
| ParasiticMarker | Syndicate Parasitic | ✅ No component needed | Positional wager redesigned v2.0. Beat 2 checks Beat 3 queue; Intel keyed to first card's submitter. No marker, no deferred effect. Decision S67. |
| TierPenaltyMarker | Directorate Regulatory Downgrade | ✅ No component needed | Redesigned v2.0 as Permanent PublicAct. Card-on-board IS the condition. Clearing: target pays 2 native to Reservoir. S67. |
| TierFreezeMarker | Directorate Regulatory Freeze | ✅ No component needed | Redesigned v2.0 as Permanent PublicAct. Card-on-board IS the condition. S67. |
| InjunctionMarker | Directorate Standing Injunction | ✅ No component needed | Redesigned v2.0 as Seasonal PublicAct. Card-on-board IS the condition. target_taxonomy field introduced. Art 03 void procedure outstanding (04-n27). S67. |

### Cluster B — Information-state objects (private reveal + visibility)

*Andy S67: Many of these may be taxonomy labels, not physical components. Walk each card before committing to registration.*

| Component | Card | Key Question |
|-----------|------|-------------|
| CardHandContents | C18 Dossier Breach | Is this a physical component or a taxonomy subject label? Ghost reads hand — no physical object changes hands. |
| ActionAttribution | C19 Deep Cover, C26 Leak | Concept of "who did the action" — is this a component or a record in ARBITER's ledger? |
| ClassifiedDirective | Ghost Signals Analysis | IS a physical component — the faction's secret objective card. Likely already registered or easily registered. |
| WrittenRecord | C23 Evidence Preservation | Locks an existing record (Intel token, Accord). May not need separate registration — acts on existing components. |
| PrivateCommunications | C28 Open Channel | Scope undefined: which ARBITER-to-faction comms qualify? Intel Delivery Slips and Notification Slips confirmed in scope. |

### Cluster C — Taxonomy mismatch

| Component | Card | Fix |
|-----------|------|-----|
| SurveillanceDevice | C24 Surveillance Placement | `subject = IntelToken` is wrong — primary effect is surveillance infrastructure. Needs `subject = SurveillanceDevice` once a SurveillanceDevice component is defined. Design SurveillanceDevice before fixing subject field. |

### Standing Injunction open flags (under 04-n26)
1. Restriction wording: "Directorate Established+ in any district where target also has Established+" — confirm intent vs. original "same ring as primary operations"
2. InjunctionMarker: component registration
3. PA type declaration: by card name or by taxonomy (e.g., Territory/Add)?
4. Art 03 gap: Phase B procedure for voiding a declared PA not specified
5. Accord overlap: does PA block apply to Accord-type PAs (P08/P10)?

**ALWAYS read `TheSignal/Whiteboard/design_reference.md` before any Art 04+ design work.**
**ALSO read `TheSignal/Whiteboard/gap_card_sketches_S62.md` before any Art 04 gap card work.

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.7 | 🔄 Needs Re-Sign-Off — S99: §14.10 Integration added (material — new narrative anchor). Prior: ✅ S93 (L211). Open: 00-09, 00-15, 00-16 (re-sign-off). |
| 00a — Governing Rules & Design Policy | 0.8 | ✅ Signed Off — S83. L108 standard migrated to §11; 00b restructured. Prior: S74 (L196) v0.7 — §3/§4 scope additions; Narrative Origin Principle (L195). Open: 00a-73 (7.3b revision), 00a-74 (Source/Governs audit), 00a-75 (Derivability principle), 00a-76 (Action Space Governance rule). |
| 01 — Game Board: New Meridian | 2.1 | 🔄 Needs Re-Sign-Off — S90 (02-n05). §4 component narratives migrated to Art 02 §4; §6 Physical Forms table migrated to Art 02 §13; stale refs updated; now geography/zone-only. Open: 01-11 (scope overhaul §8/§11/§12). |
| 02 — Components | 2.2 | ✅ Signed Off — S98 (L213). S97–S98: applicable_verbs seeded into all §§5–12 entries; §13 matrix removed; d10 (DB:119) added §11; ARBITER Dominance Marker Flip corrected; DB-42 seeded (74 rows). S99: DB sync header note added; 02-n07 ✅. Open PM05: 02-n17, 02-n21, 02-n22, 02-n25. |
| 02a — Resource Systems: Board State | 1.6 | ⛔ Superseded — S88 by Art 02 v1.0. Moved to Retired/Paper/ S90. |
| 03 — Quarter Structure & Gameplay | 4.8 | ✅ Signed Off — S104 (L217). §24 Resolution State Reference: three states (Succeeded/Failed/Voided); Discovered alongside Failed; RO-xx removed; targeting restriction → face-down model. Open PM05: 03a-n01 (3 residual RO-xx refs in 03a, lines 1038/1363/1370 — non-material). |
| 04b — Action Taxonomy | 1.7 | ✅ Signed Off S105 (L221). ID-04 renumber applied (all C/P IDs → [FAC].[TYPE].n). §9 Pass card entry removed. §§6/7/8 living — update as gap cards are designed. |
| 04 — Action Card System | 0.9.34 | S75: §5 P19–P25 added (card design constraints migrated from 00a §7 — effect duration types, partial payment, crit cost, portrait card property, ring modifier scope, corrupt scope, standard language). P5 updated (authoritative R26 constraint). P6 cross-ref P19. Checklist rows updated. XA-46 rule ID sweep applied. S71: C31 v1.4. C41A v2.0. C41B v1.0. C42 v2.0. §6 boost field. Signals Analysis BLOCKED (Art 06.x). C17 ⚠ re-sign-off pending (04-n50). S89: C28 Breaking News — Issues Resolved ✓ (gates 04-n75/76 cleared; sign-off pending set-level gates). C40B Live Coverage — Issues Resolved ✓ (04-n77 in Art 03 §9.0; sign-off pending set-level gates). |
| 00c — Economy Manifest | 0.4 | §8, §9 stubs only. |
| 03a — Game Engine Specification | 0.98 | Tier 4 stub remaining. XA-37 pending (strip "Layer N —" prefixes from section headings). |
| 06 — Messaging System | 0.4 | ✅ §9 Signed Off — S83 (L205). §9.3 clause vocabulary complete (6 types incl. Duration); §9.5 board state as sole compliance basis; §9.8 ACCORD DISSOLVED on form; §9.10 Transfer → Alter Named Party subtype. Open: §§1–8, 10–13 non-canonical stubs. |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure (03-11) + initial draft pending. |

Signed-off artifacts: 00 (v1.7), 00b (v0.3), 03 (v4.7), 04b (v1.6 — pending re-sign-off). 01 v2.1 needs re-sign-off (02-n05). 02 v2.2 signed off (L213). 02a + 02b superseded → Art 02; files moved to Retired/Paper/. Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **00-07** | Art 00 multicultural texture pass | ✅ S40 |
| **00a-08** | 00a v0.3 re-sign-off | ✅ S40 |
| **01-05** | Art 01 overhaul — physical zone hierarchy, all Overview children | ✅ S40 |
| **04-54** | Art 04 §5 P1–P15 signed off + C17 signed off | ✅ S49 |
| **XA-37** | Haiku sweep: rename Ln/Layer N expansion tier refs → Tier N across 00b, 00c, 03a, Art 07–11; strip "Layer N —" from 03a section headings | ✅ S49 |
| **DB-22–26** | agy S48+S50 DB fixes — upkeep primitives, Status marker, Portrait marker, SitRep/Target Profile, Move mismatch | ✅ S50 (agy) |
| **DB-27** | agy: register Emergency Response card id=97 in tmp_component + seed role/beat primitives | ✅ S50 (agy) |
| **DB-09** | Create district_adjacency table — ✅ S50 (agy). 21 districts, 104 adjacency rows seeded. | ✅ S50 |
| **DB-11** | agy ALTER TABLE component_positions — rename anchored_to_component_id → on_component_id + add on_game_zone_id | ✅ S46 (agy) |
| **03-14** | Art 03 v2.1 sign-off — Beat 3/4 outcome steps restructured (7a/7b/7b.i); L170 locked | ✅ S52 |
| **01-07** | Art 01 §4 Narrative Function — remove (content in §3 + Physical Table Layout) | ✅ S41 |
| **01-08** | Art 01 narrative anchor pass — staged in Whiteboard/Art01_Narrative_Anchors_S41.md | Open — after 02a sign-off |
| **08-00** | Art 08 — define scope + create stub (Faction Player Tableau + ARBITER Tableau) | Open |
| **03-12** | Battlefield Strength trigger model | ✅ S43 — L160 |
| **04-48** | Art 03 v2.0 sign-off | ✅ S43 |
| **01-06** | Claude Design visual wireframe — table layout + mat layout | Open |
| **04b-03** | Action taxonomy audit | ✅ S46 — §4 redesigned, pending sign-off |
| **04b-04** | Art 04b §3 cleanup — update stale verb refs (Block→Flip, Redirect→Move, React reclassification); prerequisite to v1.3 sign-off | Open — S46 |
| **DB-11** | agy ALTER TABLE live_state rename | ✅ Confirmed executed agy S46 |
| **DB-14** | Decision — promote tmp_ taxonomy tables to permanent the_signal_db schema | Deferred — after 04b sign-off |
| **XA-32** | Art 07 — ARBITER ring modifier calculation guide | Open |
| **GEM-01** | Cross-reference integrity audit — assigned to Gem | Active — deploy via 3-file upload |
| **PM06-01** | Create PM06 — Lessons Learned | Deferred — next session |
| **00-09** | World Conditions panel — content undefined | Open |
| **00-10** | Faction Representative as named component — design question | Open |
| **FS-01-WBS** | Add faction screen to PM01 WBS 2 | Open |
| **04-n10** | Pentagram gap — Ghost↔Guild opposed pair has no card-level expression | Open — P-series pass |
| **04-n11** | Pentagram gap — Guild↔Network neighbor pair has no cooperative mechanic | Open — P-series pass |
| **04-n12** | Faction Terminal unique zone design direction (L183) — define per-faction named zones in Art 08 | Open — Art 08 |
| **04-n13** | Network modifier card — auto-trigger off C42 Sanctioned Raid sweep | Open — modifier card pass |
| **04-n14** | C32 Short the Market — mechanical redesign required ("applied silently" doesn't survive paper prototype; tagline/code conflict on generation vs stockpile) | Open — redesign pass |
| **04-n15** | Standard equivalents for Source Substitution, Backdate, Field Verification — hired data specialist / PI versions; higher cost or lower threshold (Principle 17) | Open — S62 |
| **04-n16** | Apply Principle 17 systematically — audit full card set for faction-native capabilities lacking outsourced standard counterparts | Open — S62 |
| **04-n17** | Gap card specs: Disinformation Campaign ✓, Standing Injunction ✓, Disprove ✓, Intel Extraction ✓, Modifier Raid ✓. Standing Injunction 5 open flags → tracks under 04-n26. | ✅ S64 |
| **04-n18** | Art 04b §5.2 refresh complete (artifact side). agy DB cascade outstanding (DB-S63-01/02/03 queued). | ✅ S63 (agy pending) |
| **04-n19** | Accord procedure design pass (Art 06) required before Group A gap cards. After 04-n27 (Art 03 gaps). | Blocked — after 04-n27 |
| **04-n20** | Directorate covert reclassification — review C21 Invoke Jurisdiction, C22 Detain, C23 Evidence Preservation, C25 Tactical Redirection, C42 Sanctioned Raid for PA reclassification | Open |
| **04-n23** | P09–P18 Voice fit gap — 20 perspectives written. Gates Issues Resolved ✓ for all P09–P18. | ✅ S63 |
| **04-n25** | CRITICAL — Art 04 §6 schema field gaps: `target_ring`, `pre_loss_calc`, PS-as-cost | Critical — S65 |
| **04-n26** | HIGH — Component interaction design pass: 12+ components needing lifecycle design before Art 02 registration | High — S65+ |
| **04-n27** | HIGH (before accord) — Art 03 procedure gaps: 6 holes blocking Issues Resolved on multiple cards | High — S65+ |
| **04-n28** | Overture full spec written (Art 04 §11.8). §11.7 Outcome addition formalized. Art 06 §9.4 re-signed off (L198). | ✅ S77 |
| **04-n40** | C28 Network replacement (Breaking News v2.0) — design complete S78. Gates: 04-n75 (Beat 2 d100 procedure) + 04-n76 (VM-xx + Beat 3 public resolution) must be resolved before sign-off. | 🟡 Design complete S78 — sign-off gates open |
| **04-n74** | Accord initiation cost/value review — C09 (2 Capital + threshold 50), P08 (2 native, Automatic), P10 (2 Capacity + 2 native, Automatic). AccordForm cross-Quarter persistence changes value proposition. | Open — S77+ |
| **04-n75** | Art 03 Beat 2 d100 procedure — C28 Breaking News is the first Beat 2 dice roll. Beat 2 resolution procedure (§11) currently handles only Automatic cards. Requires new sub-step for probabilistic resolution at Beat 2. | Open — S78 |
| **04-n76** | VM-xx component registration (Art 00b §4) + Art 03 Beat 3 Step 1 public resolution clause. VM-xx = ARBITER-held Visibility Marker; placed on Beat 3 grid card at Beat 2; flags public announcement of op name/type/targets before dice roll. | Open — S78 |
| **04-n77** | Art 03 Phase A procedure — Live Coverage comply/resist model requires Phase A sub-step: ARBITER checks active C40B obligations; target faction elects comply (hand face-up) or resist (dispatch disabled this Month). | Open — S78 |
| **04-n78** | Card narrative structural sweep — add Card Story block (between Design Rationale and Design Checklist) + 15th checklist row to ALL existing cards in Art 04. | Open — S78 |
| **04-n79** | Card narrative content pass — populate Card Story blocks for all existing cards (those receiving blocks in 04-n78). | Open — S78 |
| **04-n80** | Andy review pass — review all Card Story blocks after 04-n79 content pass. | Open — S78 |
| **XA-46** | 00a rule ID sweep — all 11 files. | ✅ S75 |
| **XA-47** | Art 04 §5 P19–P25 added (card design constraints from 00a §7). | ✅ S75 |
| **XA-48** | Art 07 §9 ARBITER Registers already had content. Source ref cleaned. | ✅ S75 |
| **XA-49** | design_reference.md reset — review before Art 04 card spec work resumes. Gate: before 04-card-spec. | Open — S76 |
| **04-n73** | Art 04 §5 P1–P18 restatement audit — identify and replace upstream duplicates. | Open — S75+ |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L221** (S105): Art 04b v1.7 signed off. ID-04 renumber complete — [FAC].[TYPE].n format applied across Art 04, Art 04b, card_ref DB, and ref files. card_id field added to Art 04 §6.1/§6.2. §9 Pass card entry removed. §§6/7/8 living sections — updated as gap cards are designed, not re-sign-off gates.
- **L220** (S104): DB script idempotency convention locked — INSERT IGNORE, portable session patches, archive/ subfolder for originals.
- **L219** (S104): Card ID schema locked — [FAC].[TYPE].n; varchar(15). 20-deck inventory. Full schema in PM02.
- **L212** (S96): Art 02 v2.1 signed off. Grant Deed (DB:113) added §9; §4.1 movement_path field definition clarified (board event trigger, not timing); 13 movement_path timing violations corrected §§5–12. Open PM05: 02-n07, 02-n17, 02-n20, 02-n21, 02-n22.
- **L210** (S92): Art 02 v2.0 signed off. §§5–12 rubric pass, metadata population, and GR validation complete across all 68 components. Conditional on PM05: 00-16, 02-n10, 02-n11, 02-n12, 02-n13, DB-38.
- **L207** (S88): Art 03 v4.4 signed off. Component lifecycle sweep complete; §13.7 Board State Update Rules added (Tension marker placement trigger; Structure block removal + return); Control flag renamed Dominant marker (same component — DB-14 = rename, not new registration); Target Profile added to 03-init §2.7; return-to-supply language (§7.3.3, §8.2); §12.0 BEC scope clarified.
- **L206** (S84): DB-registered component names are canonical source of truth for all terminology. Changes begin at DB component table, cascade through artifacts. No artifact may introduce a component name not registered in the DB.
- **L205** (S83): Art 06 §9 Accord Documents re-signed off (v0.4). §9.3 clause vocabulary complete (6 types incl. Duration); §9.4 PS formation mechanic; §9.5 board state sole compliance basis; §9.10 Transfer → Alter Named Party subtype.
- **L196** (S74): Art 00a v0.7 signed off. §3 renamed "Design Principles for This Document" + scope routing note. §4 scope line added. §4.6 amended: Art 00 as origin of all canonical narrative (L195).
- **L195** (S74): Art 00 as sole canonical narrative origin. No canonical narrative may originate in a downstream artifact. Art 00 amended first; downstream artifacts reference it. Written to 00a §4.6. Governs all V1 artifacts.
- **L185** (S65): Art 03 v3.1 signed off. Golden Parachute bribe mechanic written to Beat 0/2/3. Art 04 §6.2 cost field (fungible only). §6.6 added (pre_loss_calc). C37 Sacrifice + C34 Golden Parachute redesigned.
- **L184** (S63): L108 amended — 3NF requirements (6 + 7) added; component.transformable → virtual generated; action.prereq_beat_id dropped.
- **L183** (S61): C22 Detain — detention zone on Directorate public tableau; faction Terminals may be unique per faction doctrine.
- **L182** (S61): Art 00a v0.4 signed off. 00-R21 (4-type duration taxonomy), 00-R22 (partial payment model), 00-R29b (Missing Author Vacuum renamed from duplicate 00-R30), 00-R39 (covers covert ops + public acts). 43 rules.
- **L181** (S61): Art 03 v3.0 signed off. Beat 3 Step 12 cleaned; Beat 4 Submit Payment → Step 1, steps renumbered 1–13; section breaks added; duration taxonomy 5→4 types.

*S62 design decisions (not locked — draft pass only): PA persistence policy; Territory/Recover removed from valid taxonomy; Copy/PA no narrative value; Principle 17 (outsourced equivalents); Accord procedure prerequisite for Group A gap cards.*

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L175)

---

## Pending Sign-Offs

- **Art 00 v1.6** — ✅ Signed Off S74 (L194)
- **00a v0.7** — ✅ Signed Off S74 (L196)
- **Art 01 v2.0** — ✅ Signed Off S74 (L197)
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v4.4** — ✅ Signed Off S88 (L207)
- **Art 06 §9** — ✅ Signed Off S83 (L205)
- **Art 00 v1.7** — 🔄 Needs Re-Sign-Off S99 (§14.10 Integration added — material). Prior sign-off: L211 S93.
- **Art 02 v2.2** — ✅ Signed Off S98 (L213).
- **Art 03 v4.5** — ✅ Signed Off S101 (L214).
- **Art 03 v4.7** — ✅ Signed Off S102 (L216).
- **00b** — ⚠ S81 VM-xx + S82 BM-xx registration pending re-sign-off
- **Art 04b v1.7** — ✅ Signed Off S105 (L221)
- **C17** — ⚠ v1.1 pending re-sign-off (beat=2 correction S70 — tracked 04-n50)

---

## Key Concepts Established S39–S40 (Not Yet in All Artifacts)

- **MIRROR** = Meridian Interface for Real-time Reporting, Observation, and Recording. Holographic projection device at Chorus Node. Predates The Table and possibly ARBITER. Origin of "New Meridian" name. Written to Art 00 §8.
- **Zone vs. Component distinction** = Zones are named physical locations (infrastructure); components are portable objects placed within zones. Central Area is a zone; The Overview is the component that fills it. Established S40 — in Art 01 §6 Physical Environment.
- **district_adjacency** = bidirectional adjacency table for all 21 districts. In Art 01 §[City]. DB table needed (agy). Feeds Entry Rule A/B and Battlefield Strength (03-12).
- **component_positions** = renamed from live_state (S45). Spec in 00b §8. DB-11 queued for agy: RENAME TABLE, RENAME COLUMN anchored_to_component_id → on_component_id (nullable), ADD COLUMN on_game_zone_id.
- **Art 08** = new planned artifact for Faction Player Tableau and ARBITER Tableau physical component placement. Referenced in Art 01 §8–§9 stubs. Not yet defined.
- **Force-reveal action class** = actions compelling faction to expose Terminal contents. L154. Design direction for Art 04 card design.
- **Faction Terminal unique zones** = L183. Terminals may have named zones per faction doctrine. Directorate: public Detention zone (C22). Others TBD — develop in Art 08.

---

## Key Files

| File | Purpose |
|------|---------|
| `Session/THE_SIGNAL___Project_Save_State.md` | Full session history, complete artifact table |
| `Session/PRIVATE___True_State.md` | Read before writing ARBITER or Chorus content |
| `Whiteboard/Art01_Scope_S39.md` | Physical layout decisions from S39 — migrate to Art 01 during overhaul |
| `V1/PM02___Decision_Log___Validation_Tracker.md` | All locked decisions |
| `V1/PM03___Master_Artifact_Index.md` | Authoritative sign-off status, dependency map |
| `V1/PM05___Active_Punch_List.md` | Full punch list |
| `gem_task.md` | Active Gem task — edit this to assign new work; script copies to Desktop |

---

## Terminology

| Use | Not |
|-----|-----|
| Quarter | Round |
| The Overview | Game mat / board |
| MIRROR | (device name — use in narrative context) |
| Terminal | Faction tableau / personal board |
| Presence token | Influence token |
| Deployment marker / Operational marker | Claim marker |
| Public Standing track | Popularity track |
| Covert operation | Private action |
| Public act | Political act / Public action |
| Situation report | World event card |
| The Mid | Infrastructure ring |
| Baryo | Sprawl |
| The Backlog | Reservoir (for Dispatch Tokens) |
| Session Timeline | Round Tracker / Quarter Tracker |

ARBITER: always all-caps. All other game terms: Title Case.

**Four Registers** (Art 00 §9, Art 07 §9): The Record · The Observation · The Reckoning · The Witness

---

## Standing Methodology (Established S39)

**Foundational-first:** Foundational artifacts must be complete and signed off before downstream work proceeds. Gaps in upstream documentation propagate as inconsistencies throughout the artifact tree. Dependency order is the work order: 00 → 00a → 01 → 02a → 03 → 04.

---

---


*Updated S39 Phase 1 close. Sources of truth: PM03 (artifacts), PM02 (decisions), PM05 (punch list).*
