-- ============================================================
-- create_component_metadata.sql
-- THE SIGNAL — DB-42 Create component_metadata table
-- ============================================================

CREATE TABLE component_metadata (
  component_id INT NOT NULL,
  physical_form VARCHAR(2048) NOT NULL,
  quantity_expr VARCHAR(255) NOT NULL,
  visibility ENUM('Public', 'Player-private', 'ARBITER-only', 'Variable') NOT NULL,
  states VARCHAR(255) DEFAULT NULL,
  faction_keyed ENUM('Yes', 'No', 'N/A') NOT NULL DEFAULT 'N/A',
  max_placement_count INT DEFAULT NULL,
  max_placement_ref INT DEFAULT NULL,
  privacy_model ENUM('Open', 'Faction-private', 'ARBITER-private') DEFAULT NULL,
  display_fields VARCHAR(2048) DEFAULT NULL,
  back_design ENUM('Faction-keyed', 'Neutral', 'ARBITER-keyed') DEFAULT NULL,
  card_source ENUM('Deck', 'Hand', 'ARBITER supply', 'Sealed') DEFAULT NULL,
  recorded_fields VARCHAR(2048) DEFAULT NULL,
  function_prose VARCHAR(2048) DEFAULT NULL,
  scale_prose VARCHAR(2048) DEFAULT NULL,
  init_value_prose VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (component_id),
  CONSTRAINT fk_metadata_component FOREIGN KEY (component_id)
    REFERENCES component (id) ON DELETE CASCADE,
  CONSTRAINT fk_metadata_max_ref FOREIGN KEY (max_placement_ref)
    REFERENCES component (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
