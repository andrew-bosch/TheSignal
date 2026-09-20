# 04c — CARD SYSTEM COST MODEL
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.0  
**Status:** ✅ Signed Off — initial version  
**Last Updated:** 2026-09-20  
**Companion to:** 04 — Card System

> **Revisit before Art 04 signs off.** This version is signed off as a sound account of where card economics currently stands — not as a finished model. It deliberately records several open questions rather than resolving them: no cost magnitude rule is locked for any card type (§3), the ModReact cost convention is described rather than governing (§5), the ⚠ governing caveat cannot be lifted until §12 is buildable (§9), and §12 itself is gated. These are expected to be worked as Art 04 approaches sign-off. Tracked at PM05 **04c-01**.

**Purpose:** The canonical account of card economics — what a card charges the faction that plays it, and how the effect it delivers is priced into a `value_rating` tier. Art 04 §6 specifies the `cost` and `value_rating` fields; this document holds the reasoning behind their values.

**Scope:** Every card that charges a resource or an Intel Token, across all card types. The pricing model in §8–§11 covers Covert Act and Public Act cards only — Modifier and React cards are rated on a separate convention, stated in §5.

**Depends on:** 04 — Card System (§6 card schema); 03 — Round Structure & Gameplay (§7.4, §13, §20); `the_signal_db` (`v_card_pair_uvm_cost`, `v_card_value_to_acting`, `uvm_pair_assumptions`, `card_effect_component`, `card_body`)

**Source versions:** 04 v0.9.100; 03 v4.15

---

## 1. Overview

Two different questions live in this document, and keeping them apart is the whole point.

**What does a card cost?** — the resources a faction hands over to play it. This is a designed value, printed on the card face, and it is an *input* to everything else here. §3–§7.

**What is a card worth?** — how much of the game its effect moves, expressed as a 1–4 `value_rating`. This is a *derived* value, computed from the card's effects by the pricing model. §8–§11.

The two are deliberately not the same number and do not subtract from one another. A card that pays a fair price for a large effect is a high-value card that costs a lot, not a low-value card.

The honest limitation, stated once here and again where it governs: **the pricing model is calibrated from the corpus's own designed costs.** Those costs were set by design judgement against Principle 15, not by playtest. The model can therefore tell you a card is priced unlike its siblings. It cannot tell you the siblings are right. §12 is the analysis that would close that gap, and it is not yet buildable.

---

## 2. Index

