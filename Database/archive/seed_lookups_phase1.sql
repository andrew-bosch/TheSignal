-- ============================================================
-- seed_lookups_phase1.sql
-- THE SIGNAL — DB-43 Phase 1 Static Lookup Tables
-- ============================================================

START TRANSACTION;

-- public_standing_tier
CREATE TABLE IF NOT EXISTS public_standing_tier (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  range_min TINYINT NOT NULL,
  range_max TINYINT NOT NULL,
  drift_delta TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT IGNORE INTO public_standing_tier (id, name, range_min, range_max, drift_delta) VALUES
  (1, 'Celebrated', 17, 20, -1),
  (2, 'Respected',  13, 16, -1),
  (3, 'Neutral',     7, 12,  0),
  (4, 'Suspect',     3,  6,  1),
  (5, 'Discredited', 0,  2,  1);

-- difficulty_tier
CREATE TABLE IF NOT EXISTS difficulty_tier (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  base_threshold TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT IGNORE INTO difficulty_tier (id, name, base_threshold) VALUES
  (1, 'Easy', 75),
  (2, 'Average', 50),
  (3, 'Challenging', 25);

-- resolution_outcome
CREATE TABLE IF NOT EXISTS resolution_outcome (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT IGNORE INTO resolution_outcome (id, name) VALUES
  (1, 'Succeeded'),
  (2, 'Failed'),
  (3, 'Voided'),
  (4, 'Discovered'),
  (5, 'Auto-failed');

-- influence_level
CREATE TABLE IF NOT EXISTS influence_level (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  chip_threshold TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT IGNORE INTO influence_level (id, name, chip_threshold) VALUES
  (1, 'Dominant',    3),
  (2, 'Established', 2),
  (3, 'Present',     1),
  (4, 'None',        0);

COMMIT;
