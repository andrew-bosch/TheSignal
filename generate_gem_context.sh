#!/bin/bash

CONTEXT_FILE="$HOME/Desktop/gem_context.txt"
MESSAGE_FILE="$HOME/Desktop/gem_message.txt"
LOCAL_DIR="/home/abosch/Projects/TheSignal"
SCRIPT_NAME="$(basename "$0")"

echo "Building Gemini web context from $LOCAL_DIR..."
cd "$LOCAL_DIR" || { echo "Directory not found. Exiting."; exit 1; }

# --- File 1: Message to Gem (gem_web_context.md → Desktop) ---
if [ -f "gem_web_context.md" ]; then
  cp gem_web_context.md "$MESSAGE_FILE"
  echo "Message: $MESSAGE_FILE"
else
  echo "Warning: gem_web_context.md not found — no message file written."
fi

# --- File 2: Project context dump ---
{
  echo "=== THE SIGNAL PROJECT CONTEXT ==="
  echo "Generated on: $(date)"
  echo "Target Directory: $LOCAL_DIR"
  echo "=================================="
} > "$CONTEXT_FILE"

# README
if [ -f "README.md" ]; then
  {
    echo ""
    echo "----------------------------------------"
    echo "FILE: ./README.md"
    echo "----------------------------------------"
    cat README.md
  } >> "$CONTEXT_FILE"
  echo "Extracted: ./README.md"
fi

# Folder structure (V1 + Creative only)
{
  echo ""
  echo "=== FOLDER STRUCTURE (V1 + Creative) ==="
  find ./V1 ./Creative -not -path "*/\.*" | sort
  echo "========================================"
} >> "$CONTEXT_FILE"

# File contents
# Scope: V1/ and Creative/ only.
# Excluded by design: Session/ (PRIVATE___True_State.md), ClaudeIOS/, GEMINI_CONTEXT.md,
# Claude_context.md, GEMINI.md, mariadb_credentials.md, this script, output files.
{
  echo ""
  echo "=== FILE CONTENTS ==="
} >> "$CONTEXT_FILE"

find ./V1 ./Creative \
  -type f \( -name "*.md" -o -name "*.txt" -o -name "*.py" -o -name "*.js" \
             -o -name "*.json" -o -name "*.html" -o -name "*.css" -o -name "*.csv" \) \
  -not -path "*/\.*" \
  -not -name "$SCRIPT_NAME" \
  -not -name "$(basename "$CONTEXT_FILE")" \
  -not -name "$(basename "$MESSAGE_FILE")" \
  | sort | while read -r filepath; do
    {
      echo ""
      echo "----------------------------------------"
      echo "FILE: $filepath"
      echo "----------------------------------------"
      cat "$filepath"
    } >> "$CONTEXT_FILE"
    echo "Extracted: $filepath"
done

# Summary
echo ""
echo "Done."
wc -c "$MESSAGE_FILE" | awk '{printf "Message: %.1f KB\n", $1/1024}'
wc -c "$CONTEXT_FILE" | awk '{printf "Context: %.1f KB\n", $1/1024}'
