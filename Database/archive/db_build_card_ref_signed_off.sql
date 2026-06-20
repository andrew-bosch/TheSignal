-- Recreate card_ref table
DROP TABLE IF EXISTS card_ref;
CREATE TABLE card_ref (
    card_id VARCHAR(15) NOT NULL,
    card_name VARCHAR(100) NOT NULL,
    layer VARCHAR(50) NOT NULL,
    function VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    PRIMARY KEY (card_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Seed ONLY officially signed-off standard cards
INSERT INTO card_ref (card_id, card_name, layer, function, subject) VALUES
('C01', 'Build Structure', 'Territory', 'Add', 'Structure block'),
('C02', 'Demolish', 'Territory', 'Remove', 'Structure block'),
('C03', 'Campaign', 'Territory', 'Add', 'Presence token'),
('C04', 'Undermine', 'Territory', 'Remove', 'Presence token'),
('C06', 'Broadcast Interference', 'Submission', 'Modify', 'Political act (cost)'),
('C07', 'Amplify', 'Resolution', 'Modify', 'Political act (outcome scale)'),
('C08', 'Buy Influence', 'Territory', 'Add', 'Presence token'),
('C10', 'Protect', 'Resolution', 'Protect', 'Covert operation (difficulty)'),
('C17', 'Intercept', 'Information', 'Reveal', 'Covert operation — named faction');

-- Create/Recompile v_card_primitive_map View with robust prefix matching
CREATE OR REPLACE VIEW v_card_primitive_map AS
SELECT
    cr.card_id,
    cr.card_name,
    cr.layer,
    cr.function AS card_function,
    cr.subject AS card_subject,
    c.id AS component_id,
    c.name AS component_name,
    v.id AS verb_id,
    v.name AS verb_name,
    a.id AS action_id,
    a.beat_id,
    a.notes AS action_notes
FROM card_ref cr
LEFT JOIN function f ON cr.function = f.name
LEFT JOIN function_verb fv ON f.id = fv.function_id
LEFT JOIN verb v ON fv.verb_id = v.id
LEFT JOIN component c ON cr.subject = c.name 
    OR cr.subject LIKE CONCAT(c.name, ' %')
LEFT JOIN action a ON a.verb_id = v.id 
    AND a.component_id = c.id
ORDER BY cr.card_id, a.id;
