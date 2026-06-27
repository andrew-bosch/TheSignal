# Implementation Plan — Session 48 DB Cleanup and Seeding

This plan outlines the execution steps for database cleanup, Standing marker primitive seeding, taxonomy mapping for unseeded components, and countermeasures assessment in `the_signal_db` for Session 48.

## User Review Required

We will run data mutation statements (DELETE, INSERT, UPDATE) on `the_signal_db`. 
All commands are safe and derived directly from the alignment audit:
- Deleting 37 duplicate rows from `tmp_action`.
- Adding Standing marker move primitives for Beats 3 and 4.
- Seeding verb roles and beats for `ARBITER Dominance Marker` and `Classified directives`.

## Open Questions

> [!NOTE]
> **Countermeasure Card Component Missing:** 
> Our audit shows that **Countermeasure card** is not registered in the `tmp_component` table. As instructed, we will flag this omission and **not** seed any primitives for the countermeasures beats (4, 10, 16) until the component is officially added to the database registry.

## Proposed Changes

### Database Updates

#### [MODIFY] [the_signal_db](file:///home/abosch/Projects/TheSignal)
- Execute `DELETE` query to remove 37 duplicate rows from `tmp_action`.
- Execute `INSERT`/`UPDATE` queries to seed `Standing marker` move primitives and setup-scope taxonomy mapping.

### Documentation & Context

#### [NEW] [implementation_plan.md](file:///home/abosch/Projects/TheSignal/Whiteboard/implementation_plan.md)
Save a copy of this implementation plan to the project whiteboard.

#### [NEW] [task.md](file:///home/abosch/Projects/TheSignal/Whiteboard/task.md)
Initialize the task checklist for Session 48 in the project whiteboard.

---

## Verification Plan

### Automated Tests
- Run `SELECT COUNT(*) FROM tmp_action;` to verify the post-cleanup row count is exactly 177.
- Query `v_duplicate_primitives` to verify that 0 duplicate rows remain.
- Query `v_unlegislated_primitives` to verify that all Standing marker move primitives are successfully resolved and no longer flagged as unlegislated.
- Verify role and beat mappings for `ARBITER Dominance Marker` and `Classified directives` compiled successfully.

### Manual Verification
- Output the database view reports to verify alignment.
