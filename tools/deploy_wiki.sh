#!/bin/bash
set -e

echo "=== Building Wiki Structure Locally ==="
python3 tools/build_wiki.py

echo "=== Syncing Markdown Files to Pi Zero ==="
rsync -avz --delete wiki_src/ abosch@10.0.1.15:/home/abosch/wiki/

echo "=== Compiling Static Site on Pi Zero ==="
ssh abosch@10.0.1.15 "cd /home/abosch/wiki && mkdocs build"

echo "=== Deploy Complete! ==="
