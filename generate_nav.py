#!/usr/bin/env python3
"""
Generate navigation for separate builds architecture.
Scans docs/en/ and docs/fr/ directories and updates config/en/mkdocs.yml and config/fr/mkdocs.yml
"""

import os
from pathlib import Path
import re
import yaml

def get_folder_structure(docs_dir):
    """Get folder structure with all .md files."""
    structure = {}
    for item in sorted(docs_dir.iterdir()):
        if item.is_dir() and not item.name.startswith('.') and item.name != 'assets':
            files = []
            for file in sorted(item.glob('*.md')):
                files.append(file)
            structure[item.name] = files
    return structure

def escape_single_quotes(text):
    """Escape single quotes in YAML."""
    return text.replace("'", "''")

def generate_nav_yaml(docs_dir, structure, language='en'):
    """Generate nav YAML section for a language."""
    nav_lines = ['nav:']
    
    # Home page first
    nav_lines.append("  - Home: index.md")
    
    # Then folders with their contents
    for folder_name in sorted(structure.keys()):
        folder = structure[folder_name]
        
        nav_lines.append(f"  - '{escape_single_quotes(folder_name)}':")
        
        # Check if index.md exists in folder
        index_md = None
        for f in folder:
            if f.name == 'index.md':
                index_md = f
                break
        
        # Add index.md first if it exists
        if index_md:
            rel_path = f"{folder_name}/index.md"
            nav_lines.append(f"    - index: '{escape_single_quotes(rel_path)}'")
        
        # Add other .md files
        for file in folder:
            if file.name != 'index.md':
                rel_path = f"{folder_name}/{file.name}"
                nav_lines.append(f"    - '{escape_single_quotes(file.stem)}': '{escape_single_quotes(rel_path)}'")
    
    return '\n'.join(nav_lines)

def update_config_yaml(config_path, nav_yaml):
    """Update mkdocs config file with new nav section."""
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace nav section
    nav_pattern = r'nav:\s*(?:\n\s*-[^:\n]+\n(?:\s{4}[^:\n]+\n)*)*'
    new_content = re.sub(nav_pattern, nav_yaml, content, flags=re.MULTILINE)
    
    # If pattern didn't match, append nav after plugins section
    if new_content == content:
        # Try to find plugins section and add nav after
        plugins_match = re.search(r'(plugins:[\s\S]+?)(?=\n[a-z_]+:|\Z)', content, re.DOTALL)
        if plugins_match:
            new_content = content[:plugins_match.end()] + '\n\n' + nav_yaml + '\n'
        else:
            # Just append at the end
            new_content = content.rstrip() + '\n\n' + nav_yaml + '\n'
    
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"[OK] Updated {config_path}")

def main():
    base_dir = Path(__file__).parent / 'docs'
    en_dir = base_dir / 'en'
    fr_dir = base_dir / 'fr'
    en_config = Path(__file__).parent / 'config' / 'en' / 'mkdocs.yml'
    fr_config = Path(__file__).parent / 'config' / 'fr' / 'mkdocs.yml'
    
    if not en_dir.exists():
        print("Error: docs/en directory not found")
        return
    
    if not fr_dir.exists():
        print("Error: docs/fr directory not found")
        return
    
    if not en_config.exists():
        print("Error: config/en/mkdocs.yml not found")
        return
    
    if not fr_config.exists():
        print("Error: config/fr/mkdocs.yml not found")
        return
    
    print("Scanning English structure...")
    en_structure = get_folder_structure(en_dir)
    
    print("Scanning French structure...")
    fr_structure = get_folder_structure(fr_dir)
    
    print(f"\nEnglish: {len(en_structure)} folders")
    for folder in sorted(en_structure.keys()):
        print(f"  {folder}: {len(en_structure[folder])} files")
    
    print(f"\nFrench: {len(fr_structure)} folders")
    for folder in sorted(fr_structure.keys()):
        print(f"  {folder}: {len(fr_structure[folder])} files")
    
    print("\nGenerating English navigation...")
    en_nav = generate_nav_yaml(en_dir, en_structure, language='en')
    print(en_nav)
    
    print("\nGenerating French navigation...")
    fr_nav = generate_nav_yaml(fr_dir, fr_structure, language='fr')
    print(fr_nav)
    
    print("\nUpdating English config...")
    update_config_yaml(en_config, en_nav)
    
    print("\nUpdating French config...")
    update_config_yaml(fr_config, fr_nav)
    
    print("\n[OK] Done! Navigation updated for both languages.")

if __name__ == '__main__':
    main()
