-- ============================================================
-- db_build_action_v2.sql  —  THE SIGNAL: primitive action library
-- Session 47
--
-- Phase 1: Populate atomic primitives derived from existing taxonomy tables.
--   Source: tmp_comp_verb_beat (what/when) JOIN tmp_comp_verb_role (who)
--   Filter: phase_id=1 (initiator only — who calls for the action)
--   Result: one row per valid (beat, subject, verb, component) combination
--   All prereq fields NULL — these are standalone legal primitives.
--
-- Phase 2 (separate): chain primitives into sequences via prereq_id.
--
-- Grammar per row:
--   "During [beat], [subject] may [verb] [component]"
-- ============================================================

SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE tmp_action;
SET FOREIGN_KEY_CHECKS=1;

-- ============================================================
-- PHASE 1: Primitive actions
-- Derived from tmp_comp_verb_beat × tmp_comp_verb_role (initiators only)
-- ============================================================
INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id,
   subject_id, verb_id, component_id, notes)
SELECT
  cvb.beat_id,
  'during'    AS beat_trigger,
  NULL        AS prereq_id,
  NULL        AS prereq_beat_id,
  cvr.role_id AS subject_id,
  cvb.verb_id,
  cvb.component_id,
  cvb.notes
FROM tmp_comp_verb_beat cvb
JOIN tmp_comp_verb_role cvr
  ON  cvr.component_id = cvb.component_id
  AND cvr.verb_id      = cvb.verb_id
  AND cvr.phase_id     = 1        -- initiator phase only
ORDER BY cvb.beat_id, cvr.role_id, cvb.verb_id, cvb.component_id;

-- ============================================================
-- VIEWS — primitive analysis
-- ============================================================

-- Full readable primitive library
CREATE OR REPLACE VIEW v_primitives AS
SELECT
  a.id,
  b.name  AS beat,
  r.name  AS subject,
  v.name  AS verb,
  c.name  AS component,
  a.notes
FROM tmp_action a
JOIN tmp_beat        b ON a.beat_id      = b.id
JOIN tmp_player_role r ON a.subject_id   = r.id
JOIN tmp_verb        v ON a.verb_id      = v.id
JOIN tmp_component   c ON a.component_id = c.id
WHERE a.prereq_id IS NULL
ORDER BY b.id, r.id, v.name, c.name;

-- What Faction can initiate, by beat
CREATE OR REPLACE VIEW v_faction_primitives AS
SELECT b.name AS beat, v.name AS verb, c.name AS component, a.notes
FROM tmp_action a
JOIN tmp_beat      b ON a.beat_id      = b.id
JOIN tmp_verb      v ON a.verb_id      = v.id
JOIN tmp_component c ON a.component_id = c.id
WHERE a.subject_id = 1 AND a.prereq_id IS NULL
ORDER BY b.id, v.name, c.name;

-- What ARBITER can initiate, by beat
CREATE OR REPLACE VIEW v_arbiter_primitives AS
SELECT b.name AS beat, v.name AS verb, c.name AS component, a.notes
FROM tmp_action a
JOIN tmp_beat      b ON a.beat_id      = b.id
JOIN tmp_verb      v ON a.verb_id      = v.id
JOIN tmp_component c ON a.component_id = c.id
WHERE a.subject_id = 2 AND a.prereq_id IS NULL
ORDER BY b.id, v.name, c.name;

-- Beat × Verb summary: what verbs are active in each beat, by subject
CREATE OR REPLACE VIEW v_beat_verb_summary AS
SELECT
  b.name  AS beat,
  r.name  AS subject,
  v.name  AS verb,
  COUNT(*) AS component_cnt
FROM tmp_action a
JOIN tmp_beat        b ON a.beat_id    = b.id
JOIN tmp_player_role r ON a.subject_id = r.id
JOIN tmp_verb        v ON a.verb_id    = v.id
WHERE a.prereq_id IS NULL
GROUP BY b.id, b.name, r.id, r.name, v.id, v.name
ORDER BY b.id, r.id, v.name;
