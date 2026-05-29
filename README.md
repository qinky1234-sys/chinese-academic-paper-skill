# Chinese Academic Paper Skill

一个面向中文学术论文写作的 Codex skill：先整理真实文献，再生成文献矩阵、研究脉络、研究空白、创新点建议和去 AI 化中文综述段落。

`chinese-academic-paper-assistant` is a Codex skill for Chinese academic-paper workflows. It helps users import Chinese literature, build a verifiable literature matrix, analyze research relationships, identify possible innovation points, write natural Chinese literature-review paragraphs, and prepare cautious journal recommendations.

## Why This Skill

普通 AI 写论文很容易出现三个问题：编造引用、综述像模板、创新点空泛。这个 skill 的默认流程反过来做：

1. 先让用户导入 CNKI、万方、维普、学校图书馆、期刊官网或 PDF 中已有的文献资料。
2. 如果文献不够，再用公开来源或已配置接口补充候选文献。
3. 先输出文献矩阵和研究脉络，再写中文综述段落。
4. 所有正文内容默认去 AI 化，但不改变事实和引用。

## What It Does

- Prioritizes user-imported CNKI, Wanfang, VIP, school-library, journal-site, PDF, DOI, BibTeX, RIS, EndNote, and NoteExpress records.
- Supplements with public sources such as OpenAlex and Crossref when the imported corpus is insufficient.
- Builds a literature matrix with author, title, journal/source, publication date, key finding, limitation, relationship, and source status.
- Analyzes common themes, timeline, literature relationships, research gaps, and feasible innovation points.
- Produces de-AI Chinese academic prose that preserves citations and evidence.
- Recommends Chinese journals with explicit verification caveats.

## Quick Install

Copy the skill folder into your Codex skills directory:

```powershell
mkdir $env:USERPROFILE\.codex\skills -Force
Copy-Item -Recurse .\chinese-academic-paper-assistant $env:USERPROFILE\.codex\skills\
```

Then ask Codex:

```text
使用 chinese-academic-paper-assistant，帮我整理这些中文文献，生成文献矩阵、研究脉络、创新点和去 AI 化综述段落。
```

If your Codex environment supports installing skills directly from GitHub, install from this repository path:

```text
https://github.com/qinky1234-sys/chinese-academic-paper-skill/tree/main/chinese-academic-paper-assistant
```

## Demo Prompts

完整的输入与输出示例见 [examples](./examples/README.md)。如果你想先看效果，可以直接打开下面三个示例：

- [CNKI/万方/维普题录导入到文献矩阵](./examples/01-imported-records-to-matrix.md)
- [从研究主题生成中文数据库检索策略](./examples/02-topic-to-search-strategy.md)
- [从文献矩阵生成去 AI 化中文综述段落](./examples/03-matrix-to-review-paragraph.md)

### 1. CNKI/Wanfang/VIP records to matrix

```text
我已经从 CNKI 导出了 12 篇乡村振兴相关文献。请先整理文献矩阵，再分析研究脉络和创新点。
```

Expected output:

- 文献矩阵
- 文献共同点
- 谁较早提出相关问题
- 哪些研究可能存在承接关系
- 当前研究空白
- 3-5 个可选创新点

### 2. Topic to search strategy

```text
围绕“数字治理与基层公共服务”帮我生成 CNKI、万方、维普可用的检索关键词和高级检索式。如果文献不够，再用公开来源补充候选文献。
```

Expected output:

- 中文数据库检索式
- 推荐导出字段
- 公开来源补充策略
- 待核验候选文献说明

### 3. Literature to de-AI review paragraph

```text
根据这些文献，写一段可以放在中文论文引言里的文献综述。要求去 AI 化，保留引用，不要编造文献结论。
```

Expected output:

- 去 AI 化中文综述段落
- 引用标记
- 不确定内容的 TODO 核验提示

## Boundaries

This skill does not fabricate references, data, experiments, journal rankings, impact factors, review cycles, fees, or acceptance probabilities. It does not scrape CNKI, Wanfang, VIP, or school-library pages behind login, captcha, subscription, or paywall barriers. It only processes user-provided materials, public sources, or authorized interfaces.

## Good First Use Case

准备 8-15 条中文文献题录，最好包含：

- 作者
- 题名
- 期刊名称
- 发表时间
- 摘要
- 关键词
- DOI 或来源链接

然后让 Codex 使用这个 skill 先生成文献矩阵，不要一开始就要求完整论文。

## Version Plan

- v0.1: user import, public-source supplement, literature matrix, relationship analysis, innovation points, de-AI Chinese review paragraphs, basic journal recommendations.
- v0.2: authorized Wanfang integration through a backend service, paid quota, stronger Chinese metadata verification, enhanced relationship analysis.
- v0.3+: better CNKI/VIP/library import workflows, more export formats, journal-site public metadata extraction.

## Support and Roadmap

如果你希望支持万方接口接入、批量文献分析、课题组定制版或机构版，可以通过 GitHub Issues 提需求。后续商业版会优先考虑：

- 万方授权接口
- 批量文献矩阵
- 引用关系增强分析
- 创新点评分
- 中文期刊推荐报告
