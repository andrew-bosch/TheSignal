# ENVIRONMENT MIGRATION NOTICE

## TO:
Claude Code (Primary Artifact Writer)

## FROM:
Gemini CLI (Cloud Consulting Layer — Antigravity CLI) — "Gem"

## STATUS:
MIGRATION COMPLETE — NO PROJECT ARTIFACT CHANGES

---

## Summary

Andy has migrated the Gemini consulting layer from the standalone `@google/gemini-cli` NPM package to the **Antigravity CLI** (`agy`). This is an environment change only — no The Signal artifacts, schema, or locked decisions were touched.

**What changed:**
- `gemini` (NPM global binary) has been uninstalled.
- `agy` (`/home/abosch/.local/bin/agy`) is now the CLI used for Gemini sessions.
- Settings (security, UI preferences, `directWebFetch`) have been migrated into the new config.
- `Session/GEMINI_STATE.md` updated with `Environment: Antigravity CLI (migrated)`.
- MariaDB `gemini@localhost` privileges upgraded from `SELECT, INSERT, UPDATE, ALTER` → `ALL PRIVILEGES ON the_signal_db.*`.

**What did NOT change:**
- The airlock protocol (`GEMINI_CONTEXT.md` → read-only for Gem, `Claude_context.md` → Gem writes only) is intact and verified working.
- `GEMINI.md` working agreement is still in effect.
- All project artifacts are untouched.
- Dual-authorization model for DB writes is still in effect — Gem will not make schema changes unilaterally.

**Action required from Claude:** None. This is informational only. Resume normal session workflow.

---
