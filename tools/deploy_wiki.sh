#!/bin/bash
# deploy_wiki.sh — build the wiki locally, sync to pinky (10.0.0.15), compile there.
#
# S160 hardening, after the S159 closeout took the wiki down (lev's post-mortem):
#   The queue executor ran `bash tools/deploy_wiki.sh 2>&1 | head -50`. `rsync -avz`
#   prints a line per file, `head` closed the pipe at 50, and the SIGPIPE killed the
#   script under `set -e` *after* the sync had run `--delete` but *before* mkdocs
#   rebuilt the site. The executor then checked `ps aux | grep deploy_wiki`, saw
#   nothing, and read that as success. Absence of a process is not evidence of
#   completion.
#
# Guards, so this is safe however it is invoked:
#   1. `--exclude 'site/'` (lev) — never delete the live build before the new one
#      compiles.
#   2. ALL work runs with stdout redirected to a log file. This is the guard that
#      actually holds: `trap '' PIPE` alone is NOT enough — ignoring SIGPIPE just
#      converts it to an EPIPE write error, which `set -e` kills the script on
#      regardless (verified). With the work's output going to a file, a truncating
#      pipe downstream can only cut the short summary, and only after every step
#      including verification has already run.
#   3. A positive end-to-end HTTP check — success is proven by the site answering
#      200, not inferred from the script having exited.
#
# Verify independently at any time with:  curl -I http://10.0.0.15/
set -uo pipefail

WIKI_HOST=10.0.0.15
LOG="${TMPDIR:-/tmp}/deploy_wiki_$(date +%Y%m%d_%H%M%S).log"

run_deploy() {
    set -e
    echo "=== Building wiki structure locally ==="
    python3 tools/build_wiki.py
    echo "=== Syncing markdown to pinky ($WIKI_HOST) ==="
    rsync -az --delete --exclude 'site/' --info=stats1 \
          wiki_src/ "abosch@${WIKI_HOST}:/home/abosch/wiki/"
    echo "=== Compiling static site on pinky ==="
    ssh "abosch@${WIKI_HOST}" "cd /home/abosch/wiki && mkdocs build"
}

run_deploy > "$LOG" 2>&1
rc=$?

code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "http://${WIKI_HOST}/" || echo 000)

if [[ $rc -ne 0 || "$code" != "200" ]]; then
    {
        echo "DEPLOY FAILED — exit=${rc}, http://${WIKI_HOST}/ returned ${code} (expected 200)."
        echo "Last 15 lines of ${LOG}:"
        tail -15 "$LOG"
        echo "Recover with: ssh abosch@${WIKI_HOST} 'cd /home/abosch/wiki && mkdocs build'"
    } >&2
    exit 1
fi

echo "=== Deploy complete — http://${WIKI_HOST}/ returned 200 (log: ${LOG}) ==="
