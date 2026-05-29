-- ============================================================
-- THE SIGNAL — Taxonomy Dimension Build: Who × When (v2)
-- Session 47
--
-- Adds three-phase role model to the Component × Verb foundation:
--   tmp_player_role    — Faction | ARBITER
--   tmp_role_phase     — initiator | executor | fulfiller
--   tmp_beat           — full 20-phase Quarter sequence
--   tmp_comp_verb_role — Component × Verb × Role × Phase
--   tmp_comp_verb_beat — Component × Verb × Phase (unchanged)
--
-- Role model:
--   initiator  = who calls for the action / commits the card
--   executor   = who physically performs the operation
--   fulfiller  = who validates, adjudicates, and closes the action
--
-- DRAFT DATA — for Andy review and correction.
-- ============================================================

-- ============================================================
-- 1. DROP (clean rebuild)
-- ============================================================
DROP VIEW  IF EXISTS v_split_agency;
DROP VIEW  IF EXISTS v_fulfiller_summary;
DROP VIEW  IF EXISTS v_beat_role_matrix;
DROP VIEW  IF EXISTS v_shared_actions;
DROP VIEW  IF EXISTS v_faction_exclusive;
DROP VIEW  IF EXISTS v_arbiter_exclusive;
DROP VIEW  IF EXISTS v_role_matrix;
DROP TABLE IF EXISTS tmp_comp_verb_beat;
DROP TABLE IF EXISTS tmp_comp_verb_role;
DROP TABLE IF EXISTS tmp_role_phase;
DROP TABLE IF EXISTS tmp_player_role;
DROP TABLE IF EXISTS tmp_beat;

-- ============================================================
-- 2. LOOKUP TABLES
-- ============================================================

CREATE TABLE tmp_player_role (
  id          INT(11)      NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(30)  NOT NULL,
  description VARCHAR(200) NOT NULL
);
INSERT INTO tmp_player_role (name, description) VALUES
  ('Faction', 'A human faction player — initiates via card play or procedural rules'),
  ('ARBITER', 'The ARBITER player — acts as game engine (neutral processing) or as character');

CREATE TABLE tmp_role_phase (
  id          INT(11)      NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(20)  NOT NULL,
  description VARCHAR(200) NOT NULL
);
INSERT INTO tmp_role_phase (name, description) VALUES
  ('initiator', 'Who calls for the action — commits the card, triggers the request, or issues the directive'),
  ('executor',  'Who physically performs the operation — moves the component, alters the value, places the piece'),
  ('fulfiller', 'Who validates, adjudicates, and closes the action — determines outcome and confirms board state');

-- Full 20-phase Quarter sequence.
CREATE TABLE tmp_beat (
  id            INT(11)      NOT NULL PRIMARY KEY,
  name          VARCHAR(60)  NOT NULL,
  month         VARCHAR(4)   NULL     COMMENT 'M1 | M2 | M3 | NULL',
  beat_num      INT(11)      NULL     COMMENT '0-5 for numbered beats; NULL otherwise',
  primary_agent VARCHAR(30)  NOT NULL COMMENT 'Faction | ARBITER | Both',
  description   VARCHAR(200) NOT NULL
);
INSERT INTO tmp_beat VALUES
( 1, 'Upkeep',                      NULL, NULL, 'Both',    'World updates, resources, tokens, initiative, Situation Reports'),
( 2, 'Placement',                   NULL, NULL, 'Both',    'Deployment markers placed; entry requirements enforced; influence levels updated'),
( 3, 'Month 1 — Dispatch',          'M1', NULL, 'Faction', 'Operations assembled, sealed, submitted with Dispatch Tokens'),
( 4, 'Month 1 — Countermeasures',   'M1', NULL, 'Faction', 'Countermeasure cards deployed; handed to ARBITER for Month 1 application'),
( 5, 'Month 1 — Beat 0',            'M1', 0,    'Both',    'The Cases Open: ARBITER opens cases, sorts grid; factions validate submissions'),
( 6, 'Month 1 — Beat 1',            'M1', 1,    'ARBITER', 'Check Active Restrictions: ARBITER removes ops violating restriction cards'),
( 7, 'Month 1 — Beat 2',            'M1', 2,    'Both',    'The Ground Shifts: modifier cards resolve; ARBITER places modifier tokens'),
( 8, 'Month 1 — Beat 3',            'M1', 3,    'ARBITER', 'Covert Operations Resolve: ARBITER resolves each op; board effects applied'),
( 9, 'Month 2 — Dispatch',          'M2', NULL, 'Faction', 'Second covert pass; remaining Dispatch Tokens used'),
(10, 'Month 2 — Countermeasures',   'M2', NULL, 'Faction', 'Countermeasure cards deployed for Month 2'),
(11, 'Month 2 — Beat 0',            'M2', 0,    'Both',    'The Cases Open: Month 2 grid sorted'),
(12, 'Month 2 — Beat 1',            'M2', 1,    'ARBITER', 'Check Active Restrictions: Month 2 grid audited'),
(13, 'Month 2 — Beat 2',            'M2', 2,    'Both',    'The Ground Shifts: Month 2 modifier pass'),
(14, 'Month 2 — Beat 3',            'M2', 3,    'ARBITER', 'Covert Operations Resolve: Month 2 operations resolved'),
(15, 'Month 3 — Declaration',       'M3', NULL, 'Both',    'Political acts declared face-up in initiative order'),
(16, 'Month 3 — Countermeasures',   'M3', NULL, 'Faction', 'Countermeasure cards deployed for Month 3'),
(17, 'Month 3 — Beat 4',            'M3', 4,    'Both',    'Political Acts Resolve: declared acts resolved; board and resource effects applied'),
(18, 'Month 3 — Beat 5',            'M3', 5,    'ARBITER', 'The Table Speaks: ARBITER updates Portrait, Chronicle, Session Timeline, Chorus Activity'),
(19, 'Battlefield Strength',        NULL, NULL, 'ARBITER', 'Contested districts resolved; d10 roll-off; Tension markers cleared'),
(20, 'Debrief',                     NULL, NULL, 'Both',    'Resource and Intel trades; ARBITER Debrief observation; Chorus Question window');

