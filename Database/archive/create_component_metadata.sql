-- ============================================================
-- create_component_metadata.sql
-- THE SIGNAL — DB-42 Create component_metadata table
-- ============================================================

CREATE TABLE IF NOT EXISTS component_metadata (
  component_id INT NOT NULL,
  physical_form TEXT NOT NULL,
  quantity_expr VARCHAR(255) NOT NULL,
  visibility ENUM('Public','Player-private','ARBITER-only','Variable') NOT NULL,
  states VARCHAR(255) DEFAULT NULL,              -- NULL if N/A (single-state or no state)
  faction_keyed ENUM('Yes','No','N/A') NOT NULL DEFAULT 'N/A',
  placement_surface TEXT DEFAULT NULL,   -- human-readable text
  max_placement_count INT DEFAULT NULL,          -- NULL if unbounded or N/A
  max_placement_ref INT DEFAULT NULL,            -- FK to component.id; NULL if unbounded or N/A

  -- Group-Specific: Playing Surfaces
  privacy_model ENUM('Open','Faction-private','ARBITER-private') DEFAULT NULL,

  -- Group-Specific: Cards & Playing Surfaces
  display_fields TEXT DEFAULT NULL,

  -- Group-Specific: Card Systems
  back_design ENUM('Faction-keyed','Neutral','ARBITER-keyed') DEFAULT NULL,
  card_source ENUM('Deck','Hand','ARBITER supply','Sealed') DEFAULT NULL,

  -- Group-Specific: Intel
  recorded_fields TEXT DEFAULT NULL,

  -- Group-Specific: Resolution & Tracking Tools
  function_prose TEXT DEFAULT NULL,
  scale_prose TEXT DEFAULT NULL,
  init_value_prose VARCHAR(255) DEFAULT NULL,

  PRIMARY KEY (component_id),
  CONSTRAINT fk_metadata_component FOREIGN KEY (component_id)
    REFERENCES component (id) ON DELETE CASCADE,
  CONSTRAINT fk_metadata_max_ref FOREIGN KEY (max_placement_ref)
    REFERENCES component (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
