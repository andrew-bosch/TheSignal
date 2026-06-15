START TRANSACTION;

-- DB-S90-04 (03-n06): Register Dispatch Packet (ID=108)
INSERT INTO component (id, name, actionable, receivable, transform_visibility, transform_orientation, transform_data)
VALUES (108, 'Dispatch Packet', 1, 1, 0, 0, 0);

COMMIT;
