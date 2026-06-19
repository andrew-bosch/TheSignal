-- ============================================================
-- seed_comp_cleanup_2.sql
-- THE SIGNAL — S101 View Seeding Pass and Prohibited Cleanup
-- ============================================================

-- 1. Clean up prohibited combinations from junction tables
START TRANSACTION;
DELETE FROM comp_verb_role WHERE component_id = 3 AND verb_id = 16 AND role_id = 1;
DELETE FROM comp_verb_role WHERE component_id = 9 AND verb_id = 1 AND role_id = 1;

DELETE FROM comp_verb_role WHERE component_id = 42 AND verb_id IN (1, 2, 16);
DELETE FROM comp_verb_phase WHERE component_id = 42 AND verb_id IN (1, 2, 16);

DELETE FROM comp_verb_role WHERE component_id = 106 AND verb_id IN (1, 2);
DELETE FROM comp_verb_phase WHERE component_id = 106 AND verb_id IN (1, 2);

DELETE FROM comp_verb_role WHERE component_id = 17 AND verb_id IN (1, 2, 14, 16);
DELETE FROM comp_verb_phase WHERE component_id = 17 AND verb_id IN (1, 2, 14, 16);

DELETE FROM comp_verb_role WHERE component_id = 107 AND verb_id IN (1, 2, 13, 16);
DELETE FROM comp_verb_phase WHERE component_id = 107 AND verb_id IN (1, 2, 13, 16);
COMMIT;


-- 2. Register missing phase associations in comp_verb_phase
START TRANSACTION;
INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES (100, 1, 20, 'DebriefActionCard introduced during Debrief');

INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES 
(10, 16, 20, 'Accord agreement moved during Debrief'),
(10, 16, 17, 'Faction moves Accord to Accord Placement Area during Month 3 Beat 4');

INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES
(96, 10, 8, 'Intel Delivery Slip revealed during Month 1 Beat 3'),
(96, 10, 14, 'Intel Delivery Slip revealed during Month 2 Beat 3'),
(96, 14, 20, 'Intel Delivery Slip concealed during Debrief');
COMMIT;


-- 3. Seed actions for permitted combinations
START TRANSACTION;

-- ARBITER Add DebriefActionCard (100)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 1, 100, 'ARBITER introduces/adds DebriefActionCard during Month 1 Beat 3'),
(14, 'during', 5, 2, 1, 100, 'ARBITER introduces/adds DebriefActionCard during Month 2 Beat 3'),
(20, 'during', 5, 2, 1, 100, 'ARBITER introduces DebriefActionCard from supply during Debrief');

-- ARBITER Conceal DebriefActionCard (100)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 14, 100, 'ARBITER places DebriefActionCard in dispatch packet during Month 1 Beat 3'),
(14, 'during', 5, 2, 14, 100, 'ARBITER places DebriefActionCard in dispatch packet during Month 2 Beat 3');

-- ARBITER Corrupt DebriefActionCard (100)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 13, 100, 'ARBITER writes fields on DebriefActionCard during Month 1 Beat 3'),
(14, 'during', 5, 2, 13, 100, 'ARBITER writes fields on DebriefActionCard during Month 2 Beat 3'),
(20, 'during', 5, 2, 13, 100, 'ARBITER writes fields on DebriefActionCard during Debrief');

-- ARBITER Move DebriefActionCard (100)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 16, 100, 'ARBITER moves/delivers DebriefActionCard to Faction hand during Month 1 Beat 3'),
(14, 'during', 5, 2, 16, 100, 'ARBITER moves/delivers DebriefActionCard to Faction hand during Month 2 Beat 3'),
(20, 'during', 5, 2, 16, 100, 'ARBITER delivers DebriefActionCard to Faction hand during Debrief');

-- ARBITER Move Accord agreement (10)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 4, 2, 16, 10, 'ARBITER moves Accord agreement per card effect during Month 1 Beat 3'),
(14, 'during', 4, 2, 16, 10, 'ARBITER moves Accord agreement per card effect during Month 2 Beat 3'),
(20, 'during', 5, 2, 16, 10, 'ARBITER moves completed Accord agreement to Accord Placement Area during Debrief');

-- ARBITER Move ARBITER Threshold Slider (106)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 16, 106, 'ARBITER adjusts ARBITER Threshold Slider during Month 1 Beat 3 resolution'),
(14, 'during', 5, 2, 16, 106, 'ARBITER adjusts ARBITER Threshold Slider during Month 2 Beat 3 resolution'),
(17, 'during', 5, 2, 16, 106, 'ARBITER adjusts ARBITER Threshold Slider during Month 3 Beat 4 resolution');

-- ARBITER Move Presence chip (1)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 4, 2, 16, 1, 'ARBITER moves Presence chip per card effect during Month 1 Beat 3'),
(14, 'during', 4, 2, 16, 1, 'ARBITER moves Presence chip per card effect during Month 2 Beat 3'),
(17, 'during', 4, 2, 16, 1, 'ARBITER moves Presence chip per card effect during Month 3 Beat 4');

-- ARBITER Move Structure block (3)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 4, 2, 16, 3, 'ARBITER moves Structure block per card effect during Month 1 Beat 3'),
(14, 'during', 4, 2, 16, 3, 'ARBITER moves Structure block per card effect during Month 2 Beat 3'),
(17, 'during', 4, 2, 16, 3, 'ARBITER moves Structure block per card effect during Month 3 Beat 4');

-- Faction Conceal Intel Delivery Slip (96)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 8, 1, 14, 96, 'Faction player voluntarily conceals Intel Delivery Slip during Month 1 Beat 3'),
(14, 'during', 8, 1, 14, 96, 'Faction player voluntarily conceals Intel Delivery Slip during Month 2 Beat 3'),
(20, 'during', 8, 1, 14, 96, 'Faction player voluntarily conceals Intel Delivery Slip during Debrief');

-- Faction Reveal Intel Delivery Slip (96)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 8, 1, 10, 96, 'Faction player voluntarily reveals Intel Delivery Slip during Month 1 Beat 3'),
(14, 'during', 8, 1, 10, 96, 'Faction player voluntarily reveals Intel Delivery Slip during Month 2 Beat 3'),
(20, 'during', 8, 1, 10, 96, 'Faction player voluntarily reveals Intel Delivery Slip during Debrief');

-- Faction Move Accord agreement (10)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 4, 1, 16, 10, 'Faction moves Accord agreement per card effect during Month 1 Beat 3'),
(14, 'during', 4, 1, 16, 10, 'Faction moves Accord agreement per card effect during Month 2 Beat 3'),
(17, 'during', 7, 1, 16, 10, 'Faction moves Accord agreement from Terminal to Accord Placement Area during Month 3 Beat 4');

-- Faction Add Accord agreement (10)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 4, 1, 1, 10, 'Faction initiates/adds Accord agreement per card effect during Month 1 Beat 3'),
(14, 'during', 4, 1, 1, 10, 'Faction initiates/adds Accord agreement per card effect during Month 2 Beat 3'),
(17, 'during', 4, 1, 1, 10, 'Faction initiates/adds Accord agreement per card effect during Month 3 Beat 4');

COMMIT;
