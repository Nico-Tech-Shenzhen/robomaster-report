#!/usr/bin/env python3
"""
validate_chinese_chars.py
Detect suspicious simplified Chinese characters in Japanese prose.
Excludes: URLs, code blocks, Chinese source titles, reference entries,
intentional first-use Chinese annotations.
"""

import re
import sys
from pathlib import Path

# Simplified Chinese characters that commonly appear where Japanese equivalents should be used.
# These are characters that exist in simplified Chinese but are NOT standard Japanese kanji (新字体).
SUSPICIOUS_CHARS = {
    # Common tech/competition terms that should be katakana or Japanese equivalents
    '开', '赛', '区', '参', '培', '训', '算', '硬', '组', '委',
    '智', '点', '云', '封', '装', '单', '板', '增', '益', '交',
    '流', '成', '本', '价', '课', '堂', '场', '职', '视', '觉',
    '雷', '达', '底', '盘', '电', '控', '嵌', '入', '式', '总',
    '线', '保', '研', '改', '题', '沙', '龙', '攻', '略', '图',
    '传', '拨', '盘', '机', '关', '能', '量', '轮', '腿', '兵',
    '英', '雄', '程', '哨', '飞', '镖', '环', '节',
}

# Patterns to exclude from checking
EXCLUDE_PATTERNS = [
    re.compile(r'https?://\S+'),           # URLs
    re.compile(r'`[^`]+`'),                # inline code
    re.compile(r'```[\s\S]*?```'),         # code blocks
    re.compile(r'\[.*?\]\(.*?\)'),        # markdown links
    re.compile(r'^\s*\|.*\|\s*$'),       # table rows
    re.compile(r'^\s*>.*$'),              # blockquotes
    re.compile(r'^\s*#+\s.*$'),           # headings
    re.compile(r'^\s*[-*]\s.*$'),         # list items (may contain Chinese titles)
    re.compile(r'^\s*\d+\.\s.*$'),        # numbered list items
    re.compile(r'\（[^）]*\）'),           # Chinese annotations in parentheses
    re.compile(r'\([^)]*\)'),             # any parenthetical
]

# Files to skip entirely
SKIP_FILES = {'dic.md', 'references.md', 'README.md'}


def should_exclude_line(line: str) -> bool:
    for pattern in EXCLUDE_PATTERNS:
        if pattern.search(line):
            return True
    return False


def check_file(filepath: Path) -> list:
    issues = []
    lines = filepath.read_text(encoding='utf-8').splitlines()
    for lineno, line in enumerate(lines, 1):
        if should_exclude_line(line):
            continue
        for char in SUSPICIOUS_CHARS:
            if char in line:
                # Double-check: is this char part of a known Japanese compound?
                # Allow common Japanese words that happen to contain these chars
                if char in ('機', '器', '人', '大', '会', '学', '生', '中', '国'):
                    continue
                # Check surrounding context
                idx = line.index(char)
                context = line[max(0, idx-5):idx+6]
                issues.append((filepath.name, lineno, char, context.strip()))
                break  # One issue per line is enough
    return issues


def main():
    docs_dir = Path('docs')
    all_issues = []
    for md_file in sorted(docs_dir.glob('*.md')):
        if md_file.name in SKIP_FILES:
            continue
        all_issues.extend(check_file(md_file))

    # Also check root-level md files
    for md_file in sorted(Path('.').glob('*.md')):
        if md_file.name in SKIP_FILES:
            continue
        all_issues.extend(check_file(md_file))

    if not all_issues:
        print("OK: No suspicious simplified Chinese characters detected.")
        return 0

    print(f"WARN: Found {len(all_issues)} potential issues:")
    for filename, lineno, char, context in all_issues:
        print(f"  {filename}:{lineno}: char '{char}' in: {context}")
    return 1


if __name__ == '__main__':
    sys.exit(main())
