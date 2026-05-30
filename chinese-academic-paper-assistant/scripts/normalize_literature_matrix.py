#!/usr/bin/env python3
"""Normalize records for matrices and one-click literature review coverage checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = ("authors", "title", "journal", "published_date")


def as_text(value: object) -> str:
    if isinstance(value, list):
        return "; ".join(str(item).strip() for item in value if str(item).strip())
    return str(value or "").strip()


def normalize(record: dict[str, object], index: int) -> dict[str, object]:
    published = as_text(record.get("published_date") or record.get("year"))
    normalized = {
        "id": as_text(record.get("id") or str(index)),
        "authors": as_text(record.get("authors")),
        "year": as_text(record.get("year") or published[:4]),
        "title": as_text(record.get("title")),
        "journal": as_text(record.get("journal") or record.get("source")),
        "published_date": published,
        "object": as_text(record.get("object")),
        "method": as_text(record.get("method")),
        "key_finding": as_text(record.get("key_finding") or record.get("abstract")),
        "limitation": as_text(record.get("limitation")),
        "paper_relation": as_text(record.get("paper_relation")),
        "doi": as_text(record.get("doi")),
        "url": as_text(record.get("url")),
        "source_status": as_text(record.get("source_status") or "needs_manual_verification"),
    }
    missing = [field for field in REQUIRED if not normalized[field]]
    normalized["usable_in_formal_review"] = not missing and normalized["source_status"] != "needs_manual_verification"
    normalized["missing_required_fields"] = missing
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON list of literature records")
    parser.add_argument("-o", "--output", help="Write normalized JSON to this path")
    args = parser.parse_args()

    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    normalized = [normalize(record, idx + 1) for idx, record in enumerate(records)]
    data = json.dumps(normalized, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(data + "\n", encoding="utf-8")
    else:
        print(data)


if __name__ == "__main__":
    main()