-- ============================================================
-- 3. FACT TABLES
-- ============================================================

-- Component × Verb × Role × Phase
-- PK: (component_id, verb_id, role_id, phase_id)
-- Multiple rows per (component, verb) — one per valid (role, phase) combination.
-- Where a phase has two valid roles (e.g., Both can initiate), two rows exist.
CREATE TABLE tmp_comp_verb_role (
  component_id  INT(11)      NOT NULL,
  verb_id       INT(11)      NOT NULL,
  role_id       INT(11)      NOT NULL,
  phase_id      INT(11)      NOT NULL,
  notes         VARCHAR(200) NULL,
  PRIMARY KEY (component_id, verb_id, role_id, phase_id),
  FOREIGN KEY (component_id) REFERENCES tmp_component(id),
  FOREIGN KEY (verb_id)      REFERENCES tmp_verb(id),
  FOREIGN KEY (role_id)      REFERENCES tmp_player_role(id),
  FOREIGN KEY (phase_id)     REFERENCES tmp_role_phase(id)
);

CREATE TABLE tmp_comp_verb_beat (
  component_id INT(11)      NOT NULL,
  verb_id      INT(11)      NOT NULL,
  beat_id      INT(11)      NOT NULL,
  notes        VARCHAR(200) NULL,
  PRIMARY KEY (component_id, verb_id, beat_id),
  FOREIGN KEY (component_id) REFERENCES tmp_component(id),
  FOREIGN KEY (verb_id)      REFERENCES tmp_verb(id),
  FOREIGN KEY (beat_id)      REFERENCES tmp_beat(id)
);

-- ============================================================
-- 4. ROLE DATA
--
-- Role IDs:  Faction=1, ARBITER=2
-- Phase IDs: initiator=1, executor=2, fulfiller=3
-- Verb IDs:  Add=1, Remove=2, Move=16, Reveal=10,
--            Conceal=14, Flip=15, Corrupt=13
-- ============================================================

