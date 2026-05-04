from pathlib import Path
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "00.references" / "past-books" / "originals"
OUT_DIR = ROOT / "00.references" / "past-books" / "markdown"

BOOKS = [
    ("2025-05-05第1話.docx", "volume-01.md", 1, "女子高生でもわかる不動産 第1巻"),
    ("2025-05-15_第2巻.docx", "volume-02.md", 2, "女子高生でもわかる不動産 第2巻"),
    ("2025-05-22_第3巻.docx", "volume-03.md", 3, "女子高生でもわかる不動産 第3巻"),
    ("2025-06-01_女子高生でもわかる不動産_第4巻.docx", "volume-04.md", 4, "女子高生でもわかる不動産 第4巻"),
]


def iter_blocks(document):
    for child in document.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def clean_text(text):
    return "\n".join(" ".join(line.split()) for line in text.splitlines()).strip()


def escape_table_cell(text):
    return clean_text(text).replace("|", "\\|").replace("\n", "<br>")


def table_to_markdown(table):
    rows = []
    for row in table.rows:
        rows.append([escape_table_cell(cell.text) for cell in row.cells])
    if not rows:
        return []

    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    out = []
    out.append("| " + " | ".join(rows[0]) + " |")
    out.append("| " + " | ".join(["---"] * width) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(row) + " |")
    return out


def looks_character_heading(text):
    markers = ("■", "🌀", "🪶", "📚")
    return text.startswith(markers)


def looks_learning_heading(text):
    return (
        "学びまとめ" in text
        or text.startswith("✅ まとめ")
        or text.startswith("✅ 教訓まとめ")
        or text.startswith("✅ この回の学び")
    )


def paragraph_to_markdown(paragraph, in_intro=False):
    text = clean_text(paragraph.text)
    if not text:
        return []

    style = paragraph.style.name
    if style == "Heading 1":
        return [f"## {text}"]
    if style == "Heading 2":
        return [f"### {text}"]
    if style.startswith("Heading "):
        try:
            level = int(style.split()[-1]) + 1
        except ValueError:
            level = 3
        return [f"{'#' * min(level, 6)} {text}"]
    if looks_character_heading(text):
        return [f"### {text}"]
    if looks_learning_heading(text):
        return [f"### {text}"]
    return [text]


def convert_book(source_name, out_name, volume, yaml_title):
    doc = Document(str(SOURCE_DIR / source_name))
    blocks = list(iter_blocks(doc))

    plain_opening = []
    start_index = 0
    for idx, block in enumerate(blocks):
        if isinstance(block, Paragraph):
            text = clean_text(block.text)
            if not text:
                continue
            if block.style.name.startswith("Heading"):
                start_index = idx
                break
            plain_opening.append(text)
        else:
            start_index = idx
            break

    title = plain_opening[0] if plain_opening else yaml_title
    subtitle = plain_opening[1] if len(plain_opening) > 1 else ""
    catchcopy = plain_opening[2] if len(plain_opening) > 2 else ""
    intro = plain_opening[3:]

    lines = [
        "---",
        f"title: {yaml_title}",
        f"volume: {volume}",
        "series: 女子高生でもわかる不動産",
        "role: 過去作品・文体参考資料",
        "purpose: 新作書籍制作時の文体・構成・キャラクター運用の参考",
        "---",
        "",
        f"# {title}",
    ]

    if subtitle:
        lines += ["", f"## {subtitle}"]
    if catchcopy:
        lines += ["", catchcopy]
    if intro:
        lines += ["", "## はじめに", ""]
        for text in intro:
            lines += [text, ""]

    for block in blocks[start_index:]:
        if isinstance(block, Paragraph):
            converted = paragraph_to_markdown(block)
        else:
            converted = table_to_markdown(block)

        if not converted:
            continue
        if lines and lines[-1] != "":
            lines.append("")
        lines.extend(converted)
        lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    (OUT_DIR / out_name).write_text(text, encoding="utf-8", newline="\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for args in BOOKS:
        convert_book(*args)


if __name__ == "__main__":
    main()
