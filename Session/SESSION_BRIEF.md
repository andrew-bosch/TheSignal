# THE SIGNAL — Session Brief
**Session 62 (close) | Updated: 2026-06-02**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

S61: Art 03 v3.0 ✅ signed off (L181). Art 00a v0.4 ✅ signed off (L182). XA-40 (Art 04 PA→Public Act sweep) ✅ and XA-42 (design_reference.md L180 sweep) ✅ complete. XA-41 deferred.

§5a Narrative Anchor section added; Faction Goals reordered (Anchor first, Goals below); Ghost goal corrected (Delay — no premature answer to the Chorus); playstyle summaries reformatted to bullet lists. L183: C22 Detain locked — detention zone on Directorate public tableau; faction Terminals may be unique per faction doctrine. C22 card spec updated (move to Detention zone, PS/NotificationSlip removed). C42 Sanctioned Raid updated: Mandate×2 (was ×1), PS −1 on success added. C32 Short the Market flagged for mechanical redesign (04-n14 — "applied silently" doesn't survive paper prototype). 04-n13 (Network modifier card responding to C42 sweep) added.

Key S61 changes to Art 03: Beat 3 Step 12 "(Month 3 only)" label and flavor line removed; Beat 4 Submit Payment promoted to Step 1 (steps renumbered 1–13, repeated initiative order header removed); Gameplay Procedure and Reference Material section breaks added in index and body. Duration taxonomy: 5→4 types (Tripwire collapsed into Permanent).

Key S61 changes to Art 00a: 00-R21 updated to 4-type taxonomy; 00-R22 rewritten (partial payment model); 00-R29b (Missing Author Vacuum, renamed from duplicate 00-R30); 00-R39 revised to cover both covert ops and public acts. 43 rules.

**ALWAYS read `TheSignal/Whiteboard/design_reference.md` before any Art 04+ design work.**
**ALSO read `TheSignal/Whiteboard/gap_card_sketches_S62.md` before any Art 04 gap card work.**

**Next session:** P-series sign-off pass (P01–P18); write full specs for Disprove / Disinformation Campaign / Standing Injunction / Asset Extraction (sketches in Whiteboard); Directorate covert reclassification (C21–C24, C42); Art 04b §5.2 update (P-series entries stale); Outstanding Issues C13/C15/C16; C32 redesign (04-n14).

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.6 | ✅ Signed Off — S57. Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a — Governing Rules & Design Policy | 0.4 | ✅ Signed Off — S61 (L182). 00-R21 (4-type taxonomy), 00-R22 (partial payment), 00-R29b (Author Vacuum), 00-R39 (covert+public). 43 rules. |
| 01 — Game Board: New Meridian | 1.9 | ✅ Signed Off — S44. S44: §4 Narrative Function, §6 Physical Environment renamed, §7–§12 renumbered, all cross-refs resolved, procedure clutter removed (01-08 ✅). Open: §9/§10 Tableau stubs (Art 08); district_adjacency DB (DB-09); DB-11 (agy DDL — component_positions rename + columns). |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Quarter Structure & Gameplay | 3.0 | ✅ Signed Off — S61 (L181). Beat 3 Step 12 cleaned; Beat 4 steps renumbered 1–13; section breaks added. |
| 04b — Action Taxonomy | 1.5 | ✅ Signed Off — S48. S55: §4.2/§4.4 updated (Economy narrowed; IntelToken = Information), §5.2 table updated (C05, C24 → Information). 04-63 flagged (stale C27 §4.6 entry). |
| 04 — Action Card System | 0.9.25 | S62: P01–P18 full specs (Draft S62 — not signed off). Schema: `persistence` field added. Principle 17 added. Ghost: Source Substitution, Backdate, Field Verification specs added. Coverage analysis complete. Gap card sketches in Whiteboard. **Next: P-series sign-off pass; Disprove/Disinformation Campaign/Standing Injunction/Asset Extraction full specs; Directorate covert reclassification; 04-n10/11/13/14.** |
| 00c — Economy Manifest | 0.4 | §8, §9 stubs only. |
| 03a — Game Engine Specification | 0.98 | Tier 4 stub remaining. XA-37 pending (strip "Layer N —" prefixes from section headings). |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure (03-11) + initial draft pending. |

Signed-off artifacts: 00b (v0.2), 01 (v1.9), 02b (v1.5), 03 (v2.0), 04b (v1.2 — 04b-03 audit pending). Authoritative: PM03.

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
| **04-n17** | Write full specs: Disprove, Disinformation Campaign, Standing Injunction, Asset Extraction (sketches in Whiteboard/gap_card_sketches_S62.md) | Open — S62 |
| **04-n18** | Art 04b §5.2 update — refresh P01–P18 entries (all stale placeholders); add Source Substitution / Backdate / Field Verification; taxonomy corrections (P11 = Submission/Modify, P07 = Standing/Shift, P16 = Economy/Add) | Open — S62 |
| **04-n19** | Accord procedure design pass (Art 06) required before Group A gap cards: Economy/Remove/Accord, Economy/Redirect/Accord (C-S3), Information/Corrupt/Accord | Blocked — Art 06 |
| **04-n20** | Directorate covert reclassification — review C21 Invoke Jurisdiction, C22 Detain, C23 Evidence Preservation, C25 Tactical Redirection, C42 Sanctioned Raid for PA reclassification | Open — next session |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L183** (S61): C22 Detain — detention zone on Directorate public tableau; faction Terminals may be unique per faction doctrine.
- **L182** (S61): Art 00a v0.4 signed off. 00-R21 (4-type duration taxonomy), 00-R22 (partial payment model), 00-R29b (Missing Author Vacuum renamed from duplicate 00-R30), 00-R39 (covers covert ops + public acts). 43 rules.
- **L181** (S61): Art 03 v3.0 signed off. Beat 3 Step 12 cleaned; Beat 4 Submit Payment → Step 1, steps renumbered 1–13; section breaks added; duration taxonomy 5→4 types.

*S62 design decisions (not locked — draft pass only): PA persistence policy; Territory/Recover removed from valid taxonomy; Copy/PA no narrative value; Principle 17 (outsourced equivalents); Accord procedure prerequisite for Group A gap cards.*

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L175)

---

## Pending Sign-Offs

- **Art 00 v1.6** — ✅ Signed Off S57
- **00a v0.4** — ✅ Signed Off S61 (L182)
- **Art 01 v1.9** — ✅ Signed Off S44
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v3.0** — ✅ Signed Off S61 (L181).
- **C17** — ✅ Signed Off S49

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
