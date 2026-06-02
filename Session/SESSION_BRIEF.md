# THE SIGNAL — Session Brief
**Session 60 (close) | Updated: 2026-06-01**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

S60: Art 03 v3.0 full review pass — all S60 corrections applied. L180 architecture (monthly A/B/C/D structure, Public Act rename, dispatch token parity) fully reflected in document. **Art 03 v3.0 sign-off (03-17) pending — must happen before 00a 00-R39 revision, XA-40 (Art 04 PA→Public Act sweep), XA-41 (Art 03a schema rename), XA-42 (design_reference.md L180 sweep) can proceed.**

Key S60 changes to Art 03: all factions = 4 Dispatch Tokens; face-down = void (no Voided Resolution Card component); Phase C/D labels removed; Beat 2 renamed "Conditions Set"; §17 = Contested District Resolution; §18 = Month 3 Quarter Notes; §20 = End of Quarter; §21 = Operation System; Beat 3 Step 12 = Dispatch Case Return (Month 3); Beat 4 Step 2 = board state validation; Pass cards removed; Contested/Failed TBD blocks removed.

**ALWAYS read `TheSignal/Whiteboard/design_reference.md` before any Art 04+ design work.**

**Next session:** 03-17 sign-off (Art 03 v3.0) → then 00a-xx (00-R39 revision) → then Art 04 work resumes (04-n8, Directorate+Syndicate sanity checks, P-series PA pass, Outstanding Issues C13/C15/C16/C17).

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.6 | ✅ Signed Off — S57. Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a — Governing Rules & Design Policy | 0.3 | ✅ Signed Off — S40. S57: 00-R30 added (Missing Author Vacuum) — material change, re-sign-off pending. |
| 01 — Game Board: New Meridian | 1.9 | ✅ Signed Off — S44. S44: §4 Narrative Function, §6 Physical Environment renamed, §7–§12 renumbered, all cross-refs resolved, procedure clutter removed (01-08 ✅). Open: §9/§10 Tableau stubs (Art 08); district_adjacency DB (DB-09); DB-11 (agy DDL — component_positions rename + columns). |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Quarter Structure & Gameplay | 3.0 | 🔄 In Progress S60 — L180 full revision applied. **03-17 sign-off required.** Blocks: 00a-xx (00-R39 rev), XA-40, XA-41, XA-42. |
| 04b — Action Taxonomy | 1.5 | ✅ Signed Off — S48. S55: §4.2/§4.4 updated (Economy narrowed; IntelToken = Information), §5.2 table updated (C05, C24 → Information). 04-63 flagged (stale C27 §4.6 entry). |
| 04 — Action Card System | 0.9.24 | S59: All C01–C42 baseline drafted. Scaffold on C18–C35. C36–C42 migrated. New faction cards (Ghost/Guild/Directorate/Syndicate gaps). Entry/Exit Controls (§10). **Next: Directorate+Syndicate sanity checks; Art 02 component registration (6 new); P-series PA pass; Outstanding Issues (C13/C15/C16/C17).** |
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

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

*S60: No new L-decisions. Art 03 review execution session — all pre-planned changes applied.*

- **L179** (S57): C10 Protect affinity −45 locked. Guild/Directorate near-nullification of C02 Demolish (50→5%) narratively justified: Guild knows their own infrastructure intimately; Directorate has institutional security apparatus. Attacker doesn't see protection coming (C10 is covert). Base −25 for other factions (50→25%) remains.
- **L178** (S57): P16 — Portrait entries are submitter-bounded. A portrait entry may only affect the portrait of the faction that submitted the card. ARBITER evaluates the acting faction's doctrinal alignment — not the reactions of factions that did not act.
- **L177** (S57): Missing Author Vacuum as governing rule. No faction can author the Chorus response content — structural gap in doctrinal geometry is permanent and deliberate. Governs all card flavor, Chronicle entries, faction perspectives. See Art 00a 00-R30; True State §1.

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L175)

---

## Pending Sign-Offs

- **Art 00 v1.6** — ✅ Signed Off S57
- **00a v0.3** — ✅ Signed Off S40 · S57 material change (00-R30) — re-sign-off pending
- **Art 01 v1.9** — ✅ Signed Off S44
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v3.0** — 🔄 In Progress S60 — re-sign-off required (03-17). Blocks 00a-xx, XA-40/41/42.
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
