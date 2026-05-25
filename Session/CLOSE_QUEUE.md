## CLOSE QUEUE — Session 34
## Execute every instruction in order. No interpretation. Delete this file last.

---

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: | 00 — Factions & World | 1.4 | 🔄 Pending Re-Sign-Off. Ring renames (Infrastructure→The Mid, Sprawl→Baryo). Session 33: 00-06 (quarter worldbuilding), XA-15 (ARBITER as sixth party), 00-03 (Layer Structure) added. Re-sign-off pending; 00-07 multicultural texture pass queued after. |
NEW: | 00 — Factions & World | 1.4 | ✅ Signed Off — Session 34. Ring renames (The Mid / Baryo). 00-06 (quarter worldbuilding), XA-15 (ARBITER as sixth party), 00-03 (Layer Structure). 00-07 multicultural texture pass queued. |

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: | PM02 | 3.8 | ✅ Active — locked decisions L01–L142 (L141: ring numbering; L142: ring names The Mid/Baryo) |
NEW: | PM02 | 3.8 | ✅ Active — locked decisions L01–L143 (L143: deliberation cycles as in-world term for Quarters) |

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: | PM04 | 0.5 |
NEW: | PM04 | 0.7 |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | PM04 | Glossary & Data Dictionary | 0.6 | 🔄 Updated — Active | Single source of truth for all terminology and design conventions. §1: In-World Data Dictionary — fully populated session 11 (Component & System Terms, Faction Resources, Influence Levels, Temporal Conventions). §2: Design Terminology — narrative language table, voice & typography, code block standard, terminology sequencing, cross-artifact reference convention, reception language convention, roll mechanics terminology, data document types (schema vs. data table). Absorbs PM03 §1 and §2. |
NEW: | PM04 | Glossary & Data Dictionary | 0.7 | 🔄 Updated — Active | Single source of truth for all terminology and design conventions. §1: In-World Data Dictionary — Component Physical Glossary added (S34); Asset token removed. §2: Design Terminology — Category column pattern (S34), L109 Component Terminology Standard (S34) added alongside existing conventions. |

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: ## Session History
CONTENT:

**Session 34 summary (2026-05-24 — complete):**
- **Art 00 v1.4 re-sign-off complete.** First pass clean. "Deliberation cycles" confirmed as in-world term for Quarters (L143). Ring name propagation: "The Mid" / "Baryo" applied across 00a, 00b, 00c, 03a (non-material). 00-07 multicultural texture pass now unblocked.
- **iOS batch processed.** 12 vignettes (M365 Copilot, 2026-05-22) archived. Canon candidates approved: Elias Rook and Marek Ionescu. Mara Ionescu → Mara Seo (surname collision resolved). CANON_CANDIDATES.md updated. CREATIVE_BRIEF.md canonical home confirmed as Creative/ (duplicate removed from ClaudeIOS/).
- **Non-material queue partial clear.** XA-32 (Fringe ring → Ring 3 (Baryo) in 00a), 02a-04 (§10 cross-ref added), 02a-07 (Asset token removed from PM04 §1), PM04-03 (Category column pattern), PM04-04 (L109 standard + Component Physical Glossary). PM04 v0.6 → v0.7.
- **New PM05 item: 00b-04.** RG entity ID numbering (outside-in) vs. L141 inside-out canonical Ring numbers — design decision required before 00b signs off. Gemini-flagged risk.
- **Remaining non-material:** XA-29 (L109 component scan across 00–04b), XA-23 (Index→Contents rename), 04-35 (Affinity bonus N/A on C15–C35), 00b-04 (RG numbering decision — careful execution required).

---

### XA-23 — §2 Index → §2 Contents heading rename
Run the following sed commands on each file to rename "## §2 Index" to "## §2 Contents". Skip any file where the heading is not found.

sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/00___Factions_World_Narrative_Context.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/00a___Governing_Rules___Design_Policy.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/01___District_Map_Territory_Control.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/02a___Resource_Systems_Board_State.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/02b___Resource_Systems_Tracking.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/03___Setup_and_Round_Structure.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/04___Card_System.md
sed -i 's/^## §2 Index$/## §2 Contents/' /home/abosch/Projects/TheSignal/V1/04b___Card_Taxonomy_Index.md

After running, verify by running: grep -rn "## §2 Index" /home/abosch/Projects/TheSignal/V1/
Expected result: no output (all renamed). If any remain, they use a different heading format — leave them and note in output.

Then update PM05 item XA-23 status from "⬜ Queued — run unsupervised" to "✅ S34 — §2 Index → §2 Contents rename applied across 00, 00a, 01, 02a, 02b, 03, 04, 04b. Anchor link conversion deferred — non-critical."

FILE: /home/abosch/Projects/TheSignal/V1/PM05___Active_Punch_List.md
Find: | XA-23 | **Index → Contents rename + anchor links — all artifacts.**
Replace the status cell at the end of that row from: | ⬜ Queued — run unsupervised |
To: | ✅ S34 — §2 Index → §2 Contents rename applied. Anchor link conversion deferred — non-critical. |

---

### COMMIT
source ~/Projects/credentials.env && git -C /home/abosch/Projects/TheSignal add -A && git -C /home/abosch/Projects/TheSignal commit -m "session 34 — Art 00 v1.4 signed off; ring names propagated; PM04 v0.7; non-material queue partial clear; canon candidates Rook/Ionescu approved" && git -C /home/abosch/Projects/TheSignal push

### SYNC
rclone sync /home/abosch/Projects/TheSignal/ "googledrive:The Signal Workspace" --exclude ".git/**"

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
