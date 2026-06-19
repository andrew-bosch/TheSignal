-- ============================================================
-- seed_comp_cleanup.sql
-- THE SIGNAL — S101 View Cleanup Pass and Seeding
-- ============================================================

START TRANSACTION;

-- Category A + C: Delete container/set components from comp_verb_phase and comp_verb_role
DELETE FROM comp_verb_phase WHERE component_id IN (94, 114, 115, 118, 116, 117, 92, 93, 90, 91, 89, 53, 54, 55, 86, 109, 87, 110);
DELETE FROM comp_verb_role WHERE component_id IN (94, 114, 115, 118, 116, 117, 92, 93, 90, 91, 89, 53, 54, 55, 86, 109, 87, 110);

-- Category B: Seed ARBITER resolution tooling as rule.resolution (trigger_type_id=5)
-- d10 Add/Remove/Flip/Move
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(7, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Month 1 Beat 2 resolution'),
(8, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Month 1 Beat 3 resolution'),
(13, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Month 2 Beat 2 resolution'),
(14, 'during', 5, 2, 1, 119, 'ARBITER rolls d10 during Month 2 Beat 3 resolution'),
(7, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Month 1 Beat 2 resolution'),
(8, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Month 1 Beat 3 resolution'),
(13, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Month 2 Beat 2 resolution'),
(14, 'during', 5, 2, 2, 119, 'ARBITER clears d10 after Month 2 Beat 3 resolution'),
(7, 'during', 5, 2, 15, 119, 'ARBITER flips d10 during Month 1 Beat 2 resolution'),
(8, 'during', 5, 2, 15, 119, 'ARBITER flips d10 during Month 1 Beat 3 resolution'),
(13, 'during', 5, 2, 15, 119, 'ARBITER flips d10 during Month 2 Beat 2 resolution'),
(14, 'during', 5, 2, 15, 119, 'ARBITER flips d10 during Month 2 Beat 3 resolution'),
(7, 'during', 5, 2, 16, 119, 'ARBITER rerolls d10 during Month 1 Beat 2 resolution'),
(8, 'during', 5, 2, 16, 119, 'ARBITER rerolls d10 during Month 1 Beat 3 resolution'),
(13, 'during', 5, 2, 16, 119, 'ARBITER rerolls d10 during Month 2 Beat 2 resolution'),
(14, 'during', 5, 2, 16, 119, 'ARBITER rerolls d10 during Month 2 Beat 3 resolution');

-- Sliders
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(20, 'during', 5, 2, 13, 106, 'ARBITER adjusts ARBITER Threshold Slider during Debrief'),
(20, 'during', 5, 2, 13, 107, 'ARBITER adjusts Faction Threshold Slider during Debrief');

-- Modifier token
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 15, 47, 'ARBITER flips modifier token during Month 1 Beat 3 resolution'),
(14, 'during', 5, 2, 15, 47, 'ARBITER flips modifier token during Month 2 Beat 3 resolution');

-- Category D: Individual gameplay pieces
-- Presence chip (Faction moves to contested district in Battlefield Strength)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(19, 'during', 5, 1, 16, 1, 'Faction relocates Presence chip to contested district during Battlefield Strength resolution (press)');

-- Structure block (Faction removes due to zero influence in phase 17 and 19)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(17, 'during', 9, 1, 2, 3, 'Faction structure block removed due to zero influence state condition'),
(19, 'during', 9, 1, 2, 3, 'Faction structure block removed due to zero influence state condition');

-- Accord agreement Reveal
-- Step A: Add phase 20 to comp_verb_phase first
INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES (10, 10, 20, 'Accord revealed during Debrief');
-- Step B: Insert action
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(20, 'during', 7, 1, 10, 10, 'Faction reveals negotiated Accord agreement during Debrief');

-- Deployment marker (ARBITER Add/Remove in Upkeep conversion)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(1, 'during', 5, 2, 1, 2, 'ARBITER places/adds deployment marker per upkeep conversion'),
(1, 'during', 5, 2, 2, 2, 'ARBITER removes deployment marker per upkeep conversion');

-- DebriefActionCard (Reveal/Remove by ARBITER in Debrief)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(20, 'during', 5, 2, 10, 100, 'ARBITER reveals DebriefActionCard during Debrief'),
(20, 'during', 5, 2, 2, 100, 'ARBITER removes/discards DebriefActionCard during Debrief');

-- Grant Deed (Move/Reveal/Conceal)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 1, 16, 113, 'Faction receives completed Grant Deed in dispatch case'),
(14, 'during', 5, 1, 16, 113, 'Faction receives completed Grant Deed in dispatch case'),
(20, 'during', 5, 2, 16, 113, 'ARBITER distributes completed Grant Deed to Faction hand during Debrief'),
(20, 'during', 2, 1, 10, 113, 'Faction voluntarily reveals completed Grant Deed at Debrief'),
(20, 'during', 2, 1, 14, 113, 'Faction player voluntarily conceals Grant Deed in hand');

-- Notification Slip (Reveal/Conceal)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 1, 10, 95, 'Faction player reveals Notification Slip contents'),
(14, 'during', 5, 1, 10, 95, 'Faction player reveals Notification Slip contents'),
(8, 'during', 5, 2, 10, 95, 'ARBITER reveals Notification Slip contents to player'),
(14, 'during', 5, 2, 10, 95, 'ARBITER reveals Notification Slip contents to player'),
(8, 'during', 5, 2, 14, 95, 'ARBITER conceals/files Notification Slip in terminal'),
(14, 'during', 5, 2, 14, 95, 'ARBITER conceals/files Notification Slip in terminal');

-- Modifier card (Move/Remove/Reveal by ARBITER)
INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
(8, 'during', 5, 2, 16, 11, 'ARBITER moves Modifier card out of resolution queue after execution'),
(14, 'during', 5, 2, 16, 11, 'ARBITER moves Modifier card out of resolution queue after execution'),
(17, 'during', 5, 2, 16, 11, 'ARBITER moves Modifier card out of resolution queue after execution'),
(8, 'during', 5, 2, 2, 11, 'ARBITER removes Modifier card from active play after resolution'),
(14, 'during', 5, 2, 2, 11, 'ARBITER removes Modifier card from active play after resolution'),
(17, 'during', 5, 2, 2, 11, 'ARBITER removes Modifier card from active play after resolution'),
(8, 'during', 5, 2, 10, 11, 'ARBITER reveals Modifier card for resolution'),
(14, 'during', 5, 2, 10, 11, 'ARBITER reveals Modifier card for resolution'),
(17, 'during', 5, 2, 10, 11, 'ARBITER reveals Modifier card for resolution');

COMMIT;
