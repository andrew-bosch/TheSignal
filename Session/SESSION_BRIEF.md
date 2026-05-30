# THE SIGNAL — Session Brief
**Session 51 (close) | Updated: 2026-05-29**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

S51 complete. DB infrastructure: `Database/db_create_tmp_tables.sql`, `db_seed_lookups.sql`, `db_rebuild.sh`, `register_component.py`, `component_template.yaml` — all new. `schema_reference.md` updated: views 29→27 (dropped v_object_from, v_validact, v_verb; added v_primitive_actual_coverage), DB-09 status corrected, row counts updated.

Art 04 S51: C18 → **Dossier Breach** (Information — Reveal — Card hand contents); C25 → **Tactical Redirection** (Territory — Move — Presence token); C27 → **Disclosure Loop** (Economy — Add — Exposure). Full schema pass C01–C35: Ring 0–3 modifier fields added to all cards; C13 resolution type corrected (Transactional→Probabilistic); C22/C32/C33 resolution fields corrected (Dice→d100). Card index updated. Unused design candidates (Ghost/Directorate/Network rejected alternates + Gem S51 concepts) → `Whiteboard/card_ideas_S51.md`.

**Next session:** C03–C35 retrofit to Python object notation (§6 class format). Card ID hybrid field decision (04-55) before any P-type cards assigned IDs. Then P01–P18 development.

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.5 | ✅ Signed Off — S40. Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a — Governing Rules & Design Policy | 0.3 | ✅ Signed Off — S40. |
| 01 — Game Board: New Meridian | 1.9 | ✅ Signed Off — S44. S44: §4 Narrative Function, §6 Physical Environment renamed, §7–§12 renumbered, all cross-refs resolved, procedure clutter removed (01-08 ✅). Open: §9/§10 Tableau stubs (Art 08); district_adjacency DB (DB-09); DB-11 (agy DDL — component_positions rename + columns). |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Quarter Structure & Gameplay | 2.1 | ✅ Signed Off — S52. Beat 3/4 outcome steps restructured (7a/7b/7b.i). L170 locked. 03-15 open: generalize when Art 07/08 developed. |
| 04b — Action Taxonomy | 1.5 | ✅ Signed Off — S48. §9 removed; §10 → §9 (Standalone Card Types). React collapsed into Modifier cards. Emergency Response penultimate context added. |
| 04 — Action Card System | 0.9.21 | §5 P1–P15 + C17 signed off ✅ S49. S51: C18/C25/C27 replaced; full schema pass C01–C35 (Ring 0–3 fields, C17 canonical format). **Next: P01–P18 development.** |
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
| **DB-11** | agy ALTER TABLE component_positions — rename anchored_to_component_id → on_component_id + add on_game_zone_id | Open — unblocked |
| **03-14** | Art 03 v2.0 re-sign-off — Beat 3 Steps 7/8 extended S50 (material change) | Open — pending |
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

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L171** (S52): Full program architecture — six artifact sections. Governing Constraints (00, 00a) — narrative IS the primary design constraint, not a category alongside it; Design Pillar 6 is the enforcement mechanism. Logical Data Model (00b, 00c). Imports (01, 02a/b). Main() (03-init, 03, 03a). Stored Procedures (04–08, 10a). Documentation (09, 10, 11). Formal equivalence: artifacts = source code; DB = runtime; physical components = I/O; ARBITER = interpreter. New artifact 03-init created (setup_state / game init). Extends L170.
- **L170** (S52): Artifact architecture = program design. Art 01 = Zone; Art 02 = Component; Art 03 = Loop; Art 07 = ARBITER subroutines; Art 08 = Faction Player subroutines; Art 04 = Actions. Art 03 owns sequence only — role execution detail migrates to 07/08 as those artifacts are developed. PM05 03-15.
- **L169** (S52): Component taxonomy schema redesign — `tmp_component` gains `parent_component_id` (self-referential); "Card" becomes parent node with card types as children, outcome subtypes as grandchildren. Two new dim tables: `tmp_component_dim` (description), `component_type` (classification). Advances DB-14. Queued as DB-32 for agy.
- **L168** (S48): Expansion/perception stages renamed Tier N. Canonical: Tier 1 Physical, Tier 2 Social, Tier 3 Wireless/Communications, Tier 4 Web/Data, Tier 5 Chorus. Tier 5 public name only — technical nature intentionally undefined. XA-37 queued.
- **L167** (S48): Six-layer card design system locked — Territory / Economy / Information / Submission / Resolution / Standing. "Layer" is the canonical taxonomy term. Cross-Category retired.
- **L166** (S47): Action taxonomy = possibility space; Art 03 = legal space. Gaps are procedure coverage signals — permit / prohibit / defer. The two artifacts co-evolve iteratively.
- **L164** (S43): The Dossier — ARBITER's hidden Intel Token storage (behind screen, not public Reservoir).

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L168)

---

## Pending Sign-Offs

- **Art 00 v1.5** — ✅ Signed Off S40
- **00a v0.3** — ✅ Signed Off S40
- **Art 01 v1.9** — ✅ Signed Off S44
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v2.0** — ✅ Signed Off S43
- **C17** — ✅ Signed Off S49

---

## Key Concepts Established S39–S40 (Not Yet in All Artifacts)

- **MIRROR** = Meridian Interface for Real-time Reporting, Observation, and Recording. Holographic projection device at Chorus Node. Predates The Table and possibly ARBITER. Origin of "New Meridian" name. Written to Art 00 §8.
- **Zone vs. Component distinction** = Zones are named physical locations (infrastructure); components are portable objects placed within zones. Central Area is a zone; The Overview is the component that fills it. Established S40 — in Art 01 §6 Physical Environment.
- **district_adjacency** = bidirectional adjacency table for all 21 districts. In Art 01 §[City]. DB table needed (agy). Feeds Entry Rule A/B and Battlefield Strength (03-12).
- **component_positions** = renamed from live_state (S45). Spec in 00b §8. DB-11 queued for agy: RENAME TABLE, RENAME COLUMN anchored_to_component_id → on_component_id (nullable), ADD COLUMN on_game_zone_id.
- **Art 08** = new planned artifact for Faction Player Tableau and ARBITER Tableau physical component placement. Referenced in Art 01 §8–§9 stubs. Not yet defined.
- **Force-reveal action class** = actions compelling faction to expose Terminal contents. L154. Design direction for Art 04 card design.

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
| Political act | Public action |
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
