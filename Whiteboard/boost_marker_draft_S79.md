# Boost Marker (BM-xx) — Draft Language S79

Draft language for Art 00b §4 component registration and Art 03 Beat 0/2/3 procedure additions.
Gates: 04-n81 (00b registration), 04-n82 (Beat 0 procedure), 04-n83 (Beat 2/3 procedure).

---

## Art 00b §4 — Component Registration Draft

**BM-xx — BoostMarker**

| Field | Value |
|-------|-------|
| Notation | BM-xx |
| Name | BoostMarker |
| Owner | ARBITER |
| Physical Form | Small token (distinct colour from other ARBITER-held tokens; recommended: white or silver) |
| Location | ARBITER tableau (supply); placed on resolution grid during covert operation resolution only |
| Lifecycle | Placed at Beat 0 when boost payments are detected; removed to ARBITER supply at beat cleanup (end of Beat 2 or Beat 3 resolution pass) |
| Scope | Covert operations only; not used for public act resolution |
| Supply Size | TBD — minimum: max anticipated boost count per card × max simultaneous boosted cards per beat; recommend 10–15 tokens at L1 |

*See Art 03 §11 (Beat 0, Beat 2/3) for placement and resolution procedures.*

---

## Art 03 — Beat 0 Boost Detection Procedure (Draft)

**Placement in Art 03:** New sub-step within Beat 0 payment validation (after cost validation, before grid placement confirmation).

---

**Beat 0 — Boost Payment Detection**

*After validating that each submitted card's base cost has been paid in full:*

For each submitted card whose spec includes a `boost` field (value ≠ None):

1. Calculate excess resources submitted beyond the base cost.
2. If excess resources are a non-zero exact multiple of the boost unit cost:
   - n = excess resources ÷ boost unit cost
   - Place n BM-xx (BoostMarker) tokens on the card's grid slot alongside the card.
   - *For threshold-scaling cards:* lock threshold at Beat 0 using total count = (1 + n). Record on ARBITER notation.
   - *Additional validation (card-specific):* apply any Beat 0 checks that depend on total n (e.g. C42: confirm faction(target) has ≥ (1 + n) presence tokens at target district).
3. If excess resources are present but not an exact multiple of the boost unit cost, or if the boost condition evaluates False: reject submission — excess resources returned; player may resubmit with corrected payment.
4. If no excess resources are submitted: no BM-xx placed; card resolves at base effect (n = 0 boost).

*BM-xx tokens are ARBITER-held during covert resolution and not visible as faction board state.*

---

## Art 03 — Beat 2/3 Boost Resolution Procedure (Draft)

**Placement in Art 03:** New clause in the resolution step for Beat 2 and Beat 3, applied immediately after outcome determination (success/fail/crit) and before effect execution.

---

**Beat 2/3 — Boost Marker Resolution**

*After determining the outcome (success / successcrit / fail / failcrit) for a card and before executing effects:*

1. Check the card's grid slot for BM-xx tokens.
2. If BM-xx count = 0: execute effect once (standard resolution).
3. If BM-xx count = n > 0: execute the outcome effect (1 + n) times in sequence.
   - *For effects targeting distinct instances* (e.g. removing n presence tokens): apply all (1 + n) instances as a single resolution event — ARBITER announces total count before executing.
   - *Fail and failcrit effects are not multiplied* — boost applies to success effects only; fail/failcrit fire once regardless of BM-xx count.
4. After effect execution: remove all BM-xx from the card's grid slot. Return to ARBITER supply.

*BM-xx removal occurs at beat cleanup even if the card's resolution is contested or partially blocked — markers are not carried to the next beat.*

---

*Whiteboard draft — migrate to Art 00b §4 and Art 03 §11 once 04-n81/82/83 are scheduled. Delete this file after migration.*
