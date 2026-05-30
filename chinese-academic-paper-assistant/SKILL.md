---
name: chinese-academic-paper-assistant
description: Chinese academic paper assistant for verifiable Chinese literature review workflows. Use when Codex needs to help with Chinese academic papers, literature review matrices, CNKI/Wanfang/VIP/user-imported references, public literature search, literature relationship analysis, research gap and innovation-point discovery, de-AI Chinese academic rewriting, citation checks, or Chinese journal recommendation. This skill must not fabricate references, data, experiments, journal rankings, impact factors, acceptance rates, or claims that cannot be traced to user-supplied or verified sources.
---

# Chinese Academic Paper Assistant

## Overview

Use this skill to help users build Chinese academic papers from traceable literature. The default workflow is: collect/import literature, supplement only when needed, create a first-upload claim map when the user provides a new corpus, build a literature matrix, analyze relationships, optionally build a research-field knowledge map, identify research gaps, propose innovation points with closest-paper and methodology notes, then write de-AI Chinese literature-review paragraphs and recommend journals with verification caveats.

## Hard Rules

- Treat user-supplied CNKI, Wanfang, VIP, school-library, journal-website, DOI, BibTeX, RIS, EndNote, NoteExpress, PDF excerpt, and copied citation data as the first source layer.
- Before searching, ask whether the user already has downloaded, exported, or copied literature data. Encourage them to paste or upload it first.
- When the user mentions Zotero, BibTeX, RIS, EndNote, NoteExpress, or database exports, load `references/zotero_bibtex_ris_import.md` and guide them through export, paste/upload, parse, normalize, and metadata-check steps.
- Use public sources or configured APIs to supplement only when the user-supplied corpus is too small, outdated, narrow, missing core works, or missing required metadata.
- If the user has no literature, search public sources or configured APIs for candidate literature and produce a candidate matrix plus a clearly labeled "待核验版" review when enough traceable metadata is available.
- When the user specifies 本科论文, 硕士论文, or 期刊论文, load `references/output_modes.md` and adapt depth, structure, review length, innovation-point expectations, and final check standards to that mode.
- Do not scrape CNKI, Wanfang, VIP, or school-library pages behind login, captcha, subscription, or paywall barriers. Process only materials the user lawfully provides or data returned by authorized interfaces.
- A source may enter formal review paragraphs only when it has at least: author(s), title, journal/source name, publication date/year, and source/identifier. Otherwise keep it in "待核验候选文献".
- When the user first uploads a literature corpus, or when public-source candidate literature is found for a user with no corpus, first produce an author-year-one-sentence-claim table, group papers by shared assumptions, mark clear contradictions/tensions, and create a macro background map before writing review paragraphs. Public-source candidate items must remain clearly labeled as pending verification.
- When generating innovation points, include the closest 1-3 papers for each point and a suitable methodology suggestion. Closest papers must come from user-supplied, verified, or clearly labeled public-source candidate literature.
- Never invent citations, journal names, publication dates, findings, data, experiments, core-journal status, impact factors, review cycles, fees, or acceptance probabilities.
- If author, title, journal/source, year/date, DOI, URL, abstract, or citation metadata is missing or uncertain, mark the item as pending verification instead of completing the field from imagination.
- Do not use phrases such as "无人研究", "首次提出", "绝对创新", or "填补空白" as factual claims. Use cautious wording such as "在当前文献范围内较少发现", "仍需进一步核验", or "可作为潜在切入点".
- Only state "X cited/referenced Y" when citation metadata proves it. Without citation data, write "从发表时间和研究内容看，可能存在承接关系，需进一步核验".
- De-AI rewriting improves naturalness, specificity, rhythm, and readability. Do not promise to bypass AI detectors or misrepresent authorship.

## Default Workflow

1. **Intake**
   - Ask for the topic, research direction, keywords, paper type, target discipline, citation style, and any existing literature.
   - If the user has CNKI/Wanfang/VIP/library/journal/PDF data, process it first.
   - If the user has no corpus, generate search terms, search public sources or configured APIs for candidate literature, and mark all found items as candidate or pending verification unless metadata is traceable.

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
   - When public-source candidate records contain enough metadata, generate a "待核验版" literature matrix, relationship analysis, gap analysis, and preliminary review paragraph. Do not call it final or formally verified until the user confirms sources.
   - Use `references/chinese_database_access.md` for source policy.

5. **First-Corpus Claim and Background Map**
   - When the user first uploads related literature, or when the skill finds public-source candidate literature for a user with no corpus, output a table with each article's author(s)+year and one-sentence core claim.
   - If the literature comes from public sources rather than user-confirmed records, title the output "待核验版首批文献主张与宏观背景图".
   - The one-sentence core claim must be grounded in title, abstract, keywords, conclusion, or user-provided excerpt. If evidence is insufficient, mark it "待核验".
   - Group papers by shared assumptions, such as theory assumptions, method assumptions, object assumptions, mechanism assumptions, or policy/practice assumptions.
   - Mark papers that clearly contradict or create tension with each other in object, method, conclusion, causal explanation, or evaluation standard.
   - Draw a macro background map rather than a narrative summary. Use layers such as policy/institutional background, social/industry background, technology/method background, theory/concept background, and practice/problem background.
   - Keep this as an open-source baseline capability. Do not claim automated contradiction scoring, citation-network visualization, or dynamic graph generation unless those tools are actually configured.
   - Use `assets/first_upload_claim_map_template.md`.

6. **Build Literature Matrix**
   - Output a table using `assets/literature_matrix_template.md`.
   - Include source status values such as `user_imported`, `public_api_verified`, `needs_manual_verification`.
   - Exclude incomplete records from formal paragraphs.

