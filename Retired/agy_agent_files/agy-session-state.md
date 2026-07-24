# AGY Session State & Learnings

## Core Directives & Boundaries
- **Signed-off Artifacts:** NEVER modify signed-off procedural artifacts (such as `03___Round_Structure___Gameplay.md`) unless explicitly instructed to amend them. Faction-specific mechanics should always be contained within the card layer (`04___Card_System.md`) or their respective faction layers. If a rule requires a core engine change, it must go through a formal amendment process, not a silent edit.

## Mechanical Rulings
- **Target Profiles:** Public TargetProfiles are placed face down on the FRG at 9.2.0 step 2, not Beat 0. They are included with the action card in the ARG for covert actions.
- **Component-Verb Taxonomy:** The `Public Standing` component is a track, so the legal verb is `Shift` acting on the `StandingMarker`. You cannot `Add/Remove` a track.
- **Covert Blindness:** Covert actions cannot force a bribe or reveal information; they must remain blind. ModReacts cannot target covert space unless specific conditions (VM-xx) are met.

## Project Structure & Tooling
- **Database Synchronization:** `04___Card_System.md` Python blocks must strictly use their string `CardID` (e.g., `id = "STD.CA.1"`) to maintain synchronization with `the_signal_db`. Do not use integers or placeholders (`"TBD"`, `"—"`).
- **Minimum Faction Palettes:** Every faction must maintain a floor of 53 unique cards in their total playable palette (Standard + Faction). Standard is 54 cards, so the floor is mathematically met, but faction-specific cards must be densely populated to maintain faction identity variance.
- **Scratch Scripts:** Create and save all scratch/temporary python scripts used during a session in `/home/abosch/Projects/TheSignal/Whiteboard/scratch`. Do not save them in the main directory. They can later be promoted to a `/tools` or `/Database` folder if generalized for reuse.
- **Wiki Deployment:** When asked to update or build the wiki, you MUST run `./tools/deploy_wiki.sh` to ensure the wiki is built, synced via rsync, and hosted on the live Pi Zero server so the user can see the changes. Do not just run the local python build script.
