START TRANSACTION;

-- S136: structure_pass column — tracks whether a card has all 4 structural
-- blocks (Design Rationale / Card Story / Design checklist / Status) per
-- tools/card_completeness_audit.py. Distinct from design_pass (content
-- reviewed) and signed_off (Andy approved) — a card can be structure_pass=1
-- with design_pass=0 (scaffolded by tools/card_scaffolder.py, not yet
-- reviewed). See PM05 09-16 / DB-XX.
ALTER TABLE card_status
  ADD COLUMN IF NOT EXISTS structure_pass TINYINT(1) NOT NULL DEFAULT 0
  COMMENT 'Has all 4 structural blocks (Design Rationale/Card Story/Checklist/Status) — S136';

-- Backfill: STD.MOD.2-133 scaffolded by tools/card_scaffolder.py this session
-- (STD.MOD.1 Overture excluded — partial completeness, not touched by the
-- scaffolder, see PM05 09-16 step 1 notes).
UPDATE card_status
SET structure_pass = 1
WHERE card_id LIKE 'STD.MOD.%'
  AND card_id != 'STD.MOD.1'
  AND CAST(SUBSTRING_INDEX(card_id, '.', -1) AS UNSIGNED) BETWEEN 2 AND 133;

-- Standard CA/PA (Part2) were already fully speced pre-split - all 24 cards
-- confirmed complete (all 4 blocks present) by tools/card_completeness_audit.py.
-- Not gated on design_pass - that column tracks Andy's review sign-off gate,
-- a separate and currently unsynced state, not structural completeness.
UPDATE card_status
SET structure_pass = 1
WHERE card_id LIKE 'STD.CA.%' OR card_id LIKE 'STD.PA.%';

COMMIT;
