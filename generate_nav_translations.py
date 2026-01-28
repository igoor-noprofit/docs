#!/usr/bin/env python3
"""
Generate nav_translations for mkdocs-static-i18n based on folder/file matching
between English and French documentation directories.
"""

import os
from pathlib import Path
import re

def get_folder_structure(docs_dir):
    structure = []
    for item in sorted(docs_dir.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            files = []
            for file in sorted(item.glob('*.md')):
                if file.name != 'index.md':
                    title = file.stem
                    files.append((file.name, title))
            structure.append((item.name, files))
    return structure

def match_folders(en_structure, fr_structure):
    mapping = {}
    for (en_folder, en_files), (fr_folder, fr_files) in zip(en_structure, fr_structure):
        mapping[fr_folder] = en_folder
        
        for en_file, fr_file in zip(en_files, fr_files):
            mapping[fr_file[0]] = en_file[0]
    
    return mapping

def generate_nav_translations_yaml(mapping):
    lines = []
    for fr_key, en_value in sorted(mapping.items()):
        safe_fr = fr_key.replace('"', '\\"')
        safe_en = en_value.replace('"', '\\"')
        lines.append(f'            "{safe_fr}": "{safe_en}"')
    return '\n'.join(lines)

def update_mkdocs_yml(mkdocs_path, nav_translations):
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the line with "locale: fr"
    fr_locale_line = -1
    for i, line in enumerate(lines):
        if 'locale: fr' in line:
            fr_locale_line = i
            break
    
    if fr_locale_line == -1:
        print("Error: Could not find 'locale: fr' in mkdocs.yml")
        return False
    
    # Find the next locale line or the end of the languages section
    next_locale_line = -1
    for i in range(fr_locale_line + 1, len(lines)):
        if re.match(r'\s*-\s+locale:', lines[i]):
            next_locale_line = i
            break
        # Or if we reach a top-level setting (not indented)
        if lines[i] and not lines[i][0].isspace() and not lines[i].strip().startswith('#'):
            # Check if it's a new top-level key
            if re.match(r'^[a-z_]+:', lines[i].strip()):
                next_locale_line = i
                break
    
    # Remove any existing nav_translations in the fr locale block
    new_lines = lines[:fr_locale_line + 1]
    skip_nav_translations = False
    for i in range(fr_locale_line + 1, next_locale_line if next_locale_line != -1 else len(lines)):
        line = lines[i]
        if 'nav_translations:' in line:
            skip_nav_translations = True
        if skip_nav_translations:
            # Check if we're done with nav_translations (dedent)
            if line and not line[0].isspace():
                skip_nav_translations = False
                new_lines.append(line)
            elif re.match(r'\s{6}[a-z_]+:', line):
                # Next setting in the fr locale
                skip_nav_translations = False
                new_lines.append(line)
            continue
        new_lines.append(line)
    
    if next_locale_line != -1:
        new_lines.extend(lines[next_locale_line:])
    
    # Insert nav_translations after the fr locale build line
    # Find the build: true line for fr locale
    fr_build_line = -1
    for i in range(fr_locale_line, len(new_lines)):
        if 'build: true' in new_lines[i] and i > fr_locale_line:
            # Make sure this is in the fr locale (indented)
            if new_lines[i].startswith('          '):
                fr_build_line = i
                break
    
    if fr_build_line == -1:
        print("Error: Could not find 'build: true' in fr locale")
        return False
    
    # Insert nav_translations after build line
    nav_translations_lines = ['\n', '          nav_translations:\n'] + [line + '\n' for line in nav_translations.split('\n')]
    new_lines = new_lines[:fr_build_line + 1] + nav_translations_lines + new_lines[fr_build_line + 1:]
    
    with open(mkdocs_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"[OK] Updated {mkdocs_path} with nav_translations")
    return True

def main():
    base_dir = Path(__file__).parent / 'docs'
    en_dir = base_dir / 'en'
    fr_dir = base_dir / 'fr'
    mkdocs_path = Path(__file__).parent / 'mkdocs.yml'
    
    if not en_dir.exists() or not fr_dir.exists():
        print("Error: docs/en or docs/fr directory not found")
        return
    
    print("Scanning English structure...")
    en_structure = get_folder_structure(en_dir)
    
    print("Scanning French structure...")
    fr_structure = get_folder_structure(fr_dir)
    
    if len(en_structure) != len(fr_structure):
        print(f"Warning: Structure mismatch! EN has {len(en_structure)} folders, FR has {len(fr_structure)}")
    
    print("Generating folder/file mappings...")
    mapping = match_folders(en_structure, fr_structure)
    
    print(f"Generated {len(mapping)} mappings")
    print("\nMappings:")
    for fr_key, en_value in sorted(mapping.items()):
        print(f"  {fr_key} -> {en_value}")
    
    print("\nGenerating YAML...")
    nav_translations = generate_nav_translations_yaml(mapping)
    
    print("\nUpdating mkdocs.yml...")
    success = update_mkdocs_yml(mkdocs_path, nav_translations)
    
    if success:
        print("\n[OK] Done!")
    else:
        print("\n[ERROR] Failed!")

if __name__ == '__main__':
    main()
