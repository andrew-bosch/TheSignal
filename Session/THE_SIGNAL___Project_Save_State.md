# THE SIGNAL — Project Save State
## Complete Context Document for Session Handoff

**Last Updated:** 2026-06-01

### Generated: 2026-05-31 (session 55 complete) — supersedes session 53 save state.

Read this document top to bottom before doing any design work in a new session. It is intended to give a fresh session full project context with no prior knowledge required.

---

## Session Log

### Session 57 — 2026-06-01
**Focus:** DB-14 Phase B confirmation; Art 00 §7 redesign + re-sign-off v1.6; Art 00a 00-R30 (Missing Author Vacuum); True State §1/§3/§4/§10 updates; Art 04 P16 added (portrait entries submitter-bounded); C01–C10 full 5-faction portrait sweep; C01/C02/C03/C04/C05/C06/C07/C08/C10 signed off; C09 portrait + dependency cleanup; C10 −45 affinity locked (L179). Ghost faction mechanics concept noted for playstyle summary.
**Decisions locked:** L177 (Missing Author Vacuum governing rule), L178 (P16 portrait submitter-bounded), L179 (C10 −45 affinity narratively justified).
**Artifacts updated:** Art 00 (v1.6, signed off S57), Art 00a (00-R30 added, re-sign-off pending), True State (§1/§3/§4/§10), Art 04 (v0.9.23, C01–C10 portrait sweep, C01/C02/C03/C04/C05/C06/C07/C08/C10 signed off).
**Next:** S58 — faction playstyle summary (blocking C11), Outstanding Issues (C13/C15/C16/C17), C11–C35 design rationale.

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

**Next session:** Resolve C01–C17 Outstanding Issues (C09 Art06 dep, C10 −45 threshold, C11 §11 procedure gap, C13 Ring 0, C15 per-Quarter cap, C16 copied op cost + prediction procedure, C17 Art 03 migration). Art 00 §7 doctrine text additions (00-13, 00-14). Then C18–C35 design rationale.

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