-- ============================================================
-- GROUP A: ARBITER owns all three phases
-- Track/system markers and ARBITER-managed documents.
-- No Faction role at any phase.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
-- Pointer marker (34): Add, Remove, Move
(34,1,2,1),(34,1,2,2),(34,1,2,3),
(34,2,2,1),(34,2,2,2),(34,2,2,3),
(34,16,2,1),(34,16,2,2),(34,16,2,3),
-- Activity marker (35)
(35,1,2,1),(35,1,2,2),(35,1,2,3),
(35,2,2,1),(35,2,2,2),(35,2,2,3),
(35,16,2,1),(35,16,2,2),(35,16,2,3),
-- Threshold marker (36)
(36,1,2,1),(36,1,2,2),(36,1,2,3),
(36,2,2,1),(36,2,2,2),(36,2,2,3),
(36,16,2,1),(36,16,2,2),(36,16,2,3),
-- Faction order marker (38)
(38,1,2,1),(38,1,2,2),(38,1,2,3),
(38,2,2,1),(38,2,2,2),(38,2,2,3),
(38,16,2,1),(38,16,2,2),(38,16,2,3),
-- Modifier token (47)
(47,1,2,1),(47,1,2,2),(47,1,2,3),
(47,2,2,1),(47,2,2,2),(47,2,2,3),
(47,16,2,1),(47,16,2,2),(47,16,2,3),
-- Situation Report card (25): Add, Remove, Move, Reveal, Conceal
(25,1,2,1),(25,1,2,2),(25,1,2,3),
(25,2,2,1),(25,2,2,2),(25,2,2,3),
(25,16,2,1),(25,16,2,2),(25,16,2,3),
(25,10,2,1),(25,10,2,2),(25,10,2,3),
(25,14,2,1),(25,14,2,2),(25,14,2,3);

-- ============================================================
-- GROUP B: Faction init + exec, ARBITER fulfill
-- Standard player action: Faction calls for it and does it;
-- ARBITER validates and confirms.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
-- Covert operation (13): Add (submitted to case), Conceal (case sealed)
(13,1,1,1),(13,1,1,2),(13,1,2,3),
(13,14,1,1),(13,14,1,2),(13,14,2,3),
-- Political act (14): Add (declared), Reveal (declared face-up)
(14,1,1,1),(14,1,1,2),(14,1,2,3),
(14,10,1,1),(14,10,1,2),(14,10,2,3),
-- Modifier card (11): Add (assigned to op in case), Conceal (assigned face-down)
(11,1,1,1),(11,1,1,2),(11,1,2,3),
(11,14,1,1),(11,14,1,2),(11,14,2,3),
-- Operative ability (15): Add, Remove, Move, Reveal
(15,1,1,1),(15,1,1,2),(15,1,2,3),
(15,2,1,1),(15,2,1,2),(15,2,2,3),
(15,16,1,1),(15,16,1,2),(15,16,2,3),
(15,10,1,1),(15,10,1,2),(15,10,2,3),
-- Dispatch token (12): Add (placed with op), Move (faction reallocates)
(12,1,1,1),(12,1,1,2),(12,1,2,3),
(12,16,1,1),(12,16,1,2),(12,16,2,3),
-- Dispatch case (44): Add (assembled), Conceal (sealed)
(44,1,1,1),(44,1,1,2),(44,1,2,3),
(44,14,1,1),(44,14,1,2),(44,14,2,3),
-- Target Profile (48): Add (faction submits in case)
(48,1,1,1),(48,1,1,2),(48,1,2,3),
-- Deployment marker (2): Add (Placement phase)
(2,1,1,1),(2,1,1,2),(2,1,2,3);

-- ============================================================
-- GROUP C: Faction init, ARBITER exec, ARBITER fulfill
-- Faction triggers via card; ARBITER physically performs and closes.
-- The "interface zone" — Faction authority, ARBITER execution.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
-- Target Profile (48): Corrupt (faction card directs; ARBITER alters written value)
(48,13,1,1),(48,13,2,2),(48,13,2,3),
-- Intel token (9): Reveal (faction card like C26 directs; ARBITER announces)
(9,10,1,1),(9,10,2,2),(9,10,2,3),
-- Intel token: Corrupt (C20 Misdirection)
(9,13,1,1),(9,13,2,2),(9,13,2,3),
-- Accord agreement (10): Add (P08 Propose Accord — faction initiates; ARBITER creates document)
(10,1,1,1),(10,1,2,2),(10,1,2,3),
-- Accord agreement: Remove (faction breaks covertly via card; ARBITER removes document)
(10,2,1,1),(10,2,2,2),(10,2,2,3),
-- Accord agreement: Reveal (P14 Open Record — faction requests; ARBITER reveals)
(10,10,1,1),(10,10,2,2),(10,10,2,3),
-- Accord agreement: Corrupt (Syndicate doctrine card; ARBITER alters terms)
(10,13,1,1),(10,13,2,2),(10,13,2,3);

