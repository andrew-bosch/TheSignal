import re

def remove_sec9_10():
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    # Find sec 9
    sec9_idx = content.find("## 9. Special Conditions & Gameplay Impacts")
    
    if sec9_idx != -1:
        # Delete everything from sec 9 onwards (since it's the end of the file)
        # But wait, there might be a trailing `---` or something before it. 
        # Let's find the `---` before sec 9 and cut there.
        # It's better to just use sec9_idx
        content = content[:sec9_idx].rstrip() + "\n"
        # also strip any trailing `---` that is now at the end of the file
        if content.endswith("---\n"):
            content = content[:-4]
        
    # Update TOC
    lines = content.split('\n')
    new_lines = [l for l in lines if "9. [Special Conditions" not in l and "10. [Examples" not in l]
    content = '\n'.join(new_lines)
    
    with open(md_file, "w") as f:
        f.write(content)
    print("Sections 9 and 10 removed and TOC updated.")

if __name__ == "__main__":
    remove_sec9_10()
