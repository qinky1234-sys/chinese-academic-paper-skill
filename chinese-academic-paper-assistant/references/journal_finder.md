# Journal Finder

## Goal

Recommend candidate Chinese journals based on the user's topic, article type, field, methods, and literature corpus. Recommendations must be traceable and cautious.

## Inputs

- Paper title or topic
- Abstract or outline
- Keywords
- Discipline and article type
- Literature matrix
- User constraints: core journal preference, fee sensitivity, publication speed, region, institution requirements

## Data Sources

Use:

- User-supplied journal information.
- Journal official websites.
- Publisher pages.
- Crossref or OpenAlex source metadata.
- Public indexing pages where accessible.

Do not invent or rely on memory for current rankings.

## Output Fields

| 期刊 | 官网/投稿链接 | 收稿范围 | 匹配理由 | 需要核验的信息 | 风险提示 | 推荐级别 |
|---|---|---|---|---|---|---|

## Required Caveats

Mark these as requiring current user verification unless the user provides authoritative evidence:

- 北大核心
- CSSCI
- CSCD
- 科技核心
- 影响因子
- 审稿周期
- 版面费
- 录用率

## Risk Signals

Flag:

- Scope too broad.
- Unclear editorial board.
- Unrealistic fast acceptance claims.
- Missing ISSN or fake metrics.
- Submission page detached from official journal domain.
- Excessive fees without transparent policy.
