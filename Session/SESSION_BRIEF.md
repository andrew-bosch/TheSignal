# THE SIGNAL — Session Brief
**Session 38 | Updated: 2026-05-26**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

Session 37 complete. Double Case Pass architecture implemented (L145–L150). Art 03 restructured to v1.9 (Month 1/2/3, Dispatch Tokens, Intel decay) — **pending Andy's full review and re-sign-off (first item Session 38)**. PM04 updated with "Month" entry. PM05: 04-41 closed (Intel as universal currency, L148); 04-47 and 04-48 added. Art 04: Intel economy cards C36–C42 drafted. C37 SACRIFICE confirmed: direct −1 PS track step (develop further at 04-47 review). `gem_web_context.md` restructured with Gem Profile protocol (Bucket A/B). Next session: Art 03 full review → re-sign-off, then C17 sign-off (now unblocked), then C20 review.

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 03 — Round Structure & Gameplay | 1.9 | ⚠️ Pending Re-Sign-Off — S37 (Double Case Pass, Intel economy, Dispatch Tokens). Andy full review = Session 38 first item. |
| 04 — Action Card System | 0.9.20 | C17 sign-off (now unblocked); C36–C42 Intel economy cards drafted (schema pass = 04-47); C18/C19 redesign (D-04-02); C20 not reviewed; P01–P18 pending (04-01) |
| 03a — Game Engine Specification | 0.98 | Layer 4 stub remaining |
| 00 — Factions, World & Narrative | 1.4 | 00-07 texture pass queued |
| 00c — Economy Manifest | 0.4 | §8 Derived Cost Analysis, §9 Round Income Analysis (stubs only) |
| 07 — ARBITER Toolkit | 0.1 | Initial sign-off pending full draft |
| 05–06, 08–11, 10, 10a | 0.1 | Draft placeholders |

Signed-off artifacts: 00 (v1.4), 00a (v0.2), 00b (v0.1), 01 (v1.2), 02a (v1.4), 02b (v1.5), 03 (v1.8), 04b (v1.2). Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **04-48** | Art 03 v1.9 re-sign-off required | Open — Session 38 first item |
| **C17 sign-off** | C17 now unblocked (04-41 closed) | Open — after 04-48 |
| **04-47** | Art 04 Intel economy cards C36–C42 full §6 schema pass | Open |
| **04-41** | Surveillance deniability | **CLOSED S37** — L148 (Intel as universal currency) |
| **XA-32** | Art 03 Beat 3/4 ring modifier step + Art 07 ring modifier guide. Coordinates with 04-48. | Open |
| **04-43** | C13 resolution type mismatch — Transactional vs. d100 (agy S36 finding). Fix: Probabilistic. | Open |
| **04-44** | C02/C04/C05/C08 difficulty hardcoding vs. 02a §7 dynamic scaling — design decision needed (agy S36). | Open |
| **DB-04** | Create `resource_types` table + `factions` column gaps. Prerequisite for DB-05. | Open |
| **04-39** | Effects normalization + ring modifier extraction from C01–C15. Unsupervised batch after schema locked. | Open |
| **04-40** | Remove pool_copies from all Art 04 card specs. Unsupervised run. | Open |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L150** (S37): "Month" provisional canon for Quarter phases; Week/Beat nomenclature: Month1.Week2.Beat1 format.
- **L148** (S37): Intel as universal currency — all factions can generate/spend Intel tokens. Closes PM05 04-41.
- **L145** (S37): Double Case Pass — Month 1 + Month 2 covert, Month 3 political; Beat 0–3 runs twice per Quarter.

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L150)

---

## Pending Sign-Offs

- **Art 03 v1.9** — Andy full review (first item Session 38)
- **C17** — unblocked; after Art 03 re-sign-off
- C20 — not yet reviewed
- Art 04 C18/C19 — redesign decision pending (D-04-02)
- Art 07 — pending full draft
- 00-07 multicultural texture pass (queued)

---

## Key Files

| File | Purpose |
|------|---------|
| `Session/THE_SIGNAL___Project_Save_State.md` | Full session history, complete artifact table |
| `Session/PRIVATE___True_State.md` | Read before writing ARBITER or Chorus content |
| `Session/PRIVATE___Design_Questions.md` | Known / Unknowable / Open per TrueState §1–§8 — living doc |
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

ARBITER: always all-caps. All other game terms: Title Case.

**Four Registers** (Art 00 §9, Art 07 §9): The Record (flat/factual) · The Observation (oblique/atmospheric) · The Reckoning (rare/direct/always true) · The Witness (expository/chronological; ambiguously ARBITER or Narrator).

---

*Updated in Phase 1 of close routine (live, before queue). Sources of truth: PM03 (artifacts), PM02 (decisions), PM05 (punch list).*
