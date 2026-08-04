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

# agent-memory's shared/ (cluster/infra facts, git repo external to this one) —
# fed into the wiki as its own "Homelab & Infra" nav section, top-level *.md only.
AGENT_MEMORY_SHARED_DIR = os.path.expanduser('~/Brain/agent-memory/shared')

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
        'title': 'Manuals and Engine',
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
    # Replace single underscores with spaces
    base = base.replace('_', ' ')
    # Capitalize nicely
    return base.strip()

def get_md_title(filepath, fallback):
    """First H1 in the file if present (markdown chars stripped), else the fallback title."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('# '):
                    return re.sub(r'[`*_]', '', line[2:]).strip()
                break
    except OSError:
        pass
    return fallback

def copy_homelab_docs():
    """Copies agent-memory's shared/*.md into the wiki as a 'Homelab & Infra' nav section."""
    if not os.path.isdir(AGENT_MEMORY_SHARED_DIR):
        print(f"Skipping Homelab & Infra section: {AGENT_MEMORY_SHARED_DIR} not found")
        return []

    dest_dir = os.path.join(DOCS_DIR, 'homelab')
    os.makedirs(dest_dir, exist_ok=True)

    nav_files = []
    for fname in sorted(os.listdir(AGENT_MEMORY_SHARED_DIR)):
        src_path = os.path.join(AGENT_MEMORY_SHARED_DIR, fname)
        if not fname.endswith('.md') or not os.path.isfile(src_path):
            continue
        dest_path = os.path.join(dest_dir, fname)
        shutil.copy2(src_path, dest_path)
        title = get_md_title(src_path, clean_title(fname))
        nav_files.append({title: f'homelab/{fname}'})

    return nav_files

def get_category_id(filename, relative_path):
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
            elif filename.startswith('03a___') or filename.startswith('09___') or filename.startswith('10___') or filename.startswith('10a___'):
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
    elif filename in ['GEMINI_CONTEXT.md', 'Claude_context.md', 'gem_task.md', 'gem_web_context.md']:
        return 'system_tasks'
    return 'whiteboard'

# Art 04 is physically split into 8 Part files as of S136 (source of truth).
# V1/04___Card_System.md is a generated monolith (tools/assemble_card_system.py)
# kept only for legacy analysis scripts - it is skipped in the normal copy loop
# below and never gets its own wiki page.
CARD_SYSTEM_PARTS = [
    '04___Card_System___Part1_Core.md',
    '04___Card_System___Part2_Standard.md',
    '04___Card_System___Part3_Ring_Modifiers.md',
    '04___Card_System___Part4a_Guild.md',
    '04___Card_System___Part4b_Ghost.md',
    '04___Card_System___Part4c_Directorate.md',
    '04___Card_System___Part4d_Network.md',
    '04___Card_System___Part4e_Syndicate.md',
]

def populate_card_slug_map(filepath, dest_filename):
    """Scan one already-copied Part file and extract card ID -> (file, slug) routes."""
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    current_slug = None
    current_section_type = 'c'  # 'c' for covert, 'p' for public

    for line in lines:
        if 'covert operations' in line.lower() or 'covert' in line.lower():
            current_section_type = 'c'
        elif 'public acts' in line.lower() or 'public act' in line.lower() or 'public' in line.lower():
            current_section_type = 'p'

        # Extract slug and card codes from card headings
        if line.startswith('### '):
            header_text = line.replace('### ', '').strip()
            slug = make_mkdocs_slug(header_text)
            current_slug = slug

            # Map heading ID token (e.g. "GUI.CA.1" -> "guica1")
            match = re.match(r'^([A-Za-z0-9\.\-_]+)', header_text)
            if match:
                raw_id = match.group(1)
                clean_id = re.sub(r'[^a-z0-9]+', '', raw_id.lower())
                card_slug_map[clean_id] = (dest_filename, slug)
                
            if ' — ' in header_text:
                parts = header_text.split(' — ', 1)
                card_name_slug = make_mkdocs_slug(parts[1])
                card_slug_map[card_name_slug] = (dest_filename, slug)

        # Parse python card blocks for integer IDs to associate c13/p09
        id_match = re.search(r'\bid\s*=\s*(\d+)', line)
        if id_match and current_slug:
            card_id = int(id_match.group(1))
            prefix = current_section_type
            card_slug_map[f"{prefix}{card_id}"] = (dest_filename, current_slug)
            card_slug_map[f"{prefix}{card_id:02d}"] = (dest_filename, current_slug)

