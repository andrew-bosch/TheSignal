import subprocess
import csv
import io

def query_db():
    query = """
    SELECT card_id, name, function, subject, base_success_pct, raw_resource_cost, 
           intel_tokens_in_cost, effective_cost, effect_text 
    FROM the_signal_db.v_card_effective_cost 
    WHERE effective_cost IS NOT NULL
    """
    result = subprocess.check_output(['mariadb', '-Bse', query], text=True)
    return list(csv.reader(io.StringIO(result), delimiter='\t'))

def score_impact(function, subject, effect_text):
    score = 0
    tags = []
    
    # Heuristic scoring on Verb + Subject
    if subject == 'StructureBlock':
        if function in ['Add', 'Remove', 'Redirect']: score += 4
    elif subject == 'PresenceToken':
        score += 2
    elif subject == 'IntelToken':
        score += 3
    elif subject == 'StandingMarker' or 'standing' in subject.lower():
        score += 5
    elif subject == 'PublicAct':
        score += 3
    elif subject == 'ClassifiedDirective':
        score += 6
        
    # Text parsing for hidden mechanics
    effect_lower = effect_text.lower()
    if 'standing +=' in effect_lower or 'standing -=' in effect_lower:
        score += 4
        tags.append('STANDING_SWING')
    if 'game.transfer' in effect_lower or 'game.replace_presence' in effect_lower:
        score += 5
        tags.append('STEAL_WIPE_MECHANIC')
    if 'boost' in effect_lower: # Catching blind spots
        tags.append('HAS_BOOST')
        score += 1 # Boosts increase theoretical ceiling
    if 'successcrit' in effect_lower:
        tags.append('CRIT_SCALING')
    if '100' in base_success_pct_str(effect_lower): # Automatic success
        tags.append('AUTO_SUCCESS')

    # Normalize into 5 Tiers
    if score <= 2: final_tier = 1
    elif score <= 4: final_tier = 2
    elif score <= 6: final_tier = 3
    elif score <= 8: final_tier = 4
    else: final_tier = 5
        
    return final_tier, tags

def base_success_pct_str(text):
    return text # Helper placeholder

def main():
    rows = query_db()
    tier_distribution = {1:0, 2:0, 3:0, 4:0, 5:0}
    mismatches = []
    
    for row in rows:
        card_id, name, function, subject, base_success_pct, raw_cost, intel_cost, eff_cost, effect_text = row
        eff_cost = float(eff_cost) if eff_cost != 'NULL' else 0.0
        
        tier, tags = score_impact(function, subject, effect_text)
        tier_distribution[tier] += 1
        
        # Game Designer Logic: Flag mismatches between Impact Tier and Mathematical Cost
        if tier >= 4 and eff_cost <= 4.0:
            mismatches.append(f"- **UNDERPRICED DANGER:** `{card_id}` '{name}' (Tier {tier} Impact | Cost {eff_cost:.2f}) | {tags}")
        elif tier <= 2 and eff_cost >= 8.0:
            mismatches.append(f"- **OVERPRICED DANGER:** `{card_id}` '{name}' (Tier {tier} Impact | Cost {eff_cost:.2f}) | {tags}")
            
    with open('/home/abosch/Projects/TheSignal/Whiteboard/scratch/power_audit_report.md', 'w') as f:
        f.write("# Game Designer Power Curve Audit\n\n")
        f.write("### Impact Tier Distribution\n")
        for t in range(1, 6):
            f.write(f"- Tier {t}: {tier_distribution[t]} cards\n")
        f.write("\n### Flagged Costing Mismatches (Requires Review)\n")
        for m in mismatches:
            f.write(m + "\n")

if __name__ == "__main__":
    main()
