import re

def remove_sec7():
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    # Find sec 7 and sec 8
    sec7_idx = content.find("## 7. Starting Configuration")
    sec8_idx = content.find("## 8. Faction Player Tableau")
    
    if sec7_idx != -1 and sec8_idx != -1:
        # Delete sec 7 (including the trailing HR if it's there)
        content = content[:sec7_idx] + content[sec8_idx:]
        
    # Renumber 8 -> 7, 9 -> 8, 10 -> 9, 11 -> 10
    content = content.replace("## 8. Faction Player Tableau", "## 7. Faction Player Tableau")
    content = content.replace("## 9. ARBITER Tableau", "## 8. ARBITER Tableau")
    content = content.replace("## 10. Special Conditions & Gameplay Impacts", "## 9. Special Conditions & Gameplay Impacts")
    content = content.replace("## 11. Examples & Exceptions", "## 10. Examples & Exceptions")
    
    # Update TOC
    # Remove "7. Starting Configuration" line
    lines = content.split('\n')
    new_lines = [l for l in lines if "7. [Starting Configuration]" not in l]
    content = '\n'.join(new_lines)
    
    content = content.replace("8. [Faction Player Tableau](#8-faction-player-tableau)", "7. [Faction Player Tableau](#7-faction-player-tableau)")
    content = content.replace("9. [ARBITER Tableau](#9-arbiter-tableau)", "8. [ARBITER Tableau](#8-arbiter-tableau)")
    content = content.replace("10. [Special Conditions & Gameplay Impacts](#10-special-conditions-gameplay-impacts)", "9. [Special Conditions & Gameplay Impacts](#9-special-conditions-gameplay-impacts)")
    content = content.replace("11. [Examples & Exceptions](#11-examples-exceptions)", "10. [Examples & Exceptions](#10-examples-exceptions)")
    
    with open(md_file, "w") as f:
        f.write(content)
    print("Section 7 Removed and TOC updated.")

if __name__ == "__main__":
    remove_sec7()
