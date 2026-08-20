#!/usr/bin/env python3
"""Check RM2026 identifiers outside research archives against source cards."""

from __future__ import annotations
import re
import sys
from pathlib import Path

ID = re.compile(r"RM2026-\d{4}")
ROOTS = [Path("docs"), Path("REPORT_PLAN.md"), Path("MEDIA_PLAN.md")]
CARDS = {path.stem for path in Path("research/china-2026/sources").glob("RM2026-*.md")}


def main() -> int:
    issues = []
    for root in ROOTS:
        paths = root.glob("*.md") if root.is_dir() else [root]
        for path in paths:
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if "legacy" in line.lower() or "lookup lead" in line.lower():
                    continue
                for source_id in ID.findall(line):
                    if source_id not in CARDS:
                        issues.append((path, number, source_id))
    if issues:
        print(f"FAIL: {len(issues)} source ID(s) have no card")
        for path, number, source_id in issues:
            print(f"{path}:{number}: {source_id}")
        return 1
    print(f"OK: referenced source IDs have cards ({len(CARDS)} cards indexed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
