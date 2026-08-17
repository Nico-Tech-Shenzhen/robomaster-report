#!/usr/bin/env python3
"""Curated lint for Chinese leakage in reader-facing Japanese Markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path

FILES = [Path("docs")]  # bibliography and dic intentionally contain source titles/forms
CHAR_RULES = {
    "简": "簡", "体": "体", "国": "国",  # harmless mappings are not checked
    "学": "学", "车": "車", "门": "門", "电": "電", "发": "発",
    "机": "機", "器": "器", "战": "戦", "队": "隊", "开": "開",
    "发": "発", "华": "華", "术": "術", "计": "計", "设": "設",
    "线": "線", "网": "網", "团": "団", "师": "師", "东": "東",
}
SUSPICIOUS_WORDS = {
    "开源": "オープンソース", "赛季": "シーズン", "战队": "チーム",
    "机器人": "ロボット", "总线": "バス", "图传": "画像伝送",
    "具身智能": "エンボディドAI", "白名单": "ホワイトリスト",
    "上位机": "上位コンピューター/操作端", "检录": "技術検査",
}
MIXED_NAMES = ["上海交通大學", "西南交通大學", "哈爾浜工業大学", "華南理工大學"]
URL = re.compile(r"https?://[^\s)>]+")
LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
INLINE = re.compile(r"`[^`]*`")


def visible_lines(text: str):
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or line.startswith("    "):
            continue
        clean = LINK.sub("", URL.sub("", INLINE.sub("", line)))
        # Original-language titles and explicit source-form cells are allowed.
        if "本章の主要資料" in clean or re.search(r"[「『].*[」』]", clean):
            continue
        yield number, clean


def main() -> int:
    issues = []
    for root in FILES:
        for path in sorted(root.glob("*.md")):
            for line_no, line in visible_lines(path.read_text(encoding="utf-8")):
                if path.name == "appendix.md" and line.startswith("|"):
                    continue  # glossary source-form column intentionally preserves Chinese
                for word, replacement in SUSPICIOUS_WORDS.items():
                    if word in line:
                        issues.append((path, line_no, word, replacement))
                for name in MIXED_NAMES:
                    if name in line:
                        issues.append((path, line_no, name, "normalize via dic.md"))
                # Check only high-signal simplified-only characters in prose.
                for char in set(CHAR_RULES) - {"体", "国", "学", "器"}:
                    if char in line:
                        issues.append((path, line_no, char, CHAR_RULES[char]))
    if issues:
        print(f"FAIL: {len(issues)} suspicious Japanese-text issue(s)")
        for path, line, found, advice in issues:
            print(f"{path}:{line}: {found!r} -> {advice}")
        return 1
    print("OK: Japanese text lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
