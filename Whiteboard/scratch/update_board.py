import sys

def main():
    file_path = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    new_table_path = "/home/abosch/Projects/TheSignal/Whiteboard/scratch/new_table.md"
    
    with open(new_table_path, "r") as f:
        new_table = f.read().strip()
        
    with open(file_path, "r") as f:
        lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if line.startswith("| Ring | Origin # | Origin District |"):
            start_idx = i
        if start_idx != -1 and i > start_idx and line.strip() == "":
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [new_table + "\n"] + lines[end_idx:]
        with open(file_path, "w") as f:
            f.writelines(new_lines)
        print("Successfully updated the adjacency table.")
    else:
        print(f"Could not find the table. start_idx={start_idx}, end_idx={end_idx}")

if __name__ == "__main__":
    main()
