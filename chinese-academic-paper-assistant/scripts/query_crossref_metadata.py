#!/usr/bin/env python3
"""Query Crossref works for candidate records used in one-click review drafts."""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request


def first(value: object) -> str:
    if isinstance(value, list) and value:
        return str(value[0])
    return str(value or "")


def date_parts(item: dict[str, object]) -> str:
    issued = item.get("published-print") or item.get("published-online") or item.get("issued") or {}
    parts = issued.get("date-parts", [[]]) if isinstance(issued, dict) else [[]]
    return "-".join(str(part) for part in parts[0]) if parts and parts[0] else ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    params = urllib.parse.urlencode({"query": args.query, "rows": args.limit})
    url = f"https://api.crossref.org/works?{params}"
    request = urllib.request.Request(url, headers={"User-Agent": "chinese-academic-paper-assistant/0.1"})
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))

    records = []
    for item in payload.get("message", {}).get("items", []):
        authors = []
        for author in item.get("author", []):
            name = " ".join(part for part in [author.get("given", ""), author.get("family", "")] if part)
            if name:
                authors.append(name)
        published = date_parts(item)
        records.append(
            {
                "id": item.get("DOI", ""),
                "title": first(item.get("title")),
                "authors": authors,
                "journal": first(item.get("container-title")),
                "year": published[:4],
                "published_date": published,
                "doi": item.get("DOI", ""),
                "url": item.get("URL", ""),
                "abstract": item.get("abstract", ""),
                "source_status": "public_api_verified",
            }
        )
    print(json.dumps(records, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
