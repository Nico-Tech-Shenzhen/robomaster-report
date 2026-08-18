#!/usr/bin/env python3
"""
validate_headings.py
Detect duplicated headings across chapters (potential duplication).
"""

import sys
from pathlib import Path
from collections import defaultdict


def extract_headings(filepath: Path) -> list:
    headings = []
    for lineno, line in enumerate(filepath.read_text(encoding='utf-8').splitlines(), 1):
        if line.startswith('#'):
            # Strip markdown heading syntax
            text = line.lstrip('#').strip()
            headings.append((filepath.name, lineno, text))
    return headings


def main():
    heading_map = defaultdict(list)
    for md_file in sorted(Path('docs').glob('*.md')):
        for filename, lineno, text in extract_headings(md_file):
            heading_map[text].append((filename, lineno))

    allowed = {'参考文献'}
    duplicates = {h: locs for h, locs in heading_map.items() if len(locs) > 1 and h not in allowed}

    if not duplicates:
        print("OK: No duplicated headings detected.")
        return 0

    print(f"WARN: Found {len(duplicates)} duplicated headings:")
    for heading, locations in duplicates.items():
        locs_str = ', '.join(f"{f}:{l}" for f, l in locations)
        print(f"  '{heading}' in: {locs_str}")
    return 1


if __name__ == '__main__':
    sys.exit(main())
