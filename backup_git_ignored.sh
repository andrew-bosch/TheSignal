#!/bin/bash
set -e

PROJECT_DIR="/home/abosch/Projects/TheSignal"
ARCHIVE_DIR="/mnt/storage/backups/TheSignal_Ignored"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$ARCHIVE_DIR"

cd "$PROJECT_DIR"
echo "Archiving git-ignored files in TheSignal..."
git ls-files --others --ignored --exclude-standard -z | xargs -0 tar -czf "$ARCHIVE_DIR/the_signal_ignored_${TIMESTAMP}.tar.gz"

find "$ARCHIVE_DIR" -name "the_signal_ignored_*.tar.gz" -mtime +7 -delete

echo "Archive complete: $ARCHIVE_DIR/the_signal_ignored_${TIMESTAMP}.tar.gz"
