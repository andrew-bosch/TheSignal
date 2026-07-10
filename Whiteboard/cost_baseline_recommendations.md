# The Signal: Cost Baseline & value_rating Derivation

*Drafted S76 (agy). Rewritten S143 (Claude/Andy) — the original verb-multiplier model was tested against real card data and rejected; this version reflects what actually held up.*

## Goal

Everything in this document is in service of one thing: assigning **`value_rating`** (1–4) to every CA/PA/ModReact card — a floor-to-ceiling power tier (1 = basic/floor action, 4 = end-game-power card), consistent across the whole set. The pricing/UVM work isn't the deliverable; it's the evidence base for that tier assignment.

---

## 1. What agy originally proposed (S76) — superseded

The original model: `recommended_effective_cost = Base Subject Value × Function Multiplier × Certainty Tax`, with a fixed verb-multiplier table (Add=1.0x, Remove=1.5x, Redirect=2.5x, Protect=0.75x) applied to a single per-Subject baseline (PresenceToken=2.0, from Town Hall).

**Tested against real data (S143) and rejected.** Comparing the same Subject under different Functions with n≥2 samples each, the Remove/Add ratio ranges from **1.15x (StructureBlock) to 8.58x (NativeResource)** — no universal multiplier fits any subject consistently. Verb "premium" is subject-specific, not a fixed ratio you can apply generically.

## 2. What replaced it: pair-based pricing

Instead of decomposing cost into `subject-value × verb-multiplier`, treat **(Subject, Function) as one atomic priced unit**, calibrated directly from real card data:

- **`uvm_assumptions`** — per-Subject baseline (28 Subjects, tiered `validated`/`single_example`/`fallback_avg` by sample size). Used as a fallback when a specific pair has no data.
- **`uvm_pair_assumptions`** — 58 real `(subject, function)` pairs, per-unit normalized (divides by magnitude — critical fix, since raw averaging silently blended 1-unit and 2-unit cards together).
- **`v_card_pair_uvm_cost`** — the working view. Infers a verb per effect row (magnitude sign for delta-style effects; `Shift` always for StandingMarker, which has no Add/Remove convention; the card's own declared Function when there's no clean per-row signal), dedupes to distinct pairs per card, sums each pair's calibrated value × its actual magnitude, folds in `successcrit` at a flat 5% weight (crit-success is an unconditional floor per Pillar 4.8b, not conditional on threshold), excludes `failcrit` entirely (mutually exclusive with success — this view specifically answers "what does success cost").
- **Key columns:** `total_pair_cost` (model's estimate of the card's raw worth), `delta_vs_current_cost` (as a **percentage**: `(total_pair_cost − current_effective_cost) / total_pair_cost × 100` — normalizes miss-magnitude by scale, so outliers are comparable across cheap and expensive cards), `has_boost`, `has_multipliers`, `n_fallback_to_subject_only`.

**Current fit:** 129 paid cards (72 `cost=None` cards excluded from the percentage metric — dividing by their own zero cost always shows a trivial +100%, not a real signal). Of the 129: 34 within ±10% (well-calibrated), 30 at 10–30%, 34 at 30–60%, **31 genuine outliers over 60%** — these are the redesign candidates below.

---

## 3. Redesign needs identified (S143 outlier review)

Concrete, actionable items surfaced by comparing `total_pair_cost` against `current_effective_cost`:

- [ ] **SYN.CA.8 Land Title / GUI.CA.10 Development Order — reprice.** Both deliver GD-01 Grant Deed, which was just redesigned (v0.3→v0.4, added a 3rd fire effect: remove the triggering faction's structure block). Deed's raw value nearly doubled (4.20→8.20). Land Title (5 Capital) and Development Order (3 Capacity + 1 district-native) are both now more underpriced than before. **Not recalculated mechanically** — Capital's own UVM rate (8.75) is a single-example, too thin to extrapolate a specific number from. Needs Andy's judgment once Capital/Capacity have better calibration, or a felt-sense number now.
- [ ] **SYN.PA.1 Acquisition Offer — underpriced**, confirmed (+89.6% delta, priced well below its 5-effect ElectPlayer payoff).
- [ ] **GUI.PA.9 City Ledger / SYN.CA.9 Hostile Takeover — underpriced for their potential.** Both `has_boost` (board-state-dependent variable count), so their true upside isn't captured by a fixed-magnitude model at all — current pricing reflects only a floor case, not the real potential.
- [ ] **GHO.CA.2 Intercept — overpriced**, confirmed (−107.5%). Andy's read: needs a **threshold or success-effect redesign**, not a cost change.
- [ ] **STD.CA.15 Intel Extraction — needs threshold redesign** specifically (not cost).
- [ ] **The 5-cluster** (`DIR.MOD.6`, `NET.CA.4`, `STD.CA.6`, `STD.CA.7`, all landing at ~−100%, i.e. costing ~2x model baseline): all four are `PublicAct/Modify` cards that alter *another action's* cost/threshold/impact rather than deliver a countable resource. `DIR.MOD.6`/`NET.CA.4` are persistent/broad-scope (Seasonal, affects all future opposing PAs district-wide); `STD.CA.6`/`STD.CA.7` are one-shot single-target tweaks. All four get the same generic `PublicAct/Modify` baseline (1.00, n=9) regardless of that scope difference. This is a **model resolution limit**, not a data bug — supports the underpriced read, especially for the persistent two. (`GHO.CA.5` was in the same cluster but is unrelated — just a thin IntelToken/Corrupt calibration, n=2.)

## 4. Open modeling gaps (not card redesigns — the pricing model itself needs more work)

- **Self-cost vs. delivered-value confusion.** `NET.CA.6` Sacrifice correctly pays its cost via `faction(acting).standing -= 2` in the success field (PS isn't a valid `cost`-field value per schema convention — this is right). But the pricing model has no way to distinguish "the acting faction sacrificing their own Standing as payment" from "inflicting Standing loss on an opponent as a delivered effect" — both look like the same mutation, and the model currently prices the self-sacrifice as if it were a benefit. Needs a fix (likely: any success-tier mutation targeting the *acting* faction's own resource downward should subtract from total_pair_cost, or be treated as additional cost, not added value) before the model can be trusted on cards using this pattern.
- **`PublicAct/Modify` (and likely other Function categories) bundle wildly different effect scopes** under one flat per-pair value — see the 5-cluster above. A persistent, all-opponents rule change and a one-shot single-card nudge get priced identically. No fix proposed yet; flagging that `(Subject, Function)` alone may not be enough resolution for every Function.

## 5. Next step toward actual `value_rating` assignment

Once the redesign needs above are addressed (or at least acknowledged as known-soft), the natural next move is bucketing `total_pair_cost` (or a redesign-corrected version of it) into 4 tiers — floor/basic through end-game ceiling. Tier boundaries not yet proposed; that's a design call once the outlier list above stops moving.
