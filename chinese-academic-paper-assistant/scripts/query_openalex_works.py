#!/usr/bin/env python3
"""Query OpenAlex works and output normalized candidate literature records."""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request


def inverted_index_to_text(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    words = sorted(((pos, word) for word, positions in index.items() for pos in positions))
    return " ".join(word for _, word in words)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    params = urllib.parse.urlencode({"search": args.query, "per-page": args.limit})
    url = f"https://api.openalex.org/works?{params}"
    with urllib.request.urlopen(url, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))

    records = []
    for item in payload.get("results", []):
        authors = [a.get("author", {}).get("display_name", "") for a in item.get("authorships", [])]
        source = (item.get("primary_location") or {}).get("source") or {}
        records.append(
            {
                "id": item.get("id", ""),
                "title": item.get("title", ""),
                "authors": [a for a in authors if a],
                "journal": source.get("display_name", ""),
                "year": item.get("publication_year", ""),
                "published_date": item.get("publication_date", ""),
                "doi": item.get("doi", ""),
                "url": item.get("id", ""),
                "abstract": inverted_index_to_text(item.get("abstract_inverted_index")),
                "source_status": "public_api_verified",
            }
        )
    print(json.dumps(records, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
