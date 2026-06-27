#!/usr/bin/env python3
import os
import shutil
import re
import yaml

# Directories to source files from
SOURCE_DIRS = {
    'V1': 'V1',
    'Whiteboard': 'Whiteboard',
    'Creative': 'Creative',
    'ClaudeIOS': 'ClaudeIOS'
}

WIKI_DIR = 'wiki_src'
DOCS_DIR = os.path.join(WIKI_DIR, 'docs')

# Category configuration mapping (clean names and sorting)
CATEGORIES = [
    {
        'id': 'home',
        'title': 'Overview',
        'files': []
    },
    {
        'id': 'world_factions',
        'title': 'World & Factions',
        'files': []
    },
    {
        'id': 'rules_design',
        'title': 'Rules & Design Policy',
        'files': []
    },
    {
        'id': 'components_mechanics',
        'title': 'Components & Mechanics',
        'files': []
    },
    {
        'id': 'toolkits_engine',
        'title': 'Toolkits & Engine',
        'files': []
    },
    {
        'id': 'project_management',
        'title': 'Project Management',
        'files': []
    },
    {
        'id': 'creative_vignettes',
        'title': 'Creative & Vignettes',
        'files': []
    },
    {
        'id': 'whiteboard',
        'title': 'Whiteboard & Notes',
        'files': []
    },
    {
        'id': 'system_tasks',
        'title': 'System & Tasks',
        'files': []
    }
]

# Global map of card IDs/slugs to support dynamic cross-document anchor routing
# Maps clean_token (e.g. 'c13', 'synpa3', 'dirca6') -> (filename, mkdocs_slug)
card_slug_map = {}

