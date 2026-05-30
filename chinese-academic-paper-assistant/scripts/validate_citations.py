#!/usr/bin/env python3
"""Check whether one-click review citations match records in a literature matrix."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


AUTHOR_YEAR_RE = re.compile(r"([\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z\s·\.\-]{0,20})(?:等)?[（(](\d{4})[）)]")
PAREN_RE = re.compile(r"[（(]([\u4e00-\u9fffA-Za-z][^，,；;（）()]{0,20})[，,]\s*(\d{4})[）)]")


def load_keys(matrix: list[dict[str, object]]) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for record in matrix:
        year = str(record.get("year") or record.get("published_date") or "")[:4]
        authors = record.get("authors") or ""
        if isinstance(authors, list):
            author_text = "; ".join(str(item) for item in authors)
        else:
            author_text = str(authors)
        first = re.split(r"[;；,\s、]+", author_text.strip())[0]
        if first and year:
            keys.add((first, year))
    return keys


def extract_citations(text: str) -> set[tuple[str, str]]:
    matches = set(AUTHOR_YEAR_RE.findall(text))
    matches.update(PAREN_RE.findall(text))
    return {(author.strip().removesuffix("等"), year) for author, year in matches}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", help="Normalized literature matrix JSON")
    parser.add_argument("draft", help="Draft text file")
    args = parser.parse_args()

    matrix = json.loads(Path(args.matrix).read_text(encoding="utf-8"))
    draft = Path(args.draft).read_text(encoding="utf-8")
    known = load_keys(matrix)
    cited = extract_citations(draft)
    missing = sorted(cited - known)

    print(json.dumps({"citations_found": sorted(cited), "missing_from_matrix": missing}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
