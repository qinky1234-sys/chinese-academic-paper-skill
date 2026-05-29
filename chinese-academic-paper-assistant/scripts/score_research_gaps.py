#!/usr/bin/env python3
"""Heuristically flag possible literature coverage gaps from a matrix."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", help="Normalized literature matrix JSON")
    args = parser.parse_args()

    matrix = json.loads(Path(args.matrix).read_text(encoding="utf-8"))
    years = [str(r.get("year") or r.get("published_date") or "")[:4] for r in matrix]
    methods = [str(r.get("method") or "").strip() for r in matrix if str(r.get("method") or "").strip()]
    objects = [str(r.get("object") or "").strip() for r in matrix if str(r.get("object") or "").strip()]
    journals = [str(r.get("journal") or "").strip() for r in matrix if str(r.get("journal") or "").strip()]

    current_years = [y for y in years if y.isdigit() and int(y) >= 2021]
    findings = []
    if len(matrix) < 8:
        findings.append("文献数量少于 8 篇，通常不足以支撑正式综述。")
    if len(current_years) < max(2, len(matrix) // 4):
        findings.append("近 3-5 年文献占比较低，建议补充近期研究。")
    if len(set(methods)) <= 1:
        findings.append("研究方法较单一，可考虑方法扩展或混合方法。")
    if len(set(objects)) <= 1:
        findings.append("研究对象较集中，可考虑对象、地区、行业或场景扩展。")
    if journals and Counter(journals).most_common(1)[0][1] > len(journals) * 0.5:
        findings.append("文献来源期刊较集中，建议扩大来源范围。")

    print(json.dumps({"possible_gaps": findings}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
