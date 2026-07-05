START TRANSACTION;

-- S136 (cont.): structure_pass backfill for the 5 per-faction Part files
-- (Guild/Ghost/Directorate/Network/Syndicate), scaffolded by
-- tools/card_scaffolder.py same session as db_update_session136.sql.
-- Exact ID list derived from tools/card_completeness_audit.py's
-- state=='scaffolded' rows for these 5 files - not a numeric range guess,
-- since faction files aren't sequential (partial-completeness cards like
-- GUI.MOD.9/10 are deliberately excluded, matching the scaffolder's skip).
UPDATE card_status
SET structure_pass = 1
WHERE card_id IN ('GUI.CA.7','GUI.CA.8','GUI.PA.3','GUI.PA.4','GUI.PA.5','GUI.PA.6','GUI.PA.7','GUI.PA.8','GUI.MOD.1','GUI.MOD.2','GUI.MOD.3','GUI.MOD.4','GUI.MOD.5','GUI.MOD.6','GUI.MOD.7','GUI.MOD.8','GUI.MOD.11','GUI.MOD.12','GUI.MOD.13','GUI.MOD.14','GUI.MOD.15','GUI.MOD.16','GUI.MOD.17','GUI.MOD.18','GUI.MOD.19','GUI.MOD.20','GUI.MOD.21','GUI.MOD.22','GUI.MOD.23','GUI.MOD.24','GUI.MOD.25','GUI.MOD.26','GHO.CA.15','GHO.CA.13','GHO.CA.14','GHO.MOD.2','GHO.MOD.3','GHO.MOD.4','GHO.MOD.5','GHO.MOD.6','GHO.MOD.7','GHO.MOD.8','GHO.MOD.9','GHO.MOD.10','GHO.MOD.11','GHO.MOD.12','GHO.MOD.13','GHO.MOD.14','GHO.MOD.15','GHO.MOD.16','GHO.MOD.17','GHO.MOD.18','GHO.MOD.19','GHO.MOD.20','GHO.MOD.21','GHO.MOD.22','GHO.MOD.23','GHO.MOD.24','GHO.MOD.25','GHO.MOD.26','GHO.MOD.27','DIR.PA.4','DIR.PA.5','DIR.PA.7','DIR.PA.8','DIR.PA.9','DIR.PA.10','DIR.PA.11','DIR.MOD.1','DIR.MOD.2','DIR.MOD.3','DIR.MOD.4','DIR.MOD.5','DIR.MOD.6','DIR.MOD.7','DIR.MOD.8','DIR.MOD.9','DIR.MOD.10','DIR.MOD.11','DIR.MOD.12','DIR.MOD.13','DIR.MOD.14','DIR.MOD.15','DIR.MOD.16','DIR.MOD.17','DIR.MOD.18','DIR.MOD.19','DIR.MOD.20','DIR.MOD.21','DIR.MOD.22','DIR.MOD.23','DIR.MOD.24','DIR.MOD.25','NET.CA.8','NET.PA.4','NET.PA.5','NET.PA.6','NET.MOD.3','NET.MOD.4','NET.MOD.5','NET.MOD.6','NET.MOD.7','NET.MOD.8','NET.MOD.9','NET.MOD.10','NET.MOD.11','NET.MOD.12','NET.MOD.13','NET.MOD.14','NET.MOD.15','NET.MOD.16','NET.MOD.17','NET.MOD.18','NET.MOD.19','NET.MOD.20','NET.MOD.21','NET.MOD.22','NET.MOD.23','NET.MOD.24','NET.MOD.25','NET.MOD.26','NET.MOD.27','NET.MOD.28','NET.MOD.29','NET.MOD.30','SYN.CA.12','SYN.PA.4','SYN.PA.5','SYN.MOD.2','SYN.MOD.3','SYN.MOD.4','SYN.MOD.5','SYN.MOD.6','SYN.MOD.7','SYN.MOD.8','SYN.MOD.9','SYN.MOD.10','SYN.MOD.11','SYN.MOD.12','SYN.MOD.13','SYN.MOD.14','SYN.MOD.15','SYN.MOD.16','SYN.MOD.17','SYN.MOD.18','SYN.MOD.19','SYN.MOD.20','SYN.MOD.21','SYN.MOD.22','SYN.MOD.23','SYN.MOD.24','SYN.MOD.25','SYN.MOD.26','SYN.MOD.27');

COMMIT;
