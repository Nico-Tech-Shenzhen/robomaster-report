#!/usr/bin/env python3
"""
validate_links.py
Detect missing Markdown links (bare URLs or unlinked references).
Checks that URLs in text are clickable links.
"""

import re
import sys
from pathlib import Path

# Pattern to find bare URLs (not already in a markdown link)
BARE_URL_PATTERN = re.compile(
    r'(?<![\[(])https?://[^\s\)>\]]+(?![\)\]])'
)

# Exclude patterns
EXCLUDE_PATTERNS = [
    re.compile(r'```[\s\S]*?```'),         # code blocks
    re.compile(r'`[^`]+`'),                # inline code
    re.compile(r'\[.*?\]\(.*?\)'),        # already a markdown link
]


def check_file(filepath: Path) -> list:
    issues = []
    text = filepath.read_text(encoding='utf-8')
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        # Skip code blocks and inline code
        clean_line = line
        for pat in EXCLUDE_PATTERNS:
            clean_line = pat.sub('', clean_line)
        matches = BARE_URL_PATTERN.findall(clean_line)
        for url in matches:
            issues.append((filepath.name, lineno, url))
    return issues


def main():
    all_issues = []
    for md_file in sorted(Path('.').rglob('*.md')):
        if '.git' in str(md_file):
            continue
        all_issues.extend(check_file(md_file))

    if not all_issues:
        print("OK: No bare URLs detected.")
        return 0

    print(f"WARN: Found {len(all_issues)} bare URLs (should be markdown links):")
    for filename, lineno, url in all_issues:
        print(f"  {filename}:{lineno}: {url[:60]}...")
    return 1


if __name__ == '__main__':
    sys.exit(main())
