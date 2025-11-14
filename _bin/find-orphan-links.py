#!/usr/bin/env python3
"""
Find orphan wiki links - links that exist in pages but don't have corresponding files.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

def extract_wiki_links(content):
    """Extract all [[wiki links]] from content."""
    pattern = r'\[\[([^\]]+)\]\]'
    links = re.findall(pattern, content)
    # Handle [[Page|display text]] syntax - extract just the page name
    return [link.split('|')[0] for link in links]

def normalize_filename(link_text):
    """Convert wiki link text to expected filename."""
    return f"{link_text}.md"

def main():
    # Get all markdown files in repository root
    repo_root = Path('/home/user/ogm-2025-11-13')
    md_files = list(repo_root.glob('*.md'))

    # Build set of existing pages (without .md extension)
    existing_pages = {f.stem for f in md_files}

    # Find all wiki links and track which pages link to them
    all_links = defaultdict(list)

    for md_file in md_files:
        content = md_file.read_text()
        links = extract_wiki_links(content)
        for link in links:
            all_links[link].append(md_file.stem)

    # Find orphan links (linked to but don't exist)
    orphans = {}
    for link, linking_pages in sorted(all_links.items()):
        if link not in existing_pages:
            orphans[link] = linking_pages

    # Output results
    if orphans:
        print(f"Found {len(orphans)} orphan links:\n")
        for link, linking_pages in sorted(orphans.items()):
            print(f"  [[{link}]]")
            print(f"    Linked from: {', '.join(linking_pages[:5])}")
            if len(linking_pages) > 5:
                print(f"    ... and {len(linking_pages) - 5} more")
            print()
    else:
        print("No orphan links found!")

    return len(orphans)

if __name__ == '__main__':
    exit(main())
