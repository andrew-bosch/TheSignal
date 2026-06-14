START TRANSACTION;

-- Delete duplicate component ID 22 (Chorus Portrait)
DELETE FROM component WHERE id = 22;

-- Rename ID 50 to 'Chorus Portrait track' and make it receivable=1
UPDATE component 
SET name = 'Chorus Portrait track', 
    receivable = 1 
WHERE id = 50;

-- Register Visibility Marker (id=103)
INSERT INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (103, 'Visibility Marker', 1, 0, 0, 0, 0);

-- Register Boost Marker (id=104)
INSERT INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (104, 'Boost Marker', 1, 0, 0, 0, 0);

-- Recreate v_placement_matrix view with updated component names and columns
CREATE OR REPLACE VIEW v_placement_matrix AS
select `c`.`name` AS `subject`,
  max(if(`t`.`name` = 'District tile',if(`st`.`target_id` is not null,1,0),0)) AS `District_tile`,
  max(if(`t`.`name` = 'Public Standing',if(`st`.`target_id` is not null,1,0),0)) AS `Public_Standing`,
  max(if(`t`.`name` = 'Chorus Portrait track',if(`st`.`target_id` is not null,1,0),0)) AS `Chorus_Portrait_track`,
  max(if(`t`.`name` = 'Session Timeline',if(`st`.`target_id` is not null,1,0),0)) AS `Session_Timeline`,
  max(if(`t`.`name` = 'Initiative strip',if(`st`.`target_id` is not null,1,0),0)) AS `Initiative_strip`,
  max(if(`t`.`name` = 'Faction Terminal',if(`st`.`target_id` is not null,1,0),0)) AS `Faction_Terminal`,
  max(if(`t`.`name` = 'The Overview',if(`st`.`target_id` is not null,1,0),0)) AS `The_Overview`,
  max(if(`t`.`name` = 'Arbiter Tableau',if(`st`.`target_id` is not null,1,0),0)) AS `Arbiter_Tableau`,
  max(if(`t`.`name` = 'Chorus Activity Track',if(`st`.`target_id` is not null,1,0),0)) AS `Chorus_Activity_Track`,
  max(if(`t`.`name` = 'Reservoir',if(`st`.`target_id` is not null,1,0),0)) AS `Reservoir`,
  max(if(`t`.`name` = 'Backlog',if(`st`.`target_id` is not null,1,0),0)) AS `Backlog`,
  max(if(`t`.`name` = 'Dispatch case',if(`st`.`target_id` is not null,1,0),0)) AS `Dispatch_case` 
from ((`component` `c` join `component` `t`) 
  left join `subject_target` `st` on(`st`.`subject_id` = `c`.`id` and `st`.`target_id` = `t`.`id`)) 
where `c`.`actionable` = 1 and `t`.`receivable` = 1 
group by `c`.`id`,`c`.`name` 
order by `c`.`name`;

COMMIT;
