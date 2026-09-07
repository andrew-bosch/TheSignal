-- v_card_value_to_acting — S160, PM05 04-n234 / Art 00c gap #1.
--
-- The pricing chain has no beneficiary axis: v_card_pair_uvm_cost sums ABS(magnitude),
-- so a faction paying its own resource down and inflicting that same loss on an
-- opponent price identically, and paying an opponent (SYN.PA.1's 2 Capital per chip)
-- reads as value DELIVERED rather than value spent.
--
-- With `card_effect_component.target` corrected (S160) to name the entity whose
-- holdings the row changes, the missing axis derives directly:
--
--     value_to_acting = magnitude x (+1 acting / -1 target|third_party / 0 otherwise)
--
-- The third branch matters. Signing `district`/`none`/`other` rows negative reads a
-- board placement whose faction the card never names -- GHO.PA.5's
-- `game.add(PresenceToken, to=target_district, count=2)`, a genuine gain -- as though
-- the acting faction had given something away. Those rows carry no beneficiary to
-- reason from, so they contribute 0 and are counted in `n_unattributed_rows` instead
-- of being guessed at.
--
--   acting  +n  -> +n   the acting faction gains
--   acting  -n  -> -n   the acting faction pays (NET.CA.6's -2 PS)
--   target  -n  -> +n   an opponent loses; a benefit (STD.CA.2's structure removal)
--   target  +n  -> -n   the acting faction paid an opponent (SYN.PA.1's capital)
--   third_party +n -> -n  the acting faction gave it away (GUI.CA.3's intel to Directorate)
--
-- DELIBERATELY NOT WIRED into v_card_pair_uvm_cost, and the reason is now stronger than
-- when this view was written. It was briefly wired in at S160 and reverted: Andy's ruling
-- (L376, 04-n236) is that `value_rating` means GROSS EFFECT DELIVERED -- how much of the
-- game a card moves -- not a net ledger. Signing the tier rated pay-to-impose cards as
-- floor-tier for paying a fair price. What the acting faction pays is already recorded by
-- `cost`, and does not belong in the tier as well.
--
-- So this axis answers a COST/BALANCE question ("is this card's price right, and is it
-- spending or receiving?"), not a TIER question. Keep it separate.
--   Load:  mariadb the_signal_db < Database/view_card_value_to_acting.sql

CREATE OR REPLACE VIEW v_card_value_to_acting AS
SELECT e.card_id,
       cs.name,
       cs.card_type,
       SUM(CASE WHEN e.magnitude IS NULL THEN 0
                WHEN e.target = 'acting' THEN
                     (CASE e.tier WHEN 'success' THEN 1.00 ELSE 0.05 END) * e.magnitude
                WHEN e.target IN ('target','third_party') THEN
                     (CASE e.tier WHEN 'success' THEN 1.00 ELSE 0.05 END) * -e.magnitude
                ELSE 0
           END) AS net_signed_units,
       SUM(CASE WHEN e.magnitude IS NULL THEN 0
                ELSE ABS(e.magnitude) END)                    AS abs_units,
       SUM(CASE WHEN e.target = 'acting'      AND e.magnitude < 0 THEN 1 ELSE 0 END) AS n_self_cost_rows,
       SUM(CASE WHEN e.target IN ('target','third_party') AND e.magnitude > 0 THEN 1 ELSE 0 END) AS n_paid_other_rows,
       SUM(CASE WHEN e.target IN ('target','third_party') AND e.magnitude < 0 THEN 1 ELSE 0 END) AS n_opponent_loss_rows,
       SUM(CASE WHEN e.magnitude IS NULL THEN 1 ELSE 0 END)   AS n_unsigned_rows,
       SUM(CASE WHEN e.magnitude IS NOT NULL
                 AND e.target NOT IN ('acting','target','third_party')
                THEN 1 ELSE 0 END)                             AS n_unattributed_rows
FROM card_effect_component e
JOIN card_status cs ON cs.card_id = e.card_id
WHERE e.tier IN ('success','successcrit')
GROUP BY e.card_id, cs.name, cs.card_type;
