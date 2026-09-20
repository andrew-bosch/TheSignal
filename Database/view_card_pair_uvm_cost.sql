-- v_card_pair_uvm_cost — the working view of the UVM cost model.
--
-- HISTORY: this view existed ONLY in the live DB until S160. No Database/*.sql file
-- defined it, so a rebuild would have silently lost the entire cost model's working
-- view. Captured here as the versioned source of truth; edit this file, then load it.
--   Load:  mariadb the_signal_db < Database/view_card_pair_uvm_cost.sql
--
-- S160 CHANGE (PM05 04-n229): a card whose own Function is Redirect performs ONE
-- transfer, but its two halves (+n place, -n remove) were each billed as a full
-- priced operation. Worse, which two depended on the effect row's `category`:
-- `board_condition` rows took the card's-own-Function path and were charged twice at
-- the Redirect rate (GD-01: 2 x StructureBlock/Redirect = 20.00), while
-- `presence_delta` rows took the magnitude-sign path and were charged Add + Remove
-- (GHO.MOD.7 / NET.MOD.10: 2.00 + 3.44 = 5.44) -- never touching the
-- PresenceToken/Redirect rate that exists for exactly this shape. The `xfer` CTE
-- below collapses matched opposing legs into a single Redirect unit, which fixes the
-- double-count and makes both category paths converge on the same rate.
--
-- S160 CHANGE 2, MADE THEN REVERSED (PM05 04-n234 / 04-n236). The beneficiary axis was
-- briefly wired in here. It is NOT wired in now, and must not be re-wired: Andy's ruling
-- (S160) is that `value_rating` means GROSS EFFECT DELIVERED -- a way to bucket cards by
-- how much of the game they move, so cards affecting more of it sit in higher tiers.
-- Signing each row by who benefits produces a NET LEDGER, a different quantity: it rated
-- GUI.CA.7 (which buys a presence removal for 2 native) and STD.PA.6 (a sanction offset
-- by its own PS cost) as floor-tier for paying a fair price, and it wrongly moved
-- NET.CA.6 3->1 and GUI.PA.10 4->1 before the ruling landed. What the acting faction
-- pays is already recorded by `cost`; it does not belong in the tier as well.
--
-- The signed axis is still built and still useful -- it lives in `v_card_value_to_acting`
-- (Database/view_card_value_to_acting.sql), which is where Art 04c §6 gap #1 is answered.
-- Units below are UNSIGNED magnitude, as they were before the experiment.
--
-- Two findings kept, because they still apply if anyone rewires it: a sign has to be
-- applied at PRICING, not before the collapse below (signing first flips both of a
-- transfer's legs positive and the `xfer` detection, which keys on opposing RAW
-- magnitudes, stops firing); and `district`/`none`/`other` rows must stay unsigned
-- either way, since an unattributed board placement -- GHO.PA.5's 2 chips, whose faction
-- the card never names -- is not a giveaway.
--
-- SCOPED DELIBERATELY to cards whose own Function is Redirect, and StandingMarker is
-- excluded: `standing_delta` rows always map to the verb 'Shift' by design and never
-- sign-infer, so a PS swing up and down is two real movements, not one transfer.
-- (Whether a cross-faction PS swap should be Standing/Redirect is 04-n232, not this.)

CREATE OR REPLACE VIEW v_card_pair_uvm_cost AS
WITH dp AS (
    SELECT ec.card_id, ec.tier,
           CASE ec.tier WHEN 'success' THEN 1.00 ELSE 0.05 END AS tier_weight,
           CASE WHEN ec.category = 'standing_delta' THEN 'StandingMarker'
                WHEN ec.category IN ('board_condition','accord_action','reveal','other')
                     THEN COALESCE(cs2.subject, m.mapped_subject)
                WHEN ec.magnitude IS NULL THEN COALESCE(cs2.subject, m.mapped_subject)
                ELSE m.mapped_subject END AS subject,
           CASE WHEN ec.raw_expr REGEXP 'threshold|apply_modifier|boost\\s*='
                THEN NULL ELSE ec.magnitude END AS usable_magnitude,
           CASE WHEN ec.category = 'standing_delta' THEN 'Shift'
                WHEN ec.category IN ('board_condition','accord_action','reveal','other')
                     THEN cs2.function
                WHEN ec.magnitude IS NULL THEN cs2.function
                WHEN ec.magnitude > 0 THEN 'Add'
                WHEN ec.magnitude < 0 THEN 'Remove'
                ELSE cs2.function END AS verb,
           CASE WHEN ec.raw_expr REGEXP 'n_boost|count\\(|\\.each\\(|declared\\(|n_declared'
                THEN 1 ELSE 0 END AS is_boost,
           cs2.function AS card_function,
           ec.target    AS acts_on
    FROM card_effect_component ec
    LEFT JOIN effect_category_uvm_map m ON m.category = ec.category
    JOIN card_status cs2 ON cs2.card_id = ec.card_id
    WHERE ec.tier IN ('success','successcrit')
      AND (m.mapped_subject IS NOT NULL OR cs2.subject IS NOT NULL)
),
-- (card, subject) pairs on a Redirect card carrying BOTH a positive and a negative
-- leg: the two halves of one transfer.
xfer AS (
    SELECT card_id, subject,
           SUM(CASE WHEN usable_magnitude > 0 THEN tier_weight *  usable_magnitude ELSE 0 END) AS pos,
           SUM(CASE WHEN usable_magnitude < 0 THEN tier_weight * -usable_magnitude ELSE 0 END) AS neg,
           SUM(CASE WHEN usable_magnitude IS NULL THEN tier_weight ELSE 0 END)                 AS nullunits,
           MAX(is_boost) AS any_boost,
           MAX(CASE WHEN tier = 'success' AND ABS(usable_magnitude) > 1 THEN 1 ELSE 0 END) AS any_multiplier,
           -- a transfer is worth +1 unit when the acting faction is the one receiving
           MAX(CASE WHEN usable_magnitude > 0 AND acts_on = 'acting' THEN 1 ELSE 0 END) AS gain_is_acting
    FROM dp
    WHERE card_function = 'Redirect' AND subject IS NOT NULL AND subject <> 'StandingMarker'
    GROUP BY card_id, subject
    HAVING pos > 0 AND neg > 0
),
grp AS (
    -- every (card, subject) NOT identified as a transfer: unchanged behaviour
    SELECT d.card_id, d.subject, d.verb,
           SUM(d.tier_weight * CASE WHEN d.usable_magnitude IS NOT NULL
                                    THEN ABS(d.usable_magnitude) ELSE 1 END) AS weighted_units,
           MAX(d.is_boost) AS any_boost,
           MAX(CASE WHEN d.tier = 'success' AND ABS(d.usable_magnitude) > 1 THEN 1 ELSE 0 END) AS any_multiplier
    FROM dp d
    LEFT JOIN xfer x ON x.card_id = d.card_id AND x.subject = d.subject
    WHERE x.card_id IS NULL
    GROUP BY d.card_id, d.subject, d.verb

    UNION ALL
    -- the transfer itself, billed ONCE
    SELECT card_id, subject, 'Redirect', LEAST(pos,neg) + nullunits, any_boost, any_multiplier
    FROM xfer
    UNION ALL
    -- any unmatched surplus stays a plain Add / Remove
    SELECT card_id, subject, 'Add',    pos - LEAST(pos,neg), any_boost, any_multiplier
    FROM xfer WHERE pos - LEAST(pos,neg) > 0
    UNION ALL
    SELECT card_id, subject, 'Remove', neg - LEAST(pos,neg), any_boost, any_multiplier
    FROM xfer WHERE neg - LEAST(pos,neg) > 0
),
pairs AS (
    SELECT grp.card_id,
           COUNT(0) AS n_distinct_pairs,
           SUM(grp.weighted_units * COALESCE(pa.base_uvm_cost, ua.base_uvm_cost, 0)) AS total_pair_cost,
           SUM(CASE WHEN pa.subject IS NULL THEN 1 ELSE 0 END) AS n_fallback_to_subject_only,
           MAX(grp.any_boost) AS has_boost,
           MAX(grp.any_multiplier) AS has_multipliers
    FROM grp
    LEFT JOIN uvm_pair_assumptions pa ON pa.subject = grp.subject AND pa.function = grp.verb
    LEFT JOIN uvm_assumptions      ua ON ua.subject = grp.subject
    GROUP BY grp.card_id
)
SELECT v.card_id, v.name, cs.faction, cs.card_type,
       v.subject  AS primary_subject,
       v.function AS primary_function,
       v.current_effective_cost,
       COALESCE(pairs.n_distinct_pairs, 0) AS n_distinct_pairs,
       COALESCE(pairs.total_pair_cost, 0)  AS total_pair_cost,
       COALESCE(pairs.n_fallback_to_subject_only, 0) AS n_fallback_to_subject_only,
       ROUND((COALESCE(pairs.total_pair_cost,0) - v.current_effective_cost)
             / NULLIF(pairs.total_pair_cost,0) * 100, 1) AS delta_vs_current_cost,
       COALESCE(pairs.has_boost, 0)       AS has_boost,
       COALESCE(pairs.has_multipliers, 0) AS has_multipliers
FROM v_card_recommended_cost_full v
JOIN card_status cs ON cs.card_id = v.card_id
LEFT JOIN pairs ON pairs.card_id = v.card_id;
