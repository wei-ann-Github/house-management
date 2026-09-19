#!/usr/bin/env python3
"""
Demo extractor: reads config/extract_demo.yml and extracts text using pdfplumber.
Writes one text file per PDF to .planning/research/ and prints a short preview.

Usage: run in repo root with `uv run script/extract_demo.py`.
"""

from pathlib import Path
import sys

CONFIG_PATH = Path("config/extract_demo.yml")
OUT_DIR = Path(".planning/research/")


def read_config(path: Path) -> dict:
    if not path.exists():
        print(f"Config not found: {path}", file=sys.stderr)
        sys.exit(2)
    raw = path.read_text(encoding="utf-8")

    # Prefer a real YAML parser when available.
    try:
        import yaml  # type: ignore

        cfg = yaml.safe_load(raw) or {}
        return cfg if isinstance(cfg, dict) else {}
    except Exception as e:
        raise e


def extract_page(page, region: dict | None = None) -> str:
    """Flatten configured numbered table rows; retain text above and below them.

    Coordinates are PDF points measured from the top-left. The first column
    must contain an integer item number at the start of each logical row.
    """
    if region is None:
        return page.extract_text() or ""
    left, top, right, bottom = region["bbox"]
    columns = region["columns"]
    area = page.crop((left, top, right, bottom))
    starts = sorted({
        word["top"] - 1
        for word in area.extract_words()
        if columns[0] <= word["x0"] < columns[1]
        and word["text"].isdigit()
    })
    if not starts:
        raise ValueError("Configured table region contains no numbered rows")
    rows = area.extract_table({
        "vertical_strategy": "explicit",
        "horizontal_strategy": "explicit",
        "explicit_vertical_lines": columns,
        "explicit_horizontal_lines": [top, *starts[1:], bottom],
    })
    if not rows:
        raise ValueError("Could not extract the configured table")
    parts = []
    if top > page.bbox[1]:
        parts.append(page.crop((page.bbox[0], page.bbox[1], page.bbox[2], top)).extract_text() or "")
    parts.extend(" | ".join(" ".join((cell or "").split()) for cell in row) for row in rows)
    if bottom < page.bbox[3]:
        parts.append(page.crop((page.bbox[0], bottom, page.bbox[2], page.bbox[3])).extract_text() or "")
    return "\n".join(parts)


def extract_text(pdf_path: str, table_regions: dict | None = None) -> str | None:
    try:
        import pdfplumber
    except Exception:
        print(
            "pdfplumber not available in this environment. Run `uv sync`.",
            file=sys.stderr,
        )
        return None
    p = Path(pdf_path)
    if not p.exists():
        print(f"PDF not found: {p}", file=sys.stderr)
        return None
    try:
        with pdfplumber.open(p) as pdf:
            return "\n\n".join(
                extract_page(page, (table_regions or {}).get(number))
                for number, page in enumerate(pdf.pages, start=1)
            )
    except Exception as e:
        print("Failed to extract PDF text:", e, file=sys.stderr)
        return None


def main() -> int:
    cfg = read_config(CONFIG_PATH)
    fnames = cfg.get("filenames") or cfg.get("files") or cfg.get("paths")
    print(fnames)
    if not fnames:
        print(
            "No filenames provided in config (expected key: filenames).",
            file=sys.stderr,
        )
        return 2
    for fname in fnames:
        output_fname = Path(fname).stem + ".txt"
        regions = cfg.get("table_regions", {}).get(Path(fname).name, {})
        text = extract_text(fname, regions)
        if text is None or output_fname is None:
            print("No text extracted.", file=sys.stderr)
            return 1
        output_fname
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        OUT_PATH = OUT_DIR / output_fname
        OUT_PATH.write_text(text, encoding="utf-8")
        preview = text.replace("\n", " ")[:1000]
        print(f"Extracted text length: {len(text)}")
        print("Preview:", preview)
        print("Saved full extraction to", OUT_PATH)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
