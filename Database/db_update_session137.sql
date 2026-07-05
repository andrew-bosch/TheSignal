START TRANSACTION;

-- S137: Ring ModReactCard design-review content pass (09-16 step 2) —
-- STD.MOD.98-133 (36 cards, all 3 rings) got real Design Rationale, Card
-- Story, and honest 22-row checklist verdicts written this session.
-- design_pass=1 means a full first review pass is done (Andy's Status-table
-- semantics, S137) — NOT the same as issues_resolved, which stays 0 for
-- every one of these: each carries at least one genuinely open item
-- (deferred persistence/resolution_type schema question, undocumented
-- Stack-behavior question, or the Standing-vs-Information taxonomy
-- conflict tracked at PM05 04-n173). See Whiteboard/schema_cleanup_log.md
-- and PM05 04-n171/04-n173.
UPDATE card_status
SET design_pass = 1
WHERE card_id LIKE 'STD.MOD.%'
  AND CAST(SUBSTRING_INDEX(card_id, '.', -1) AS UNSIGNED) BETWEEN 98 AND 133;

-- 04-n173 (closed S137): Standing-track mutations (`faction(holder).standing.add(1)`)
-- were tagged two different inconsistent ways (Standing/Add on 107/108/109/119/120/
-- 121/131/132/133, Information/Add on 102/114/126). Andy's correction: the matrix
-- marks Standing x Add as invalid ("subsumed by Shift") — unify all 12 to
-- Standing/Shift, the layer matching what the effect actually mutates.
UPDATE card_status
SET layer = 'Standing', function = 'Shift'
WHERE card_id IN (
  'STD.MOD.102','STD.MOD.107','STD.MOD.108','STD.MOD.109','STD.MOD.114',
  'STD.MOD.119','STD.MOD.120','STD.MOD.121','STD.MOD.126',
  'STD.MOD.131','STD.MOD.132','STD.MOD.133'
);

-- 04-n175 (in progress S137): faction ModReactCard taxonomy sweep, Directorate
-- pattern-set (9 cards, all previously untagged). DIR.MOD.6/8/9 required real
-- judgment calls (Andy confirmed 8/9; 6 revised after checking DIR.PA.1 directly
-- and finding the cited precedent didn't actually match this card's mechanism).
UPDATE card_status SET layer='Territory', function='Remove',  subject='PresenceToken' WHERE card_id='DIR.MOD.1';
UPDATE card_status SET layer='Territory', function='Remove',  subject='PresenceToken' WHERE card_id='DIR.MOD.2';
UPDATE card_status SET layer='Territory', function='Remove',  subject='PresenceToken' WHERE card_id='DIR.MOD.3';
UPDATE card_status SET layer='Economy',   function='Add',     subject='NativeResource' WHERE card_id='DIR.MOD.4';
UPDATE card_status SET layer='Economy',   function='Add',     subject='NativeResource' WHERE card_id='DIR.MOD.5';
UPDATE card_status SET layer='Submission',function='Modify',  subject='PublicAct'      WHERE card_id='DIR.MOD.6';
UPDATE card_status SET layer='Territory', function='Add',     subject='PresenceToken' WHERE card_id='DIR.MOD.7';
UPDATE card_status SET layer='Submission',function='Remove',  subject='NativeResource' WHERE card_id='DIR.MOD.8';
UPDATE card_status SET layer='Submission',function='Block',   subject='PublicAct'      WHERE card_id='DIR.MOD.9';

-- 04-n173 follow-up (S137): the Standing/Shift fix left subject=PublicStanding
-- unchanged; S126 had already corrected 5 other cards to subject=StandingMarker
-- for this exact mutation shape. Applying the same correction to all 12 Ring cards.
UPDATE card_status SET subject='StandingMarker'
WHERE card_id IN (
  'STD.MOD.102','STD.MOD.107','STD.MOD.108','STD.MOD.109','STD.MOD.114',
  'STD.MOD.119','STD.MOD.120','STD.MOD.121','STD.MOD.126',
  'STD.MOD.131','STD.MOD.132','STD.MOD.133'
);

-- 04-n175 (in progress S137): faction ModReactCard taxonomy sweep, Ghost (8 cards,
-- GHO.MOD.9/10/11 excluded — already tagged, tracked separately at 04-n174).
UPDATE card_status SET layer='Information', function='Remove', subject='IntelToken'     WHERE card_id='GHO.MOD.1';
UPDATE card_status SET layer='Information', function='Add',    subject='IntelToken'     WHERE card_id='GHO.MOD.2';
UPDATE card_status SET layer='Information', function='Add',    subject='IntelToken'     WHERE card_id='GHO.MOD.3';
UPDATE card_status SET layer='Information', function='Add',    subject='IntelToken'     WHERE card_id='GHO.MOD.4';
UPDATE card_status SET layer='Standing',    function='Shift',  subject='StandingMarker' WHERE card_id='GHO.MOD.5';
UPDATE card_status SET layer='Economy',     function='Copy',   subject='NativeResource' WHERE card_id='GHO.MOD.6';
UPDATE card_status SET layer='Territory',   function='Redirect',subject='PresenceToken' WHERE card_id='GHO.MOD.7';
UPDATE card_status SET layer='Territory',   function='Remove', subject='PresenceToken' WHERE card_id='GHO.MOD.8';

