#!/usr/bin/env python3
"""
validate_numbers.py
Detect obvious numerical conflicts across chapters.
Flags the same metric with different values.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# Metrics to check: (pattern, description)
METRIC_PATTERNS = [
    (re.compile(r'近20万[^名]?'), 'cumulative participants (200k)'),
    (re.compile(r'近10万[^名]?'), 'cumulative participants (100k)'),
    (re.compile(r'超1,000名'), 'DJI hires (over 1000)'),
    (re.compile(r'近1,000名'), 'DJI hires (near 1000)'),
    (re.compile(r'1,000名以[上内]'), 'DJI hires (1000+)'),
    (re.compile(r'累計約100[^社個]'), 'startup count (~100)'),
    (re.compile(r'200余[り個社]'), 'startup count (~200)'),
    (re.compile(r'3\.5億元'), 'DJI investment (350M yuan)'),
    (re.compile(r'5,394万元'), 'DJI education support (5394W)'),
]


def main():
    # This is a lightweight check - just warn about known conflicting patterns
    # that appeared in the old report.
    docs_dir = Path('docs')
    findings = defaultdict(list)

    for md_file in sorted(docs_dir.glob('*.md')):
        text = md_file.read_text(encoding='utf-8')
        for pattern, desc in METRIC_PATTERNS:
            for match in pattern.finditer(text):
                lineno = text[:match.start()].count('\n') + 1
                findings[desc].append((md_file.name, lineno, match.group()))

    # Check for conflicts
    conflicts = []
    # Participants
    if 'cumulative participants (200k)' in findings and 'cumulative participants (100k)' in findings:
        conflicts.append(('Participant count', findings['cumulative participants (200k)'], findings['cumulative participants (100k)']))
    # DJI hires
    hire_keys = [k for k in findings if 'DJI hires' in k]
    if len(hire_keys) > 1:
        all_hires = []
        for k in hire_keys:
            all_hires.extend(findings[k])
        if len(set(x[2] for x in all_hires)) > 1:
            conflicts.append(('DJI hire count', all_hires, []))
    # Startups
    startup_keys = [k for k in findings if 'startup count' in k]
    if len(startup_keys) > 1:
        all_starts = []
        for k in startup_keys:
            all_starts.extend(findings[k])
        if len(set(x[2] for x in all_starts)) > 1:
            conflicts.append(('Startup count', all_starts, []))

    if not conflicts:
        print("OK: No obvious numerical conflicts detected.")
        return 0

    print(f"WARN: Found {len(conflicts)} potential numerical conflicts:")
    for desc, locs_a, locs_b in conflicts:
        print(f"  {desc}:")
        for fn, ln, val in locs_a:
            print(f"    {fn}:{ln}: '{val}'")
        for fn, ln, val in locs_b:
            print(f"    {fn}:{ln}: '{val}'")
    return 1


if __name__ == '__main__':
    sys.exit(main())
