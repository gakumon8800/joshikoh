from __future__ import annotations

import posixpath
import sys
import zipfile
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
REL_DOC_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def normalize_word_target(target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join("word", target)).replace("\\", "/")


def strip(input_path: str, output_path: str) -> None:
    input_docx = Path(input_path)
    output_docx = Path(output_path)
    output_docx.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(input_docx, "r") as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    parser = etree.XMLParser(remove_blank_text=False)
    removed_targets: set[str] = set()

    document_name = "word/document.xml"
    rels_name = "word/_rels/document.xml.rels"

    if document_name in files:
        root = etree.fromstring(files[document_name], parser)
        for elem in root.xpath("//w:headerReference|//w:footerReference", namespaces={"w": W_NS}):
            elem.getparent().remove(elem)
        files[document_name] = etree.tostring(
            root, encoding="UTF-8", xml_declaration=True, standalone=True
        )

    if rels_name in files:
        rels_root = etree.fromstring(files[rels_name], parser)
        for rel in list(rels_root):
            rel_type = rel.get("Type", "")
            if rel_type.endswith("/header") or rel_type.endswith("/footer"):
                target = rel.get("Target", "")
                if target:
                    removed_targets.add(normalize_word_target(target))
                rels_root.remove(rel)
        files[rels_name] = etree.tostring(
            rels_root, encoding="UTF-8", xml_declaration=True, standalone=True
        )

    for name in list(files):
        if (
            name in removed_targets
            or name.startswith("word/header")
            or name.startswith("word/footer")
            or name.startswith("word/_rels/header")
            or name.startswith("word/_rels/footer")
        ):
            del files[name]

    ct_name = "[Content_Types].xml"
    if ct_name in files:
        ct_root = etree.fromstring(files[ct_name], parser)
        for elem in list(ct_root):
            part_name = elem.get("PartName", "").lstrip("/")
            content_type = elem.get("ContentType", "")
            if (
                part_name.startswith("word/header")
                or part_name.startswith("word/footer")
                or content_type.endswith(".header+xml")
                or content_type.endswith(".footer+xml")
            ):
                ct_root.remove(elem)
        files[ct_name] = etree.tostring(
            ct_root, encoding="UTF-8", xml_declaration=True, standalone=True
        )

    with zipfile.ZipFile(output_docx, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: strip_headers_footers.py input.docx output.docx")
    strip(sys.argv[1], sys.argv[2])