-- 04-n175 (in progress S137): faction ModReactCard taxonomy sweep, Guild.
-- GUI.MOD.1 already correct in DB (Territory/Add/PresenceToken) — MD-only cleanup,
-- no DB change needed. GUI.MOD.10 deliberately left untagged (04-n176 — no
-- taxonomy-supported effect shape exists for this card; needs redesign).
UPDATE card_status SET layer='Economy',   function='Add', subject='NativeResource' WHERE card_id='GUI.MOD.2';
UPDATE card_status SET layer='Economy',   function='Add', subject='NativeResource' WHERE card_id='GUI.MOD.3';
UPDATE card_status SET layer='Economy',   function='Add', subject='NativeResource' WHERE card_id='GUI.MOD.4';
UPDATE card_status SET layer='Economy',   function='Add', subject='ModifierCard'   WHERE card_id='GUI.MOD.5';
UPDATE card_status SET layer='Territory', function='Add', subject='StructureBlock' WHERE card_id='GUI.MOD.6';
UPDATE card_status SET layer='Territory', function='Add', subject='PresenceToken'  WHERE card_id='GUI.MOD.7';
UPDATE card_status SET layer='Economy',   function='Add', subject='NativeResource' WHERE card_id='GUI.MOD.8';
UPDATE card_status SET layer='Economy',   function='Add', subject='NativeResource' WHERE card_id='GUI.MOD.9';

-- 04-n175 (in progress S137): faction ModReactCard taxonomy sweep, Network (12 of
-- 14 cards — NET.MOD.11/12 already tagged, excluded here). NET.MOD.1/2 had no
-- layer/function/subject fields declared at all (not just None) — added them.
UPDATE card_status SET layer='Territory', function='Add',      subject='PresenceToken' WHERE card_id='NET.MOD.1';
UPDATE card_status SET layer='Standing',  function='Shift',    subject='StandingMarker' WHERE card_id='NET.MOD.2';
UPDATE card_status SET layer='Standing',  function='Shift',    subject='StandingMarker' WHERE card_id='NET.MOD.3';
UPDATE card_status SET layer='Territory', function='Add',      subject='PresenceToken' WHERE card_id='NET.MOD.4';
UPDATE card_status SET layer='Territory', function='Add',      subject='PresenceToken' WHERE card_id='NET.MOD.5';
UPDATE card_status SET layer='Territory', function='Add',      subject='PresenceToken' WHERE card_id='NET.MOD.6';
UPDATE card_status SET layer='Economy',   function='Add',      subject='ModifierCard'  WHERE card_id='NET.MOD.7';
UPDATE card_status SET layer='Territory', function='Add',      subject='PresenceToken' WHERE card_id='NET.MOD.8';
UPDATE card_status SET layer='Economy',   function='Add',      subject='ModifierCard'  WHERE card_id='NET.MOD.9';
UPDATE card_status SET layer='Territory', function='Redirect', subject='PresenceToken' WHERE card_id='NET.MOD.10';
UPDATE card_status SET layer='Submission',function='Protect',  subject='PublicAct'     WHERE card_id='NET.MOD.13';
UPDATE card_status SET layer='Economy',   function='Add',      subject='ModifierCard'  WHERE card_id='NET.MOD.14';

-- 04-n175 (S137): faction ModReactCard taxonomy sweep, Syndicate (10 of 11 cards —
-- SYN.MOD.1 is Issued/ModIssuedCard, a different subclass, excluded). Completes
-- 04-n175 across all 5 factions.
UPDATE card_status SET layer='Economy',    function='Add',    subject='NativeResource' WHERE card_id='SYN.MOD.2';
UPDATE card_status SET layer='Economy',    function='Add',    subject='NativeResource' WHERE card_id='SYN.MOD.3';
UPDATE card_status SET layer='Economy',    function='Add',    subject='NativeResource' WHERE card_id='SYN.MOD.4';
UPDATE card_status SET layer='Economy',    function='Add',    subject='NativeResource' WHERE card_id='SYN.MOD.5';
UPDATE card_status SET layer='Submission', function='Modify', subject='PublicAct'      WHERE card_id='SYN.MOD.6';
UPDATE card_status SET layer='Economy',    function='Add',    subject='NativeResource' WHERE card_id='SYN.MOD.7';
UPDATE card_status SET layer='Territory',  function='Add',    subject='StructureBlock' WHERE card_id='SYN.MOD.8';
UPDATE card_status SET layer='Standing',   function='Shift',  subject='StandingMarker' WHERE card_id='SYN.MOD.9';
UPDATE card_status SET layer='Submission', function='Modify', subject='PublicAct'      WHERE card_id='SYN.MOD.10';
UPDATE card_status SET layer='Information',function='Corrupt',subject='Accord'         WHERE card_id='SYN.MOD.11';

COMMIT;
