# Task Checklist — Session 48 DB Cleanup and Seeding

- [x] DB-cleanup-01: Delete 37 duplicate rows from `tmp_action` and verify count = 177
- [x] DB-cleanup-02: Seed Standing marker move primitives
  - [x] Add ARBITER Move Standing marker to Beat 8 (Month 1 Beat 3)
  - [x] Add ARBITER Move Standing marker to Beat 14 (Month 2 Beat 3)
  - [x] Update notes on Beat 17 (Month 3 Beat 4) Standing marker moves to match card-specified outcome
  - [x] Verify `Standing marker` is mapped to Beat 17 (Month 3 Beat 4) in `tmp_comp_verb_beat`
- [x] DB-cleanup-03: Seed taxonomy mappings for unseeded components
  - [x] Seed `tmp_comp_verb_role` and `tmp_comp_verb_beat` for `ARBITER Dominance Marker` (id=42)
  - [x] Seed `tmp_comp_verb_role` and `tmp_comp_verb_beat` for `Classified directives` (id=17)
- [x] DB-cleanup-04: Assess and report on countermeasures beats (4, 10, 16)
  - [x] Check if `Countermeasure card` component exists in registry (it does: id=52)
  - [x] Seed Countermeasure card (id=52) action primitives for beats 2, 4, 7, 10, 13, 16, 17
- [x] Documentation and Report Updates
  - [x] Update `Claude_context.md` with final findings and execution outcomes
  - [x] Update `Session/GEMINI_STATE.md` with Session 48 progress
