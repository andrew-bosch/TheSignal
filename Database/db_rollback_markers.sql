START TRANSACTION;

-- Delete actions associated with the markers
DELETE FROM action WHERE component_id IN (98, 99);

-- Delete comp_verb_role rows
DELETE FROM comp_verb_role WHERE component_id IN (98, 99);

-- Delete comp_verb_beat rows
DELETE FROM comp_verb_beat WHERE component_id IN (98, 99);

-- Delete components
DELETE FROM component WHERE id IN (98, 99);

-- Reset auto_increment to 98
ALTER TABLE component AUTO_INCREMENT = 98;

COMMIT;
