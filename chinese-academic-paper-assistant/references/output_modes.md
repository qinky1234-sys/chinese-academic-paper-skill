# Output Modes

Use this reference when the user asks for 本科论文模式, 硕士论文模式, 期刊论文模式, or when the paper type is clear from context.

## Mode Selection

One-click review mode can be combined with any paper mode. When the user asks to 一键生成文献综述, apply the selected paper mode to tone and depth, but keep the output narrow: 完整文献综述 + 文献覆盖简表 + 必要核验提醒.

If the user does not specify a mode, ask for the paper type when the answer would materially change depth or structure. If the user wants a quick first pass, default to 硕士论文模式 only when the topic is explicitly graduate-level; otherwise default to 本科论文模式.

Supported modes:

- `本科论文模式`
- `硕士论文模式`
- `期刊论文模式`

Do not offer a 博士论文 mode in v0.1.5 unless the user explicitly asks; use 硕士论文模式 plus a note that doctoral-level work needs deeper corpus and method design.

## 本科论文模式

Use for undergraduate thesis, course paper, or first literature review draft.

Recommended corpus:

- Minimum: 8 usable sources
- Better: 10-15 sources
- Recent sources: include at least 3-5 from the last 5 years when the topic is current

Output emphasis:

- Explain concepts clearly.
- Classify literature by theme, time, or research object.
- Avoid overly complex theoretical disputes.
- Innovation points should be modest and feasible.
- Use simpler but still academic Chinese.

Required output:

1. 文献接收与字段核验
2. 简明文献矩阵
3. 2-3 个研究主题归类
4. 研究现状概括
5. 主要不足
6. 2-3 个可写创新点
7. 约 600-900 字中文综述段落
8. 下一步补充文献建议

One-click version:

1. 600-900 字左右完整文献综述
2. 文献覆盖简表
3. 必要核验提醒

Innovation-point standard:

- Prefer topic angle, case selection, local sample, comparison object, or application scenario.
- Avoid proposing complex models or large empirical designs unless the user has data.

## 硕士论文模式

Use for master thesis, graduate course paper, or opening-report literature review.

Recommended corpus:

- Minimum: 15 usable sources
- Better: 20-35 sources
- Include classic works, recent works, and competing views when possible

Output emphasis:

- Build a clearer research lineage.
- Distinguish theory, method, object, data, and scenario.
- Explain "who proposed earlier" and possible inheritance/extension relationships.
- Identify research gaps cautiously.
- Innovation points should include feasibility, data/material needs, and chapter placement.

Required output:

1. 文献接收与缺口说明
2. 完整文献矩阵
3. 文献共同点与分组
4. 时间线与研究脉络
5. 理论、方法、对象和场景差异
6. 研究空白
7. 3-5 个创新点，含可行性和材料需求
8. 约 1000-1500 字中文综述段落
9. 可放入开题报告或论文绪论的过渡句
10. 待核验问题与补充检索建议

One-click version:

1. 1000-1500 字左右完整文献综述
2. 文献覆盖简表
3. 必要核验提醒

Innovation-point standard:

- Each point must include existing basis, unresolved issue, user's possible approach, required data/materials, and suitable chapter.
- Avoid saying "没人做过"; say "在当前已检索文献范围内较少发现".

## 期刊论文模式

Use for journal article,投稿论文, or paper-to-submission polishing.

Recommended corpus:

- Minimum: 12 highly relevant sources
- Better: 15-25 highly focused sources
- Prefer recent, high-match sources over broad accumulation

Output emphasis:

- Narrow the problem quickly.
- Show research contribution and argument density.
- Avoid long textbook-style background.
- Link literature review directly to the article's research question.
- Add journal-fit and verification caveats when journal recommendation is requested.

Required output:

1. 主题聚焦与投稿方向判断
2. 高相关文献矩阵
3. 研究争议或不足
4. 文章可主打的问题意识
5. 2-4 个可投稿创新点
6. 约 500-900 字引言式文献综述
7. 贡献表述候选句
8. 期刊匹配提醒与人工核验事项

One-click version:

1. 500-900 字左右引言式完整文献综述
2. 文献覆盖简表
3. 必要核验提醒

Innovation-point standard:

- Prefer sharper problem, new case, new mechanism, new data, new comparison, or practical policy implication.
- Avoid oversized thesis-style frameworks.
- Do not claim novelty without corpus evidence; write "可作为投稿时重点核验的潜在贡献".

## Mode Comparison

| 模式 | 主要目标 | 文献范围 | 综述风格 | 创新点 |
| --- | --- | --- | --- | --- |
| 本科论文 | 写清楚、分类清楚、能落地 | 8-15 篇 | 清晰、稳妥、少争论 | 小切口、易完成 |
| 硕士论文 | 建立脉络、找到空白、支撑研究设计 | 15-35 篇 | 系统、层次清楚、有研究问题 | 有依据、有材料、有章节落点 |
| 期刊论文 | 聚焦问题、突出贡献、服务投稿 | 12-25 篇高相关文献 | 紧凑、有问题意识、有论证密度 | 新问题、新机制、新数据或新场景 |

## Response Header

When applying a mode, start with:

```text
已采用【本科论文/硕士论文/期刊论文】输出模式。本模式会重点控制【深度/结构/综述长度/创新点类型】。
```

If the source corpus is insufficient for the selected mode, say so before producing the review.
