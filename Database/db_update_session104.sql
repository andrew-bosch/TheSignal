-- SESSION 104 DB UPDATE PATCH
-- Idempotent updates for tasks ID-01, ID-02, and ID-03

-- TASK ID-01: Delete G-ext rows from card_ref
DELETE FROM card_ref WHERE card_id IN ('G-ext-01', 'G-ext-02', 'G-ext-03');

-- TASK ID-02: Reclassify DebriefActionCard and Grant Deed out of Card hierarchy
UPDATE component SET parent_component_id = NULL WHERE id IN (100, 113);

-- TASK ID-03: Add faction associations to pool components
-- Faction IDs: Ghost=1, The Network=2, The Syndicate=3, The Guild=4, The Directorate=5
-- Component IDs: Operative Pool=116, Apex Ability Pool=117, Classified Directives Pool=118
INSERT IGNORE INTO component_faction (component_id, faction_id) VALUES
  (116, 1), (116, 2), (116, 3), (116, 4), (116, 5),
  (117, 1), (117, 2), (117, 3), (117, 4), (117, 5),
  (118, 1), (118, 2), (118, 3), (118, 4), (118, 5);
