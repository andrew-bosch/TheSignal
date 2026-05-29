-- ============================================================
-- db_seed_lookups.sql
-- THE SIGNAL — Seed data for all tmp_ lookup tables
--
-- INSERT IGNORE — safe to re-run; skips existing rows.
-- Run after db_create_tmp_tables.sql on a fresh schema.
-- ============================================================

-- tmp_player_role
INSERT IGNORE INTO `tmp_player_role` (`id`, `name`, `description`) VALUES
  (1, 'Faction',  'A human faction player — initiates via card play or procedural rules'),
  (2, 'ARBITER',  'The ARBITER player — acts as game engine (neutral processing) or as character');

-- tmp_role_phase
INSERT IGNORE INTO `tmp_role_phase` (`id`, `name`, `description`) VALUES
  (1, 'initiator', 'Who calls for the action — commits the card, triggers the request, or issues the directive'),
  (2, 'executor',  'Who physically performs the operation — moves the component, alters the value, places the piece'),
  (3, 'fulfiller', 'Who validates, adjudicates, and closes the action — determines outcome and confirms board state');

-- tmp_verb (id gaps reflect deprecated verbs removed during taxonomy evolution)
INSERT IGNORE INTO `tmp_verb` (`id`, `name`) VALUES
  (1,  'Add'),
  (2,  'Remove'),
  (10, 'Reveal'),
  (13, 'Corrupt'),
  (14, 'Conceal'),
  (15, 'Flip'),
  (16, 'Move'),
  (17, 'Invoke');

-- tmp_beat (fixed set — 20 rows, no AUTO_INCREMENT)
INSERT IGNORE INTO `tmp_beat` (`id`, `name`, `month`, `beat_num`, `primary_agent`, `description`) VALUES
  (1,  'Upkeep',                  NULL, NULL, 'Both',    'World updates, resources, tokens, initiative, Situation Reports'),
  (2,  'Placement',               NULL, NULL, 'Both',    'Deployment markers placed; entry requirements enforced; influence levels updated'),
  (3,  'Month 1 — Dispatch',      'M1', NULL, 'Faction', 'Operations assembled, sealed, submitted with Dispatch Tokens'),
  (4,  'Month 1 — Countermeasures','M1',NULL, 'Faction', 'Countermeasure cards deployed; handed to ARBITER for Month 1 application'),
  (5,  'Month 1 — Beat 0',        'M1', 0,    'Both',    'The Cases Open: ARBITER opens cases, sorts grid; factions validate submissions'),
  (6,  'Month 1 — Beat 1',        'M1', 1,    'ARBITER', 'Check Active Restrictions: ARBITER removes ops violating restriction cards'),
  (7,  'Month 1 — Beat 2',        'M1', 2,    'Both',    'The Ground Shifts: modifier cards resolve; ARBITER places modifier tokens'),
  (8,  'Month 1 — Beat 3',        'M1', 3,    'ARBITER', 'Covert Operations Resolve: ARBITER resolves each op; board effects applied'),
  (9,  'Month 2 — Dispatch',      'M2', NULL, 'Faction', 'Second covert pass; remaining Dispatch Tokens used'),
  (10, 'Month 2 — Countermeasures','M2',NULL, 'Faction', 'Countermeasure cards deployed for Month 2'),
  (11, 'Month 2 — Beat 0',        'M2', 0,    'Both',    'The Cases Open: Month 2 grid sorted'),
  (12, 'Month 2 — Beat 1',        'M2', 1,    'ARBITER', 'Check Active Restrictions: Month 2 grid audited'),
  (13, 'Month 2 — Beat 2',        'M2', 2,    'Both',    'The Ground Shifts: Month 2 modifier pass'),
  (14, 'Month 2 — Beat 3',        'M2', 3,    'ARBITER', 'Covert Operations Resolve: Month 2 operations resolved'),
  (15, 'Month 3 — Declaration',   'M3', NULL, 'Both',    'Political acts declared face-up in initiative order'),
  (16, 'Month 3 — Countermeasures','M3',NULL, 'Faction', 'Countermeasure cards deployed for Month 3'),
  (17, 'Month 3 — Beat 4',        'M3', 4,    'Both',    'Political Acts Resolve: declared acts resolved; board and resource effects applied'),
  (18, 'Month 3 — Beat 5',        'M3', 5,    'ARBITER', 'The Table Speaks: ARBITER updates Portrait, Chronicle, Session Timeline, Chorus Activity'),
  (19, 'Battlefield Strength',    NULL, NULL, 'ARBITER', 'Contested districts resolved; d10 roll-off; Tension markers cleared'),
  (20, 'Debrief',                 NULL, NULL, 'Both',    'Resource and Intel trades; ARBITER Debrief observation; Chorus Question window');

