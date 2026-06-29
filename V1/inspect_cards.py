import re

cards = [
    "DIR.CA.2", "DIR.PA.1", "DIR.PA.2", "DIR.MOD.6", "DIR.MOD.8",
    "SYN.CA.3", "SYN.CA.5", "SYN.MOD.5", "SYN.MOD.8",
    "NET.CA.4", "NET.PA.2", "NET.MOD.2", "NET.MOD.9",
    "GHO.PA.4", "GHO.MOD.5", "GHO.MOD.7"
]

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

for card in cards:
    print(f"--- {card} ---")
    # find python definition
    match = re.search(fr'{card.replace(".", r"\.")}\s*=\s*Card\(', content)
    if match:
        start_idx = match.start()
        end_idx = content.find('\n)', start_idx)
        block = content[start_idx:end_idx+2]
        
        # Look for design_note inside python block
        dn_match = re.search(r'design_note\s*=\s*(.*)', block)
        if dn_match:
            print("Python design_note:", dn_match.group(1)[:100])
        else:
            print("Python design_note: Not found")
            
        # Look for Markdown Design Rationale before it
        md_search_start = max(0, start_idx - 2000)
        md_block = content[md_search_start:start_idx]
        if "#### Design Rationale" in md_block:
            # find the paragraph after it
            md_match = re.search(r'#### Design Rationale\n(.*?)(?=\n#|\n\*\*)', md_block, re.DOTALL)
            if md_match:
                print("Markdown Rationale:", md_match.group(1).strip()[:100].replace('\n', ' '))
    else:
        print("Card definition not found!")
