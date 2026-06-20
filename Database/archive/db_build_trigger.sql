-- ============================================================
-- db_build_trigger.sql  —  THE SIGNAL: trigger taxonomy
-- Session 47
--
-- Adds:
--   1. tmp_trigger_type  — trigger classification (type + subtype)
--   2. tmp_state_condition     — compound condition group (AND/OR)
--   3. tmp_state_condition_clause — individual state checks within a condition
--   4. ALTER tmp_action  — add trigger_type_id FK
--   5. Status marker     — new component in tmp_component
--
-- Trigger taxonomy:
--   phase     open | during | closed      Phase lifecycle gate
--   rule      card | resolution           Card text or resolution rule mandates action
--   player    introduce_card              Player submits a card into play
--             agreement                   Bilateral consent (trade, Accord)
--             verbal_statement            Player declaration with game effect
--   condition (see tmp_state_condition)         Compound board/game state check
--   cascade   —                           Prereq action occurred (carried by prereq_id)
-- ============================================================

-- ============================================================
-- 1. TRIGGER TYPE TABLE
-- ============================================================
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS tmp_trigger_type;
SET FOREIGN_KEY_CHECKS=1;
CREATE TABLE tmp_trigger_type (
  id      INT         NOT NULL AUTO_INCREMENT,
  type    VARCHAR(20) NOT NULL,
  subtype VARCHAR(30) DEFAULT NULL,
  notes   TEXT,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO tmp_trigger_type (id, type, subtype, notes) VALUES
(1,  'phase',     'open',            'Action fires when a beat opens (entry event)'),
(2,  'phase',     'during',          'Action is valid throughout a beat window'),
(3,  'phase',     'closed',          'Action fires when a beat closes (transition gate)'),
(4,  'rule',      'card',            'Card text mandates the action on resolution — card is a portable mini-rule'),
(5,  'rule',      'resolution',      'Quarter resolution procedure mandates the action — not tied to a specific card'),
(6,  'player',    'introduce_card',  'Player decision to submit or declare a card into play'),
(7,  'player',    'agreement',       'Bilateral consent — trade, Accord counter-proposal, Debrief exchange'),
(8,  'player',    'verbal_statement','Player declaration that has a game effect — passing, conceding, signaling'),
(9,  'state_condition', NULL,         'Compound state check — one or more clauses joined by AND/OR (see tmp_state_condition)'),
(10, 'cascade',   NULL,              'Structural — prior action must have occurred; carried by prereq_id in tmp_action');

-- ============================================================
-- 2. CONDITION TABLE — compound state groups
-- ============================================================
DROP TABLE IF EXISTS tmp_state_condition_clause;
DROP TABLE IF EXISTS tmp_state_condition;

CREATE TABLE tmp_state_condition (
  id              INT         NOT NULL AUTO_INCREMENT,
  description     TEXT        NOT NULL,
  logic_operator  ENUM('AND','OR') NOT NULL DEFAULT 'AND',
  notes           TEXT,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Individual state checks within a condition
-- Multiple clauses within one condition_id are joined by the parent's logic_operator
CREATE TABLE tmp_state_condition_clause (
  id              INT          NOT NULL AUTO_INCREMENT,
  condition_id    INT          NOT NULL,
  component_id    INT          DEFAULT NULL,
  state_key       VARCHAR(50)  NOT NULL,
  operator        ENUM('=','!=','>','<','>=','<=','ALL','ANY') NOT NULL DEFAULT '=',
  value           VARCHAR(100) NOT NULL,
  clause_notes    TEXT,
  PRIMARY KEY (id),
  CONSTRAINT fk_scc_cond FOREIGN KEY (condition_id) REFERENCES tmp_state_condition(id),
  CONSTRAINT fk_scc_comp FOREIGN KEY (component_id) REFERENCES tmp_component(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- STATUS MARKER — must exist before condition clauses reference it
-- ============================================================
INSERT INTO tmp_component
  (id, name, actionable, transformable, receivable,
   transform_visibility, transform_orientation, transform_data)
VALUES
  (49, 'Status marker', 1, 1, 0, 0, 1, 1)
ON DUPLICATE KEY UPDATE name=name;

-- ============================================================
-- SEED: Status marker conditions (first concrete examples)
-- ============================================================

-- Condition: All faction Status markers = Ready (triggers Debrief close)
INSERT INTO tmp_state_condition (id, description, logic_operator, notes) VALUES
(1, 'All faction Status markers = Ready (green)', 'AND',
   'Gate for Debrief close. ARBITER closes Debrief when all players have flipped to Ready. Art 03 Debrief.');

INSERT INTO tmp_state_condition_clause (condition_id, component_id, state_key, operator, value, clause_notes) VALUES
(1, 49, 'flip_state', 'ALL', 'Ready', 'Every faction player''s Status marker must show Ready face — one instance per active faction');

-- Condition: At least one faction Status marker = Discussing (Debrief still open)
INSERT INTO tmp_state_condition (id, description, logic_operator, notes) VALUES
(2, 'Any faction Status marker = Discussing (yellow)', 'OR',
   'Debrief remains open while any faction is still discussing.');

INSERT INTO tmp_state_condition_clause (condition_id, component_id, state_key, operator, value, clause_notes) VALUES
(2, 49, 'flip_state', 'ANY', 'Discussing', 'Any Status marker on Discussing face = Debrief window stays open');

-- ============================================================
-- 3. ALTER tmp_action — add trigger_type_id (idempotent)
-- ============================================================
SET FOREIGN_KEY_CHECKS=0;
ALTER TABLE tmp_action DROP FOREIGN KEY IF EXISTS fk_act_trigger;
ALTER TABLE tmp_action DROP COLUMN IF EXISTS trigger_type_id;
SET FOREIGN_KEY_CHECKS=1;
ALTER TABLE tmp_action
  ADD COLUMN trigger_type_id INT DEFAULT NULL AFTER beat_trigger,
  ADD CONSTRAINT fk_act_trigger FOREIGN KEY (trigger_type_id)
    REFERENCES tmp_trigger_type(id);

-- (Status marker already inserted before condition seed — see above)

-- ============================================================
-- 5. UPDATE tmp_action with trigger types (primitives)
-- Best-fit assignment by beat and context:
--   Upkeep / Beat 5 cleanup = phase.during + rule.resolution
--   Dispatch submission     = player.introduce_card
--   Beat 3 effects          = rule.card (ARBITER executes per card text)
--   Standing marker Move    = rule.card (directed by card / Situation Report)
--   Debrief trades          = player.agreement
--   Phase-boundary opens    = phase.open
-- ============================================================

-- Phase entry / procedural actions (no card involved)
UPDATE tmp_action SET trigger_type_id = 2  -- phase.during
WHERE beat_id IN (1,2,5,6,7,19,20)
  AND subject_id = 2   -- ARBITER procedural
  AND trigger_type_id IS NULL;

-- Standing marker moves at Upkeep and Beat 5 (ARBITER announcement → Faction executes)
UPDATE tmp_action SET trigger_type_id = 5  -- rule.resolution
WHERE component_id = 37 AND beat_id IN (1,18)
  AND trigger_type_id IS NULL;

-- Dispatch submission sequence (Beats 3 + 9) — Faction loads and submits case
UPDATE tmp_action SET trigger_type_id = 6  -- player.introduce_card
WHERE beat_id IN (3,9) AND subject_id = 1
  AND trigger_type_id IS NULL;

-- M3 Declaration — Faction declares or passes Political act
UPDATE tmp_action SET trigger_type_id = 6  -- player.introduce_card
WHERE beat_id = 15 AND subject_id = 1
  AND trigger_type_id IS NULL;

-- Beat 3 and M2 Beat 3 resolution effects — all ARBITER (card-mandated)
UPDATE tmp_action SET trigger_type_id = 4  -- rule.card
WHERE beat_id IN (8,14)
  AND trigger_type_id IS NULL;

-- M3 Beat 4 resolution — ARBITER effects from Political act (card-mandated)
UPDATE tmp_action SET trigger_type_id = 4  -- rule.card
WHERE beat_id = 17 AND subject_id = 2
  AND trigger_type_id IS NULL;

-- M3 Beat 4 Standing marker Move (Faction) — rule.card (Political act effect)
UPDATE tmp_action SET trigger_type_id = 4  -- rule.card
WHERE beat_id = 17 AND subject_id = 1
  AND trigger_type_id IS NULL;

-- Debrief bilateral trades — player.agreement
UPDATE tmp_action SET trigger_type_id = 7  -- player.agreement
WHERE beat_id = 20 AND subject_id = 1
  AND component_id IN (9,8,10)   -- Intel token, Native resource, Accord agreement
  AND trigger_type_id IS NULL;

-- Remaining ARBITER Debrief actions — rule.resolution
UPDATE tmp_action SET trigger_type_id = 5  -- rule.resolution
WHERE beat_id = 20 AND trigger_type_id IS NULL;

-- Remaining unassigned Faction actions — phase.during (default)
UPDATE tmp_action SET trigger_type_id = 2
WHERE trigger_type_id IS NULL;

-- ============================================================
-- VIEW — primitives with trigger type
-- ============================================================
CREATE OR REPLACE VIEW v_primitives_with_trigger AS
SELECT
  a.id,
  b.name                               AS beat,
  CONCAT(tt.type,
         CASE WHEN tt.subtype IS NOT NULL
              THEN CONCAT('.', tt.subtype)
              ELSE '' END)             AS trigger_type,
  r.name                               AS subject,
  v.name                               AS verb,
  c.name                               AS component,
  a.notes
FROM tmp_action a
JOIN tmp_beat        b  ON a.beat_id          = b.id
JOIN tmp_trigger_type tt ON a.trigger_type_id = tt.id
JOIN tmp_player_role r  ON a.subject_id       = r.id
JOIN tmp_verb        v  ON a.verb_id          = v.id
JOIN tmp_component   c  ON a.component_id     = c.id
WHERE a.prereq_id IS NULL
ORDER BY b.id, tt.type, tt.subtype, r.id, v.name, c.name;

-- Trigger distribution summary
CREATE OR REPLACE VIEW v_trigger_summary AS
SELECT
  CONCAT(tt.type,
         CASE WHEN tt.subtype IS NOT NULL
              THEN CONCAT('.', tt.subtype)
              ELSE '' END) AS trigger_type,
  r.name                   AS subject,
  COUNT(*)                 AS cnt
FROM tmp_action a
JOIN tmp_trigger_type tt ON a.trigger_type_id = tt.id
JOIN tmp_player_role  r  ON a.subject_id      = r.id
WHERE a.prereq_id IS NULL
GROUP BY tt.type, tt.subtype, r.id, r.name
ORDER BY tt.type, tt.subtype, r.id;
