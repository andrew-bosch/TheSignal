import mysql.connector

def main():
    conn = mysql.connector.connect(
        host="10.0.0.14",
        user="abosch",
        password="Ptt0hds",
        database="the_signal_db"
    )
    cursor = conn.cursor()

    sql = """
    CREATE OR REPLACE VIEW v_card_recommended_cost_all AS
    SELECT 
        v.card_id,
        v.name,
        v.function,
        v.subject,
        COALESCE(v.raw_resource_cost, 0) AS current_raw_cost,
        v.base_success_pct AS current_success_pct,
        v.effective_cost AS current_effective_cost,
        
        -- Calculate Primary Base TEC
        (u.base_uvm_cost * CASE 
            WHEN v.function = 'Remove' THEN 1.5 
            WHEN v.function IN ('Redirect', 'Replace') THEN 2.5 
            WHEN v.function = 'Protect' THEN 0.75 
            WHEN v.function = 'Shift' THEN 1.0 
            ELSE 1.0 
        END) AS primary_base_tec,

        -- Calculate Secondary Additive Value
        (
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*standing \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StandingMarker'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(structure \\\\+=|StructureBlock)', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StructureBlock'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*inteltoken', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='IntelToken'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*resource\\\\.(native|capital) \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='NativeResource'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*AccordForm', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='AccordCard'), 0)
        ) AS secondary_additive_value,

        -- Calculate Final TEC (Base * Multipliers + Additive)
        (
            (u.base_uvm_cost * CASE 
                WHEN v.function = 'Remove' THEN 1.5 
                WHEN v.function IN ('Redirect', 'Replace') THEN 2.5 
                WHEN v.function = 'Protect' THEN 0.75 
                WHEN v.function = 'Shift' THEN 1.0 
                ELSE 1.0 
            END) 
            * IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 2|count=2)', 2.0, 1.0)
            * IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 3|count=3)', 3.0, 1.0)
        ) + 
        (
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*standing \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StandingMarker'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(structure \\\\+=|StructureBlock)', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StructureBlock'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*inteltoken', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='IntelToken'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*resource\\\\.(native|capital) \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='NativeResource'), 0) +
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*AccordForm', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='AccordCard'), 0)
        ) AS base_tec,
        
        -- Calculate Delta
        ROUND(
            (
                (u.base_uvm_cost * CASE 
                    WHEN v.function = 'Remove' THEN 1.5 
                    WHEN v.function IN ('Redirect', 'Replace') THEN 2.5 
                    WHEN v.function = 'Protect' THEN 0.75 
                    WHEN v.function = 'Shift' THEN 1.0 
                    ELSE 1.0 
                END) 
                * IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 2|count=2)', 2.0, 1.0)
                * IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 3|count=3)', 3.0, 1.0)
            ) + 
            (
                IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*standing \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StandingMarker'), 0) +
                IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(structure \\\\+=|StructureBlock)', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='StructureBlock'), 0) +
                IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*inteltoken', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='IntelToken'), 0) +
                IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*resource\\\\.(native|capital) \\\\+=', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='NativeResource'), 0) +
                IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*AccordForm', (SELECT base_uvm_cost FROM uvm_assumptions WHERE subject='AccordCard'), 0)
            ) - v.effective_cost, 2
        ) AS current_cost_delta,

        CONCAT_WS(', ',
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 2|count=2)','Multiplier(x2)',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(presence \\\\+= 3|count=3)','Multiplier(x3)',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*n_boost','Multiplier(Boost)',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*standing \\\\+=','+Standing',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*standing -=','-Standing',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*(structure \\\\+=|StructureBlock)','+Structure',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*structure -=','-Structure',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*inteltoken','+Intel',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*resource\\\\.(native|capital) \\\\+=','+Resource',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*ContestedMarker','+ContestedMarker',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*remove(_modifier|\\\\(modifier)','-ModifierCards',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*NotificationSlip','Intel(NotificationSlip)',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*Discovery','Intel(Discovery)',NULL),
            IF(v.effect_text REGEXP '\\\\[(success|fail)\\\\][^|]*AccordForm','+AccordForm',NULL)
        ) AS secondary_taxonomy,
        v.effect_text 
    FROM v_card_effective_cost v
    JOIN uvm_assumptions u ON v.subject = u.subject
    WHERE v.effective_cost IS NOT NULL
    ORDER BY v.function DESC, secondary_taxonomy;
    """

    cursor.execute(sql)
    conn.commit()
    print("View successfully updated with advanced Secondary Effect TEC logic!")

if __name__ == "__main__":
    main()
