#!/usr/bin/env python3
"""Build a simple chronological timeline from a normalized literature matrix."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def year_of(record: dict[str, object]) -> int:
    raw = str(record.get("year") or record.get("published_date") or "9999")[:4]
    return int(raw) if raw.isdigit() else 9999


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", help="Normalized literature matrix JSON")
    args = parser.parse_args()

    matrix = json.loads(Path(args.matrix).read_text(encoding="utf-8"))
    rows = sorted(matrix, key=year_of)
    timeline = [
        {
            "year": str(record.get("year") or record.get("published_date") or ""),
            "authors": record.get("authors", ""),
            "title": record.get("title", ""),
            "journal": record.get("journal", ""),
            "key_finding": record.get("key_finding", ""),
            "relationship_hint": "按发表时间和主题内容判断，可作为研究脉络分析素材；直接引用关系需另行核验。",
        }
        for record in rows
    ]
    print(json.dumps(timeline, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
