# Gem — Current Task
*Read after gem_message.txt and before the project context dump.*

---

## Bucket A — Current Role & Task

**Status: ACTIVE — Cross-Reference Integrity Audit**

---

**Task:** Read every V1/ artifact and produce a complete audit of all cross-references. A cross-reference is any inline pointer to another section, artifact, or PM file — e.g., `(see §X)`, `(Art 0Y §Z)`, `(PM0Z §W)`, `"as defined in §X"`, `"see Artifact 03 §7"`.

**Deliverable:** A table with one row per cross-reference found. Columns:

| Artifact | Section | Reference as written | Points to | Valid? | Correction needed |
|----------|---------|----------------------|-----------|--------|-------------------|

- **Valid?** = Yes (target section exists and content matches), No (target section does not exist or has been renumbered), Uncertain (flag for Claude to verify)
- **Correction needed** = exact fix required, or "Verify" if uncertain

**Scope:** All V1/ artifacts: 00, 00a, 00b, 00c, 01, 02a, 02b, 03, 03a, 04, 04b, 07, PM01, PM02, PM03, PM04, PM05.

**Constraints:**
- Do not flag planned stubs or `[TBD]` sections as broken — only flag references to content that should exist now in a signed-off artifact.
- Do not summarize. If there are 80 cross-references, report all 80.
- Check every reference against the actual current section numbering in the target artifact before marking Valid or No.
- Flag uncertainty explicitly rather than guessing. "I believe §7 still covers this — recommend Claude verify" is the correct output when unsure.
- Complete the full audit in one pass. Do not stop and ask Andy to continue.
