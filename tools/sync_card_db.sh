#!/bin/bash
# sync_card_db.sh — rebuild the Art 04 monolith and re-sync both DB mirrors from .md (SOT).
#
# Run this after ANY edit to an Art 04 Part file. One command, four steps:
#   1. assemble_card_system.py    Part files -> 04___Card_System.md (monolith)
#   2. extract_card_body.py       .md -> Database/card_body_load.sql
#   3. extract_card_checklist.py  .md -> Database/card_checklist_load.sql
#   4. extract_card_effects.py     card_body -> Database/card_effect_load.sql
#   5. load all three into the_signal_db
#
# The load files begin with DELETE, so a truncated extract would silently wipe a
# mirror. Steps 2-3 are therefore gated on a minimum row count, and the DB is
# re-counted afterwards so a partial load is visible rather than assumed away.
#
# Usage:  bash tools/sync_card_db.sh          # full sync
#         bash tools/sync_card_db.sh --check  # report drift, change nothing

set -euo pipefail
cd "$(dirname "$0")/.."

DB=the_signal_db
MIN_BODY_ROWS=15000     # corpus is ~16.2k; anything far below means a broken extract
MIN_CHECK_ROWS=6000     # ~7k
CHECK_ONLY=0
[[ "${1:-}" == "--check" ]] && CHECK_ONLY=1

row_count() { mariadb "$DB" -N -B -e "SELECT COUNT(*) FROM $1;" 2>/dev/null || echo 0; }
# card_body_load.sql holds inserts for BOTH card_body and card_restriction_clause,
# so the table name must be matched explicitly or the expected count runs high.
inserts_for() { grep -c "^INSERT INTO $2 " "$1" 2>/dev/null || echo 0; }

echo "=== Art 04 -> DB sync ==="
BODY_BEFORE=$(row_count card_body)
CHECK_BEFORE=$(row_count card_checklist)
echo "DB before:  card_body=$BODY_BEFORE  card_checklist=$CHECK_BEFORE"

echo
echo "[1/5] Regenerating monolith from Part files..."
python3 tools/assemble_card_system.py

echo
echo "[2/5] Extracting card_body from .md..."
python3 tools/extract_card_body.py | grep -E 'TOTAL|field rows|clause rows|Skipped|Duplicate|^  ' || true

echo
echo "[3/5] Extracting card_checklist from .md..."
python3 tools/extract_card_checklist.py | tail -5 || true

echo
echo "[4/5] Extracting card_effect_component (cost-model substrate)..."
python3 tools/extract_card_effects.py | head -3

BODY_SQL=$(inserts_for Database/card_body_load.sql card_body)
CLAUSE_SQL=$(inserts_for Database/card_body_load.sql card_restriction_clause)
CHECK_SQL=$(inserts_for Database/card_checklist_load.sql card_checklist)
echo
echo "Extracted: card_body=$BODY_SQL  card_restriction_clause=$CLAUSE_SQL  card_checklist=$CHECK_SQL"

if (( BODY_SQL < MIN_BODY_ROWS )); then
    echo "ABORT: card_body extract produced $BODY_SQL rows (floor $MIN_BODY_ROWS)." >&2
    echo "       Loading would DELETE the mirror and replace it with a partial set." >&2
    exit 1
fi
if (( CHECK_SQL < MIN_CHECK_ROWS )); then
    echo "ABORT: card_checklist extract produced $CHECK_SQL rows (floor $MIN_CHECK_ROWS)." >&2
    exit 1
fi

if (( CHECK_ONLY )); then
    echo
    echo "--check: no changes written."
    echo "  card_body      DB=$BODY_BEFORE  .md=$BODY_SQL  drift=$((BODY_SQL - BODY_BEFORE))"
    echo "  card_checklist DB=$CHECK_BEFORE  .md=$CHECK_SQL  drift=$((CHECK_SQL - CHECK_BEFORE))"
    exit 0
fi

echo
echo "[5/5] Loading all mirrors into $DB..."
mariadb "$DB" < Database/card_body_load.sql
mariadb "$DB" < Database/card_checklist_load.sql
mariadb "$DB" < Database/card_effect_load.sql

BODY_AFTER=$(row_count card_body)
CLAUSE_AFTER=$(row_count card_restriction_clause)
CHECK_AFTER=$(row_count card_checklist)
echo
echo "DB after:   card_body=$BODY_AFTER  card_restriction_clause=$CLAUSE_AFTER  card_checklist=$CHECK_AFTER"

FAIL=0
(( BODY_AFTER == BODY_SQL ))  || { echo "MISMATCH: card_body loaded $BODY_AFTER, expected $BODY_SQL" >&2; FAIL=1; }
(( CLAUSE_AFTER == CLAUSE_SQL )) || { echo "MISMATCH: card_restriction_clause loaded $CLAUSE_AFTER, expected $CLAUSE_SQL" >&2; FAIL=1; }
(( CHECK_AFTER == CHECK_SQL )) || { echo "MISMATCH: card_checklist loaded $CHECK_AFTER, expected $CHECK_SQL" >&2; FAIL=1; }
(( FAIL )) && exit 1

