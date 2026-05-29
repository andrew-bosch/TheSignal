# THE SIGNAL — Session Brief
**Session 47 | Updated: 2026-05-28**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

Session 47: Action taxonomy formalized into DB primitive model. New tables: tmp_player_role, tmp_role_phase, tmp_beat (20 beats), tmp_comp_verb_beat, tmp_comp_verb_role, tmp_action, tmp_trigger_type (10 types), tmp_state_condition, tmp_state_condition_clause. 213 primitives in tmp_action. New components: Status marker (49), Portrait track (50), Portrait marker (51). Verb Invoke (17) added for C16 meta-action. Gap analysis: v_unlegislated_primitives (60 rows) + v_unlegislated_by_trigger (14 rows — all Faction-initiated). **L166 locked:** taxonomy = possibility space; Art 03 = legal space; gaps = procedure coverage signals. Art 04b restructured: §3 physical action layer first, §4 card design layer (former §3), §5 column definitions + Status column + Primitive Verb column. agy punch list A–H queued (GEMINI_CONTEXT.md). Gem tasks queued (gem_web_context.md Bucket A). **Next: agy/Gem analysis; Art 04b v1.4 sign-off (04b-09); C17 sign-off; DB-18/19/20 legalization decisions; continue §5 gap analysis triage.**

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.5 | ✅ Signed Off — S40. Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a — Governing Rules & Design Policy | 0.3 | ✅ Signed Off — S40. |
| 01 — Game Board: New Meridian | 1.9 | ✅ Signed Off — S44. S44: §4 Narrative Function, §6 Physical Environment renamed, §7–§12 renumbered, all cross-refs resolved, procedure clutter removed (01-08 ✅). Open: §9/§10 Tableau stubs (Art 08); district_adjacency DB (DB-09); DB-11 (agy DDL — component_positions rename + columns). |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Quarter Structure & Gameplay | 2.0 | ✅ Signed Off — S43. |
| 04b — Action Taxonomy | 1.4 | Re-sign-off required (material: §3.3 DB model, §4 card design layer, §5 col defs + status). Source: tmp_action + gap views in the_signal_db. |
| 04 — Action Card System | 0.9.20 | C17 sign-off (after 04b sign-off); C36–C42 Intel economy cards; React card reclassification pending. |
| 00c — Economy Manifest | 0.4 | §8, §9 stubs only. |
| 03a — Game Engine Specification | 0.98 | Layer 4 stub remaining. |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure (03-11) + initial draft pending. |

Signed-off artifacts: 00b (v0.2), 01 (v1.9), 02b (v1.5), 03 (v2.0), 04b (v1.2 — 04b-03 audit pending). Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **00-07** | Art 00 multicultural texture pass | ✅ S40 |
| **00a-08** | 00a v0.3 re-sign-off | ✅ S40 |
| **01-05** | Art 01 overhaul — physical zone hierarchy, all Overview children | ✅ S40 |
| **DB-11** | agy ALTER TABLE live_state — rename anchored_to_component_id → on_component_id (nullable) + add on_game_zone_id | Open — unblocked S45 |
| **DB-09** | Create district_adjacency table (agy) — seed from Art 01 adjacency map | Open — Art 01 signed off |
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

- **L166** (S47): Action taxonomy = possibility space; Art 03 = legal space. Gaps are procedure coverage signals — permit / prohibit / defer. The two artifacts co-evolve iteratively.
- **L165** (S43): Portrait track dual function — narrative register + Apex pentagram geometry.
- **L164** (S43): The Dossier — ARBITER's hidden Intel Token storage (behind screen, not public Reservoir).

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L166)

---

## Pending Sign-Offs

- **Art 00 v1.5** — ✅ Signed Off S40
- **00a v0.3** — ✅ Signed Off S40
- **Art 01 v1.9** — ✅ Signed Off S44
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v2.0** — ✅ Signed Off S43
- **04b v1.4** — re-sign-off required (material additions S47)
- **C17** — after 04b sign-off

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
