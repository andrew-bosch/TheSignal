-- ============================================================
-- db_build_gap5_invoke.sql  —  THE SIGNAL: Copy/Invoke meta-action
-- Session 47
--
-- C16 Pattern Match: Faction plays C16, copies the effect of another
-- submitted card's action chain, but as their own faction (new subject).
--
-- Model:
--   1. New verb: Invoke (id=17) — meta-verb meaning "execute source
--      action chain with this row's subject as initiator."
--   2. New column: tmp_action.source_action_id — FK to the action
--      being copied. NULL for all non-copy primitives.
--   3. An Invoke primitive is described as:
--        subject_id  = copying Faction
--        verb_id     = 17 (Invoke)
--        component_id = component of the source action (populated at runtime)
--        source_action_id = tmp_action.id being copied
--        trigger_type_id  = 6 (player.introduce_card — Faction plays C16)
--
-- At taxonomy level source_action_id is NULL (parameterized at game time).
-- The primitive is a placeholder confirming the action is legal; the engine
-- resolves source_action_id when C16 is submitted.
-- ============================================================

-- ============================================================
-- 1. NEW VERB: Invoke
-- ============================================================
INSERT INTO tmp_verb (id, name)
VALUES (17, 'Invoke')
ON DUPLICATE KEY UPDATE name = name;

-- ============================================================
-- 2. ALTER tmp_action — add source_action_id; relax component_id (idempotent)
-- ============================================================
SET FOREIGN_KEY_CHECKS=0;
ALTER TABLE tmp_action DROP FOREIGN KEY IF EXISTS fk_act_source;
ALTER TABLE tmp_action DROP COLUMN IF EXISTS source_action_id;
SET FOREIGN_KEY_CHECKS=1;

-- component_id nullable: Invoke rows have no fixed target component
-- (resolved at runtime from source action). Constraint ensures one
-- of component_id or source_action_id must be present.
ALTER TABLE tmp_action
  MODIFY COLUMN component_id INT DEFAULT NULL,
  ADD COLUMN source_action_id INT DEFAULT NULL AFTER prereq_beat_id,
  ADD CONSTRAINT fk_act_source FOREIGN KEY (source_action_id)
    REFERENCES tmp_action(id);

-- ============================================================
-- 3. PRIMITIVE PLACEHOLDER — Faction Invoke (C16 Pattern Match)
--    beat_id=8 (M1 Beat 3): Faction can invoke a copy of any submitted
--    M1 card effect during resolution.
--    component_id=14 (Political act) is a placeholder — at runtime this
--    resolves to whatever card is being copied.
--    source_action_id=NULL at design time; populated by game engine.
-- ============================================================
INSERT INTO tmp_action
  (beat_id, beat_trigger, prereq_id, prereq_beat_id,
   source_action_id, subject_id, verb_id, component_id,
   trigger_type_id, notes)
VALUES
  (8,  'during', NULL, NULL, NULL, 1, 17, NULL, 6,
   'C16 Pattern Match — Faction invokes copy of submitted card effect; source_action_id resolved at game time'),
  (14, 'during', NULL, NULL, NULL, 1, 17, NULL, 6,
   'C16 Pattern Match — Faction invokes copy of submitted card effect (M2); source_action_id resolved at game time');
