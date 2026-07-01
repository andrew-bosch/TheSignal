import re

def move_section():
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    # 1. Find section 7 bounds
    sec7_start = content.find("## 7. Geometry & Display Requirements")
    sec8_start = content.find("## 8. Starting Configuration")
    
    if sec7_start == -1 or sec8_start == -1:
        print("Could not find section 7 or 8")
        return
        
    sec7_content = content[sec7_start + len("## 7. Geometry & Display Requirements\n"):sec8_start].strip()
    
    # Remove section 7 from current place
    content = content[:sec7_start] + content[sec8_start:]
    
    # 2. Insert sec7_content before "### 6.1 Universal Schemas"
    sec61_start = content.find("### 6.1 Universal Schemas")
    if sec61_start == -1:
        print("Could not find 6.1")
        return
        
    insert_content = "\n" + sec7_content + "\n\n"
    content = content[:sec61_start] + insert_content + content[sec61_start:]
    
    # 3. Renumber headers 8, 9, 10 to 7, 8, 9 in both body and TOC (if present)
    content = content.replace("## 8. Starting Configuration", "## 7. Starting Configuration")
    content = content.replace("## 9. Faction Player Tableau", "## 8. Faction Player Tableau")
    content = content.replace("## 10. ARBITER Tableau", "## 9. ARBITER Tableau")
    content = content.replace("## 11. Special Conditions & Gameplay Impacts", "## 10. Special Conditions & Gameplay Impacts")
    content = content.replace("## 12. Examples & Exceptions", "## 11. Examples & Exceptions")
    
    # Update TOC (assuming standard markdown links)
    content = content.replace("8. [Starting Configuration](#8-starting-configuration)", "7. [Starting Configuration](#7-starting-configuration)")
    content = content.replace("9. [Faction Player Tableau](#9-faction-player-tableau)", "8. [Faction Player Tableau](#8-faction-player-tableau)")
    content = content.replace("10. [ARBITER Tableau](#10-arbiter-tableau)", "9. [ARBITER Tableau](#9-arbiter-tableau)")
    content = content.replace("11. [Special Conditions & Gameplay Impacts](#11-special-conditions-gameplay-impacts)", "10. [Special Conditions & Gameplay Impacts](#10-special-conditions-gameplay-impacts)")
    content = content.replace("12. [Examples & Exceptions](#12-examples-exceptions)", "11. [Examples & Exceptions](#11-examples-exceptions)")
    
    with open(md_file, "w") as f:
        f.write(content)
    print("Section 7 moved and headers renumbered.")

if __name__ == "__main__":
    move_section()
