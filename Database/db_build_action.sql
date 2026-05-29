-- ============================================================
-- db_build_action.sql
-- THE SIGNAL — tmp_action table + dispatch case seed
-- Session 47
--
-- Grammar: CONDITION + ASSERTION
--   CONDITION = during [beat_id]
--             | on_close of [beat_id]          (beat_trigger = 'on_close')
--             | after [prereq_id] occurred      (prereq_id FK → tmp_action)
--             | when [prereq_beat_id] closed    (prereq_beat_id FK → tmp_beat)
--
--   ASSERTION = [subject] [verb] [component] → [destination]
--
-- All conditions are AND: reaching a row implies all listed prereqs are satisfied.
-- Beat tracking is electronic-only (L2+); paper game runs this procedurally.
-- game_zones empty at L1 — destination_zone_id nullable, destination_component_id carries it.
-- ============================================================

DROP TABLE IF EXISTS tmp_action;
CREATE TABLE tmp_action (
  id                       INT          NOT NULL AUTO_INCREMENT,
  beat_id                  INT          NOT NULL,
  beat_trigger             ENUM('during','on_close') NOT NULL DEFAULT 'during',
  prereq_id                INT          DEFAULT NULL,
  prereq_beat_id           INT          DEFAULT NULL,
  subject_id               INT          NOT NULL,
  verb_id                  INT          NOT NULL,
  component_id             INT          NOT NULL,
  destination_component_id INT          DEFAULT NULL,
  destination_zone_id      BIGINT       DEFAULT NULL,
  notes                    TEXT,
  PRIMARY KEY (id),
  CONSTRAINT fk_act_beat    FOREIGN KEY (beat_id)                  REFERENCES tmp_beat(id),
  CONSTRAINT fk_act_prereq  FOREIGN KEY (prereq_id)                REFERENCES tmp_action(id),
  CONSTRAINT fk_act_pb      FOREIGN KEY (prereq_beat_id)           REFERENCES tmp_beat(id),
  CONSTRAINT fk_act_subject FOREIGN KEY (subject_id)               REFERENCES tmp_player_role(id),
  CONSTRAINT fk_act_verb    FOREIGN KEY (verb_id)                  REFERENCES tmp_verb(id),
  CONSTRAINT fk_act_comp    FOREIGN KEY (component_id)             REFERENCES tmp_component(id),
  CONSTRAINT fk_act_dest_c  FOREIGN KEY (destination_component_id) REFERENCES tmp_component(id),
  CONSTRAINT fk_act_dest_z  FOREIGN KEY (destination_zone_id)      REFERENCES game_zones(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- SEED: Dispatch Case submission and opening sequence
--
-- A1  Faction places dispatch case on Overview
--     CONDITION: during M1 Dispatch (beat 3); Placement (beat 2) must be closed
--
-- A2  ARBITER opens dispatch case (Reveal)
--     CONDITION: on M1 Dispatch close; A1 must have occurred
--
-- A3  ARBITER removes Target Profile → Arbiter Tableau
-- A4  ARBITER removes Modifier card(s) → Arbiter Tableau
-- A5  ARBITER removes Dispatch token → Backlog
-- A6  ARBITER removes Native resource → Faction Terminal
--     CONDITION (A3-A6): during M1 Countermeasures (beat 4); prereq = A2
--
-- Component IDs: Dispatch case=44, Target Profile=48, Modifier card=11,
--   Dispatch token=12, Native resource=8, The Overview=29,
--   Arbiter Tableau=30, Backlog=33, Faction Terminal=26
-- Beat IDs: Placement=2, M1 Dispatch=3, M1 Countermeasures=4
-- Subject IDs: Faction=1, ARBITER=2
-- Verb IDs: Add=1, Remove=2, Reveal=10
-- ============================================================

INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id, subject_id, verb_id,
   component_id, destination_component_id, destination_zone_id, notes)
VALUES
-- A1
(3, 'during',   NULL, 2, 1, 1,  44, 29,   NULL, 'Faction submits dispatch case to Overview; window = M1 Dispatch'),
-- A2
(3, 'on_close', 1,    3, 2, 10, 44, NULL, NULL, 'ARBITER opens dispatch case; fires on M1 Dispatch close'),
-- A3
(4, 'during',   2,    3, 2, 2,  48, 30,   NULL, 'ARBITER removes Target Profile from case → Arbiter Tableau'),
-- A4
(4, 'during',   2,    3, 2, 2,  11, 30,   NULL, 'ARBITER removes Modifier card(s) from case → Arbiter Tableau'),
-- A5
(4, 'during',   2,    3, 2, 2,  12, 33,   NULL, 'ARBITER removes Dispatch token from case → Backlog'),
-- A6
(4, 'during',   2,    3, 2, 2,   8, 26,   NULL, 'ARBITER removes Native resource from case → Faction Terminal');

-- ============================================================
-- VIEWS
-- ============================================================

-- v_action_chain: full human-readable action chain
CREATE OR REPLACE VIEW v_action_chain AS
SELECT
  a.id,
  b.name                        AS beat,
  a.beat_trigger,
  a.prereq_id,
  pb.name                       AS prereq_beat,
  r.name                        AS subject,
  v.name                        AS verb,
  c.name                        AS component,
  dc.name                       AS destination,
  a.notes
FROM tmp_action a
JOIN  tmp_beat        b  ON a.beat_id                  = b.id
LEFT JOIN tmp_beat    pb ON a.prereq_beat_id            = pb.id
JOIN  tmp_player_role r  ON a.subject_id               = r.id
JOIN  tmp_verb        v  ON a.verb_id                  = v.id
JOIN  tmp_component   c  ON a.component_id             = c.id
LEFT JOIN tmp_component dc ON a.destination_component_id = dc.id
ORDER BY a.beat_id, a.id;

-- v_action_by_beat: summarise actions per beat
CREATE OR REPLACE VIEW v_action_by_beat AS
SELECT
  b.id          AS beat_id,
  b.name        AS beat,
  r.name        AS subject,
  v.name        AS verb,
  c.name        AS component,
  a.beat_trigger,
  a.prereq_id
FROM tmp_action a
JOIN tmp_beat        b ON a.beat_id    = b.id
JOIN tmp_player_role r ON a.subject_id = r.id
JOIN tmp_verb        v ON a.verb_id    = v.id
JOIN tmp_component   c ON a.component_id = c.id
ORDER BY b.id, a.id;

-- v_arbiter_triggered: actions fired by ARBITER as consequence of a prior action
CREATE OR REPLACE VIEW v_arbiter_triggered AS
SELECT
  a.id,
  b.name        AS beat,
  a.beat_trigger,
  pa.id         AS trigger_action_id,
  pv.name       AS trigger_verb,
  pc.name       AS trigger_component,
  v.name        AS verb,
  c.name        AS component,
  dc.name       AS destination
FROM tmp_action a
JOIN tmp_action      pa ON a.prereq_id               = pa.id
JOIN tmp_verb        pv ON pa.verb_id                = pv.id
JOIN tmp_component   pc ON pa.component_id           = pc.id
JOIN tmp_beat        b  ON a.beat_id                 = b.id
JOIN tmp_verb        v  ON a.verb_id                 = v.id
JOIN tmp_component   c  ON a.component_id            = c.id
LEFT JOIN tmp_component dc ON a.destination_component_id = dc.id
WHERE a.subject_id = 2   -- ARBITER
ORDER BY a.beat_id, a.id;
