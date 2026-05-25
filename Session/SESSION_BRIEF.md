# THE SIGNAL — Session Brief
**Session 36 | Updated: 2026-05-25**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus

Session 35 complete. C16 signed off. C17 grip review pending sign-off (04-41 surveillance deniability open — do not sign off until resolved). C18/C19 flagged for redesign (D-04-02) — schema uplift done, Portrait N/A pending redesign decision. C20 schema uplift done, not yet reviewed. Next session: complete C17 sign-off, C20 review, then C21–C25 (Directorate). Major schema decisions this session: L144 (1NF + snowflake), ring modifier fields added (4 fields per card, per-token rates), pool_copies deprecated (04-40), effects normalization (04-39 updated), ring modifier formula working (XA-32). Art 03 v1.8 signed off (resolution grid targeting rule added S35).

---

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 04 — Action Card System | 0.9.20 | C17 sign-off pending (04-41); C18/C19 redesign (D-04-02); C20 not reviewed; P01–P18 pending (04-01) |
| 03 — Round Structure & Gameplay | 1.8 | ✅ Re-signed off S35. |
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
| **04-23** | C15 re-sign-off — ✅ complete S35. | Done |
| **C17 sign-off** | 04-41 (surveillance deniability) must be resolved first | Open — first action |
| **04-41** | Surveillance deniability — C17 failure slip identifies Ghost if only spy card. Also: Intel token economy thin if Ghost-only. Fix options: common card, multi-faction surveillance, or redesign failure. | Open — blocks C17 sign-off |
| **XA-32** | Art 03 Beat 3/4 ring modifier step + Art 07 ARBITER ring modifier calculation guide. Formula: `ringModifier[ring] × (count(presenceToken[targetFaction][district]) − count(presenceToken[actingFaction][district]))`. Re-sign-off required for Art 03. | Open |
| **04-42** | Ring modifier narrative confirmation pass — baseline values (−15/−10/0/+10 per token) need card-by-card narrative validation. After full card set. | Open |
| **04-39** | Effects normalization + ring modifier extraction from C01–C15 Difficulty field. Unsupervised batch after schema locked. | Open |
| **04-40** | Remove pool_copies from all Art 04 card specs. Unsupervised run. | Open |
| **04-35** | Affinity bonus: N/A field missing from C16–C35 — C15 done S35, C16–C20 done S35. | Partially done |
| **XA-29** | L109 component terminology scan (00–04b) — unsupervised run | Open |
| **XA-23** | Index→Contents rename + anchor links — unsupervised run | Open |
| **00b-04** | RG entity ID numbering vs. L141 — design decision required | Open |
| **04-24** | Cross-beat flag mechanism (C06/C07/C10) — design in Art 07 | Open |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L144** (S35): Card schema design — 1NF + snowflake. All fields atomic; compound-value fields refactored to linked child tables; dimensions fully normalized. Governs Art 04 and 00b.
- **L143** (S34): "Deliberation cycles" confirmed as Art 00 in-world term for Quarters — factions use own internal names; institutional neutral language in Art 00.
- **L142** (S29): Ring names — Ring 2 = "The Mid," Ring 3 = "Baryo"

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L144)

---

## Pending Sign-Offs

- **C17** — first action (04-41 must be resolved)
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