-- ============================================================
-- GROUP D: ARBITER init + exec + fulfill (ARBITER game engine actions)
-- Faction has no role at any phase.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
-- Covert operation (13): Move (ARBITER sorts to grid), Remove, Reveal
(13,16,2,1),(13,16,2,2),(13,16,2,3),
(13,2,2,1),(13,2,2,2),(13,2,2,3),
(13,10,2,1),(13,10,2,2),(13,10,2,3),
-- Political act (14): Move, Remove (ARBITER processes and clears)
(14,16,2,1),(14,16,2,2),(14,16,2,3),
(14,2,2,1),(14,2,2,2),(14,2,2,3),
-- Modifier card (11): Move, Remove, Reveal (ARBITER processes from grid)
(11,16,2,1),(11,16,2,2),(11,16,2,3),
(11,2,2,1),(11,2,2,2),(11,2,2,3),
(11,10,2,1),(11,10,2,2),(11,10,2,3),
-- Dispatch token (12): Remove (ARBITER collects post-Beat 3)
(12,2,2,1),(12,2,2,2),(12,2,2,3),
-- Dispatch case (44): Move, Remove, Reveal (ARBITER processes)
(44,16,2,1),(44,16,2,2),(44,16,2,3),
(44,2,2,1),(44,2,2,2),(44,2,2,3),
(44,10,2,1),(44,10,2,2),(44,10,2,3),
-- Target Profile (48): Remove, Reveal, Move (ARBITER processes after resolution)
(48,2,2,1),(48,2,2,2),(48,2,2,3),
(48,10,2,1),(48,10,2,2),(48,10,2,3),
(48,16,2,1),(48,16,2,2),(48,16,2,3),
-- Accord agreement (10): Move, Conceal (ARBITER manages document storage)
(10,16,2,1),(10,16,2,2),(10,16,2,3),
(10,14,2,1),(10,14,2,2),(10,14,2,3),
-- Control flag (6): Remove, Move (ARBITER adjusts when control changes)
(6,2,2,1),(6,2,2,2),(6,2,2,3),
(6,16,2,1),(6,16,2,2),(6,16,2,3),
-- Tension marker (7): Remove (ARBITER clears after Battlefield Strength)
(7,2,2,1),(7,2,2,2),(7,2,2,3);

-- ============================================================
-- GROUP E: Faction init + exec, Faction fulfill
-- Faction-only throughout: pass decisions, Conceal of own cards,
-- bilateral Debrief free actions.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
-- Political act (14): Conceal (pass — faction holds face-down; no ARBITER role)
(14,14,1,1),(14,14,1,2),(14,14,1,3),
-- Operative ability (15): Conceal (faction hides own operative; self-managed)
(15,14,1,1),(15,14,1,2),(15,14,1,3),
-- Native resource (8): free trade in Debrief (bilateral)
(8,16,1,1),(8,16,1,2),(8,16,1,3),
-- Intel token (9): free trade in Debrief (bilateral)
(9,16,1,1),(9,16,1,2),(9,16,1,3);

