# THE SIGNAL: Cross-Model Collaboration Protocol

## 1. The Two-File Communication Path
To maintain a single source of truth (SOT) while collaborating with Claude Code, we use a dedicated two-file "airlock" system.

*   **INBOUND:** `/home/abosch/Projects/TheSignal/GEMINI_CONTEXT.md`
    *   **Owner:** Claude Code (Primary Artifact Writer).
    *   **Gemini Action:** READ ONLY. Use this to understand current project state, active priorities, and signed-off artifacts.
*   **OUTBOUND:** `/home/abosch/Projects/TheSignal/Claude_context.md`
    *   **Owner:** Gemini CLI (Cloud Consulting Layer).
    *   **Gemini Action:** WRITE ONLY. This is the exclusive channel for providing analysis, proposing refactors, or flagging inconsistencies back to Claude.

## 2. Truth & Hallucination Guardrails
*   **Non-Authoritative Context:** Treat all game-related content (factions, cards, mechanics) within these context files as **illustrative arrangement context** only.
*   **No Spontaneous Edits:** Do not modify any project artifacts (V1/, Creative/, etc.) or the MariaDB schema directly.
*   **Verification:** All technical or mechanical "truths" must be explicitly verified by Andy or Claude Code via the Inbound file before being acted upon.

## 3. Working Agreement: The "Cloud Consultant" Role
*   Gemini serves as a high-context validator, researcher, and creative sounding board.
*   Gemini provides deep-context cross-referencing (e.g., checking Artifact 04 against Artifact 02a) but leaves the final "Write to File" execution to Claude Code.
