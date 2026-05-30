# Paid Wanfang Integration

This is v0.2 planning guidance. Do not assume Wanfang access is configured in v0.1.

## Product Model

- Free: user import, public-source supplement, basic matrix, basic relationship analysis, basic innovation points.
- Paid: authorized Wanfang search, more Chinese metadata, stronger verification, quota, usage logs, and enhanced reports.

## Architecture

Place Wanfang API credentials and paid quota logic in a backend service, not in the skill repository.

Backend responsibilities:

- User account and quota.
- API key storage.
- Wanfang API calls.
- Rate limits.
- Usage logs.
- Standard JSON response.

## Standard JSON

```json
{
  "source": "wanfang",
  "query": "乡村振兴 数字治理",
  "results": [
    {
      "title": "文章标题",
      "authors": ["作者A", "作者B"],
      "journal": "期刊名称",
      "published_date": "2024-05",
      "abstract": "摘要",
      "keywords": ["关键词1", "关键词2"],
      "doi": "",
      "url": "来源链接",
      "database_id": "万方记录ID",
      "verification_status": "wanfang_verified"
    }
  ]
}
```
# One-Click Review Note

Future authorized Wanfang access may support the one-click review workflow by improving candidate discovery and metadata verification. Until configured, one-click review must rely on user-imported records or public-source candidates marked 待核验.