-- ============================================================
-- GROUP F: Both roles can initiate; executor matches initiator;
-- ARBITER fulfills in-round.
-- Represents contested board state — either role can trigger.
-- ============================================================
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id, notes) VALUES
-- Presence token (1): Add, Remove, Move
(1,1,1,1,'Faction plays card to add presence'),(1,1,1,2,NULL),(1,1,2,3,NULL),
(1,1,2,1,'ARBITER adds per rule consequence'),(1,1,2,2,NULL),
(1,2,1,1,'Faction plays card to remove presence'),(1,2,1,2,NULL),(1,2,2,3,NULL),
(1,2,2,1,'ARBITER removes per rule consequence'),(1,2,2,2,NULL),
(1,16,1,1,'Faction moves presence via card'),(1,16,1,2,NULL),(1,16,2,3,NULL),
(1,16,2,1,'ARBITER moves per rule consequence'),(1,16,2,2,NULL),
-- Structure block (3): Add, Remove, Move
(3,1,1,1,'Faction builds via card'),(3,1,1,2,NULL),(3,1,2,3,NULL),
(3,1,2,1,'ARBITER places per rule consequence'),(3,1,2,2,NULL),
(3,2,1,1,'Faction demolishes via card'),(3,2,1,2,NULL),(3,2,2,3,NULL),
(3,2,2,1,'ARBITER removes per rule consequence'),(3,2,2,2,NULL),
(3,16,1,1,NULL),(3,16,1,2,NULL),(3,16,2,3,NULL),
(3,16,2,1,NULL),(3,16,2,2,NULL),
-- Deployment marker (2): Remove, Move, Flip
(2,2,1,1,'Faction card removes marker'),(2,2,1,2,NULL),(2,2,2,3,NULL),
(2,2,2,1,'ARBITER removes per rule'),(2,2,2,2,NULL),
(2,16,1,1,NULL),(2,16,1,2,NULL),(2,16,2,3,NULL),
(2,16,2,1,NULL),(2,16,2,2,NULL),
(2,15,1,1,'Faction flips to/from Blocked per card effect'),(2,15,1,2,NULL),(2,15,2,3,NULL),
(2,15,2,1,'ARBITER flips to Blocked per Situation Report'),(2,15,2,2,NULL),
-- Established marker (5): Add, Remove, Move
(5,1,1,1,'Faction achieves Established threshold; places own marker'),(5,1,1,2,NULL),(5,1,2,3,NULL),
(5,1,2,1,'ARBITER adds per rule consequence'),(5,1,2,2,NULL),
(5,2,1,1,'Faction drops below threshold; removes own marker'),(5,2,1,2,NULL),(5,2,2,3,NULL),
(5,2,2,1,'ARBITER removes per rule consequence'),(5,2,2,2,NULL),
(5,16,1,1,NULL),(5,16,1,2,NULL),(5,16,2,3,NULL),
(5,16,2,1,NULL),(5,16,2,2,NULL),
-- Control flag (6): Add
(6,1,1,1,'Faction achieves Dominant; places own control flag'),(6,1,1,2,NULL),(6,1,2,3,NULL),
(6,1,2,1,'ARBITER places per rule consequence'),(6,1,2,2,NULL),
-- Tension marker (7): Add, Move
(7,1,1,1,'Faction creates Dominant contest; placing faction updates marker'),(7,1,1,2,NULL),(7,1,2,3,NULL),
(7,1,2,1,'ARBITER adds per rule consequence'),(7,1,2,2,NULL),
(7,16,1,1,NULL),(7,16,1,2,NULL),(7,16,2,3,NULL),
(7,16,2,1,NULL),(7,16,2,2,NULL),
-- Native resource (8): Add, Remove (in-round)
(8,1,1,1,'Faction earns income'),(8,1,1,2,NULL),(8,1,2,3,NULL),
(8,1,2,1,'ARBITER grants per rule/card resolution'),(8,1,2,2,NULL),
(8,2,1,1,'Faction spends resource'),(8,2,1,2,NULL),(8,2,2,3,NULL),
(8,2,2,1,'ARBITER removes as rule consequence'),(8,2,2,2,NULL),
-- Intel token (9): Add, Remove, Conceal
(9,1,1,1,'Faction gathers via C05 or card'),(9,1,1,2,NULL),(9,1,2,3,NULL),
(9,1,2,1,'ARBITER adds per rule/card resolution'),(9,1,2,2,NULL),
(9,2,1,1,'Faction spends or discards intel'),(9,2,1,2,NULL),(9,2,2,3,NULL),
(9,2,2,1,'ARBITER removes per rule'),(9,2,2,2,NULL),
(9,14,1,1,'Faction conceals own intel token'),(9,14,1,2,NULL),(9,14,2,3,NULL),
-- Standing marker (37): Add, Remove, Move
-- Two initiator contexts: Faction plays card (Beat 4); ARBITER directs per event (Upkeep)
-- Executor is always Faction (each player moves own marker)
(37,1,1,1,'Faction initiates via political act effect'),(37,1,1,2,NULL),(37,1,2,3,NULL),
(37,1,2,1,'ARBITER initiates via Situation Report announcement'),
(37,2,1,1,NULL),(37,2,1,2,NULL),(37,2,2,3,NULL),
(37,2,2,1,'ARBITER initiates via rule consequence'),
(37,16,1,1,'Faction moves own Standing marker'),(37,16,1,2,NULL),(37,16,2,3,NULL),
(37,16,2,1,'ARBITER directs Standing marker move');

-- ============================================================
-- 5. BEAT/PHASE DATA (unchanged from v1 — beat_ids updated to 1-20)
-- ============================================================

-- Phase 1 — Upkeep
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(38,16,1,'ARBITER determines initiative; updates Faction order marker'),
(25,1,1, 'ARBITER draws Situation Report / Broadcast Card'),
(25,10,1,'ARBITER places Broadcast Card face-up in Event Zone'),
(37,16,1,'Faction Players move Standing markers per ARBITER announcement'),
(2,15,1, 'ARBITER flips deployment marker to Blocked face per event card'),
(8,1,1,  'Faction Players collect native resource income'),
(12,1,1, 'Faction Players receive Dispatch Tokens from Backlog'),
(11,1,1, 'Faction Players draw Modifier Cards'),
(11,14,1,'Modifier Cards held privately in tableau modifier area');

