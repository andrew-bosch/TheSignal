START TRANSACTION;

-- DB-35: retire Pass card, repurpose id=88 as Faction Resolution Grid
UPDATE component 
SET name = 'Faction Resolution Grid', 
    actionable = 0, 
    receivable = 1, 
    transform_visibility = 0, 
    transform_orientation = 0, 
    transform_data = 0 
WHERE id = 88;

-- DB-36: register Situation Report (id=102)
INSERT INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (102, 'Situation Report', 0, 1, 0, 0, 0);

COMMIT;
