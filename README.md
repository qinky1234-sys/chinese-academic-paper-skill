# Chinese Academic Paper Skill

`chinese-academic-paper-assistant` is a Codex skill for Chinese academic-paper workflows. It helps users import Chinese literature, build a verifiable literature matrix, analyze research relationships, identify possible innovation points, write natural Chinese literature-review paragraphs, and prepare cautious journal recommendations.

## What It Does

- Prioritizes user-imported CNKI, Wanfang, VIP, school-library, journal-site, PDF, DOI, BibTeX, RIS, EndNote, and NoteExpress records.
- Supplements with public sources such as OpenAlex and Crossref when the imported corpus is insufficient.
- Builds a literature matrix with author, title, journal/source, publication date, key finding, limitation, relationship, and source status.
- Analyzes common themes, timeline, literature relationships, research gaps, and feasible innovation points.
- Produces de-AI Chinese academic prose that preserves citations and evidence.
- Recommends Chinese journals with explicit verification caveats.

## Boundaries

This skill does not fabricate references, data, experiments, journal rankings, impact factors, review cycles, fees, or acceptance probabilities. It does not scrape CNKI, Wanfang, VIP, or school-library pages behind login, captcha, subscription, or paywall barriers. It only processes user-provided materials, public sources, or authorized interfaces.

## Install

Place the `chinese-academic-paper-assistant` folder in your Codex skills directory, or install it from this repository if your Codex environment supports GitHub skill installation.

## Example Prompts

```text
我已经从 CNKI 导出了 12 篇乡村振兴相关文献。请先整理文献矩阵，再分析研究脉络和创新点。
```

```text
围绕“数字治理与基层公共服务”帮我生成检索关键词，如果文献不够，再用公开来源补充候选文献。
```

```text
根据这些文献，写一段可以放在中文论文引言里的文献综述，要求去 AI 化并保留引用。
```

## Version Plan

- v0.1: user import, public-source supplement, literature matrix, relationship analysis, innovation points, de-AI Chinese review paragraphs, basic journal recommendations.
- v0.2: authorized Wanfang integration through a backend service, paid quota, stronger Chinese metadata verification, enhanced relationship analysis.
- v0.3+: better CNKI/VIP/library import workflows, more export formats, journal-site public metadata extraction.
