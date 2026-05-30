# Zotero, BibTeX, and RIS Import

Use this reference when the user wants to import literature from Zotero, CNKI, Wanfang, VIP, school-library databases, journal websites, EndNote, NoteExpress, BibTeX, or RIS.

If the user's goal is 一键生成文献综述, treat Zotero/BibTeX/RIS import as the fastest path into one-click review mode: parse the records, check whether there are 8+ usable sources, then output the complete literature review plus coverage table.

## User-Facing Import Path

Tell the user they can provide literature in any of these forms:

- Paste BibTeX text beginning with `@article{`, `@inproceedings{`, `@book{`, or similar entries.
- Paste RIS text containing tags such as `TY  - JOUR`, `AU  -`, `TI  -`, `JO  -`, `PY  -`, and `ER  -`.
- Upload or paste records exported from Zotero, EndNote, NoteExpress, CNKI, Wanfang, VIP, school-library databases, journal websites, or PDF reference managers.
- Paste a manual list containing author, title, journal/source, publication year/date, abstract, keywords, DOI, URL, and database name.

If the user has not prepared literature yet, give them the export steps below before doing public-source supplement search.

## Zotero Export Steps

1. Open Zotero and select the target references.
2. Right-click the selected items.
3. Choose `Export Items...`.
4. Select `BibTeX` or `RIS`.
5. Keep notes/files unchecked unless the user specifically wants to inspect notes.
6. Save the `.bib` or `.ris` file, then paste its content or provide the file for parsing.

Preferred format:

- Use BibTeX when the user wants stable citation keys and DOI/URL fields.
- Use RIS when the records come from Chinese databases, EndNote, NoteExpress, or mixed reference managers.

## Chinese Database Export Path

For CNKI, Wanfang, VIP, school-library systems, and journal websites:

1. Search and select relevant records in the database UI.
2. Use the database's own export/citation function.
3. Prefer formats in this order: `RIS`, `BibTeX`, `EndNote`, `NoteExpress`, `RefWorks`, then plain text citation.
4. Include abstracts and keywords when the database allows it.
5. Do not ask the assistant to bypass login, captcha, payment, subscription, or school-library restrictions.
6. Paste or upload the exported content for parsing.

If only copied citation text is available, ask the user to include:

- 作者
- 题名
- 期刊或来源名称
- 发表年份或日期
- 摘要
- 关键词
- DOI、链接或数据库来源

## Parsing Procedure

When file access is available:

```bash
python scripts/parse_bibtex.py input.bib -o imported.json
python scripts/parse_ris.py input.ris -o imported.json
python scripts/normalize_literature_matrix.py imported.json -o normalized.json
```

When file access is not available, parse the pasted records directly and convert them into the literature matrix fields:

- authors
- title
- journal/source
- published_date/year
- abstract
- keywords
- DOI
- URL
- database/source
- source_status

Set `source_status` to `user_imported` for user-provided exports. Use `needs_manual_verification` only when required metadata is missing or the record is ambiguous.

## Metadata Check

A record can enter formal literature-review paragraphs only when it has:

- author(s)
- title
- journal/source name
- publication date or year
- source, DOI, URL, database name, or other traceable identifier

If abstracts or key findings are missing, do not invent them. Mark the item as usable for citation metadata only and ask the user to provide the abstract/full text excerpt if deeper synthesis is needed.

## Response Template

After importing records, respond in this shape:

1. 已识别的导入格式：BibTeX / RIS / 纯文本 / 混合格式
2. 成功解析数量
3. 缺字段数量与缺失字段
4. 可进入正式综述的文献数量
5. 需要用户补充或核验的文献
6. 下一步：生成文献矩阵、补充检索、研究脉络分析或综述段落

## Safety Boundary

Do not scrape or automate access to CNKI, Wanfang, VIP, or school-library pages behind login, captcha, subscription, or paywall barriers. Only process user-provided records, public metadata, or explicitly authorized interfaces.
