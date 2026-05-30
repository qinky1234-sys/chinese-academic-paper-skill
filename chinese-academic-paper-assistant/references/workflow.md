# Workflow

## Intake Prompt

Start by asking the user to provide any existing literature they already have. Mention CNKI, Wanfang, VIP, school-library databases, journal websites, downloaded PDFs, DOI lists, BibTeX, RIS, EndNote, NoteExpress, copied abstracts, and copied citation records.

If the user is unsure how to provide records, offer the Zotero/BibTeX/RIS path:

- Zotero: select references, right-click, export items, choose BibTeX or RIS, then paste/upload the file content.
- CNKI/Wanfang/VIP/library/journal sites: use the database's own export/citation function, prefer RIS or BibTeX when available, then paste/upload the exported text.
- Manual fallback: paste author, title, journal/source, year/date, abstract, keywords, DOI/URL, and database/source.

If the user has no literature, ask for:

- Paper topic
- Research field
- 3-8 keywords
- Paper type
- Target citation style
- Required period, region, industry, sample, or method constraints

Then generate search terms and use public sources or configured authorized APIs to find candidate literature when available. If candidate records have traceable metadata, the skill may produce a candidate matrix and a clearly labeled "待核验版" literature review. Do not present it as a final verified review until the user confirms the sources.

## Main Sequence

If the user asks for 一键生成文献综述, 一键综述, 直接生成综述, 只要最终综述, or 不用其他功能, use the one-click review sequence instead of the full analytical sequence:

1. Identify whether the user uploaded literature or needs public candidate search.
2. Check source count and metadata. Recommend 8+ usable sources for a stronger review.
3. Generate a complete textual literature review that covers every source.
4. Append a literature coverage table.
5. Add only necessary verification reminders.

Do not output the full matrix, knowledge map, innovation points, journal matching, or other advanced modules in one-click review mode unless the user explicitly asks for them.

1. Import and normalize user-supplied literature.
2. For Zotero/BibTeX/RIS/database exports, identify the format, parse it, and normalize fields.
3. Check whether required metadata exists.
4. Assess coverage by count, year range, topic coverage, methods, and source diversity.
5. Supplement from public sources or configured authorized APIs when the user has no literature or when imported literature is insufficient.
6. Generate the literature matrix.
7. Analyze shared themes and disagreements.
8. Build the research timeline and relationship map.
9. Identify research gaps.
10. Propose feasible innovation points.
11. Write de-AI Chinese review paragraphs with citations.
12. Recommend journals if requested.
13. Run final integrity checks.

## Source Status

Use these statuses consistently:

- `user_imported`: supplied by the user from a database, PDF, export file, or copied record.
- `public_api_verified`: returned from public sources such as OpenAlex or Crossref with enough metadata.
- `wanfang_verified`: reserved for future authorized Wanfang integration.
- `needs_manual_verification`: incomplete, ambiguous, or not yet confirmed by the user.

## Insufficient Corpus Signals

Recommend supplementing when:

- Fewer than 8 usable sources exist.
- Most sources are older than 5 years and the topic is current.
- All sources come from one database or one journal.
- There are no empirical/case/theoretical/method papers where those are expected.
- Abstracts or key findings are missing for most records.
- The topic has obvious subfields not represented in the matrix.

## Required Response Shape

For one-click review work, use this order:

1. 综述状态说明（已核验版/待核验版；文献数量是否达到 8 篇建议线）
2. 完整版文字式文献综述
3. 文献覆盖简表
4. 必要核验提醒

For literature-review work, use this order unless the user asks for a narrower output:

1. 文献接收与缺口说明
2. 导入格式识别与字段核验
3. 文献矩阵
4. 文献共同点
5. 研究脉络与逻辑关系
6. 研究空白
7. 可选创新点
8. 去 AI 化后的综述段落；如果来源尚未由用户确认，标注为“待核验版”
9. 需要用户确认的问题