-- tmp_trigger_type
INSERT IGNORE INTO `tmp_trigger_type` (`id`, `type`, `subtype`, `notes`) VALUES
  (1,  'phase',           'open',             'Action fires when a beat opens (entry event)'),
  (2,  'phase',           'during',           'Action is valid throughout a beat window'),
  (3,  'phase',           'closed',           'Action fires when a beat closes (transition gate)'),
  (4,  'rule',            'card',             'Card text mandates the action on resolution — card is a portable mini-rule'),
  (5,  'rule',            'resolution',       'Quarter resolution procedure mandates the action — not tied to a specific card'),
  (6,  'player',          'introduce_card',   'Player decision to submit or declare a card into play'),
  (7,  'player',          'agreement',        'Bilateral consent — trade, Accord counter-proposal, Debrief exchange'),
  (8,  'player',          'verbal_statement', 'Player declaration that has a game effect — passing, conceding, signaling'),
  (9,  'state_condition', NULL,               'Compound state check — one or more clauses joined by AND/OR (see tmp_state_condition)'),
  (10, 'cascade',         NULL,               'Structural — prior action must have occurred; carried by prereq_id in tmp_action');

-- tmp_visibility_scope
INSERT IGNORE INTO `tmp_visibility_scope` (`id`, `code`, `name`, `description`, `status`) VALUES
  (1, 'VS-01', 'Public',          'All players, spectators, public display',                   'Active'),
  (2, 'VS-02', 'Faction-Only',    'All players of that faction',                               'Active'),
  (3, 'VS-03', 'Bilateral',       'Two specific parties + ARBITER',                            'Active'),
  (4, 'VS-04', 'ARBITER-Only',    'ARBITER only; never surfaced directly',                     'Active'),
  (5, 'VS-05', 'Player-Only',     'Single player within a multi-player faction',               'Active'),
  (6, 'VS-06', 'Conditional',     'After a specific reveal mechanism triggers',                'Active'),
  (7, 'VS-07', 'Website-Public',  'Any authenticated player via website',                      'L2+'),
  (8, 'VS-08', 'Website-Private', 'Authenticated player only; personal records',               'L2+');

-- tmp_function
INSERT IGNORE INTO `tmp_function` (`id`, `name`, `description`) VALUES
  (1,  'Add',      'Brings a new element into active play from supply or off-board'),
  (2,  'Remove',   'Takes an element out of active play'),
  (3,  'Redirect', 'Changes ownership, destination, or allegiance of an element'),
  (4,  'Recover',  'Returns a spent, removed, or degraded element to active play'),
  (5,  'Modify',   'Alters a cost, value, or attribute without changing the elements fundamental state'),
  (6,  'Protect',  'Preserves the current state of a target against a named change'),
  (7,  'Block',    'Prevents another action from being initiated or resolving'),
  (8,  'Copy',     'Duplicates another actions effect chain with a new initiating subject'),
  (9,  'Reveal',   'Makes hidden information visible to a named audience'),
  (10, 'Conceal',  'Places information or attribution into a hidden state'),
  (11, 'Shift',    'Moves a track value up or down'),
  (12, 'Corrupt',  'Alters a physically written or recorded value on a component');

-- tmp_layer (FK → tmp_visibility_scope — seed visibility_scope first)
INSERT IGNORE INTO `tmp_layer` (`id`, `name`, `description`, `default_visibility_id`) VALUES
  (1, 'Territory',  'Influence landscape: presence tokens, structures, control flags, spatial markers', 1),
  (2, 'Economy',    'Quantitative holdings: native resources, token counts, card counts, Accord existence', 1),
  (3, 'Information','Qualitative content: token content, written records, attribution, reconnaissance', 6),
  (4, 'Submission', 'What enters the resolution queue: costs, eligibility, blocks, scope', 6),
  (5, 'Resolution', 'd100 system: threshold, modifier stack, difficulty, Battlefield Strength, outcome scale', 6),
  (6, 'Standing',   'Reputation tracks: Public Standing and Portrait', 6);
