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
    "01-competition-2026.md", "02-rules-as-engineering.md", "03-machines-2026.md",
    "04-knowledge-system.md", "05-team-year.md", "06-people-industry-dji.md",
    "07-institutions-comparison.md", "08-lessons-for-japan.md", "appendix.md",
]


def markup(text: str) -> str:
    text = html.escape(text.strip())
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
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(TTFont("NotoJP", r"C:\Windows\Fonts\NotoSansJP-VF.ttf"))
    styles = getSampleStyleSheet()
    body = ParagraphStyle("JPBody", fontName="NotoJP", fontSize=9.3, leading=15, spaceAfter=5, wordWrap="CJK", textColor=colors.HexColor("#20242a"))
    h1 = ParagraphStyle("JPH1", parent=body, fontSize=19, leading=27, spaceAfter=12, textColor=colors.HexColor("#173f70"))
    h2 = ParagraphStyle("JPH2", parent=body, fontSize=13, leading=19, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor("#245b91"))
    h3 = ParagraphStyle("JPH3", parent=body, fontSize=11, leading=17, spaceBefore=7, spaceAfter=4)
    bullet = ParagraphStyle("JPBullet", parent=body, leftIndent=5 * mm, firstLineIndent=-3 * mm)
    story = [Spacer(1, 35 * mm), Paragraph("RoboMaster 2026", ParagraphStyle("TitleJP", parent=h1, fontSize=28, leading=36, alignment=TA_CENTER)), Paragraph("学生が作るロボット群と、それを支える仕組み", ParagraphStyle("SubJP", parent=h2, alignment=TA_CENTER)), Spacer(1, 15 * mm), Paragraph("調査基準日：2026年8月17日", ParagraphStyle("DateJP", parent=body, alignment=TA_CENTER)), PageBreak()]

    for doc_index, name in enumerate(DOCS):
        lines = (ROOT / "docs" / name).read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1; continue
            if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-+", lines[i + 1].strip().lstrip("|")):
                rows = [[markup(c) for c in line.strip("|").split("|")]]
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    rows.append([markup(c) for c in lines[i].strip().strip("|").split("|")]); i += 1
                table = Table([[Paragraph(c, body) for c in row] for row in rows], repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#dce8f4")), ("GRID", (0,0), (-1,-1), .35, colors.HexColor("#9aa7b3")), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4)]))
                story.extend([table, Spacer(1, 4 * mm)]); continue
            if line.startswith("# "):
                if doc_index: story.append(PageBreak())
                story.append(Paragraph(markup(line[2:]), h1))
            elif line.startswith("## "): story.append(Paragraph(markup(line[3:]), h2))
            elif line.startswith("### "): story.append(Paragraph(markup(line[4:]), h3))
            elif re.match(r"^[-*] ", line): story.append(Paragraph("• " + markup(line[2:]), bullet))
            elif re.match(r"^\d+\. ", line): story.append(Paragraph(markup(line), bullet))
            else: story.append(Paragraph(markup(line), body))
            i += 1
    SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=17*mm, bottomMargin=19*mm, title="RoboMaster 2026 Research Report", author="Scramble").build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)


if __name__ == "__main__": build()
