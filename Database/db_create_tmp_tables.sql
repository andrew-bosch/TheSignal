-- ============================================================
-- db_create_tmp_tables.sql
-- THE SIGNAL — Canonical DDL for all tmp_ workspace tables
--
-- Use: CREATE TABLE IF NOT EXISTS — safe to run on existing DB.
-- For full wipe+rebuild, use db_rebuild.sh instead.
-- Dependency order: referenced tables before referencing tables.
-- ============================================================

SET FOREIGN_KEY_CHECKS = 0;

-- ── Tier 1: no tmp_ dependencies ─────────────────────────────

CREATE TABLE IF NOT EXISTS `tmp_player_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_role_phase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_verb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_beat` (
  `id` int(11) NOT NULL,
  `name` varchar(60) NOT NULL,
  `month` varchar(4) DEFAULT NULL COMMENT 'M1 | M2 | M3 | NULL',
  `beat_num` int(11) DEFAULT NULL COMMENT '0-5 for numbered beats; NULL otherwise',
  `primary_agent` varchar(30) NOT NULL COMMENT 'Faction | ARBITER | Both',
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `actionable` tinyint(1) NOT NULL DEFAULT 0,
  `transformable` tinyint(1) NOT NULL DEFAULT 0,
  `receivable` tinyint(1) NOT NULL DEFAULT 0,
  `transform_visibility` tinyint(1) NOT NULL DEFAULT 0,
  `transform_orientation` tinyint(1) NOT NULL DEFAULT 0,
  `transform_data` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_trigger_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `subtype` varchar(30) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_function` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_condition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text NOT NULL,
  `logic_operator` enum('AND','OR') NOT NULL DEFAULT 'AND',
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_state_condition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text NOT NULL,
  `logic_operator` enum('AND','OR') NOT NULL DEFAULT 'AND',
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_visibility_scope` (
  `id` tinyint(3) unsigned NOT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(40) NOT NULL,
  `description` varchar(200) NOT NULL,
  `status` enum('Active','L2+') NOT NULL DEFAULT 'Active',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Deprecated — drop after Art 04b sign-off (DB-16)
CREATE TABLE IF NOT EXISTS `tmp_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Deprecated — drop after Art 04b sign-off (DB-16)
CREATE TABLE IF NOT EXISTS `tmp_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ── Tier 2: depends on Tier 1 ────────────────────────────────

CREATE TABLE IF NOT EXISTS `tmp_layer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  `default_visibility_id` tinyint(3) unsigned NOT NULL COMMENT 'FK → tmp_visibility_scope.id (VS-xx); split layers use VS-06 Conditional as default',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_layer_visibility` (`default_visibility_id`),
  CONSTRAINT `fk_layer_visibility` FOREIGN KEY (`default_visibility_id`) REFERENCES `tmp_visibility_scope` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_comp_verb_beat` (
  `component_id` int(11) NOT NULL,
  `verb_id` int(11) NOT NULL,
  `beat_id` int(11) NOT NULL,
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`beat_id`),
  KEY `verb_id` (`verb_id`),
  KEY `beat_id` (`beat_id`),
  CONSTRAINT `tmp_comp_verb_beat_ibfk_1` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `tmp_comp_verb_beat_ibfk_2` FOREIGN KEY (`verb_id`) REFERENCES `tmp_verb` (`id`),
  CONSTRAINT `tmp_comp_verb_beat_ibfk_3` FOREIGN KEY (`beat_id`) REFERENCES `tmp_beat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_comp_verb_role` (
  `component_id` int(11) NOT NULL,
  `verb_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `phase_id` int(11) NOT NULL,
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`role_id`,`phase_id`),
  KEY `verb_id` (`verb_id`),
  KEY `role_id` (`role_id`),
  KEY `phase_id` (`phase_id`),
  CONSTRAINT `tmp_comp_verb_role_ibfk_1` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `tmp_comp_verb_role_ibfk_2` FOREIGN KEY (`verb_id`) REFERENCES `tmp_verb` (`id`),
  CONSTRAINT `tmp_comp_verb_role_ibfk_3` FOREIGN KEY (`role_id`) REFERENCES `tmp_player_role` (`id`),
  CONSTRAINT `tmp_comp_verb_role_ibfk_4` FOREIGN KEY (`phase_id`) REFERENCES `tmp_role_phase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Note: tmp_action also has FKs to legacy tables game_zones (destination_zone_id).
-- game_zones must exist before this table can be created in a fresh environment.
CREATE TABLE IF NOT EXISTS `tmp_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `beat_id` int(11) NOT NULL,
  `beat_trigger` enum('during','on_close') NOT NULL DEFAULT 'during',
  `trigger_type_id` int(11) DEFAULT NULL,
  `prereq_id` int(11) DEFAULT NULL,
  `prereq_beat_id` int(11) DEFAULT NULL,
  `source_action_id` int(11) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `verb_id` int(11) NOT NULL,
  `component_id` int(11) DEFAULT NULL,
  `destination_component_id` int(11) DEFAULT NULL,
  `destination_zone_id` bigint(20) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_act_beat` (`beat_id`),
  KEY `fk_act_prereq` (`prereq_id`),
  KEY `fk_act_pb` (`prereq_beat_id`),
  KEY `fk_act_subject` (`subject_id`),
  KEY `fk_act_verb` (`verb_id`),
  KEY `fk_act_comp` (`component_id`),
  KEY `fk_act_dest_c` (`destination_component_id`),
  KEY `fk_act_dest_z` (`destination_zone_id`),
  KEY `fk_act_trigger` (`trigger_type_id`),
  KEY `fk_act_source` (`source_action_id`),
  CONSTRAINT `fk_act_beat` FOREIGN KEY (`beat_id`) REFERENCES `tmp_beat` (`id`),
  CONSTRAINT `fk_act_comp` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `fk_act_dest_c` FOREIGN KEY (`destination_component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `fk_act_dest_z` FOREIGN KEY (`destination_zone_id`) REFERENCES `game_zones` (`id`),
  CONSTRAINT `fk_act_pb` FOREIGN KEY (`prereq_beat_id`) REFERENCES `tmp_beat` (`id`),
  CONSTRAINT `fk_act_prereq` FOREIGN KEY (`prereq_id`) REFERENCES `tmp_action` (`id`),
  CONSTRAINT `fk_act_source` FOREIGN KEY (`source_action_id`) REFERENCES `tmp_action` (`id`),
  CONSTRAINT `fk_act_subject` FOREIGN KEY (`subject_id`) REFERENCES `tmp_player_role` (`id`),
  CONSTRAINT `fk_act_trigger` FOREIGN KEY (`trigger_type_id`) REFERENCES `tmp_trigger_type` (`id`),
  CONSTRAINT `fk_act_verb` FOREIGN KEY (`verb_id`) REFERENCES `tmp_verb` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_function_verb` (
  `function_id` int(11) NOT NULL,
  `verb_id` int(11) NOT NULL,
  PRIMARY KEY (`function_id`,`verb_id`),
  KEY `verb_id` (`verb_id`),
  CONSTRAINT `tmp_function_verb_ibfk_1` FOREIGN KEY (`function_id`) REFERENCES `tmp_function` (`id`),
  CONSTRAINT `tmp_function_verb_ibfk_2` FOREIGN KEY (`verb_id`) REFERENCES `tmp_verb` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_condition_clause` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_id` int(11) NOT NULL,
  `component_id` int(11) DEFAULT NULL,
  `state_key` varchar(50) NOT NULL,
  `operator` enum('=','!=','>','<','>=','<=','ALL','ANY') NOT NULL DEFAULT '=',
  `value` varchar(100) NOT NULL,
  `clause_notes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_clause_cond` (`condition_id`),
  KEY `fk_clause_comp` (`component_id`),
  CONSTRAINT `fk_clause_comp` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `fk_clause_cond` FOREIGN KEY (`condition_id`) REFERENCES `tmp_condition` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_state_condition_clause` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_id` int(11) NOT NULL,
  `component_id` int(11) DEFAULT NULL,
  `state_key` varchar(50) NOT NULL,
  `operator` enum('=','!=','>','<','>=','<=','ALL','ANY') NOT NULL DEFAULT '=',
  `value` varchar(100) NOT NULL,
  `clause_notes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_scc_cond` (`condition_id`),
  KEY `fk_scc_comp` (`component_id`),
  CONSTRAINT `fk_scc_comp` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `fk_scc_cond` FOREIGN KEY (`condition_id`) REFERENCES `tmp_state_condition` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- No declared FKs. Used by v_comp_verb_matrix to determine Move=1 for a component.
CREATE TABLE IF NOT EXISTS `tmp_subject_target` (
  `subject_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  PRIMARY KEY (`subject_id`,`target_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- FKs reference legacy tables (factions, city_rings)
CREATE TABLE IF NOT EXISTS `tmp_component_faction` (
  `component_id` int(11) NOT NULL,
  `faction_id` bigint(20) NOT NULL,
  PRIMARY KEY (`component_id`,`faction_id`),
  KEY `faction_id` (`faction_id`),
  CONSTRAINT `tmp_component_faction_ibfk_1` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `tmp_component_faction_ibfk_2` FOREIGN KEY (`faction_id`) REFERENCES `factions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tmp_component_ring` (
  `component_id` int(11) NOT NULL,
  `ring_id` bigint(20) NOT NULL,
  PRIMARY KEY (`component_id`,`ring_id`),
  KEY `ring_id` (`ring_id`),
  CONSTRAINT `tmp_component_ring_ibfk_1` FOREIGN KEY (`component_id`) REFERENCES `tmp_component` (`id`),
  CONSTRAINT `tmp_component_ring_ibfk_2` FOREIGN KEY (`ring_id`) REFERENCES `city_rings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

SET FOREIGN_KEY_CHECKS = 1;