-- Phase 2 — Placement
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(2,1,2,  'Faction Player places deployment marker on chosen district'),
(2,16,2, 'ARBITER redirects illegal placement'),
(5,1,2,  'Faction updates Established marker if influence threshold reached'),
(5,2,2,  'Faction removes Established marker if influence drops'),
(6,1,2,  'Faction places Control flag if Dominant achieved'),
(6,2,2,  'Faction removes Control flag if Dominant control lost'),
(7,1,2,  'Faction places Tension marker if two factions Dominant in same district'),
(7,2,2,  'Tension marker removed if contest resolves during Placement');

-- Month 1 — Dispatch
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,1,3, 'Faction loads covert operation into dispatch case'),
(11,1,3, 'Faction loads assigned Modifier Card into case with operation'),
(48,1,3, 'Faction loads Target Profile slip into case'),
(12,1,3, 'Faction places Dispatch Token with each operation'),
(8,2,3,  'Faction loads resource payment into case'),
(44,14,3,'Faction seals dispatch case'),
(44,16,3,'Faction transmits sealed case to ARBITER receive queue');

-- Month 1 — Beat 0
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(44,10,5,'ARBITER opens dispatch cases'),
(13,10,5,'ARBITER inspects case contents for validity'),
(48,10,5,'ARBITER reads Target Profile'),
(13,16,5,'ARBITER moves operation to Resolution Grid lane'),
(12,2,5, 'ARBITER removes invalid Token-less submissions'),
(36,1,5, 'ARBITER places threshold marker if operation underpaid'),
(8,2,5,  'ARBITER returns resources from invalid submissions');

-- Month 1 — Beat 1
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,2,6, 'ARBITER removes operations violating active restrictions');

-- Month 1 — Beat 2
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(11,10,7,'ARBITER reveals modifier card from Resolution Grid'),
(11,2,7, 'Modifier card removed after application'),
(47,1,7, 'ARBITER places modifier token on target operation'),
(47,2,7, 'Modifier token removed after Beat 2 processing'),
(13,10,7,'Target operation revealed for modifier application');

-- Month 1 — Beat 3
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,10,8,'ARBITER reveals operation card for resolution'),
(48,13,8,'ARBITER corrupts Target Profile if directed by card effect'),
(13,2,8, 'Operation removed from grid after resolution'),
(36,2,8, 'Threshold marker removed after partial payment check'),
(47,2,8, 'Remaining modifier tokens returned to ARBITER Tableau'),
(12,2,8, 'ARBITER collects Dispatch Tokens'),
(1,1,8,  'Presence token placed on success'),(1,2,8,  'Presence token removed on success'),
(3,1,8,  'Structure block placed'),(3,2,8,  'Structure block removed'),
(2,1,8,  'Deployment marker placed'),(2,2,8,  'Deployment marker removed'),(2,15,8, 'Deployment marker flipped'),
(5,1,8,  'Established marker placed'),(5,2,8,  'Established marker removed'),
(6,1,8,  'Control flag placed'),(6,2,8,  'Control flag removed'),
(7,1,8,  'Tension marker placed'),(7,2,8,  'Tension marker removed'),
(9,1,8,  'Intel token added'),(9,2,8,  'Intel token removed'),
(9,10,8, 'Intel token revealed'),(9,14,8, 'Intel token concealed'),(9,13,8, 'Intel token corrupted'),
(10,1,8, 'Accord created'),(10,2,8, 'Accord broken'),(10,13,8,'Accord corrupted'),
(8,1,8,  'Native resource gained'),(8,2,8,  'Native resource removed');

-- Month 2 — same patterns as Month 1 (beat_ids 9-14 map to phases 9-14)
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,1,9,(SELECT notes FROM (SELECT notes FROM tmp_comp_verb_beat WHERE component_id=13 AND verb_id=1 AND beat_id=3) t)),
(11,1,9,'Faction loads Modifier Card (Month 2)'),(48,1,9,'Faction loads Target Profile (Month 2)'),
(12,1,9,'Faction places Dispatch Token (Month 2)'),(8,2,9,'Faction loads resource payment'),
(44,14,9,'Faction seals dispatch case (Month 2)'),(44,16,9,'Faction transmits case (Month 2)');

INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(44,10,11,'ARBITER opens Month 2 cases'),(13,10,11,'ARBITER inspects contents'),
(48,10,11,'ARBITER reads Target Profile'),(13,16,11,'ARBITER moves op to grid'),
(12,2,11,'ARBITER removes invalid submissions'),(36,1,11,'ARBITER places threshold marker'),
(8,2,11,'ARBITER returns resources from invalid submissions');

INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,2,12,'ARBITER removes Month 2 ops violating restrictions');

INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(11,10,13,'ARBITER reveals Month 2 modifier card'),(11,2,13,'Modifier card removed'),
(47,1,13,'ARBITER places modifier token'),(47,2,13,'Modifier token removed'),
(13,10,13,'Target operation revealed for modifier application');

INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(13,10,14,'ARBITER reveals Month 2 operation'),(48,13,14,'ARBITER corrupts Target Profile if directed'),
(13,2,14,'Operation removed'),(36,2,14,'Threshold marker removed'),(47,2,14,'Modifier tokens returned'),
(12,2,14,'ARBITER collects Month 2 Dispatch Tokens'),
(1,1,14,'Presence placed'),(1,2,14,'Presence removed'),
(3,1,14,'Structure placed'),(3,2,14,'Structure removed'),
(2,1,14,'Marker placed'),(2,2,14,'Marker removed'),(2,15,14,'Marker flipped'),
(5,1,14,'Established placed'),(5,2,14,'Established removed'),
(6,1,14,'Control flag placed'),(6,2,14,'Control flag removed'),
(7,1,14,'Tension placed'),(7,2,14,'Tension removed'),
(9,1,14,'Intel added'),(9,2,14,'Intel removed'),
(9,10,14,'Intel revealed'),(9,14,14,'Intel concealed'),(9,13,14,'Intel corrupted'),
(10,1,14,'Accord created'),(10,2,14,'Accord broken'),(10,13,14,'Accord corrupted'),
(8,1,14,'Resource gained'),(8,2,14,'Resource removed');

-- Month 3 — Declaration
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(14,10,15,'Faction declares political act face-up'),
(14,14,15,'Faction holds political act (pass)');

-- Month 3 — Beat 4
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(14,10,17,'Political act revealed for resolution'),(14,2,17,'Political act removed after resolution'),
(1,1,17,'Presence placed'),(1,2,17,'Presence removed'),
(3,1,17,'Structure placed'),(8,1,17,'Resource added'),(8,2,17,'Resource spent'),
(10,1,17,'Accord created'),(10,10,17,'Accord revealed'),
(37,16,17,'Faction moves Standing marker — Public Standing shift'),
(5,1,17,'Established placed'),(5,2,17,'Established removed'),
(6,1,17,'Control flag placed'),(6,2,17,'Control flag removed'),
(7,1,17,'Tension placed'),(7,2,17,'Tension removed');

-- Month 3 — Beat 5
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(37,16,18,'Faction updates Standing markers per ARBITER Portrait announcement'),
(25,1,18,'ARBITER draws next Situation Report card'),(25,10,18,'Situation Report revealed'),
(34,16,18,'ARBITER advances Session Timeline pointer'),
(35,16,18,'ARBITER updates Chorus Activity marker'),
(13,2,18,'Resolution Grid cleared'),(14,2,18,'Political act slots cleared');

-- Battlefield Strength
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(7,2,19, 'Tension markers removed from resolved contested districts'),
(1,2,19, 'Presence tokens removed from losing faction'),
(6,16,19,'Control flag moved to winning faction'),
(5,16,19,'Established marker updated after resolution');

-- Debrief
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id, notes) VALUES
(8,16,20, 'Resource traded bilaterally — no ARBITER adjudication'),
(9,16,20, 'Intel token traded bilaterally — examination permitted'),
(10,1,20, 'Accord proposed or counter-proposed'),
(37,16,20,'ARBITER delivers Debrief observation; Portrait noted'),
(35,16,20,'ARBITER moves Chorus Activity marker if threshold reached'),
(2,15,20, 'Status markers flipped to Ready when faction signals done');

-- ============================================================
-- 6. ANALYSIS VIEWS
-- ============================================================

-- Full readable matrix
CREATE VIEW v_role_matrix AS
SELECT c.name AS component, v.name AS verb, r.name AS role, p.name AS phase, cvr.notes
FROM tmp_comp_verb_role cvr
JOIN tmp_component  c ON cvr.component_id = c.id
JOIN tmp_verb       v ON cvr.verb_id      = v.id
JOIN tmp_player_role r ON cvr.role_id     = r.id
JOIN tmp_role_phase  p ON cvr.phase_id    = p.id
ORDER BY c.name, v.name, p.id, r.name;