def resolve_card_anchor(anchor_link):
    clean_anchor = anchor_link.lower().lstrip('#')
    if not clean_anchor:
        return None
        
    # Prioritize exact key matches and endswith matches (handles legacy cp IDs and prefixed anchors)
    for key in sorted(card_slug_map.keys(), key=len, reverse=True):
        if clean_anchor == key or clean_anchor.endswith('-' + key):
            return card_slug_map[key]
            
    # Fallback to prefix-based match (e.g. finding GUI.CA.1 from guica1)
    clean_alphanum = re.sub(r'[^a-z0-9]+', '', clean_anchor)
    matched_key = None
    for key in card_slug_map:
        if clean_alphanum.startswith(key):
            if matched_key is None or len(key) > len(matched_key):
                matched_key = key
                
    if matched_key:
        return card_slug_map[matched_key]
    return None

def split_large_markdown_file(src_path, dest_dir, dest_filename_prefix, max_cards_per_file=12):
    """Splits a large card system markdown file into multiple smaller files by card headings."""
    with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    cards = []
    header_lines = []
    lines = content.split('\n')
    current_card = None
    
    for line in lines:
        if line.startswith('### '):
            if current_card is not None:
                cards.append(current_card)
            current_card = [line]
        else:
            if current_card is None:
                header_lines.append(line)
            else:
                current_card.append(line)
    if current_card is not None:
        cards.append(current_card)
        
    header_text = '\n'.join(header_lines)
    
    # If total cards is smaller than threshold, write as a single file
    if len(cards) <= max_cards_per_file:
        dest_filename = f"{dest_filename_prefix}.md"
        shutil.copy2(src_path, os.path.join(dest_dir, dest_filename))
        return [dest_filename]
        
    # Otherwise, split into multiple files
    num_chunks = (len(cards) + max_cards_per_file - 1) // max_cards_per_file
    suffixes = [chr(97 + i) for i in range(num_chunks)]  # a, b, c...
    
    generated_filenames = [f"{dest_filename_prefix}_{s}.md" for s in suffixes]
    
    for i in range(num_chunks):
        suffix = suffixes[i]
        filename = generated_filenames[i]
        filepath = os.path.join(dest_dir, filename)
        
        chunk_cards = cards[i * max_cards_per_file : (i + 1) * max_cards_per_file]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            if i == 0:
                f.write(header_text)
                f.write('\n\n')
            else:
                f.write(f"# {clean_title(dest_filename_prefix)} — Part {suffix.upper()}\n\n")
                f.write(f"[← Back to Part A / Main]({generated_filenames[0]})\n\n")
                
            nav_links = []
            if i > 0:
                nav_links.append(f"[← Previous (Part {suffixes[i-1].upper()})]({generated_filenames[i-1]})")
            if i < num_chunks - 1:
                nav_links.append(f"[Next (Part {suffixes[i+1].upper()}) →]({generated_filenames[i+1]})")
                
            if nav_links:
                f.write(' | '.join(nav_links) + '\n\n---\n\n')
                
            for card in chunk_cards:
                f.write('\n'.join(card) + '\n\n')
                
            if nav_links:
                f.write('\n---\n\n' + ' | '.join(nav_links) + '\n')
                
    return generated_filenames

