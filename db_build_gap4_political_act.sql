-- ============================================================
-- db_build_gap4_political_act.sql  —  THE SIGNAL: Gap 4 fix
-- Session 47
--
-- Gap: ARBITER Add Political act absent from M1 Beat 3 (beat_id=8)
--      and M2 Beat 3 (beat_id=14).
--
-- C09 card effect: ARBITER places a free Political act (Accord card)
-- during Beat 3 resolution. ARBITER is the initiator and executor
-- here — not Faction.
-- ============================================================

-- ============================================================
-- 1. TAXONOMY — ARBITER as initiator for Add on Political act
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, phase_id, role_id, notes)
VALUES
  (14, 1, 1, 2, 'ARBITER adds Political act per card effect (C09 free Accord)')
ON DUPLICATE KEY UPDATE notes = notes;

-- ============================================================
-- 2. TAXONOMY — beat coverage
-- ============================================================
INSERT INTO tmp_comp_verb_beat (component_id, beat_id, verb_id, notes)
VALUES
  (14, 8,  1, 'ARBITER adds Political act per M1 Beat 3 card effect (C09)'),
  (14, 14, 1, 'ARBITER adds Political act per M2 Beat 3 card effect (C09)')
ON DUPLICATE KEY UPDATE notes = notes;

-- ============================================================
-- 3. PRIMITIVES
--    trigger_type_id = 4 (rule.card)
-- ============================================================
INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id,
   subject_id, verb_id, component_id, trigger_type_id, notes)
VALUES
  (8,  'during', NULL, NULL, 2, 1, 14, 4, 'ARBITER adds Political act (Accord card) per M1 Beat 3 card effect — C09'),
  (14, 'during', NULL, NULL, 2, 1, 14, 4, 'ARBITER adds Political act (Accord card) per M2 Beat 3 card effect — C09');
