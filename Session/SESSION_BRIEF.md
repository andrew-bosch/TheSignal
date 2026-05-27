# THE SIGNAL — Session Brief
**Session 42 | Updated: 2026-05-27**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

Session 42: Gem consulting integration + terminology decisions. **02a v1.6 signed off** (02a-10 ✅). S42 changes to 02a: §8a Narrative Anchor subheader; Art 01 Supply stub resolved; "Quarter" sweep; Baryo/The Mid ring names; Deployment marker consistency; "Round 1" → "Quarter 1". **Three locked decisions:** L157 (Presence chip canonical), L158 (Intel Token canonical — physical form is token, not paper slip), L159 ("Quarter" locked globally, "Round" retired). **Terminology sweeps applied:** 02a, 02b (Intel Tokens throughout), 00a (Intel Tokens; Dispatch Case; Quarter sweep; §9 renamed "Quarter & Timing"), 01 (Tension marker — was Contested marker), PM04 (canonical terms updated), PM02 (L157–L159 logged), PM05 (XA-33, 00a-09 added). **Next: Art 03 v1.9 re-sign-off (04-48 + XA-33 bundled).**

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.5 | ✅ Signed Off — S40. Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a — Governing Rules & Design Policy | 0.3 | ✅ Signed Off — S40. |
| 01 — Game Board: New Meridian | 1.8 | ✅ Signed Off — S40. §4 removed S41 (01-07 ✅). Open: §8/§9 Tableau stubs (Art 07 + Art 08); narrative anchor pass (01-08); district_adjacency DB table (agy); live_state → L156 + 00b. |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Round Structure & Gameplay | 1.9 | ⚠️ Pending Re-Sign-Off. Flags: §3 "Eight rounds" → "Eight Quarters" (fix not yet applied); §20 "Round Tracker" (needs in-world name); XA-32 ring modifier step; XA-33 (rename to "Quarter Structure & Gameplay" + 00a time convention rewrite — bundle in this pass). |
| 04 — Action Card System | 0.9.20 | C17 sign-off (after Art 03); C36–C42 Intel economy cards; 04b-03 action taxonomy audit required before C16+ work. |
| 00c — Economy Manifest | 0.4 | §8, §9 stubs only. |
| 03a — Game Engine Specification | 0.98 | Layer 4 stub remaining. |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure (03-11) + initial draft pending. |

Signed-off artifacts: 00b (v0.1), 01 (v1.8), 02b (v1.5), 04b (v1.2 — 04b-03 audit pending). Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **00-07** | Art 00 multicultural texture pass | ✅ S40 |
| **00a-08** | 00a v0.3 re-sign-off | ✅ S40 |
| **01-05** | Art 01 overhaul — physical zone hierarchy, all Overview children | ✅ S40 |
| **00b-05** | 00b live_state spec update (on_component_id + on_game_zone_id) → then agy DDL (L156) | Open |
| **DB-09** | Create district_adjacency table (agy) — seed from Art 01 adjacency map | Open — Art 01 signed off |
| **01-07** | Art 01 §4 Narrative Function — remove (content in §3 + Physical Table Layout) | ✅ S41 |
| **01-08** | Art 01 narrative anchor pass — staged in Whiteboard/Art01_Narrative_Anchors_S41.md | Open — after 02a sign-off |
| **08-00** | Art 08 — define scope + create stub (Faction Player Tableau + ARBITER Tableau) | Open |
| **03-12** | Battlefield Strength trigger model — resolve in Art 03 re-sign-off (see 04-48) | Open |
| **01-06** | Claude Design visual wireframe — table layout + mat layout | Open |
| **02a-10** | 02a v1.6 combined review — §8a (S38) + narrative anchors (S41); one focused pass | Open — Session 42 first item |
| **04-48** | Art 03 v1.9 re-sign-off (§3 Quarter fix + §20 naming + XA-32) | Open — after 02a |
| **04b-03** | Action taxonomy audit — prerequisite to Art 04 continuation (C16+) | Open — after Art 01 |
| **XA-32** | Art 03 Beat 3/4 ring modifier step + Art 07 ring modifier guide | Open |
| **PM06-01** | Create PM06 — Lessons Learned | Deferred — next session |
| **00-09** | World Conditions panel — content undefined | Open |
| **00-10** | Faction Representative as named component — design question | Open |
| **FS-01-WBS** | Add faction screen to PM01 WBS 2 | Open |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L159** (S42): "Quarter" locked globally — "Round" retired as a game term. Art 03 rename to "Quarter Structure & Gameplay" pending (XA-33, bundle with 04-48). 00a time convention rule to be rewritten same pass.
- **L158** (S42): Intel Token canonical (also: Intelligence Token). Physical form = small token/chit, not paper slip. "Intel note" deprecated. Swept 02b, 00a, PM04.
- **L157** (S42): Presence chip = canonical physical name. "Presence token" = card text shorthand only. PM04 updated. 00a R10/R13 sweep pending (00a-09).

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L159)

---

## Pending Sign-Offs

- **Art 00 v1.5** — ✅ Signed Off S40
- **00a v0.3** — ✅ Signed Off S40
- **Art 01 v1.8** — ✅ Signed Off S40
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v1.9** — next; §3 "Eight Quarters" fix + XA-32 ring modifier + XA-33 rename bundle
- C17 — after Art 03

---

## Key Concepts Established S39–S40 (Not Yet in All Artifacts)

- **MIRROR** = Meridian Interface for Real-time Reporting, Observation, and Recording. Holographic projection device at Chorus Node. Predates The Table and possibly ARBITER. Origin of "New Meridian" name. Written to Art 00 §8.
- **Zone vs. Component distinction** = Zones are named physical locations (infrastructure); components are portable objects placed within zones. Central Area is a zone; The Overview is the component that fills it. Established S40 — in Art 01 [NEW] Physical Table Layout.
- **district_adjacency** = bidirectional adjacency table for all 21 districts. In Art 01 §[City]. DB table needed (agy). Feeds Entry Rule A/B and Battlefield Strength (03-12).
- **live_state schema addition** = on_component_id + on_game_zone_id columns confirmed S40. L156 needed; 00b update required before agy executes DDL.
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

## Gem Actions Pending (write to GEMINI_CONTEXT.md at session close)

- **Component narrative audit:** For every known physical component in the game (presence tokens, deployment markers, structure blocks, established markers, dispatch tokens, intel notes, faction Terminals, faction screens, Ring Modifier decks, Session Timeline, Situation Report zone cards, ARBITER screen, ARBITER tableau, status markers, dispatch cases, initiative strips, control flags, tension markers), confirm that a narrative reference or anchor exists in Art 00. For any component with no narrative grounding in Art 00, flag it with a recommended location (existing §, or new narrative anchor in §14). Output: table of component → Art 00 reference or flag.

---

*Updated S39 Phase 1 close. Sources of truth: PM03 (artifacts), PM02 (decisions), PM05 (punch list).*
