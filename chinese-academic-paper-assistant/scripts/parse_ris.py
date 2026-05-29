#!/usr/bin/env python3
"""Parse RIS records into normalized JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TAG_MAP = {
    "TI": "title",
    "T1": "title",
    "AU": "authors",
    "JO": "journal",
    "JF": "journal",
    "JA": "journal",
    "PY": "year",
    "Y1": "published_date",
    "DO": "doi",
    "UR": "url",
    "AB": "abstract",
    "KW": "keywords",
}


def parse_ris(text: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    current: dict[str, object] = {}

    for raw_line in text.splitlines():
        if len(raw_line) < 6 or raw_line[2:6] != "  - ":
            continue
        tag = raw_line[:2]
        value = raw_line[6:].strip()
        if tag == "TY":
            current = {"source_status": "user_imported"}
            continue
        if tag == "ER":
            if current:
                records.append(current)
            current = {}
            continue
        field = TAG_MAP.get(tag)
        if not field or not current:
            continue
        if field in {"authors", "keywords"}:
            current.setdefault(field, [])
            assert isinstance(current[field], list)
            current[field].append(value)
        else:
            current[field] = value

    if current:
        records.append(current)
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to .ris file")
    parser.add_argument("-o", "--output", help="Write JSON to this path")
    args = parser.parse_args()

    records = parse_ris(Path(args.input).read_text(encoding="utf-8"))
    data = json.dumps(records, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(data + "\n", encoding="utf-8")
    else:
        print(data)


if __name__ == "__main__":
    main()
