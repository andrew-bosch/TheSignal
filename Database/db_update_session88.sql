START TRANSACTION;

-- Rename components in component table (DB-14, DB-15)
UPDATE component SET name = 'Presence chip' WHERE id = 1;
UPDATE component SET name = 'Dominant marker' WHERE id = 6;
UPDATE component SET name = 'Operative card' WHERE id = 15;

-- Register new components (DB-15, DB-34)
INSERT INTO component (name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES ('Sealed Apex ability', 1, 0, 1, 0, 0);

INSERT INTO component (name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES ('DebriefActionCard', 1, 1, 0, 0, 0);

INSERT INTO component (name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES ('SCIFRecord', 1, 1, 0, 0, 1);

-- Update card_ref references (Presence token -> Presence chip)
UPDATE card_ref SET subject = 'Presence chip' WHERE subject = 'Presence token';

-- Update comp_verb_beat notes
UPDATE comp_verb_beat SET notes = REPLACE(notes, 'Presence token', 'Presence chip') WHERE notes LIKE '%Presence token%';
UPDATE comp_verb_beat SET notes = REPLACE(notes, 'Presence tokens', 'Presence chips') WHERE notes LIKE '%Presence tokens%';
UPDATE comp_verb_beat SET notes = REPLACE(notes, 'Control flag', 'Dominant marker') WHERE notes LIKE '%Control flag%';

-- Update comp_verb_role notes
UPDATE comp_verb_role SET notes = REPLACE(notes, 'Presence token', 'Presence chip') WHERE notes LIKE '%Presence token%';
UPDATE comp_verb_role SET notes = REPLACE(notes, 'Presence tokens', 'Presence chips') WHERE notes LIKE '%Presence tokens%';
UPDATE comp_verb_role SET notes = REPLACE(notes, 'Control flag', 'Dominant marker') WHERE notes LIKE '%Control flag%';

-- Update action notes
UPDATE action SET notes = REPLACE(notes, 'Presence token', 'Presence chip') WHERE notes LIKE '%Presence token%';
UPDATE action SET notes = REPLACE(notes, 'Presence tokens', 'Presence chips') WHERE notes LIKE '%Presence tokens%';
UPDATE action SET notes = REPLACE(notes, 'Control flag', 'Dominant marker') WHERE notes LIKE '%Control flag%';

COMMIT;