| Section | Content |
|---------|---------|
| **§3** | [The Cost Principle](#3-the-cost-principle) — what a cost is, and what may not be one |
| **§4** | [Cost Vocabulary](#4-cost-vocabulary) — resource types, Intel Tokens, invalid cost values |
| **§5** | [Cost by Card Type](#5-cost-by-card-type) — who charges, who cannot, and the ModReact convention |
| **§6** | [Cross-Resource Costs](#6-cross-resource-costs) — why cards charge resources a faction does not generate |
| **§7** | [Intel Tokens as Cost](#7-intel-tokens-as-cost) — the discrete-object cost category |
| **§8** | [What `value_rating` Means](#8-what-value_rating-means) — gross effect delivered |
| **§9** | [Methodology — UVM Pair-Based Pricing](#9-methodology--uvm-pair-based-pricing) — derivation and the governing caveat |
| **§10** | [Tier Boundaries](#10-tier-boundaries) — the 1–4 bands |
| **§11** | [Model Limits](#11-model-limits) — where the model is still wrong |
| **§12** | [Derived Cost Analysis](#12-derived-cost-analysis) — cost against outcome probability *(blocked)* |

---

## 3. The Cost Principle

**Principle 15 — Cost is equitable to the success effect.** The resource cost of a card is calibrated to the expected value of its success outcome. A high-cost card must deliver a commensurately significant success.

Principle 15 is the governing statement, and it is a principle rather than a formula: **no magnitude rule has been locked for any card type.** Costs across the corpus were set by design judgement, card by card, against that principle. This is the acknowledged state of the system, not an oversight to be quietly corrected — §12 is the analysis intended to put numbers behind it, and it is gated on Art 04 sign-off.

Everything downstream inherits that. The pricing model in §9 calibrates its rates by averaging these designed costs, so the model is internally consistent by construction and externally unvalidated by construction.

**A cost is paid at submission and is not contingent on the outcome.** A faction pays to act, not to succeed; a failed operation does not refund. Shortfalls do not block the action — under Principle 20, actions proceed with whatever resources are committed, and the shortfall carries its own consequence.

---

## 4. Cost Vocabulary

A `cost` is expressed as a `CostExpr` (Art 04 §6.3) and may combine two kinds of payment.

**Fungible resources** — five types, each the native resource of one faction:

| Resource | Faction native to |
|----------|-------------------|
| Findings | Ghost |
| Exposure | The Network |
| Capital | The Syndicate |
| Capacity | The Guild |
| Mandate | The Directorate |

**"Native" has two referents, and the difference matters for cost.** Each of the five types is native to a *faction*, as above — and independently, **every district has a Resource Type of its own** (Art 01 §6.4). The two are unrelated: a district whose Resource Type is Capital is not Syndicate territory, and a faction holding influence there collects Capital regardless of its own native type (Art 03 §20).

`faction.acting.native` and `district.<x>.native` therefore resolve to different things at play time, and a cost naming the district's native is not a cost naming the faction's. This is what makes §6 work: a faction can hold a resource it does not generate.

**Intel Tokens** — a discrete-object cost category, not a fungible quantity. See §7.

**What may not be a cost.** Non-fungible markers — Public Standing, presence tiers, influence levels — are not valid cost values. A card whose mechanism involves losing standing expresses that as an effect in `success`/`fail`, not as a cost. The distinction is not cosmetic: costs are paid at submission regardless of outcome, while effects resolve conditionally, so encoding a marker shift as a cost would change when it fires.

**Notation is not yet uniform.** Four `CostExpr` styles coexist in the corpus — bare `ResourceType * n`, `Resource(type, n)` wrapper calls, `ResourceType(n)`, and `list([...])`. This is a known open defect tracked at `schema_cleanup_log` #56; it is a notation question, not an economy question, and no cost value depends on its resolution.

---

## 5. Cost by Card Type

Not every card charges anything, and for two Modifier subclasses that is a schema guarantee rather than a design choice.

| Card type | Carries `cost` | Costed / total |
|---|---|---|
| Covert Act | Per card design | 64 / 69 |
| Public Act | Per card design | 46 / 46 |
| ModActionCard | **Never — schema `None`** | 0 / 132 |
| ModBattleCard | **Never — schema `None`** | 0 / 44 |
| ModReactCard | Per card design | 27 / 93 |

**ModActionCard charges nothing of its own** because it is never played alone. It is bundled with a host operation at Covert Dispatch and fires with it, so its cost folds into the host operation's packet total under the splay-display convention (Art 03 §9.4.0.1 Step 4). The faction pays once, for the packet.

**ModBattleCard charges nothing** by schema lock, for a different and non-inherited reason: **Art 03 §10.1.2's commit sequence has no cost validation or payment step at all**, so a resource cost on a Battlefield Modifier would be unenforceable in procedure. The lock records a procedural fact, not an economic judgement — if §10.1.2 ever gains a payment step, the lock is worth revisiting.

**ModReactCard is the only Modifier subclass that charges resources** — 27 of 93 do; the remaining 66 are free to play. A React card is presented in response to a triggering event rather than submitted in a packet, so it has no host to fold into and pays on its own account.

### ModReactCard — observed cost convention

No magnitude rule is locked for React costs. What follows is **the pattern the existing 27 cards actually exhibit**, recorded so it is legible and so departures from it are visible — not as a rule to price new cards against. Whether it should become one is an open question (PM05 **04c-01**).

- **One unit per resource type is the norm.** 22 of 27 charge exactly ×1 of each type named. The exceptions are three Syndicate cards charging Capital ×2, one Ghost card charging Findings ×2, and one variable Capital ×N.
- **Breadth, not depth, is how React costs scale.** Cards range from one to four named resource types. A more demanding React card charges *more types*, not a larger amount of one.
- **The card's own faction native anchors the cost.** 23 of 27 include the playing faction's native resource. Four do not: two Ghost cards charge the *triggering* faction's native rather than Ghost's, one Directorate card charges only an Intel Token, and one Syndicate card charges Findings and an Intel Token with no Capital.
- **Intel Tokens appear as an additional discrete cost**, never as the scaling term — see §7.

**React cost does not track `value_rating`.** A single Exposure is the full cost of five Network React cards rated 1, 1, 1, 3 and 4. This is expected: React ratings follow the magnitude convention described in §8, not the pricing model, so cost and tier are independent for this card type by design.

---

## 6. Cross-Resource Costs

Many cards charge a resource the playing faction does not natively generate — a Ghost card charging Capacity, a Network card charging Mandate. **This is deliberate, and such cards are not dead cards.**

Two acquisition paths exist for foreign resources, and both are ordinary play rather than exceptions:

1. **Territorial expansion.** District income is paid in *the district's own* Resource Type, not the collecting faction's native one (Art 03 §20). A faction holding influence outside its home resource accumulates foreign resources naturally as it expands, with no conversion step. This is the primary path.
2. **Inter-faction trade.** Resources change hands at Debrief on any terms the parties agree (Art 03 §11.0).

The Translation (Art 03 §19.1) — the Bank exchange — is the fallback when neither path is available, not the intended route.

Cross-resource costs are therefore a design lever with a clear narrative warrant: a card that charges outside a faction's native resource is a card that asks the faction to have reached beyond its own ground, by holding territory or by dealing.

---

## 7. Intel Tokens as Cost

**18 cards take an Intel Token as part of their cost** — 10 Covert Acts, 4 Public Acts, 4 ModReact cards.

An Intel Token is a **discrete object, not a quantity.** It is held, it has an age and a subject, and it is surrendered whole. This makes it different in kind from a fungible resource, and the difference shows up in three places:

**It is usually qualified.** An Intel cost commonly names what the token must be *about* and sometimes what condition it must be in — `IntelToken(about=faction(target))`, or `status=[Fresh, Stale]`. A faction holding Intel on the wrong subject cannot pay. The cost is therefore a gate on prior intelligence work as much as it is a price.

**It cannot be generated on demand.** Unlike a native resource, which accrues every Quarter, an Intel Token is acquired by specific play. A card charging Intel is charging a scarcer and less substitutable thing than its nominal single-unit size suggests.

**The pricing model treats it separately.** In §9, an Intel Token cost is priced through its own calibrated pair rather than being converted to a fungible-resource equivalent, because no exchange rate between the two is defined anywhere in the system — and none should be inferred from the calibrated rates, which are averages of designed costs rather than a conversion table.

---

## 8. What `value_rating` Means

**Gross effect delivered.** `value_rating` buckets cards by how much of the game they move: cards that affect more of it sit in higher tiers.

It is **not a net ledger.** What the acting faction pays does not subtract from it — `cost` is already its own field and records that separately. A card that buys a large effect at a fair price is a high-tier card, not a floor-tier one.

Three consequences follow, and they are the practical test:

- Every effect row counts by its magnitude regardless of whose holdings it lands on.
- A card that both spends and inflicts counts both.
- A transfer counts once, not twice.

A signed, net-of-payments measure of the same corpus is a legitimate quantity and is built — it lives in `v_card_value_to_acting` — but it is deliberately kept out of the tier and must not be wired into it.

**Scope.** The pricing model applies to Covert Act and Public Act cards. **Modifier and React cards are rated on a separate magnitude convention** — their `value_rating` mirrors the size of the effect they apply rather than a modeled cost. A Modifier card whose rating differs from what the pricing model would compute is therefore expected, not defective, and must not be audited against §10's boundaries.

---

## 9. Methodology — UVM Pair-Based Pricing

A fixed per-Subject value × per-Function multiplier was tried first and rejected against real card data: the Remove/Add cost ratio alone ranges from 1.15× to 8.58× depending on Subject, so no universal multiplier fits every Subject consistently.

In its place, each confirmed **(Subject, Function) pair** is priced as one atomic calibrated unit, derived from the corpus's own designed costs. A card's total modeled value sums its distinct pairs' calibrated rates × actual magnitude, with `successcrit` folded in at a flat 5% weight — crit-success is an unconditional floor per Design Pillar 4.8b — and `failcrit` excluded, since it is mutually exclusive with success and the model specifically answers *what does success cost*.

> **⚠ Governing caveat.** Calibration is by averaging the *existing designed cost* of cards that already use a given pair — not by playtesting, simulation, or any external measure of in-game value. "Validated" means *two or more existing cards agreed closely enough to average*, not *confirmed correct by play*. Every rate and every rating derived from it is a self-consistency check against the current corpus: it can catch a card priced out of line with its siblings, but cannot confirm the sibling group itself is priced right. Re-derive once real playtest data exists — session counts, win-rate correlation, and "this felt broken" reports against actual cost.

**Five Public Acts are unpriceable and their ratings are held rather than derived** — NET.PA.4, NET.PA.5, NET.PA.6, SYN.PA.4 and SYN.PA.5. Their outcome fields are prose rather than `MutationExpr`, so the model has nothing to price. Their ratings are *unverifiable rather than wrong*; they must not be re-rated to floor, and they must be re-derived once those fields are converted (PM05 04-n218 / 04-n220).

---

## 10. Tier Boundaries

Counts are the priced population — the 205 cards `v_card_pair_uvm_cost` returns a modeled value for — bucketed by that modeled value, not by assigned rating.

| `value_rating` | Range (modeled value) | Count |
|---|---|---|
| 1 — floor | < 3.0 | 113 |
| 2 — standard | 3.0 – 4.99 | 49 |
| 3 — advanced | 5.0 – 6.99 | 21 |
| 4 — ceiling | ≥ 7.0 | 22 |

These are **natural-break boundaries, not equal-population.** A histogram of the priced corpus thins going up in a clean pyramid, which matches the intended design shape of 1 as floor/basic and 4 as end-game ceiling. Equal-population quartiles were checked and rejected: they would force a roughly 50/50 floor-to-non-floor split, contradicting that intent.

---

## 11. Model Limits

**Quantification asymmetry.** When some of a card's effect rows carry a readable magnitude and others do not, and the two fall on opposite sides of the acting / non-acting split, the unreadable side is floored at one unit while the other counts in full. This distorts in *both* directions — it can overstate a card as readily as understate it.

The floor applies to any effect built on a `count(...)` board-state read rather than a literal magnitude: there is no number to read at query time, so it prices at N=1, the absolute floor rather than an average or a realistic case. Most NULL-magnitude rows are unaffected, being a fixed single thing or not a quantity at all.

Five cards are held on this basis rather than treated as drift — STD.CA.9, GUI.PA.2, SYN.PA.1, STD.PA.6 and DIR.PA.3 — each mixing an unquantified gain priced at the one-unit floor with a payment counted in full. The sync tool reports them in their own bucket. Tracked at PM05 **04-n235**.

**Out of scope for this model entirely:** hand size, deck construction economics, and the Burst Play threshold. These are unaddressed and still pending; nothing here prices them.

---

## 12. Derived Cost Analysis

> **Blocked.** Requires the full card set locked — gated on Art 04 sign-off.

This is the analysis that would give Principle 15 (§3) numbers, and its absence is why §9's governing caveat cannot yet be lifted.

**Purpose:** express each card's cost in terms of *expected outcome value* rather than nominal cost. A card costing 3 Capital at Average difficulty costs 6 Capital per successful outcome on expected value. That comparison is invisible from the card face, and it is the core balance signal — two cards with identical printed costs are not equally expensive if their difficulties differ.

**Per-card columns:**

| Column | Description |
|--------|-------------|
| Card ID | Source: Art 04 §7 |
| Nominal Cost | Resources spent to play the card |
| Base Difficulty | Easy / Average / Challenging (Art 03 §13.3) |
| Success Probability | At base difficulty, no modifiers |
| Cost per Success | Nominal Cost ÷ P(success) |
| Cost per Crit Success | Nominal Cost at the 5% floor — always possible |
| Cost per Crit Fail | Nominal Cost at the 5% ceiling — always possible |
| Expected Cost | Weighted average across all four outcomes at base difficulty |

**Formulae — to be derived, not inherited.** The column definitions above are the specification. The arithmetic is *not yet settled*: a threshold is a d100 value (Art 03 §13.3 — Easy 75, Average 50, Challenging 25), so any expression treating it as a probability is wrong by a factor of 100, and "expected cost weighted across all four outcomes" is a different quantity from "cost per success" rather than a restatement of it. Both errors were present in the inherited draft of this section and are not reproduced here.

What is settled:

- `P(success)` at base difficulty is `threshold / 100`, and the critical bands (Art 03 §13.1–§13.2) put an unconditional 5% floor and 5% ceiling on every roll regardless of the modifier stack.
- Difficulty modifiers (Art 03 §13.4, M-01–M-12) shift probability without changing nominal cost, so the modifier stack applies to the threshold before any per-scenario computation.
- A card's cost is paid whether or not it succeeds (§3), which is why cost-per-success exceeds nominal cost for every card in the system.

**Relationship to §9.** The two are complementary and must not be conflated. §9 prices what a card *delivers* and is computable now. §12 prices what a card *costs to actually land* and needs locked costs and difficulties. Principle 15 asserts these should be proportionate; only §12 can test whether they are.

---
