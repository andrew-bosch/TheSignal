# THE SIGNAL — Session Brief
**Session 39 | Updated: 2026-05-26**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

Session 38 complete. Dispatch Token foundation built from scratch: Art 00 §14 anchor ("The Backlog" narrative, approved S38), 00a R39 (governing rule — covert ops require one token), 02a §8a (Dispatch Tokens & The Backlog — component definition, spend rules, Ghost asymmetry, operational meaning). Three L-decisions locked: L151 (The Backlog canonical term), L152 (base_difficulty = Integer), L153 (Assets definition for C10). Art 03 v1.9 review started — initiative procedure moved to Art 07 (03-11); two terminology flags still pending Andy review (§3 "Eight rounds" → "Eight Quarters"; §20 "Round Tracker" = component name or terminology violation?); XA-32 ring modifier step still open. **Art 03 re-sign-off = Session 39 first item.** Multiple signed-off artifacts now pending re-sign-off: 00a (v0.3, R39), 02a (v1.5, §8a). Art 01 overhaul flagged as major new project (01-05, physical space definition + game_zones DB alignment).

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 03 — Round Structure & Gameplay | 1.9 | ⚠️ Pending Re-Sign-Off — S37/S38. Flags: §3 "Eight rounds" (terminology fix, Andy to confirm); §20 "Round Tracker" (component name vs. terminology violation — Andy to confirm); XA-32 ring modifier step; 03-11 initiative procedure to Art 07. |
| 00a — Governing Rules & Design Policy | 0.3 | ⚠️ Pending Re-Sign-Off — R39 (Dispatch Tokens) added S38. |
| 02a — Resource Systems: Board State | 1.5 | ⚠️ Pending Re-Sign-Off — §8a (Dispatch Tokens & The Backlog) added S38. |
| 04 — Action Card System | 0.9.20 | C17 sign-off (unblocked after Art 03 re-sign-off); C36–C42 Intel economy cards (04-47 schema pass); C20 not yet reviewed; P01–P18 pending (04-01). |
| 00 — Factions, World & Narrative | 1.5 | ✅ Re-sign-off complete S38. 00-07 multicultural texture pass queued. |
| 03a — Game Engine Specification | 0.98 | Layer 4 stub remaining. |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure migration (03-11) + initial sign-off pending full draft. |
| 00c — Economy Manifest | 0.4 | §8 Derived Cost Analysis, §9 Round Income Analysis (stubs only). |

Signed-off artifacts: 00 (v1.5), 00b (v0.1), 01 (v1.2), 02b (v1.5), 04b (v1.2). Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **04-48** | Art 03 v1.9 re-sign-off | Open — Session 39 first item |
| **00a-08** | 00a v0.3 re-sign-off (R39 added S38) | Open — after Art 03 |
| **02a-10** | 02a v1.5 re-sign-off (§8a added S38) | Open |
| **C17 sign-off** | Unblocked after Art 03 re-sign-off | Open |
| **01-05** | Art 01 overhaul — physical space definition + game_zones DB alignment | New S38 — major project |
| **XA-32** | Art 03 Beat 3/4 ring modifier step + Art 07 ring modifier guide | Open — coordinates with 04-48 |
| **04-47** | Art 04 Intel economy cards C36–C42 full §6 schema pass | Open |
| **03-11** | Art 07 — migrate initiative procedure from Art 03 §7 Step 2 | Open |
| **NP1-01** | Art 04 §6 base_difficulty field type + value cleanup (Integer) | Open — unsupervised pass |
| **DB-08** | card_metadata — 00b §8 spec update + DDL via agy | Open — agent task |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L153** (S38): Assets definition — C10 Protect scope: faction's Influence, Structure Blocks, Deployment Markers, and any covert or political actions declared this round. Narrative: everything the faction is doing, passive or active.
- **L152** (S38): base_difficulty = INTEGER (or N/A) in card_metadata and Art 04 §6. Tier name ("Average", "Easy", "Challenging") is a derived dimension, not stored. NP1-01 queued to clean up existing card entries.
- **L151** (S38): The Backlog — canonical name for the Dispatch Token pool on the table. Physically and terminologically distinct from the Reservoir. 16 tokens total (Ghost: 4, all others: 3). Backlog vs. active framing: token spent = operation moved from backlog to active.

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L153)

---

## Pending Sign-Offs

- **Art 03 v1.9** — Session 39 first item (two terminology flags + XA-32)
- **00a v0.3** — after Art 03; R39 Dispatch Tokens
- **02a v1.5** — coordinate with 00a; §8a Dispatch Tokens & The Backlog
- C17 — after Art 03 re-sign-off
- Art 01 — overhaul required (01-05, major project)
- Art 07 — pending full draft

---

## Key Files

| File | Purpose |
|------|---------|
| `Session/THE_SIGNAL___Project_Save_State.md` | Full session history, complete artifact table |
| `Session/PRIVATE___True_State.md` | Read before writing ARBITER or Chorus content |
| `Session/PRIVATE___Design_Questions.md` | Known / Unknowable / Open per TrueState §1–§8 |
| `V1/PM02___Decision_Log___Validation_Tracker.md` | All locked decisions |
| `V1/PM03___Master_Artifact_Index.md` | Authoritative sign-off status, dependency map |
| `V1/PM04___Glossary___Data_Dictionary.md` | In-world terms, design terminology |
| `V1/PM05___Active_Punch_List.md` | Full punch list |
| `V1/PM___Cross_Artifact_Inconsistency_Audit.md` | 24 open inconsistency items |

---

## Terminology

| Use | Not |
|-----|-----|
| Quarter | Round |
| The Overview | Game mat |
| Presence token | Influence token |
| Deployment marker / Operational marker | Claim marker |
| Public Standing track | Popularity track |
| Covert operation | Private action |
| Political act | Public action |
| Situation report | World event card |
| The Mid | Infrastructure ring |
| Baryo | Sprawl |
| The Backlog | Reservoir (for Dispatch Tokens) |

ARBITER: always all-caps. All other game terms: Title Case.

**Four Registers** (Art 00 §9, Art 07 §9): The Record (flat/factual) · The Observation (oblique/atmospheric) · The Reckoning (rare/direct/always true) · The Witness (expository/chronological; ambiguously ARBITER or Narrator).

---

*Updated in Phase 1 of close routine (live, before queue). Sources of truth: PM03 (artifacts), PM02 (decisions), PM05 (punch list).*
