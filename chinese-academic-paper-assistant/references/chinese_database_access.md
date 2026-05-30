# Chinese Database Access

## Default Policy

Use user-imported Chinese database records first. Do not scrape CNKI, Wanfang, VIP, school-library databases, or paywalled journal pages without authorization.

For 一键生成文献综述, ask the user to upload or paste 8+ exported records when possible. If the user has no literature, generate public-source candidates and output only a clearly labeled 待核验版完整文献综述 plus coverage table.

Accept these user-provided inputs:

- CNKI, Wanfang, VIP, school library, or journal website export records.
- BibTeX, RIS, EndNote, NoteExpress, DOI lists.
- Copied title/author/journal/year/abstract records.
- Downloaded PDF excerpts or abstract-page text.
- Public article links.

## Recommended User Prompt

Ask:

> 如果你已经从 CNKI、万方、维普、学校图书馆数据库、期刊官网或已下载 PDF 中整理了文献，请先粘贴或上传题录、摘要、BibTeX、RIS、EndNote、NoteExpress、DOI、文章链接或复制的引用信息。我会优先使用你提供的文献；如果数量不足、主题覆盖不够、时间过旧、缺少核心研究或缺少作者/期刊/发表时间等必要字段，再通过公开来源或已配置接口补充查找。

## Manual Search Assistance

For CNKI, VIP, and school-library databases, help users by generating:

- Topic and keyword combinations.
- Advanced search strings.
- Year, document type, discipline, journal, and core-database filters.
- Export field requirements.

Example:

```text
主题 = "乡村振兴" AND "数字治理"
年份 = 2020-2026
文献类型 = 期刊
建议导出字段 = 作者、题名、期刊、发表时间、摘要、关键词、DOI/链接
```

## Wanfang v0.2 Direction

If authorized Wanfang access is configured, use it as the preferred Chinese literature source. Never expose API keys in the skill repository. Account, quota, payment, API key, logging, and rate limits belong in a backend service.

## Public Fallback Sources

Use OpenAlex, Crossref, Semantic Scholar, DOAJ, PubMed, publisher pages, and journal websites for supplemental discovery and metadata verification where appropriate.
