-- ============================================================
-- db_build_portrait.sql  —  THE SIGNAL: Portrait system
-- Session 47
--
-- Adds:
--   1. Portrait track (ID 50)  — non-actionable track on Arbiter Tableau
--   2. Portrait marker (ID 51) — ARBITER-controlled, moves along track only
--   3. tmp_comp_verb_beat rows — ARBITER Move Portrait marker at resolution beats
--   4. tmp_comp_verb_role rows — ARBITER as initiator + executor
--   5. tmp_action primitives   — inserted directly (avoids TRUNCATE/re-derive)
--
-- Beats: resolution windows where portrait movement can be mandated by card
--   beat_id=8  Month 1 — Beat 3 (M1 resolution)
--   beat_id=14 Month 2 — Beat 3 (M2 resolution)
--   beat_id=17 Month 3 — Beat 4 (Political act resolution)
--   beat_id=18 Month 3 — Beat 5 (M3 resolution)
-- ============================================================

-- ============================================================
-- 1. COMPONENTS
-- ============================================================
INSERT INTO tmp_component
  (id, name, actionable, transformable, receivable,
   transform_visibility, transform_orientation, transform_data)
VALUES
  (50, 'Portrait track',   0, 0, 0, 0, 0, 0),
  (51, 'Portrait marker',  1, 0, 0, 0, 0, 0)
ON DUPLICATE KEY UPDATE name = name;

-- ============================================================
-- 2. COMP-VERB-BEAT  (verb 16 = Move)
-- ============================================================
INSERT INTO tmp_comp_verb_beat (component_id, beat_id, verb_id, notes)
VALUES
  (51, 8,  16, 'ARBITER moves Portrait marker per M1 Beat 3 card effect'),
  (51, 14, 16, 'ARBITER moves Portrait marker per M2 Beat 3 card effect'),
  (51, 17, 16, 'ARBITER moves Portrait marker per M3 Beat 4 political act effect'),
  (51, 18, 16, 'ARBITER moves Portrait marker per M3 Beat 5 card effect')
ON DUPLICATE KEY UPDATE notes = notes;

-- ============================================================
-- 3. COMP-VERB-ROLE  (ARBITER-only: initiator + executor)
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, phase_id, role_id, notes)
VALUES
  (51, 16, 1, 2, 'ARBITER initiates Portrait marker Move'),   -- initiator
  (51, 16, 2, 2, 'ARBITER executes Portrait marker Move')     -- executor
ON DUPLICATE KEY UPDATE notes = notes;

-- ============================================================
-- 4. PRIMITIVES — inserted directly into tmp_action
--    trigger_type_id = 4 (rule.card) — card text mandates ARBITER to move
-- ============================================================
INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id,
   subject_id, verb_id, component_id, trigger_type_id, notes)
VALUES
  (8,  'during', NULL, NULL, 2, 16, 51, 4, 'ARBITER moves Portrait marker per M1 Beat 3 card effect'),
  (14, 'during', NULL, NULL, 2, 16, 51, 4, 'ARBITER moves Portrait marker per M2 Beat 3 card effect'),
  (17, 'during', NULL, NULL, 2, 16, 51, 4, 'ARBITER moves Portrait marker per M3 Beat 4 political act effect'),
  (18, 'during', NULL, NULL, 2, 16, 51, 4, 'ARBITER moves Portrait marker per M3 Beat 5 card effect');
