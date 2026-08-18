#!/usr/bin/env python3
"""Detect high-signal Chinese orthography in reader-facing Japanese prose."""

import re
import sys
from pathlib import Path

WORDS = {
    "开源": "オープンソース", "赛季": "シーズン", "战队": "チーム",
    "机器人": "ロボット", "参赛": "出場", "图传": "画像伝送",
    "总线": "バス", "检录": "技術検査", "梯队队员": "育成枠の登録メンバー",
    "智能": "スマート/知能", "算法": "アルゴリズム", "硬件": "ハードウェア",
}
MIXED = ["大學", "學院", "國際", "團隊", "上海交通大學", "西南交通大學"]
LINK = re.compile(r"\[[^]]*\]\([^)]*\)")
URL = re.compile(r"https?://\S+")
CODE = re.compile(r"`[^`]*`")
OFFICIAL = re.compile(r"（[^）]+ / [^）]+）")


def main() -> int:
    issues = []
    for path in sorted(Path("docs").glob("*.md")):
        fenced = False
        in_refs = False
        for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if raw.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if fenced:
                continue
            if raw.startswith("## 参考文献"):
                in_refs = True
                continue
            if in_refs:
                continue
            if path.name == "appendix.md" and raw.startswith("|"):
                continue
            line = OFFICIAL.sub("", LINK.sub("", URL.sub("", CODE.sub("", raw))))
            for word, replacement in WORDS.items():
                if word in line:
                    issues.append((path, number, word, replacement))
            for word in MIXED:
                if word in line:
                    issues.append((path, number, word, "modern Japanese form"))
    if issues:
        print(f"FAIL: {len(issues)} Chinese-orthography issue(s)")
        for path, number, word, replacement in issues:
            print(f"{path}:{number}: {word!r} -> {replacement}")
        return 1
    print("OK: No Chinese orthography found in Japanese prose.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