def make_mkdocs_slug(text):
    """
    Reproduces Python-Markdown's default TOC slugify behavior:
    1. Lowercase
    2. Strip any characters that are not alphanumeric, spaces, hyphens, or underscores (removes dots)
    3. Replace spaces and underscores with hyphens
    4. Collapse multiple hyphens
    """
    s = text.lower()
    s = re.sub(r'[^a-z0-9\s\-_]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def clean_title(filename):
    # Remove file extension
    base = os.path.splitext(filename)[0]
    # Replace triple underscores or double underscores with spaces
    base = re.sub(r'_{2,}', ' ', base)
    # Strip leading numbers like "01 " or "PM01 "
    base = re.sub(r'^(?:PM)?\d+(?:-init)?[ \-_]*', '', base)
    # Replace single underscores with spaces
    base = base.replace('_', ' ')
    # Capitalize nicely
    return base.strip()

def get_category_id(filename, relative_path):
    # Split files for card system
    if 'v1_04___Card_System_Part_' in filename:
        return 'components_mechanics'
        
    parts = relative_path.split(os.sep)
    if len(parts) > 1:
        parent_dir = parts[0]
        if parent_dir == 'V1':
            if filename.startswith('PM'):
                return 'project_management'
            elif filename.startswith('00 ') or filename.startswith('00___'):
                return 'world_factions'
            elif filename.startswith('00a') or filename.startswith('00b') or filename.startswith('00c') or filename.startswith('11___'):
                return 'rules_design'
            elif filename.startswith('07___') or filename.startswith('08___') or filename.startswith('03a___'):
                return 'toolkits_engine'
            else:
                return 'components_mechanics'
        elif parent_dir == 'Whiteboard':
            return 'whiteboard'
        elif parent_dir == 'Creative':
            return 'creative_vignettes'
        elif parent_dir == 'ClaudeIOS':
            return 'system_tasks'
            
    # Root markdown files
    if filename == 'README.md':
        return 'home'
    elif filename in ['GEMINI_CONTEXT.md', 'gem_task.md', 'gem_web_context.md']:
        return 'system_tasks'
    return 'whiteboard'

def split_card_system(src_path, dest_dir, file_map):
    print("Splitting V1/04___Card_System.md and extracting card IDs for slug-routing...")
    with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    parts = {
        'Core': [],
        'Standard': [],
        'Guild': [],
        'Ghost': [],
        'Directorate': [],
        'Network': [],
        'Syndicate': [],
        'Rules': []
    }
    
    filenames = {
        'Core': 'v1_04___Card_System_Part_1_Core.md',
        'Standard': 'v1_04___Card_System_Part_2_Standard.md',
        'Guild': 'v1_04___Card_System_Part_3a_Guild.md',
        'Ghost': 'v1_04___Card_System_Part_3b_Ghost.md',
        'Directorate': 'v1_04___Card_System_Part_3c_Directorate.md',
        'Network': 'v1_04___Card_System_Part_3d_Network.md',
        'Syndicate': 'v1_04___Card_System_Part_3e_Syndicate.md',
        'Rules': 'v1_04___Card_System_Part_4_Rules.md'
    }
    
    current_part = 'Core'
    current_file = filenames['Core']
    current_slug = None
    current_section_type = 'c' # 'c' for covert, 'p' for public
    
    for line in lines:
        # Detect section shifts
        if line.startswith('## Standard'):
            current_part = 'Standard'
            current_file = filenames['Standard']
        elif line.startswith('## Guild'):
            current_part = 'Guild'
            current_file = filenames['Guild']
        elif line.startswith('## Ghost'):
            current_part = 'Ghost'
            current_file = filenames['Ghost']
        elif line.startswith('## Directorate'):
            current_part = 'Directorate'
            current_file = filenames['Directorate']
        elif line.startswith('## Network'):
            current_part = 'Network'
            current_file = filenames['Network']
        elif line.startswith('## Syndicate'):
            current_part = 'Syndicate'
            current_file = filenames['Syndicate']
        elif line.startswith('## 8. Card Taxonomy Index'):
            current_part = 'Rules'
            current_file = filenames['Rules']
            
        parts[current_part].append(line)
        
        # Track if standard/faction covert vs public for correct C/P routing fallback
        if 'covert operations' in line.lower() or 'covert' in line.lower():
            current_section_type = 'c'
        elif 'public acts' in line.lower() or 'public act' in line.lower() or 'public' in line.lower():
            current_section_type = 'p'

        # Extract slug and card codes from card headings
        if line.startswith('### '):
            header_text = line.replace('### ', '').strip()
            
            # Generate MkDocs-style slug using standard slugify rules
            slug = make_mkdocs_slug(header_text)
            current_slug = slug
            
            # Map heading ID token (e.g. "GUI.CA.1" -> "guica1")
            match = re.match(r'^([A-Za-z0-9\.\-_]+)', header_text)
            if match:
                raw_id = match.group(1)
                clean_id = re.sub(r'[^a-z0-9]+', '', raw_id.lower())
                card_slug_map[clean_id] = (current_file, slug)
                
        # Parse python card blocks for integer IDs to associate c13/p09
        id_match = re.search(r'\bid\s*=\s*(\d+)', line)
        if id_match and current_slug and current_file:
            card_id = int(id_match.group(1))
            prefix = current_section_type
            
            # Add mappings for c11, c011, etc.
            card_slug_map[f"{prefix}{card_id}"] = (current_file, current_slug)
            card_slug_map[f"{prefix}{card_id:02d}"] = (current_file, current_slug)
            
    # Write files
    for part_name, part_lines in parts.items():
        filename = filenames[part_name]
        filepath = os.path.join(dest_dir, filename)
        
        content = "".join(part_lines)
        # Ensure the file starts with a title for MkDocs
        if not content.strip().startswith('#'):
            title = part_name
            if part_name == 'Rules':
                title = 'Rules & Appendix'
            elif part_name == 'Core':
                title = 'Overview & Structure'
            else:
                title = f"{title} Cards"
            content = f"# Card System - {title}\n\n" + content
            
        with open(filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(content)
            
        # Register in file map
        fake_rel_path = f"V1/{filename.replace('v1_', '')}"
        file_map[fake_rel_path] = filename

    # Map the original Card System link to the Core Part
    file_map['V1/04___Card_System.md'] = filenames['Core']

def resolve_card_anchor(anchor_link):
    clean_anchor = re.sub(r'[^a-z0-9]+', '', anchor_link.lower().lstrip('#'))
    if not clean_anchor:
        return None
        
    # Find the longest matching key in card_slug_map that the anchor starts with
    matched_key = None
    for key in card_slug_map:
        if clean_anchor.startswith(key):
            if matched_key is None or len(key) > len(matched_key):
                matched_key = key
                
    if matched_key:
        return card_slug_map[matched_key]
    return None

def build_wiki():
    print("Initializing Wiki Source Directories...")
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)
    
    # Ensure images scratch directory is ready if we need images
    os.makedirs(os.path.join(DOCS_DIR, 'images'), exist_ok=True)
    
    # Mapping of old paths (relative to workspace root) to new flat filenames
    file_map = {}
    
    # Copy root README.md as the index
    readme_path = 'README.md'
    if os.path.exists(readme_path):
        target_path = os.path.join(DOCS_DIR, 'index.md')
        shutil.copy2(readme_path, target_path)
        file_map['README.md'] = 'index.md'
        file_map['index.md'] = 'index.md'
        
    # Scan root files
    for f in os.listdir('.'):
        if f.endswith('.md') and f != 'README.md':
            dest_filename = f
            dest_path = os.path.join(DOCS_DIR, dest_filename)
            shutil.copy2(f, dest_path)
            file_map[f] = dest_filename

    # Scan directories
    for clean_name, src_dir in SOURCE_DIRS.items():
        if not os.path.exists(src_dir):
            continue
        
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if file.endswith('.md'):
                    # Skip the large card system file - handled separately
                    if file == '04___Card_System.md':
                        continue
                        
                    full_src_path = os.path.join(root, file)
                    rel_src_path = os.path.relpath(full_src_path, '.')
                    
                    # Flatten directory structure for mkdocs simplicity, keeping subfolder prefix
                    folder_prefix = ""
                    parts = os.path.split(root)
                    if parts[0] != '' and parts[0] != src_dir:
                        # Inside a sub-subdirectory (like Creative/Vignettes)
                        folder_prefix = os.path.basename(root).lower() + "_"
                        
                    dest_filename = f"{clean_name.lower()}_{folder_prefix}{file}"
                    dest_path = os.path.join(DOCS_DIR, dest_filename)
                    
                    shutil.copy2(full_src_path, dest_path)
                    file_map[rel_src_path] = dest_filename
                    
    # Handle the large Card System file (splitting it into parts and building slug map)
    card_system_path = os.path.join('V1', '04___Card_System.md')
    if os.path.exists(card_system_path):
        split_card_system(card_system_path, DOCS_DIR, file_map)

    # 2. Rewrite relative markdown links and resolve anchors to prevent 404s
    print("Rewriting relative links and routing anchors...")
    norm_file_map = {k.replace('\\', '/'): v for k, v in file_map.items()}
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for dest_file in os.listdir(DOCS_DIR):
        if not dest_file.endswith('.md'):
            continue
        dest_path = os.path.join(DOCS_DIR, dest_file)
        with open(dest_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        def replace_link(match):
            text = match.group(1)
            link = match.group(2)
            
            # Skip absolute web URLs, mailto, or local protocols
            if link.startswith(('http://', 'https://', 'mailto:', 'file://')):
                return match.group(0)
                
            # Special case: Anchor-only link inside split files
            if link.startswith('#'):
                routed = resolve_card_anchor(link)
                if routed:
                    target_file, target_slug = routed
                    return f"[{text}]({target_file}#{target_slug})"
                
                # If we couldn't route but it's local, normalize the local anchor to match MkDocs
                normalized_anchor = make_mkdocs_slug(link)
                return f"[{text}](#{normalized_anchor})"
                
            anchor = ""
            if "#" in link:
                link, anchor = link.split("#", 1)
                anchor = "#" + anchor
                
            if "?" in link:
                link, _ = link.split("?", 1)
                
            # Clean link path
            clean_link = re.sub(r'^[\./\\]+', '', link)
            clean_link = clean_link.replace('\\', '/')
            
            # Look for a match in the mapping
            matched_val = None
            for old_path, new_name in norm_file_map.items():
                if old_path == clean_link or old_path.endswith('/' + clean_link):
                    matched_val = new_name
                    break
                    
            if matched_val:
                # If we mapped to Core but there is an anchor, resolve it to the specific split file!
                if matched_val == 'v1_04___Card_System_Part_1_Core.md' and anchor:
                    routed = resolve_card_anchor(anchor)
                    if routed:
                        target_file, target_slug = routed
                        return f"[{text}]({target_file}#{target_slug})"
                    else:
                        normalized_anchor = make_mkdocs_slug(anchor)
                        anchor = "#" + normalized_anchor
                return f"[{text}]({matched_val}{anchor})"
            return match.group(0)
            
        new_content = link_pattern.sub(replace_link, content)
        if new_content != content:
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    # 3. Populate Categories for mkdocs navigation
    all_md_files = []
    
    # Populate root README/index
    if os.path.exists(readme_path):
        all_md_files.append(('README.md', 'index.md', 'home'))
        
    for k, v in file_map.items():
        if k in ['README.md', 'index.md', 'V1/04___Card_System.md']:
            continue
        # Split normalized path to get category
        category = get_category_id(os.path.basename(k), k)
        all_md_files.append((os.path.basename(k), v, category))
        
    for title_name, dest_name, category_id in all_md_files:
        category = next((c for c in CATEGORIES if c['id'] == category_id), None)
        if category:
            clean_name = clean_title(title_name)
            category['files'].append({
                clean_name: dest_name
            })
            
    # Sort files within categories by name
    for cat in CATEGORIES:
        cat['files'] = sorted(cat['files'], key=lambda x: list(x.keys())[0])

    # 4. Create mkdocs.yml
    config = {
        'site_name': 'The Signal Wiki',
        'site_description': 'Documentation and Specifications for Project: The Signal',
        'site_author': 'DeepMind Antigravity Team',
        'theme': {
            'name': 'material',
            'palette': [
                {
                    'media': '(prefers-color-scheme: light)',
                    'scheme': 'default',
                    'primary': 'indigo',
                    'accent': 'indigo',
                    'toggle': {
                        'icon': 'material/brightness-7',
                        'name': 'Switch to dark mode'
                    }
                },
                {
                    'media': '(prefers-color-scheme: dark)',
                    'scheme': 'slate',
                    'primary': 'indigo',
                    'accent': 'cyan',
                    'toggle': {
                        'icon': 'material/brightness-4',
                        'name': 'Switch to light mode'
                    }
                }
            ],
            'features': [
                'navigation.tabs',
                'navigation.sections',
                'navigation.top',
                'search.suggest',
                'search.highlight',
                'toc.integrate'  # Integrates TOC into the left sidebar for easy in-page navigation (e.g. card headers)
            ]
        },
        'markdown_extensions': [
            'admonition',
            'pymdownx.details',
            'pymdownx.superfences',
            'pymdownx.highlight',
            'pymdownx.inlinehilite',
            'tables',
            'toc'
        ],
        'nav': []
    }
    
    config['nav'].append({'Overview': 'index.md'})
    
    for cat in CATEGORIES:
        if cat['id'] == 'home':
            continue
        if cat['files']:
            config['nav'].append({cat['title']: cat['files']})
            
    # Write config file
    config_path = os.path.join(WIKI_DIR, 'mkdocs.yml')
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        
    print(f"Wiki sources built successfully in {WIKI_DIR}/")

if __name__ == '__main__':
    build_wiki()
