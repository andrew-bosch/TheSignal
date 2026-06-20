-- ============================================================
-- seed_comp_cleanup_3.sql
-- THE SIGNAL — Session 102 View Seeding and Prohibited Cleanup
-- ============================================================

-- 1. Part A — Prohibited Cleanups (Cleanups)
START TRANSACTION;
DELETE FROM comp_verb_phase WHERE component_id = 106 AND verb_id = 13;
DELETE FROM comp_verb_role WHERE component_id = 106 AND verb_id = 13;

DELETE FROM comp_verb_phase WHERE component_id = 119 AND verb_id = 15;
DELETE FROM comp_verb_role WHERE component_id = 119 AND verb_id = 15;

DELETE FROM comp_verb_phase WHERE component_id = 52 AND verb_id = 10;
DELETE FROM comp_verb_role WHERE component_id = 52 AND verb_id = 10;

DELETE FROM comp_verb_phase WHERE component_id = 8 AND verb_id = 1 AND phase_id IN (8, 14);
DELETE FROM comp_verb_phase WHERE component_id = 8 AND verb_id = 2 AND phase_id IN (8, 14);

DELETE FROM comp_verb_role WHERE component_id = 11 AND verb_id = 16 AND role_id = 1;
COMMIT;


-- 2. Part B — Junction Table Registrations
START TRANSACTION;
INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES 
(119, 1, 7, 'd10 added/rolled during Month 1 Beat 2'),
(119, 1, 13, 'd10 added/rolled during Month 2 Beat 2'),
(119, 2, 7, 'd10 removed/cleared during Month 1 Beat 2'),
(119, 2, 13, 'd10 removed/cleared during Month 2 Beat 2'),
(119, 16, 7, 'd10 moved during Month 1 Beat 2'),
(119, 16, 13, 'd10 moved during Month 2 Beat 2')
ON DUPLICATE KEY UPDATE notes=VALUES(notes);
COMMIT;



-- 3. Part B — Action Seeding
START TRANSACTION;

-- ARBITER Flip Modifier token (47)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(7, 'during', 5, 2, 15, 47, 'ARBITER flips modifier token during Month 1 Beat 2 resolution'),
(13, 'during', 5, 2, 15, 47, 'ARBITER flips modifier token during Month 2 Beat 2 resolution');

-- Faction Move Accord agreement (10)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(20, 'during', 7, 1, 16, 10, 'Faction moves Accord agreement during Debrief');

-- Faction Add / Remove Native resource (8)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 5, 1, 1, 8, 'Faction adds/collects Native resource during Month 3 Beat 4 resolution'),
(17, 'during', 5, 1, 2, 8, 'Faction removes/spends Native resource during Month 3 Beat 4 resolution');

-- ARBITER Add d10 (119)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Month 3 Beat 4 resolution'),
(19, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Battlefield Strength contested resolution');

-- ARBITER Move d10 (119)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 5, 2, 16, 119, 'ARBITER rerolls/moves d10 during Month 3 Beat 4 resolution'),
(19, 'during', 5, 2, 16, 119, 'ARBITER rerolls/moves d10 during Battlefield Strength contested resolution');

-- ARBITER Remove d10 (119)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Month 3 Beat 4 resolution'),
(19, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Battlefield Strength contested resolution');

-- ARBITER Move Accord agreement (10)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 4, 2, 16, 10, 'ARBITER moves Accord agreement per card effect during Month 3 Beat 4');

-- Faction Add Deployment marker (2)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 1, 2, 'Faction places deployment marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 1, 2, 'Faction places deployment marker during Month 2 Beat 3');

-- Faction Add Dominant marker (6)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 1, 6, 'Faction places Dominant marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 1, 6, 'Faction places Dominant marker during Month 2 Beat 3'),
(17, 'during', 2, 1, 1, 6, 'Faction places Dominant marker during Month 3 Beat 4');

-- Faction Add Established marker (5)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 1, 5, 'Faction places Established marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 1, 5, 'Faction places Established marker during Month 2 Beat 3'),
(17, 'during', 2, 1, 1, 5, 'Faction places Established marker during Month 3 Beat 4');

-- Faction Add Presence chip (1)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 1, 1, 1, 'Faction places Presence chip during Month 1 Beat 3'),
(14, 'during', 5, 1, 1, 1, 'Faction places Presence chip during Month 2 Beat 3'),
(17, 'during', 5, 1, 1, 1, 'Faction places Presence chip during Month 3 Beat 4');

-- Faction Add Tension marker (7)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 1, 7, 'Faction places Tension marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 1, 7, 'Faction places Tension marker during Month 2 Beat 3'),
(17, 'during', 2, 1, 1, 7, 'Faction places Tension marker during Month 3 Beat 4');

-- Faction Flip Deployment marker (2)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 15, 2, 'Faction flips deployment marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 15, 2, 'Faction flips deployment marker during Month 2 Beat 3');

-- Faction Remove Deployment marker (2)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 1, 2, 2, 'Faction removes/returns deployment marker during Month 1 Beat 3'),
(14, 'during', 5, 1, 2, 2, 'Faction removes/returns deployment marker during Month 2 Beat 3');

-- Faction Remove Established marker (5)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 2, 5, 'Faction removes Established marker during Month 1 Beat 3'),
(14, 'during', 2, 1, 2, 5, 'Faction removes Established marker during Month 2 Beat 3'),
(17, 'during', 2, 1, 2, 5, 'Faction removes Established marker during Month 3 Beat 4');

-- Faction Remove Presence chip (1)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 2, 1, 2, 1, 'Faction removes Presence chip during Month 1 Beat 3'),
(14, 'during', 2, 1, 2, 1, 'Faction removes Presence chip during Month 2 Beat 3'),
(17, 'during', 2, 1, 2, 1, 'Faction removes Presence chip during Month 3 Beat 4');

-- Faction Reveal Political act (14)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 6, 1, 10, 14, 'Faction reveals Political act for resolution during Month 3 Beat 4');

COMMIT;
