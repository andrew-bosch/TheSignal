#!/bin/bash
# ============================================================
# db_rebuild.sh
# THE SIGNAL — Full wipe and rebuild of tmp_ workspace tables
#
# WARNING: Destroys all tmp_ table data. Run a backup first:
#   mysqldump the_signal_db > backup_$(date +%Y%m%d).sql
#
# What this restores:
#   - Schema (all 22 tmp_ tables)
#   - Lookup seed data (8 tables: player_role, role_phase,
#     verb, beat, trigger_type, visibility_scope, function, layer)
#
# What this does NOT restore:
#   - Component registry (tmp_component — 58 rows)
#   - Action primitives (tmp_action — 213 rows)
#   - Taxonomy assignments (tmp_comp_verb_beat, tmp_comp_verb_role)
#   - Placement registry (tmp_subject_target)
#   Those require a full data backup restore (mysqldump --no-create-info).
# ============================================================

set -e
DB=the_signal_db
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== THE SIGNAL — tmp_ workspace rebuild ==="
echo ""
echo "WARNING: This will drop and recreate all tmp_ tables."
read -r -p "Continue? (yes/N): " confirm
[[ "$confirm" == "yes" ]] || { echo "Aborted."; exit 1; }

echo ""
echo "Dropping tmp_ tables..."
mysql "$DB" <<'SQL'
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS
  tmp_action, tmp_comp_verb_beat, tmp_comp_verb_role,
  tmp_component_faction, tmp_component_ring,
  tmp_function_verb, tmp_condition_clause, tmp_state_condition_clause,
  tmp_subject_target, tmp_layer,
  tmp_component, tmp_player_role, tmp_role_phase, tmp_verb, tmp_beat,
  tmp_trigger_type, tmp_function, tmp_condition, tmp_state_condition,
  tmp_visibility_scope, tmp_category, tmp_type;
SET FOREIGN_KEY_CHECKS = 1;
SQL

echo "Creating tmp_ tables..."
mysql "$DB" < "$DIR/db_create_tmp_tables.sql"

echo "Seeding lookup tables..."
mysql "$DB" < "$DIR/db_seed_lookups.sql"

echo ""
echo "Done. Schema and lookup data restored."
echo ""
echo "Next steps to restore full data:"
echo "  mysql $DB < your_backup.sql   (use --no-create-info if schema is already present)"
echo "  -- OR re-run agy seeding scripts for component registry and primitives"
