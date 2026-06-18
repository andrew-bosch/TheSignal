# 04-n70 Findings — Schema Validation Pass S95
All three sessions complete. Fix pass ready next session.

---

## SYSTEMATIC GAPS (all sets)

| ID | Issue | Fix path |
|----|-------|----------|
| S-1 | `ps_framing` absent from all cards — field added S94 | 04-n34a (PAs), 04-n34b (covert ops) |
| S-2 | `boost=None` absent from all cards — field added S71 | 04-n97 sweep (new PM05 item) |
| S-3 | `doctrine_mod=None` in some cards (C31, C38, P15, P16, Directorate PAs) but not others — field not in standard §6.1 field list | Verify §6.1 inclusion before any sweep; if not in schema, remove from affected cards |

---

## SCHEMA VIOLATIONS (hard errors — type/enum mismatch)

| Card | Issue | Set |
|------|-------|-----|
| C39 | `faction=None` — Standard subtype should use `All` | Standard |
| C23 Tort Interference | `faction=None` — same as C39 | Directorate (Standard subtype) |
| C36 Synthesize | `affinity=Ghost` — must be `ConditionalExpr \| None`; Ghost is a Faction | Ghost |
| C42 Sanctioned Raid | `affinity=Directorate` — same violation; checklist `Data schema validation=✓` is wrong | Directorate |
| C38 Parasitic | `affinity=Syndicate` — same violation (not listed in C31 Outstanding Issues — new catch) | Syndicate |
| C41 Corporate Blackmail | `affinity=Syndicate` — same violation (known, in C31 Outstanding Issues) | Syndicate |
| P05 | `threshold=None` with `resolution=d100` — None valid only for Automatic | Standard PA |
| P13 Public Disclosure | `threshold=None` with `resolution=d100` — same | Network PA |
| C16 Pattern Match | `resolution=Prediction` — not in §6.3 enum; valid: `d100 \| Automatic` only | Ghost |
| EntryExitControls | `persistence_condition = faction(acting).influence_tier(...) >= Established` — inverted; schema defines this as removal condition; should be `< Established` | Directorate PA |
| Reputational Strike stub | `layer=Information, function=Reveal, subject=PublicStanding` — modifier cards must have `layer=None, function=None, subject=None` per §11.1 | Modifier stub |

---

## MISSING PERSISTENCE FIELDS (manual insertion required)

S94 sweep only inserted persistence_condition/effect AFTER existing `persistence=` lines. Cards with no `persistence=` line were missed.

| Card | Set | Notes |
|------|-----|-------|
| Station, Full Take, SCIF, Flip, Signals Analysis | Ghost | Draft S59 flat-format stubs; 5 cards |
| C37 Sacrifice | Network | Draft S59 flat-format |
| LandTitle | Syndicate | Redesigned S67 v2.0; no persistence= line |
| HostileTakeover | Syndicate | Draft S59 flat-format |
| AccordTransfer | Syndicate | Draft S59 flat-format |

**Total: 9 cards** needing manual `persistence=Immediate, persistence_condition=None, persistence_effect=None` insertion (all are Immediate by design).

---

## PERSISTENCE MODEL INCONSISTENCIES (design question before fix)

Four Permanent/Seasonal PAs use two different models for encoding removal conditions — needs a consistent pattern decision.

| Card | Current model | Issue |
|------|---------------|-------|
| P11 Regulatory Override | `success=game.world_condition(clear_on=...)` | Removal conditions in success field; `persistence_condition=None` |
| P16 Public Dividend | Same as P11 | Seasonal persistence; conditions in success/comments |
| RegulatoryDowngrade | `persistence_effect` populated; `success=None` | No explicit card-placement action in success |
| RegulatoryFreeze | Same as RegulatoryDowngrade | Same |

Decision needed: for Permanent/Seasonal PAs, should removal conditions live in `persistence_condition` (structured) or `success=game.world_condition(clear_on=...)` (encoded in success)? Pick one model and apply consistently.

Also: EntryExitControls has `persistence_condition` inverted AND `persistence_effect` absent entirely (separate fix from the inversion fix).

---

## SPEC/CHECKLIST ERRORS

