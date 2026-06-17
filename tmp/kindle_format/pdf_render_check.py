from __future__ import annotations

import json
import sys
from pathlib import Path

import pypdfium2 as pdfium
from PIL import ImageStat


def main(pdf_path: str, output_dir: str) -> None:
    pdf = pdfium.PdfDocument(pdf_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    page_summaries = []

    for idx, page in enumerate(pdf):
        bitmap = page.render(scale=1.6)
        image = bitmap.to_pil()
        out_path = out_dir / f"page-{idx + 1:03d}.png"
        image.save(out_path)
        gray = image.convert("L")
        stat = ImageStat.Stat(gray)
        extrema = stat.extrema[0]
        mean = stat.mean[0]
        page_summaries.append(
            {
                "page": idx + 1,
                "path": str(out_path),
                "width": image.width,
                "height": image.height,
                "gray_min": extrema[0],
                "gray_max": extrema[1],
                "gray_mean": round(mean, 2),
                "nonblank": extrema[0] < 250,
            }
        )

    summary = {
        "pdf": str(pdf_path),
        "page_count": len(pdf),
        "nonblank_pages": sum(1 for p in page_summaries if p["nonblank"]),
        "blank_like_pages": [p["page"] for p in page_summaries if not p["nonblank"]],
        "pages": page_summaries,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: pdf_render_check.py input.pdf output_dir")
    main(sys.argv[1], sys.argv[2])
