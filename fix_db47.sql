ALTER TABLE card_status ADD COLUMN is_ring_modifier BOOLEAN DEFAULT FALSE;
UPDATE card_status SET is_ring_modifier = TRUE WHERE card_id LIKE 'STD.MOD.R%';

CREATE OR REPLACE VIEW v_card_faction_layer_balance AS 
SELECT cs.layer AS design_layer, 
sum(case when cs.faction = 'Standard' then 1 else 0 end) AS std_count, 
sum(case when cs.faction = 'Directorate' then 1 else 0 end) AS dir_count, 
sum(case when cs.faction = 'Ghost' then 1 else 0 end) AS gho_count, 
sum(case when cs.faction = 'Guild' then 1 else 0 end) AS gui_count, 
sum(case when cs.faction = 'Network' then 1 else 0 end) AS net_count, 
sum(case when cs.faction = 'Syndicate' then 1 else 0 end) AS syn_count, 
count(0) AS total_cards 
FROM card_status cs 
WHERE cs.blocked = 0 AND cs.layer IS NOT NULL AND cs.is_ring_modifier = FALSE
GROUP BY cs.layer;
