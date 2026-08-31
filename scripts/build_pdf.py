#!/usr/bin/env python3
"""Build the Japanese report as a styled PDF without native WeasyPrint."""

from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "robomaster-report.pdf"
DOCS = [
    "ch01.md", "ch02.md", "ch03.md", "ch04.md", "ch05.md",
    "ch06.md", "ch07.md", "ch08.md", "ch09.md", "appendix.md",
]
JP_CHAR_WIDTHS = set()


def markup(text: str, namespace: str = "") -> str:
    text = html.escape(text.strip())
    if JP_CHAR_WIDTHS:
        runs = []
        using_sc = False
        for char in text:
            fallback = 0x2E80 <= ord(char) and ord(char) not in JP_CHAR_WIDTHS
            if fallback != using_sc:
                runs.append('<font name="NotoSC">' if fallback else '</font>')
                using_sc = fallback
            runs.append(char)
        if using_sc:
            runs.append('</font>')
        text = "".join(runs)
    text = re.sub(
        r'&lt;a id=&quot;(ref-\d+)&quot;&gt;&lt;/a&gt;',
        lambda m: f'<a name="{namespace}{m.group(1)}"/>',
        text,
    )
    text = re.sub(
        r'\[\[(\d+)\]\]\(#(ref-\d+)\)',
        lambda m: f'<a href="#{namespace}{m.group(2)}" color="#2457a6">[{m.group(1)}]</a>',
        text,
    )
    text = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<a href="\2" color="#2457a6">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r'<font name="NotoJP">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("NotoJP", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(20 * mm, 12 * mm, "RoboMaster 2026 Research Report")
    canvas.drawRightString(190 * mm, 12 * mm, str(doc.page))
    canvas.restoreState()


def build():
    global JP_CHAR_WIDTHS
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(TTFont("NotoJP", r"C:\Windows\Fonts\NotoSansJP-VF.ttf"))
    pdfmetrics.registerFont(TTFont("NotoSC", r"C:\Windows\Fonts\NotoSansSC-VF.ttf"))
    JP_CHAR_WIDTHS = set(pdfmetrics.getFont("NotoJP").face.charWidths)
    styles = getSampleStyleSheet()
    body = ParagraphStyle("JPBody", fontName="NotoJP", fontSize=9.3, leading=14.5, spaceAfter=5, wordWrap="CJK", textColor=colors.HexColor("#20242a"))
    reference = ParagraphStyle("JPReference", parent=body, fontSize=7, leading=7.5, spaceAfter=0)
    h1 = ParagraphStyle("JPH1", parent=body, fontSize=19, leading=27, spaceAfter=12, textColor=colors.HexColor("#173f70"))
    h2 = ParagraphStyle("JPH2", parent=body, fontSize=13, leading=19, spaceBefore=10, spaceAfter=6, keepWithNext=True, textColor=colors.HexColor("#245b91"))
    reference_heading = ParagraphStyle("JPReferenceHeading", parent=h2, fontSize=10.5, leading=12, spaceBefore=4, spaceAfter=1, keepWithNext=True)
    h3 = ParagraphStyle("JPH3", parent=body, fontSize=11, leading=17, spaceBefore=7, spaceAfter=4, keepWithNext=True)
    bullet = ParagraphStyle("JPBullet", parent=body, leftIndent=5 * mm, firstLineIndent=-3 * mm)
    story = [Spacer(1, 35 * mm), Paragraph("RoboMaster 2026", ParagraphStyle("TitleJP", parent=h1, fontSize=28, leading=36, alignment=TA_CENTER)), Paragraph("初めて読む人のための構造と技術", ParagraphStyle("SubJP", parent=h2, alignment=TA_CENTER)), Spacer(1, 15 * mm), Paragraph("調査基準日：2026年8月18日", ParagraphStyle("DateJP", parent=body, alignment=TA_CENTER)), PageBreak()]

    for doc_index, name in enumerate(DOCS):
        lines = (ROOT / "docs" / name).read_text(encoding="utf-8").splitlines()
        chapter_body = ParagraphStyle("Body_" + name, parent=body, leading=13.5 if name == "ch03.md" else body.leading, allowWidows=0 if name == "ch03.md" else 1, spaceAfter=3 if name in {"ch03.md", "ch05.md", "ch09.md"} else body.spaceAfter)
        chapter_markup = lambda text: markup(text, Path(name).stem + "-")
        i = 0
        in_references = False
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1; continue
            if line.startswith('--8<--'):
                i += 1; continue
            if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-+", lines[i + 1].strip().lstrip("|")):
                rows = [[chapter_markup(c) for c in line.strip("|").split("|")]]
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    rows.append([chapter_markup(c) for c in lines[i].strip().strip("|").split("|")]); i += 1
                # Issue #3 evidence tables: retain readable label columns in print.
                power_widths = {
                    "大学・担当領域": (0.19, 0.43, 0.38),
                    "年・比較文書": (0.17, 0.46, 0.37),
                    "量": (0.23, 0.36, 0.41),
                }.get(rows[0][0])
                col_widths = [(174 * mm - 12) * ratio for ratio in power_widths] if power_widths else None
                table = Table([[Paragraph(c, chapter_body) for c in row] for row in rows], colWidths=col_widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#dce8f4")), ("GRID", (0,0), (-1,-1), .35, colors.HexColor("#9aa7b3")), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4)]))
                story.extend([table, Spacer(1, 4 * mm)]); continue
            if line.startswith("# "):
                if doc_index: story.append(PageBreak())
                story.append(Paragraph(chapter_markup(line[2:]), h1))
            elif line.startswith("## "):
                in_references = line[3:] == "参考文献"
                story.append(Paragraph(chapter_markup(line[3:]), reference_heading if in_references else h2))
            elif line.startswith("### "): story.append(Paragraph(chapter_markup(line[4:]), h3))
            elif re.match(r"^[-*] ", line): story.append(Paragraph("• " + chapter_markup(line[2:]), bullet))
            elif re.match(r"^\d+\. ", line): story.append(Paragraph(chapter_markup(line), bullet))
            else: story.append(Paragraph(chapter_markup(line), reference if in_references else chapter_body))
            i += 1
    SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=17*mm, bottomMargin=19*mm, title="RoboMaster 2026 Research Report", author="Scramble").build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)


if __name__ == "__main__": build()
