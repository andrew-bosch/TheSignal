-- ============================================================
-- db_build_gap1_standing_marker.sql  —  THE SIGNAL: Gap 1 fix
-- Session 47
--
-- Gap: Standing marker Move absent from M1 Beat 3 (beat_id=8)
--      and M2 Beat 3 (beat_id=14).
--
-- At Beat 3 resolution, ARBITER executes all card effects EXCEPT
-- Standing marker movement, which is publicly executed by Faction
-- per card mandate. Subject = Faction; trigger_type = rule.card.
-- ============================================================

-- ============================================================
-- 1. TAXONOMY — add beat coverage
-- ============================================================
INSERT INTO tmp_comp_verb_beat (component_id, beat_id, verb_id, notes)
VALUES
  (37, 8,  16, 'Faction publicly moves Standing marker per M1 Beat 3 card effect'),
  (37, 14, 16, 'Faction publicly moves Standing marker per M2 Beat 3 card effect')
ON DUPLICATE KEY UPDATE notes = notes;

-- ============================================================
-- 2. PRIMITIVES — Faction subject (Beat 3 exception)
--    trigger_type_id = 4 (rule.card)
-- ============================================================
INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id,
   subject_id, verb_id, component_id, trigger_type_id, notes)
VALUES
  (8,  'during', NULL, NULL, 1, 16, 37, 4, 'Faction moves Standing marker per M1 Beat 3 card mandate — public exception to ARBITER-executed beat'),
  (14, 'during', NULL, NULL, 1, 16, 37, 4, 'Faction moves Standing marker per M2 Beat 3 card mandate — public exception to ARBITER-executed beat');