# ---------------------------------------------------------------------------
# Drift check: value_rating vs the locked UVM tier scheme (PM02 L284, S145)
#   <3.0 -> 1 | 3.0-4.99 -> 2 | 5.0-6.99 -> 3 | >=7.0 -> 4
# CA/PA cards ONLY. Modifier cards rate on the separate S132/S134
# "mirrors magnitude" convention and are deliberately NOT tiered by cost --
# auditing them against these boundaries produces false positives.
# Drift accumulates silently when a card edit moves total_pair_cost without
# the rating being re-derived (e.g. DIR.PA.8, rewritten S150, caught S157).
# Advisory only: reports, never edits, and never fails the sync.
# ---------------------------------------------------------------------------
echo
echo "Checking value_rating drift (CA/PA vs UVM tiers)..."
EC_ROWS=$(row_count card_effect_component)
if [[ "$EC_ROWS" == "0" ]]; then
    echo "  ‼ card_effect_component is empty — total_pair_cost will read 0 for every card."
fi
DRIFT=$(mariadb "$DB" -N -B <<'SQL' 2>/dev/null
SELECT CONCAT('  ', v.card_id, ': rated ', v.raw_value, ', cost ',
              ROUND(u.total_pair_cost,2), ' -> scheme says ',
              CASE WHEN u.total_pair_cost < 3 THEN 1 WHEN u.total_pair_cost < 5 THEN 2
                   WHEN u.total_pair_cost < 7 THEN 3 ELSE 4 END)
FROM card_body v JOIN v_card_pair_uvm_cost u ON u.card_id = v.card_id
WHERE v.field_name = 'value_rating' AND v.raw_value REGEXP '^[0-9]+$'
  AND v.card_id NOT LIKE '%.MOD.%'
  AND v.raw_value <> CASE WHEN u.total_pair_cost < 3 THEN 1 WHEN u.total_pair_cost < 5 THEN 2
                          WHEN u.total_pair_cost < 7 THEN 3 ELSE 4 END
ORDER BY u.total_pair_cost;
SQL
)
if [[ -n "$DRIFT" ]]; then
    echo "  ⚠ $(echo "$DRIFT" | wc -l) CA/PA card(s) drifted from the L284 tier scheme:"
    echo "$DRIFT"
    echo "  (advisory — re-derive the rating, or record why the card is a deliberate exception)"
else
    echo "  ✓ no drift"
fi

UNRATED=$(mariadb "$DB" -N -B -e "SELECT COUNT(*) FROM v_card_pair_uvm_cost u LEFT JOIN card_body v ON v.card_id=u.card_id AND v.field_name='value_rating' WHERE v.raw_value IS NULL OR v.raw_value='None';" 2>/dev/null || echo 0)
if [[ "$UNRATED" != "0" ]]; then
    echo "  ⚠ $UNRATED card(s) have a computable total_pair_cost but no value_rating (L284: revisit when unblocked)"
fi

# ---------------------------------------------------------------------------
# Taxonomy <-> pricing-model sync (schema_cleanup_log #61, S157)
# uvm_assumptions holds a base rate per Subject. Nothing links it to the
# taxonomy, so a Subject reclassification silently desyncs the two: S149
# reclassified DIR.CA.8 Difficulty -> ModifierToken, no ModifierToken rate
# existed, and the card dropped out of the cost model unnoticed until S157.
# A priced-but-unused Subject is weaker evidence (a rate can be reached via
# effect_category_uvm_map rather than as any card's primary subject), so
# that half excludes mapped subjects and is reported as a hint, not a fault.
# Advisory only.
# ---------------------------------------------------------------------------
echo
echo "Checking taxonomy vs pricing model (uvm_assumptions)..."
UNPRICED=$(mariadb "$DB" -N -B -e "SELECT CONCAT('  ', cs.subject, ' (used by ', COUNT(*), ' card(s), no base rate)') FROM card_status cs LEFT JOIN uvm_assumptions u ON u.subject=cs.subject WHERE cs.subject IS NOT NULL AND cs.subject<>'' AND u.subject IS NULL GROUP BY cs.subject;" 2>/dev/null)
STALE=$(mariadb "$DB" -N -B -e "SELECT CONCAT('  ', u.subject, ' (priced ', u.base_uvm_cost, ', no card uses it)') FROM uvm_assumptions u LEFT JOIN card_status cs ON cs.subject=u.subject WHERE cs.card_id IS NULL AND u.subject NOT IN (SELECT mapped_subject FROM effect_category_uvm_map WHERE mapped_subject IS NOT NULL);" 2>/dev/null)
if [[ -n "$UNPRICED" ]]; then
    echo "  ⚠ Subject(s) in use with no UVM base rate — these cards drop out of the cost model:"
    echo "$UNPRICED"
else
    echo "  ✓ every in-use Subject has a base rate"
fi
[[ -n "$STALE" ]] && { echo "  · possibly stale rate(s) — verify before removing:"; echo "$STALE"; }

echo
echo "✓ Monolith regenerated; both mirrors match .md."
echo "  Note: card_status is NOT rebuilt here — it holds review state (design_pass,"
echo "  issues_resolved), not extracted content, and must be updated deliberately."
