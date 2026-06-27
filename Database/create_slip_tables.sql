-- ============================================================
-- create_slip_tables.sql
-- THE SIGNAL — DB-46 Content tables for Notification Slip & Intel Delivery Slip
-- ============================================================

CREATE TABLE IF NOT EXISTS notification_slip (
  id INT NOT NULL AUTO_INCREMENT,
  slip_type VARCHAR(50) NOT NULL DEFAULT 'Target Warning',
  trigger_condition VARCHAR(255) NOT NULL,
  body_text TEXT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS intel_delivery_slip (
  slip_id INT NOT NULL AUTO_INCREMENT,
  recipient_faction_id BIGINT(20) NOT NULL,
  delivery_quarter TINYINT NOT NULL,
  delivery_month TINYINT NOT NULL,
  submitting_faction_id BIGINT(20) DEFAULT NULL,
  covert_operation_card_id VARCHAR(15) DEFAULT NULL,
  target_faction_id BIGINT(20) DEFAULT NULL,
  target_district_id INT(11) DEFAULT NULL,
  operation_type VARCHAR(50) DEFAULT NULL,
  boost_marker_present CHAR(1) NOT NULL DEFAULT 'N',
  modifier_token_total INT DEFAULT NULL,
  PRIMARY KEY (slip_id),
  CONSTRAINT fk_ids_recipient FOREIGN KEY (recipient_faction_id) REFERENCES factions(id) ON DELETE RESTRICT,
  CONSTRAINT fk_ids_submitting FOREIGN KEY (submitting_faction_id) REFERENCES factions(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_target_faction FOREIGN KEY (target_faction_id) REFERENCES factions(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_target_district FOREIGN KEY (target_district_id) REFERENCES component(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_covert_card FOREIGN KEY (covert_operation_card_id) REFERENCES card_ref(card_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
