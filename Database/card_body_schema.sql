-- Art 04 Card() body projection (S156). .md is source of truth; regenerate via
-- tools/extract_card_body.py then load Database/card_body_load.sql.

DROP VIEW IF EXISTS v_card_body;
DROP TABLE IF EXISTS card_restriction_clause;
DROP TABLE IF EXISTS card_body;

-- Faithful EAV mirror: one row per (card_id, field_name), value verbatim.
CREATE TABLE card_body (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    card_id     VARCHAR(15) NOT NULL,
    field_name  VARCHAR(40) NOT NULL,
    raw_value   TEXT,
    source_file VARCHAR(80) NOT NULL,
    UNIQUE KEY uq_card_field (card_id, field_name),
    KEY idx_card (card_id),
    KEY idx_field (field_name)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- The one decomposed logic field: restriction -> top-level and/or clauses.
CREATE TABLE card_restriction_clause (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    card_id      VARCHAR(15) NOT NULL,
    clause_index INT NOT NULL,
    connector    VARCHAR(4),            -- 'and'/'or' joining to previous clause; NULL for first
    raw_clause   TEXT NOT NULL,
    subject      VARCHAR(160),
    operator     VARCHAR(4),
    value        VARCHAR(160),
    KEY idx_card (card_id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Convenience pivot: common + promoted fields as columns (the hybrid "typed" side).
CREATE VIEW v_card_body AS
SELECT
    card_id,
    MAX(CASE WHEN field_name='name'                  THEN raw_value END) AS name,
    MAX(CASE WHEN field_name='version'               THEN raw_value END) AS version,
    MAX(CASE WHEN field_name='type'                  THEN raw_value END) AS type,
    MAX(CASE WHEN field_name='subtype'               THEN raw_value END) AS subtype,
    MAX(CASE WHEN field_name='faction'               THEN raw_value END) AS faction,
    MAX(CASE WHEN field_name='layer'                 THEN raw_value END) AS layer,
    MAX(CASE WHEN field_name='function'              THEN raw_value END) AS func,
    MAX(CASE WHEN field_name='subject'               THEN raw_value END) AS subject,
    MAX(CASE WHEN field_name='beat'                  THEN raw_value END) AS beat,
    MAX(CASE WHEN field_name='value_rating'          THEN raw_value END) AS value_rating,
    MAX(CASE WHEN field_name='trigger'               THEN raw_value END) AS trigger_field,
    MAX(CASE WHEN field_name='resolution'            THEN raw_value END) AS resolution,
    MAX(CASE WHEN field_name='resolution_type'       THEN raw_value END) AS resolution_type,
    MAX(CASE WHEN field_name='threshold'             THEN raw_value END) AS threshold,
    MAX(CASE WHEN field_name='outcome_type'          THEN raw_value END) AS outcome_type,
    MAX(CASE WHEN field_name='persistence'           THEN raw_value END) AS persistence,
    MAX(CASE WHEN field_name='persistence_condition' THEN raw_value END) AS persistence_condition,
    MAX(CASE WHEN field_name='persistence_effect'    THEN raw_value END) AS persistence_effect,
    MAX(CASE WHEN field_name='effect'                THEN raw_value END) AS effect,
    MAX(CASE WHEN field_name='cost'                  THEN raw_value END) AS cost,
    MAX(CASE WHEN field_name='affinity'              THEN raw_value END) AS affinity,
    MAX(CASE WHEN field_name='restriction'           THEN raw_value END) AS restriction,
    MAX(CASE WHEN field_name='success'               THEN raw_value END) AS success,
    MAX(CASE WHEN field_name='successcrit'           THEN raw_value END) AS successcrit,
    MAX(CASE WHEN field_name='fail'                  THEN raw_value END) AS fail,
    MAX(CASE WHEN field_name='failcrit'              THEN raw_value END) AS failcrit,
    MAX(CASE WHEN field_name='tagline'               THEN raw_value END) AS tagline,
    MAX(CASE WHEN field_name='narrative'             THEN raw_value END) AS narrative,
    MAX(CASE WHEN field_name='perspectives'          THEN raw_value END) AS perspectives,
    MAX(CASE WHEN field_name='arbiter_note'          THEN raw_value END) AS arbiter_note,
    MAX(CASE WHEN field_name='ring_constraint'       THEN raw_value END) AS ring_constraint,
    MAX(CASE WHEN field_name='ring_origin'           THEN raw_value END) AS ring_origin
FROM card_body
GROUP BY card_id;
