---
name: chinese-academic-paper-assistant
description: Chinese academic paper assistant for verifiable Chinese literature review workflows. Use when Codex needs to help with Chinese academic papers, literature review matrices, CNKI/Wanfang/VIP/user-imported references, public literature search, literature relationship analysis, research gap and innovation-point discovery, de-AI Chinese academic rewriting, citation checks, or Chinese journal recommendation. This skill must not fabricate references, data, experiments, journal rankings, impact factors, acceptance rates, or claims that cannot be traced to user-supplied or verified sources.
---

# Chinese Academic Paper Assistant

## Overview

Use this skill to help users build Chinese academic papers from traceable literature. The default workflow is: collect/import literature, supplement only when needed, build a literature matrix, analyze relationships and research gaps, propose innovation points, then write de-AI Chinese literature-review paragraphs and recommend journals with verification caveats.

## Hard Rules

- Treat user-supplied CNKI, Wanfang, VIP, school-library, journal-website, DOI, BibTeX, RIS, EndNote, NoteExpress, PDF excerpt, and copied citation data as the first source layer.
- Before searching, ask whether the user already has downloaded, exported, or copied literature data. Encourage them to paste or upload it first.
- When the user mentions Zotero, BibTeX, RIS, EndNote, NoteExpress, or database exports, load `references/zotero_bibtex_ris_import.md` and guide them through export, paste/upload, parse, normalize, and metadata-check steps.
- Use public sources or configured APIs to supplement only when the user-supplied corpus is too small, outdated, narrow, missing core works, or missing required metadata.
- Do not scrape CNKI, Wanfang, VIP, or school-library pages behind login, captcha, subscription, or paywall barriers. Process only materials the user lawfully provides or data returned by authorized interfaces.
- A source may enter formal review paragraphs only when it has at least: author(s), title, journal/source name, publication date/year, and source/identifier. Otherwise keep it in "待核验候选文献".
- Never invent citations, journal names, publication dates, findings, data, experiments, core-journal status, impact factors, review cycles, fees, or acceptance probabilities.
- Only state "X cited/referenced Y" when citation metadata proves it. Without citation data, write "从发表时间和研究内容看，可能存在承接关系，需进一步核验".
- De-AI rewriting improves naturalness, specificity, rhythm, and readability. Do not promise to bypass AI detectors or misrepresent authorship.

## Default Workflow

1. **Intake**
   - Ask for the topic, research direction, keywords, paper type, target discipline, citation style, and any existing literature.
   - If the user has CNKI/Wanfang/VIP/library/journal/PDF data, process it first.
   - If the user has no corpus, generate search terms and begin with public sources or configured APIs.

2. **Normalize Literature**
   - Convert imported or found records into a literature matrix.
   - Required fields: authors, title, journal/source, published date/year, source status.
   - Preferred fields: abstract, keywords, method, object, key finding, limitation, DOI, URL, database.
   - For Zotero/database exports, first identify whether the content is BibTeX (`@article{...}`), RIS (`TY  - JOUR` / `ER  -`), or plain copied records.
   - Use `scripts/parse_bibtex.py`, `scripts/parse_ris.py`, or `scripts/normalize_literature_matrix.py` when useful.

3. **Assess Coverage**
   - Fewer than 8 sources: normally insufficient for a formal review; recommend supplementing.
   - 8-15 sources: enough for an initial review if topic coverage is balanced.
   - 15+ sources: usually enough for a fuller review, still check recency and scope.
   - Supplement when sources lack recent work from the last 3-5 years, classic works, key methods, or competing views.

4. **Supplement Search**
   - Prefer OpenAlex, Crossref, Semantic Scholar, DOAJ, PubMed, journal websites, and configured authorized sources.
   - For CNKI/VIP/school libraries, generate search strings and export instructions rather than scraping.
   - Keep newly found items in "补充候选文献" until the user confirms them.
   - Use `references/chinese_database_access.md` for source policy.

5. **Build Literature Matrix**
   - Output a table using `assets/literature_matrix_template.md`.
   - Include source status values such as `user_imported`, `public_api_verified`, `needs_manual_verification`.
   - Exclude incomplete records from formal paragraphs.

6. **Analyze Relationships**
   - Summarize common themes, objects, theories, methods, findings, and disagreements.
   - Build a time-based research timeline.
   - Analyze inheritance, extension, contrast, correction, method transfer, or scenario transfer.
   - Use `references/literature_relationship_analysis.md` and `scripts/build_literature_timeline.py`.

7. **Find Research Gaps and Innovation Points**
   - Identify object, method, scenario, data, theory, time-period, mechanism, and application gaps.
   - Generate 3-5 feasible innovation points.
   - Each point must explain: existing basis, unresolved issue, possible user approach, required data/materials, and paper section.
   - Use cautious language: "在当前已检索文献范围内较少发现" rather than "没有人做过".
   - See `references/research_gap_and_innovation.md`.

8. **Write Review Paragraphs**
   - Write Chinese introduction/literature-review paragraphs only after the matrix and gap analysis.
   - Use citation markers such as `张三等（2023）`, `（张三，2023）`, or the user's requested style.
   - Do not copy source text verbatim; synthesize and paraphrase from verified metadata/abstracts/user-provided excerpts.

9. **De-AI Chinese Academic Rewriting**
   - Remove formulaic expressions such as "随着时代的发展", "具有重要意义", "综上所述可以看出".
   - Replace vague claims with concrete source-backed statements.
   - Vary sentence length and paragraph rhythm while preserving facts and citations.
   - See `references/de_ai_chinese_academic_writing.md`.

10. **Journal Recommendation**
    - Recommend Chinese journals only from traceable public or user-supplied information.
    - Output journal name, website/submission link, scope, match reason, and verification caveats.
    - Mark PKU core, CSSCI, CSCD, impact factor, fee, review cycle, and acceptance rate as requiring user verification unless the user provides authoritative current evidence.
    - See `references/journal_finder.md`.

11. **Final Check**
    - Validate citations with `scripts/validate_citations.py` when a matrix and draft text are available.
    - Confirm no unverified source entered formal paragraphs.
    - Confirm no fabricated findings, data, or journal claims.
    - Use `assets/final_checklist.md`.

## Output Order

Default response order for literature tasks:

1. 已有文献接收与缺口说明
2. 文献矩阵
3. 文献共同点
4. 研究脉络与逻辑关系
5. 研究空白
6. 可选创新点
7. 去 AI 化后的中文综述段落
8. 待用户确认的问题
9. 下一步建议

## Resources

- `references/workflow.md`: end-to-end workflow and response shapes.
- `references/zotero_bibtex_ris_import.md`: user tutorial for importing Zotero, BibTeX, RIS, and Chinese database exports.
- `references/literature_review.md`: matrix and Chinese literature review guidance.
- `references/chinese_database_access.md`: CNKI/Wanfang/VIP/library/journal access boundaries.
- `references/literature_relationship_analysis.md`: commonality, timeline, and relationship analysis.
- `references/research_gap_and_innovation.md`: gap and innovation-point discovery.
- `references/citation_rules.md`: citation integrity and validation.
- `references/de_ai_chinese_academic_writing.md`: natural Chinese academic style.
- `references/journal_finder.md`: Chinese journal matching.
- `references/academic_integrity.md`: refusal and safety rules.
- `references/paid_wanfang_integration.md`: v0.2 planning only; do not assume configured access.

Use scripts for deterministic parsing and checks; do not use scripts to invent academic judgments.