7. **Analyze Relationships**
   - Summarize common themes, objects, theories, methods, findings, and disagreements.
   - Build a time-based research timeline.
   - Analyze inheritance, extension, contrast, correction, method transfer, or scenario transfer.
   - Use `references/literature_relationship_analysis.md` and `scripts/build_literature_timeline.py`.

8. **Build a Research-Field Knowledge Map**
   - When the user asks for a 研究领域知识地图, 知识图谱, 核心主张, 支持柱, 争议区, 前沿问题, or 初学者必读论文, output a clean table-based knowledge map.
   - Include: one core claim, 3-5 support pillars, 2-3 controversy zones, 1-2 frontier questions, and beginner must-read papers with reasons.
   - Base the map only on verified/user-supplied literature or clearly labeled public-source candidates.
   - If sources are not fully verified, title the section "待核验版研究领域知识地图".
   - Use `assets/knowledge_map_template.md`.

9. **Find Research Gaps and Innovation Points**
   - Identify object, method, scenario, data, theory, time-period, mechanism, and application gaps.
   - Generate 3-5 feasible innovation points.
   - Each point must explain: existing basis, unresolved issue, closest 1-3 papers, similarity to those papers, possible differentiation or extension, suggested methodology, required data/materials, suitable paper type, and paper section.
   - Suggested methodology may include case study, interview, survey, text analysis, policy text analysis, comparative study, empirical model, mixed methods, or literature-based theoretical synthesis.
   - Mark closest papers from public-source candidate records as "待核验"; do not treat them as confirmed evidence.
   - Do not claim automatic similarity scoring, novelty scoring, methodology-fit scoring, or visual innovation graphs in the open-source workflow.
   - Use cautious language: "在当前已检索文献范围内较少发现" rather than "没有人做过".
   - See `references/research_gap_and_innovation.md` and `assets/innovation_closest_papers_template.md`.

10. **Write Review Paragraphs**
   - Write Chinese introduction/literature-review paragraphs only after the matrix and gap analysis.
   - Use citation markers such as `张三等（2023）`, `（张三，2023）`, or the user's requested style.
   - Do not copy source text verbatim; synthesize and paraphrase from verified metadata/abstracts/user-provided excerpts.
   - Match the paper mode: 本科论文 emphasizes clarity and basic classification; 硕士论文 emphasizes research lineage, gaps, and method feasibility; 期刊论文 emphasizes problem awareness, contribution, argument density, and journal-fit caveats.

11. **De-AI Chinese Academic Rewriting**
   - Remove formulaic expressions such as "随着时代的发展", "具有重要意义", "综上所述可以看出".
   - Replace vague claims with concrete source-backed statements.
   - Vary sentence length and paragraph rhythm while preserving facts and citations.
   - See `references/de_ai_chinese_academic_writing.md`.

12. **Journal Recommendation**
   - Recommend Chinese journals only from traceable public or user-supplied information.
   - Output journal name, website/submission link, scope, match reason, and verification caveats.
   - Mark PKU core, CSSCI, CSCD, impact factor, fee, review cycle, and acceptance rate as requiring user verification unless the user provides authoritative current evidence.
   - See `references/journal_finder.md`.

13. **Final Check**
   - Validate citations with `scripts/validate_citations.py` when a matrix and draft text are available.
   - Confirm no unverified source entered formal paragraphs.
   - Confirm no fabricated findings, data, or journal claims.
   - Confirm all public-source candidate records are still marked "待核验" unless the user explicitly supplied verification details.
   - Confirm every innovation point has closest-paper, methodology, data/material, suitability, and risk fields when the user asks for innovation analysis.
   - Use `assets/final_checklist.md`.

## Output Order

Default response order for literature tasks:

1. 已有文献接收与缺口说明
2. 首批文献主张表（作者+年份+一句话核心主张，首次上传文献或公开来源找到候选文献时输出）
3. 共同假设分组
4. 互相矛盾或存在张力的论文
5. 宏观背景图
6. 文献矩阵
7. 文献共同点
8. 研究脉络与逻辑关系
9. 研究领域知识地图（用户需要时输出核心主张、支持柱、争议区、前沿问题和初学者必读论文）
10. 研究空白
11. 可选创新点（每个创新点附 1-3 篇最接近论文、相近之处、可推进空间和推荐方法论）
12. 去 AI 化后的中文综述段落；若来源尚未由用户确认，标题必须标注为“待核验版”
13. 待用户确认的问题
14. 下一步建议

## Resources

- `references/workflow.md`: end-to-end workflow and response shapes.
- `references/output_modes.md`: 本科论文、硕士论文、期刊论文三种输出模式.
- `references/zotero_bibtex_ris_import.md`: user tutorial for importing Zotero, BibTeX, RIS, and Chinese database exports.
- `references/literature_review.md`: matrix and Chinese literature review guidance.
- `assets/first_upload_claim_map_template.md`: first-upload author-year claim table, shared-assumption grouping, contradiction/tension markers, and macro background map.
- `references/chinese_database_access.md`: CNKI/Wanfang/VIP/library/journal access boundaries.
- `references/literature_relationship_analysis.md`: commonality, timeline, and relationship analysis.
- `references/research_gap_and_innovation.md`: gap and innovation-point discovery.
- `assets/innovation_closest_papers_template.md`: closest-paper and methodology template for innovation points.
- `references/citation_rules.md`: citation integrity and validation.
- `references/de_ai_chinese_academic_writing.md`: natural Chinese academic style.
- `references/journal_finder.md`: Chinese journal matching.
- `references/academic_integrity.md`: refusal and safety rules.
- `references/paid_wanfang_integration.md`: v0.2 planning only; do not assume configured access.

Use scripts for deterministic parsing and checks; do not use scripts to invent academic judgments.
