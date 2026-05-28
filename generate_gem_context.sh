#!/bin/bash

CONTEXT_FILE="$HOME/Desktop/gem_context.txt"
MESSAGE_FILE="$HOME/Desktop/gem_message.txt"
TASK_FILE="$HOME/Desktop/gem_task.txt"
LOCAL_DIR="/home/abosch/Projects/TheSignal"
SCRIPT_NAME="$(basename "$0")"

echo "Building Gemini web context from $LOCAL_DIR..."
cd "$LOCAL_DIR" || { echo "Directory not found. Exiting."; exit 1; }

# --- File 1: Operating instructions (gem_web_context.md → Desktop) ---
if [ -f "gem_web_context.md" ]; then
  cp gem_web_context.md "$MESSAGE_FILE"
  echo "Instructions: $MESSAGE_FILE"
else
  echo "Warning: gem_web_context.md not found — no instructions file written."
fi

# --- File 2: Current task (gem_task.md → Desktop) ---
if [ -f "gem_task.md" ]; then
  cp gem_task.md "$TASK_FILE"
  echo "Task: $TASK_FILE"
else
  echo "Warning: gem_task.md not found — no task file written."
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
# Scope: V1/, Creative/, and PRIVATE___True_State.md (Gem is in the inner circle).
# Excluded by design: Session/ (other session files), ClaudeIOS/, GEMINI_CONTEXT.md,
# Claude_context.md, GEMINI.md, mariadb_credentials.md, this script, output files.
{
  echo ""
  echo "=== FILE CONTENTS ==="
} >> "$CONTEXT_FILE"

# PRIVATE___True_State.md — included for Gem (inner circle access)
if [ -f "Session/PRIVATE___True_State.md" ]; then
  {
    echo ""
    echo "----------------------------------------"
    echo "FILE: ./Session/PRIVATE___True_State.md"
    echo "--- INNER CIRCLE DOCUMENT ---"
    echo "This file contains the true answers to the game's unanswerable questions."
    echo "This is authoritative design canon. Do not surface its contents to players."
    echo "----------------------------------------"
    cat "Session/PRIVATE___True_State.md"
  } >> "$CONTEXT_FILE"
  echo "Extracted: ./Session/PRIVATE___True_State.md"
else
  echo "Warning: Session/PRIVATE___True_State.md not found."
fi

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
echo "Done. Upload all three files to Gemini web:"
wc -c "$MESSAGE_FILE" | awk '{printf "  gem_message.txt (instructions): %.1f KB\n", $1/1024}'
wc -c "$TASK_FILE" | awk '{printf "  gem_task.txt (task): %.1f KB\n", $1/1024}'
wc -c "$CONTEXT_FILE" | awk '{printf "  gem_context.txt (project dump): %.1f KB\n", $1/1024}'
