START TRANSACTION;

-- DB-37: Register ARBITER Covert Resolution Grid (ID=105)
INSERT IGNORE INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (105, 'ARBITER Covert Resolution Grid', 0, 1, 0, 0, 0);

-- DB-38: Register ARBITER Threshold Slider (ID=106)
INSERT IGNORE INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (106, 'ARBITER Threshold Slider', 0, 0, 0, 0, 0);

-- DB-39: Register Faction Threshold Slider (ID=107)
INSERT IGNORE INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (107, 'Faction Threshold Slider', 0, 0, 0, 0, 0);

COMMIT;