| Card | Issue |
|------|-------|
| C09 | Duplicate "Overture delivery procedure" Outstanding Issues entry — identical text twice |
| C19 Deep Cover | Checklist Taxonomy row: `Information/Protect/ActionAttribution` but spec has `layer=Information, function=Remove, subject=IntelToken` — mismatch |
| C42 | Checklist `Data schema validation=✓` — incorrect given known `affinity=Directorate` violation |
| C41 | `arbiter_note` says "reduce Directorate PS by 1" — should be Syndicate; copy error |
| RegulatoryDowngrade, RegulatoryFreeze | Listed in Directorate Covert Ops index table but breadcrumb links to Public Acts — nav error |

---

## NON-STANDARD PORTRAYENTRY PARAMETERS

| Card | Parameter | Notes |
|------|-----------|-------|
| C35 Regulatory Capture | `modifier=`, `mod_where=` | Not seen in any other card; verify §6.2 |
| C41 Corporate Blackmail | `flat=` | Already flagged in C41 Outstanding Issues |
| C40B Live Coverage | `failcrit=` parameter inside PortraitEntry | PS shift ALSO in `failcrit` field — possible double-count |

---

## STRUCTURAL GAPS (effects missing from spec fields)

| Card | Issue |
|------|-------|
| C41 Corporate Blackmail | `success=None` — ElectPlayer effects entirely in comments/arbiter_note; not in structured fields |
| P15 Acquisition Offer | `success=None` — ElectPlayer on_accept/on_decline effects (including PS shifts) in comments only |
| C40B Live Coverage | `persistence_condition` and `persistence_effect` are prose strings, not structured expressions |

---

## NOTATION INCONSISTENCIES

| Card | Issue |
|------|-------|
| C37 Sacrifice | `success = faction(acting).public_standing -= 2` — uses `public_standing`; all other cards use `standing` |
| Overture | `perspectives = {TBD}` — invalid Python syntax |

---

## 04-n34a MIGRATION CANDIDATES (PA cards with PS shifts in effects)

Standard: P01 (+1), P02 (+1/-1/-2), P03 (+1), P04 (-2/+1/-1/-2), P05 (various), P06 (-1/+1/-1/-2), P07 (+2) — 7 cards
Directorate: P12 (-1 target, +1 self)
Network: P13 (success/fail), P14 (+1)
Syndicate: P16 (+1); P15 (on_accept/decline in comments — migration model TBD)

**Note:** Scope of 04-n34a itself needs clarification at pass time — see 04-n34a PM05 note (S95).

**Note on C_DisinformationCampaign:** PS shifts ARE the primary effect — confirmed S95 these stay in `success`/`fail`, not migrated to `ps_framing`.

---

## 04-n34b MIGRATION CANDIDATES (covert op failcrit PS shifts)

C02, C04, C08 (Standard — failcrit `standing -= N`, trigger=discovery)
C17 Intercept (Ghost — BLOCKED, awaiting 04-n50 re-sign-off)
C22 Detain (Directorate — failcrit -1)
C32 Short the Market (Syndicate — failcrit -1)
C33 Hostile Acquisition (Syndicate — failcrit -1)
C42 Sanctioned Raid (Directorate — failcrit discovery + PS scaled by n_boost)
C41 Corporate Blackmail (Syndicate — self-cost always -1, in comments)

---

## BLOCKED ITEMS (do not fix until gate clears)

| Card | Block |
|------|-------|
| C17 Intercept | 04-n50 re-sign-off required before any fix |

---

## FIX PASS GROUPING (suggested order)

1. **Schema violations** — clean enum/type errors: C39, C23, C36, C42 affinity, C38 affinity, C41 affinity, P05, P13, C16, EntryExitControls condition inversion
2. **Missing persistence triples** — 9 cards: all `persistence=Immediate, persistence_condition=None, persistence_effect=None`
3. **Spec/checklist errors** — C09 dup, C19 checklist mismatch, C42 checklist flag, C41 arbiter_note, nav fixes
4. **Notation inconsistencies** — C37 public_standing→standing, Overture perspectives syntax
5. **Persistence model decision** — P11, P16, RegulatoryDowngrade, RegulatoryFreeze (needs Andy input before fix)
6. **Non-standard PortraitEntry params** — C35, C41, C40B (verify §6.2 before fix)
7. **Structural gaps** — C41/P15 success=None, C40B prose persistence (design decisions needed)
8. **S-3 doctrine_mod** — verify §6.1 first; sweep or remove after decision
