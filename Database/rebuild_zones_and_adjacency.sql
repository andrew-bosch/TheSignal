-- 1. Rebuild game_zones to be a hierarchical registry
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS district_adjacency; -- Drop first due to FK constraints
DROP TABLE IF EXISTS game_zones;

CREATE TABLE game_zones (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(60) NOT NULL,
    parent_zone_id BIGINT NULL,               -- FK to parent (e.g. the Ring)
    position TINYINT NULL,                    -- Distinguishes position within the ring (e.g., the '2' in '1.2')
    resource_type_id BIGINT NULL,                -- FK to resource_types
    base_generation INT NULL,                 
    hex_color VARCHAR(10) NULL,
    
    FOREIGN KEY (parent_zone_id) REFERENCES game_zones(id),
    FOREIGN KEY (resource_type_id) REFERENCES resource_types(id)
);

-- 2. Rebuild district_adjacency as a pure graph edge table
CREATE TABLE district_adjacency (
    district_id BIGINT NOT NULL,
    adjacent_district_id BIGINT NOT NULL,
    allow_ingress BOOLEAN DEFAULT TRUE,
    allow_egress BOOLEAN DEFAULT TRUE,
    
    PRIMARY KEY (district_id, adjacent_district_id),
    FOREIGN KEY (district_id) REFERENCES game_zones(id),
    FOREIGN KEY (adjacent_district_id) REFERENCES game_zones(id)
);

-- 3. Create the view to reconstruct the Art 01 markdown table format
DROP VIEW IF EXISTS v_district_adjacency;
CREATE VIEW v_district_adjacency AS 
SELECT 
    parent_zone.zone_name AS Origin_Ring,
    CONCAT(
        REPLACE(parent_zone.zone_name, 'Ring ', ''), 
        '.', 
        origin_zone.position
    ) AS Origin_Address,
    origin_zone.zone_name AS Origin_District,
    
    adj_parent_zone.zone_name AS Adjacent_Ring,
    CONCAT(
        REPLACE(adj_parent_zone.zone_name, 'Ring ', ''), 
        '.', 
        adj_zone.position
    ) AS Adjacent_Address,
    adj_zone.zone_name AS Adjacent_District,
    
    da.allow_ingress,
    da.allow_egress
FROM district_adjacency da
JOIN game_zones origin_zone ON da.district_id = origin_zone.id
JOIN game_zones parent_zone ON origin_zone.parent_zone_id = parent_zone.id
JOIN game_zones adj_zone ON da.adjacent_district_id = adj_zone.id
JOIN game_zones adj_parent_zone ON adj_zone.parent_zone_id = adj_parent_zone.id
ORDER BY 
    CAST(REPLACE(parent_zone.zone_name, 'Ring ', '') AS UNSIGNED) ASC,
    origin_zone.position ASC,
    CAST(REPLACE(adj_parent_zone.zone_name, 'Ring ', '') AS UNSIGNED) ASC,
    adj_zone.position ASC;