-- ARBITER-exclusive initiators: ARBITER initiates, no Faction initiator row
CREATE VIEW v_arbiter_exclusive AS
SELECT DISTINCT c.name AS component, v.name AS verb
FROM tmp_comp_verb_role cvr
JOIN tmp_component  c ON cvr.component_id = c.id
JOIN tmp_verb       v ON cvr.verb_id      = v.id
WHERE cvr.phase_id = 1 AND cvr.role_id = 2
  AND NOT EXISTS (
    SELECT 1 FROM tmp_comp_verb_role x
    WHERE x.component_id = cvr.component_id
      AND x.verb_id      = cvr.verb_id
      AND x.phase_id     = 1
      AND x.role_id      = 1
  )
ORDER BY c.name, v.name;

-- Faction-exclusive initiators: Faction initiates, no ARBITER initiator row
CREATE VIEW v_faction_exclusive AS
SELECT DISTINCT c.name AS component, v.name AS verb
FROM tmp_comp_verb_role cvr
JOIN tmp_component  c ON cvr.component_id = c.id
JOIN tmp_verb       v ON cvr.verb_id      = v.id
WHERE cvr.phase_id = 1 AND cvr.role_id = 1
  AND NOT EXISTS (
    SELECT 1 FROM tmp_comp_verb_role x
    WHERE x.component_id = cvr.component_id
      AND x.verb_id      = cvr.verb_id
      AND x.phase_id     = 1
      AND x.role_id      = 2
  )
ORDER BY c.name, v.name;

-- Split agency: Faction initiates but ARBITER executes or fulfills
-- This is the "interface zone" — most analytically interesting for category design
CREATE VIEW v_split_agency AS
SELECT DISTINCT c.name AS component, v.name AS verb,
  'Faction' AS initiator,
  MAX(CASE WHEN p.name='executor'  AND r.name='ARBITER' THEN 'ARBITER' ELSE NULL END) AS executor,
  MAX(CASE WHEN p.name='fulfiller' AND r.name='ARBITER' THEN 'ARBITER' ELSE NULL END) AS fulfiller
FROM tmp_comp_verb_role cvr
JOIN tmp_component   c ON cvr.component_id = c.id
JOIN tmp_verb        v ON cvr.verb_id      = v.id
JOIN tmp_player_role r ON cvr.role_id      = r.id
JOIN tmp_role_phase  p ON cvr.phase_id     = p.id
WHERE EXISTS (
  SELECT 1 FROM tmp_comp_verb_role fi
  WHERE fi.component_id = cvr.component_id
    AND fi.verb_id      = cvr.verb_id
    AND fi.phase_id     = 1 AND fi.role_id = 1
)
AND EXISTS (
  SELECT 1 FROM tmp_comp_verb_role ae
  WHERE ae.component_id = cvr.component_id
    AND ae.verb_id      = cvr.verb_id
    AND ae.phase_id     IN (2,3) AND ae.role_id = 2
)
GROUP BY c.name, v.name
ORDER BY c.name, v.name;

-- Fulfiller summary: who closes each action
CREATE VIEW v_fulfiller_summary AS
SELECT c.name AS component, v.name AS verb, r.name AS fulfiller
FROM tmp_comp_verb_role cvr
JOIN tmp_component   c ON cvr.component_id = c.id
JOIN tmp_verb        v ON cvr.verb_id      = v.id
JOIN tmp_player_role r ON cvr.role_id      = r.id
WHERE cvr.phase_id = 3
ORDER BY r.name, c.name, v.name;

-- Full 4D: phase × role_phase × role × component × verb
CREATE VIEW v_beat_role_matrix AS
SELECT
  b.id AS phase_id, b.name AS phase_name, b.month, b.beat_num,
  rp.name AS role_phase, r.name AS role,
  c.name AS component, v.name AS verb, cvb.notes AS beat_notes
FROM tmp_comp_verb_beat  cvb
JOIN tmp_beat            b   ON cvb.beat_id      = b.id
JOIN tmp_component       c   ON cvb.component_id = c.id
JOIN tmp_verb            v   ON cvb.verb_id      = v.id
JOIN tmp_comp_verb_role  cvr ON cvr.component_id = cvb.component_id
                             AND cvr.verb_id     = cvb.verb_id
JOIN tmp_player_role     r   ON cvr.role_id      = r.id
JOIN tmp_role_phase      rp  ON cvr.phase_id     = rp.id
ORDER BY b.id, rp.id, r.name, c.name, v.name;
