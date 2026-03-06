import json
import os

def parse_files():
    structure = {}
    
    # We'll use os.walk to find all .py files in the current directory and subdirectories
    # excluding the dashboard folder.
    for root, dirs, files in os.walk('.'):
        if 'dashboard' in root or '.venv' in root or '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.py'):
                # Get path relative to current directory
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                
                parts = rel_path.split(os.sep)
                
                current = structure
                for part in parts[:-1]:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                
                if 'files' not in current:
                    current['files'] = []
                current['files'].append(parts[-1])
                
    return structure

res = parse_files()
with open('dashboard/src/data.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=4, ensure_ascii=False)

print("JSON created!")
