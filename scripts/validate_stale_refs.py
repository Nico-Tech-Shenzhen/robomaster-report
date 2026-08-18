#!/usr/bin/env python3
"""
validate_stale_refs.py
Detect stale chapter references in markdown files.
Looks for patterns like "第X章", "chXX.md", etc. that may be outdated.
"""

import re
import sys
from pathlib import Path

# Current valid chapter references
VALID_CHAPTERS = {
    '第1章', '第2章', '第3章', '第4章', '第5章',
    '第6章', '第7章', '第8章', '第9章',
    'ch01.md', 'ch02.md', 'ch03.md', 'ch04.md', 'ch05.md',
    'ch06.md', 'ch07.md', 'ch08.md', 'ch09.md',
}

# Old chapter references that should no longer exist
STALE_PATTERNS = [
    re.compile(r'第11章'),
    re.compile(r'第12章'),
    re.compile(r'ch11\.md'),
    re.compile(r'ch12\.md'),
    re.compile(r'第10章'),
    re.compile(r'ch10\.md'),
    re.compile(r'08-lessons-for-japan\.md'),
]


def check_file(filepath: Path) -> list:
    issues = []
    text = filepath.read_text(encoding='utf-8')
    for pattern in STALE_PATTERNS:
        for match in pattern.finditer(text):
            lineno = text[:match.start()].count('\n') + 1
            issues.append((filepath.name, lineno, match.group()))
    return issues


def main():
    all_issues = []
    for md_file in sorted(Path('.').rglob('*.md')):
        if '.git' in str(md_file):
            continue
        all_issues.extend(check_file(md_file))

    if not all_issues:
        print("OK: No stale chapter references detected.")
        return 0

    print(f"WARN: Found {len(all_issues)} stale references:")
    for filename, lineno, match in all_issues:
        print(f"  {filename}:{lineno}: '{match}'")
    return 1


if __name__ == '__main__':
    sys.exit(main())