def build_wiki():
    print("Initializing Wiki Source Directories...")
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)
    
    # Ensure images scratch directory is ready if we need images
    os.makedirs(os.path.join(DOCS_DIR, 'images'), exist_ok=True)
    
    # Mapping of old paths (relative to workspace root) to new flat filenames
    file_map = {}
    split_files_map = {}
    
    # Copy root README.md as the index
    readme_path = 'README.md'
    if os.path.exists(readme_path):
        target_path = os.path.join(DOCS_DIR, 'index.md')
        shutil.copy2(readme_path, target_path)
        file_map['README.md'] = 'index.md'
        file_map['index.md'] = 'index.md'
        split_files_map['README.md'] = ['index.md']
        split_files_map['index.md'] = ['index.md']
        
    # Scan root files
    for f in os.listdir('.'):
        if f.endswith('.md') and f != 'README.md':
            dest_filename = f
            dest_path = os.path.join(DOCS_DIR, dest_filename)
            shutil.copy2(f, dest_path)
            file_map[f] = dest_filename
            split_files_map[f] = [dest_filename]

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
                        
                    dest_prefix = f"{clean_name.lower()}_{folder_prefix}{os.path.splitext(file)[0]}"
                    dest_filename = f"{dest_prefix}.md"
                    dest_path = os.path.join(DOCS_DIR, dest_filename)
                    
                    if file in CARD_SYSTEM_PARTS and os.path.getsize(full_src_path) > 150 * 1024:
                        gen_files = split_large_markdown_file(full_src_path, DOCS_DIR, dest_prefix, max_cards_per_file=12)
                        split_files_map[rel_src_path] = gen_files
                        file_map[rel_src_path] = gen_files[0]
                        print(f"Subdivided large file: {file} -> {len(gen_files)} files")
                    else:
                        shutil.copy2(full_src_path, dest_path)
                        split_files_map[rel_src_path] = [dest_filename]
                        file_map[rel_src_path] = dest_filename
                elif file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    full_src_path = os.path.join(root, file)
                    dest_path = os.path.join(DOCS_DIR, file)
                    shutil.copy2(full_src_path, dest_path)
                    
    # Art 04's 8 Part files were just copied through the normal V1 loop above.
    # Build the card-ID -> (file, slug) routing map from those copies, then
    # route any stale links to the old monolith path at Core.
    for part in CARD_SYSTEM_PARTS:
        rel_path = f'V1/{part}'
        gen_files = split_files_map.get(rel_path)
        if gen_files:
            for gen_file in gen_files:
                populate_card_slug_map(os.path.join(DOCS_DIR, gen_file), gen_file)

    core_dest = file_map.get(f'V1/{CARD_SYSTEM_PARTS[0]}')
    if core_dest:
        file_map['V1/04___Card_System.md'] = core_dest

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
            
            # Try to resolve card system links with anchors first
            is_card_system_link = False
            for part in CARD_SYSTEM_PARTS:
                if clean_link.endswith(part) or clean_link == 'V1/04___Card_System.md':
                    is_card_system_link = True
                    break
            
            if is_card_system_link and anchor:
                routed = resolve_card_anchor(anchor)
                if routed:
                    target_file, target_slug = routed
                    return f"[{text}]({target_file}#{target_slug})"
            
            # Look for a match in the mapping
            matched_val = None
            for old_path, new_name in norm_file_map.items():
                if old_path == clean_link or old_path.endswith('/' + clean_link):
                    matched_val = new_name
                    break
                    
            if matched_val:
                # If we mapped to Core but there is an anchor, resolve it to the specific split file!
                if matched_val == core_dest and anchor:
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
        
        split_list = split_files_map.get(k)
        if split_list and len(split_list) > 1:
            for idx, gen_file in enumerate(split_list):
                suffix = chr(65 + idx) # A, B, C...
                fake_title = os.path.basename(k).replace('.md', f'___Part_{suffix}.md')
                all_md_files.append((fake_title, gen_file, category))
        else:
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
            {'toc': {'toc_depth': 3}}
        ],
        'nav': []
    }
    
    config['nav'].append({'Overview': 'index.md'})
    
    for cat in CATEGORIES:
        if cat['id'] == 'home':
            continue
        if cat['files']:
            config['nav'].append({cat['title']: cat['files']})

    homelab_files = copy_homelab_docs()
    if homelab_files:
        config['nav'].append({'Homelab & Infra': homelab_files})

    # Write config file
    config_path = os.path.join(WIKI_DIR, 'mkdocs.yml')
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        
    print(f"Wiki sources built successfully in {WIKI_DIR}/")

if __name__ == '__main__':
    build_wiki()
