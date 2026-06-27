-- ============================================================
-- audit_card_alignment.sql  —  THE SIGNAL: Card Taxonomy Alignment Audit
--
-- Usage: mysql the_signal_db < Database/audit_card_alignment.sql
--
-- Purpose: Identify active cards whose taxonomy subjects are not
-- legalized in comp_verb_phase. Run after any card spec change,
-- new card addition, or comp_verb_phase/card_subject_map update.
--
-- Output sections:
--   1. Summary count by rules_status
--   2. Rules Gaps — fixable; verb not permitted on component
--   3. Non-component subjects — card_subject_map entry missing or NULL
--   4. Abstract functions — function verb not mapped in function_verb
-- ============================================================

-- ============================================================
-- 1. SUMMARY
-- ============================================================
SELECT
  rules_status,
  COUNT(*) AS card_count
FROM v_card_mechanical_alignment
WHERE blocked = 0
GROUP BY rules_status
ORDER BY
  FIELD(rules_status,
    'Rules Gap (Verb not permitted on component)',
    'Non-component Subject',
    'Abstract Function (No Mechanical Verb)',
    'Abstract / No Subject',
    'Legalized'
  );

-- ============================================================
-- 2. RULES GAPS (primary action target)
-- Verb is mapped but not permitted on this component in comp_verb_phase.
-- Fix: (a) correct card_status.subject to the right component,
--      (b) ensure subject exists in card_subject_map,
--      (c) add verb entry to comp_verb_phase for the component.
-- Update Art 04 spec to match.
-- ============================================================
SELECT
  card_id,
  card_name,
  faction,
  card_type,
  design_layer,
  design_function,
  design_subject,
  component_name,
  verb_name,
  design_beat
FROM v_card_mechanical_alignment
WHERE rules_status = 'Rules Gap (Verb not permitted on component)'
  AND blocked = 0
ORDER BY faction, card_type, card_id;

-- ============================================================
-- 3. NON-COMPONENT SUBJECTS
-- Subject string has no entry in card_subject_map, or maps to NULL.
-- Fix: add row to card_subject_map if subject should map to a component;
--      leave NULL if subject is intentionally abstract.
-- ============================================================
SELECT
  card_id,
  card_name,
  faction,
  design_subject
FROM v_card_mechanical_alignment
WHERE rules_status = 'Non-component Subject'
  AND blocked = 0
ORDER BY design_subject, card_id;

-- ============================================================
-- 4. ABSTRACT FUNCTIONS (no mechanical verb mapped)
-- The card's function has no entry in function_verb.
-- These are design-layer functions (Block, Modify, Protect, etc.)
-- not yet reduced to physical primitives. Not errors — tracked
-- as design coverage gaps.
-- ============================================================
SELECT
  card_id,
  card_name,
  faction,
  design_function,
  design_subject
FROM v_card_mechanical_alignment
WHERE rules_status = 'Abstract Function (No Mechanical Verb)'
  AND blocked = 0
ORDER BY design_function, card_id;
