#!/usr/bin/env python3
"""Parse a small BibTeX file into normalized JSON records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,]+),(.*?)\n\}", re.DOTALL)
FIELD_RE = re.compile(r"(\w+)\s*=\s*[\{\"](.+?)[\}\"]\s*,?", re.DOTALL)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_bibtex(text: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for key, body in ENTRY_RE.findall(text):
        fields = {name.lower(): clean(value) for name, value in FIELD_RE.findall(body)}
        records.append(
            {
                "id": clean(key),
                "title": fields.get("title", ""),
                "authors": fields.get("author", ""),
                "journal": fields.get("journal") or fields.get("booktitle", ""),
                "year": fields.get("year", ""),
                "published_date": fields.get("date") or fields.get("year", ""),
                "doi": fields.get("doi", ""),
                "url": fields.get("url", ""),
                "abstract": fields.get("abstract", ""),
                "keywords": fields.get("keywords", ""),
                "source_status": "user_imported",
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to .bib file")
    parser.add_argument("-o", "--output", help="Write JSON to this path")
    args = parser.parse_args()

    records = parse_bibtex(Path(args.input).read_text(encoding="utf-8"))
    data = json.dumps(records, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(data + "\n", encoding="utf-8")
    else:
        print(data)


if __name__ == "__main__":
    main()
