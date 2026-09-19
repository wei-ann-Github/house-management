#!/usr/bin/env python3
"""
Demo extractor: reads config/extract_demo.yml for 'filename' and extracts text using PyPDF2.
Writes full extracted text to .planning/research/extract_demo_output.txt and prints a short preview.

Usage: run in repo root. Ensure PyPDF2 is available in the environment (e.g. `uv pip install PyPDF2`).
"""
from pathlib import Path
import sys

CONFIG_PATH = Path('config/extract_demo.yml')
OUT_PATH = Path('.planning/research/extract_demo_output.txt')


def read_config(path: Path) -> dict:
    if not path.exists():
        print(f'Config not found: {path}', file=sys.stderr)
        sys.exit(2)
    cfg = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            cfg[k.strip()] = v.strip().strip('"').strip("'")
    return cfg


def extract_text(pdf_path: str) -> str | None:
    try:
        from PyPDF2 import PdfReader
    except Exception:
        print('PyPDF2 not available in this environment. Install it (e.g. `uv pip install PyPDF2`).', file=sys.stderr)
        return None
    p = Path(pdf_path)
    if not p.exists():
        print(f'PDF not found: {p}', file=sys.stderr)
        return None
    try:
        reader = PdfReader(str(p))
        parts = []
        for page in reader.pages:
            try:
                parts.append(page.extract_text() or '')
            except Exception:
                parts.append('')
        full = '\n'.join(parts)
        return full
    except Exception as e:
        print('Failed to extract PDF text:', e, file=sys.stderr)
        return None


def main() -> int:
    cfg = read_config(CONFIG_PATH)
    fname = cfg.get('filename') or cfg.get('file') or cfg.get('path')
    if not fname:
        print('No filename provided in config (expected key: filename).', file=sys.stderr)
        return 2
    text = extract_text(fname)
    if text is None:
        print('No text extracted.', file=sys.stderr)
        return 1
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(text, encoding='utf-8')
    preview = text.replace('\n', ' ')[:1000]
    print(f'Extracted text length: {len(text)}')
    print('Preview:', preview)
    print('Saved full extraction to', OUT_PATH)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
