# 示例 11：真实案例：没有文献 → 8 篇候选 → 待核验综述

这个示例面向推广和新手试用，展示用户在**一篇文献都没有**的情况下，如何从论文题目出发，先得到 8 篇真实可追溯的公开候选文献，再生成一版“待核验版完整版文字式文献综述”。

> 注意：本示例中的候选文献均来自公开网页、期刊页面、DOI 页面或数据库公开摘要页。它们适合作为检索线索和演示材料，但正式写入论文前仍需用户回到 CNKI、万方、维普、学校图书馆、期刊官网、DOI 或原文 PDF 页面逐篇核验作者、题名、期刊、年份、页码和原文结论。

## 用户输入

```text
使用 chinese-academic-paper-assistant。

我的论文主题是：大学生短视频使用对学习专注度的影响。
论文类型是：本科毕业论文。
我现在还没有整理好的文献。

请先帮我查找公开候选文献，目标是先找到 8 篇左右可以支撑文献综述的候选文献。

要求：
1. 先拆解关键词。
2. 给出 CNKI、万方、维普、学校图书馆、期刊官网、Google Scholar 可用的检索式。
3. 整理 8 篇候选文献表。
4. 所有公开来源候选文献都标注为“待核验”。
5. 不要编造作者、题名、期刊、年份或 DOI。
6. 最后生成一版待核验版完整版文字式文献综述。
7. 综述正文要覆盖每一篇候选文献，格式尽量使用“XXX学者在《xxxxx》一文中提出/指出/认为……”。
```

## 第 1 步：拆解关键词

| 关键词层级 | 中文关键词 | 英文关键词 |
| --- | --- | --- |
| 研究对象 | 大学生、高校学生、本科生、职业院校学生 | college students, undergraduates, vocational college students |
| 核心现象 | 短视频使用、短视频成瘾、短视频应用成瘾、短视频过度使用 | short video use, short video addiction, short-form video addiction, excessive use of short-video applications |
| 学习结果 | 学习专注度、注意力控制、学习投入、学业成绩、学习拖延、学习动机 | attention, attentional control, academic engagement, academic achievement, academic procrastination, learning motivation |
| 机制变量 | 自我控制、正念、学业自我效能感、学习回避动机、焦虑、睡眠质量 | self-control, mindfulness, academic self-efficacy, learning avoidance motivation, anxiety, sleep quality |

## 第 2 步：检索式

### 中文数据库检索式

```text
大学生 AND 短视频 AND 学习投入
大学生 AND 短视频成瘾 AND 学业成绩
大学生 AND 短视频成瘾 AND 注意力
大学生 AND 短视频成瘾 AND 学业拖延
大学生 AND 短视频成瘾 AND 自我控制
大学生 AND 短视频成瘾 AND 睡眠质量
短视频应用成瘾 AND 学业焦虑 AND 学业投入
职业院校学生 AND 短视频成瘾 AND 学习动机
```

### 英文检索式

```text
"short video addiction" AND "college students" AND "academic engagement"
"short-form video addiction" AND "academic procrastination"
"short-form video app addiction" AND "academic anxiety"
"short video addiction" AND "learning motivation"
"excessive use of short-video applications" AND "college students"
"short video addiction" AND "attentional control"
```

### 人工核验入口

- CNKI：使用中文检索式核验中文期刊记录、页码、作者单位和引用格式。
- 万方、维普：核验中文文献的题录、摘要、期刊和发表时间。
- 学校图书馆：优先下载学校已购买数据库中的正式全文。
- 期刊官网、DOI 页面：核验英文文献的 DOI、卷期、页码或文章编号。
- Google Scholar：查看被引、相关文章和可能的 PDF 入口。

## 第 3 步：8 篇公开候选文献表

| 序号 | 作者与年份 | 题名 | 来源/期刊 | 公开入口 | 为什么相关 | 核验状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 秦浩轩、李霞、曾美红等（2019） | 大学生短视频成瘾量表的初步编制 | 中国心理学前沿，1(8): 586-598 | https://www.sciscanpub.com/index/journals/ainfo/pc/264.html | 提供“短视频成瘾”测量工具和维度，可作为后续实证研究的变量基础 | 待核验 |
| 2 | 王小凤、李思婷、索秀娟、李宸吉、王玥怡（2022） | 大学生短视频使用特点及对主观幸福感的影响研究 | 社会科学前沿，11(6): 2431-2437 | https://doi.org/10.12677/ass.2022.116334 | 讨论短视频使用、自我控制与主观幸福感关系，可支撑“自我控制/心理状态”路径 | 待核验 |
| 3 | Ye, Wu, Wu, Chen & Ye（2022） | Effects of Short Video Addiction on the Motivation and Well-Being of Chinese Vocational College Students | Frontiers in Public Health, 10: 847672 | https://doi.org/10.3389/fpubh.2022.847672 | 讨论短视频成瘾对学习动机和学习幸福感的影响，适合放在学习结果部分 | 待核验 |
| 4 | Zhang, Hazarika, Chen & Shi（2023） | A cross-national study on the excessive use of short-video applications among college students | Computers in Human Behavior, 145: 107752 | https://doi.org/10.1016/j.chb.2023.107752 | 从跨文化视角讨论大学生短视频应用过度使用及其动机，可作为理论背景 | 待核验 |
| 5 | Ye, He, Yang, Lee, Nong, Ye & Wang（2023） | Predicting the Learning Avoidance Motivation, Learning Commitment, and Silent Classroom Behavior of Chinese Vocational College Students Caused by Short Video Addiction | Healthcare, 11(7): 985 | https://doi.org/10.3390/healthcare11070985 | 直接关联短视频成瘾、学习回避动机、学习投入和课堂沉默行为 | 待核验 |
| 6 | Xie, Xu, Zhang, Tan, Wu, Shi & Huang（2023） | The effect of short-form video addiction on undergraduates' academic procrastination: a moderated mediation model | Frontiers in Psychology, 14: 1298361 | https://doi.org/10.3389/fpsyg.2023.1298361 | 讨论短视频成瘾、注意力控制与学业拖延，最接近“学习专注度”机制 | 待核验 |
| 7 | Li, Geng & Wu（2024） | Effects of short-form video app addiction on academic anxiety and academic engagement: The mediating role of mindfulness | Frontiers in Psychology, 15: 1428813 | https://doi.org/10.3389/fpsyg.2024.1428813 | 讨论短视频应用成瘾对学业焦虑、学业投入的影响，并引入正念机制 | 待核验 |
| 8 | 王兴超、田芳芳（2025） | 大学生短视频成瘾与学业成绩的关系——学习投入的中介作用和学业自我效能感的调节作用 | 华南师范大学学报（社会科学版），2025年第1期 | https://journal-s.scnu.edu.cn/cn/article/id/963c7441-4cd5-4ead-b0b2-c8a6db6ab69c | 直接讨论短视频成瘾、学习投入、学业成绩和学业自我效能感 | 待核验 |

## 第 4 步：候选文献为什么能组成一组

| 分组 | 对应候选文献 | 可支撑的综述部分 |
| --- | --- | --- |
| 概念与测量基础 | 秦浩轩等（2019） | 短视频成瘾概念、维度和测量工具 |
| 使用后果与心理机制 | 王小凤等（2022）、Ye等（2022） | 自我控制、学习动机、幸福感等心理结果 |
| 过度使用形成机制 | Zhang等（2023） | 短视频过度使用的动机和跨文化背景 |
| 学习行为影响 | Ye等（2023）、Xie等（2023）、Li等（2024）、王兴超和田芳芳（2025） | 学习投入、学业拖延、注意力控制、学业成绩、学业焦虑 |

## 第 5 步：候选文献主张表

| 文献 | 一句话核心主张 | 与本题关系 |
| --- | --- | --- |
| 秦浩轩等（2019） | 短视频成瘾可以从戒断、逃避、失控和低效等维度进行测量。 | 为“短视频使用/成瘾”变量提供测量基础 |
| 王小凤等（2022） | 大学生短视频使用强度可能通过自我控制影响主观幸福感。 | 提示自我控制可能是短视频影响学习专注的中介机制 |
| Ye等（2022） | 短视频成瘾会削弱学生的内外在学习动机，并影响学习幸福感。 | 支撑短视频成瘾与学习心理状态之间的关系 |
| Zhang等（2023） | 大学生短视频应用过度使用与使用动机、社交互动和补偿性期待有关。 | 为解释短视频为什么容易过度使用提供理论背景 |
| Ye等（2023） | 短视频成瘾与学习回避动机正相关，与学习投入负相关。 | 直接支撑短视频影响学习投入的路径 |
| Xie等（2023） | 短视频成瘾会通过注意力控制影响大学生学业拖延。 | 与“学习专注度”最直接相关 |
| Li等（2024） | 短视频应用成瘾会提高学业焦虑、降低学业投入，正念具有中介作用。 | 说明短视频影响学习状态可能包含情绪和注意调节机制 |
| 王兴超、田芳芳（2025） | 短视频成瘾负向预测学业成绩，学习投入起部分中介作用，学业自我效能感具有调节作用。 | 可作为学习投入和学业结果关系的核心文献 |

## 第 6 步：待核验版完整版文字式文献综述

> 以下综述基于公开来源候选文献生成，只能作为检索和写作草稿。正式写入论文前，必须逐篇核验作者、题名、期刊、年份、页码、DOI 和原文结论。若核验结果与本表不一致，应以正式数据库和原文为准。

围绕“大学生短视频使用对学习专注度的影响”这一主题，现有候选文献主要集中在短视频成瘾的概念测量、过度使用形成机制、学习动机变化、学习投入下降、注意力控制受损以及学业结果变化等方面。整体来看，短视频并非只是一种娱乐媒介，其高频、碎片化和即时反馈特征可能会改变大学生的时间分配、注意力维持方式和学习投入水平。

秦浩轩、李霞、曾美红等学者在《大学生短视频成瘾量表的初步编制》一文中对大学生短视频成瘾的测量问题进行了探讨。该研究将短视频成瘾划分为戒断性、逃避性、失控性和低效性等维度，为后续研究判断大学生是否存在短视频成瘾倾向提供了工具基础。对于本研究而言，这篇文献可以用于界定“短视频使用”与“短视频成瘾”之间的差异，避免把一般使用行为直接等同于问题性使用行为。

王小凤、李思婷、索秀娟、李宸吉、王玥怡等学者在《大学生短视频使用特点及对主观幸福感的影响研究》一文中关注了大学生短视频使用、自我控制和主观幸福感之间的关系。该研究提示，短视频使用强度较高时，可能会削弱个体自我控制水平，并进一步影响主观幸福感。虽然该文并不直接讨论学习专注度，但自我控制与注意力维持、学习计划执行密切相关，因此可以作为分析短视频使用影响学习状态的心理机制文献。

Ye、Wu、Wu、Chen和Ye等学者在《Effects of Short Video Addiction on the Motivation and Well-Being of Chinese Vocational College Students》一文中，从心流体验和生态系统视角分析了短视频成瘾对中国职业院校学生学习动机与学习幸福感的影响。该研究认为，短视频成瘾会削弱学生的内在学习动机和外在学习动机，并通过学习动机进一步影响学习幸福感。对于本科毕业论文而言，这篇文献可以支撑“短视频过度使用不仅影响娱乐时间，还可能影响学习动机和学习心理状态”的论点。

Zhang、Hazarika、Chen和Shi等学者在《A cross-national study on the excessive use of short-video applications among college students》一文中，从跨文化视角讨论了大学生短视频应用过度使用的形成机制。该研究将短视频过度使用与使用动机、社交互动、补偿性期待和抑制控制等因素联系起来，说明短视频过度使用并不是单纯的时间管理问题，也与个体需求和平台使用情境有关。该文可以放在文献综述的理论背景部分，用于解释为什么大学生群体容易出现短视频过度使用。

Ye、He、Yang、Lee、Nong、Ye和Wang等学者在《Predicting the Learning Avoidance Motivation, Learning Commitment, and Silent Classroom Behavior of Chinese Vocational College Students Caused by Short Video Addiction》一文中进一步把短视频成瘾与学习行为联系起来。该研究发现，短视频成瘾与学习回避动机呈正向关系，与学习投入呈负向关系，并可能进一步影响课堂沉默行为。该文对本研究具有较高相关性，因为它把短视频成瘾从一般心理健康问题推进到具体学习行为问题，为分析学习专注度下降提供了学习投入和课堂行为层面的依据。

Xie、Xu、Zhang、Tan、Wu、Shi和Huang等学者在《The effect of short-form video addiction on undergraduates' academic procrastination: a moderated mediation model》一文中直接讨论了短视频成瘾、注意力控制和学业拖延之间的关系。该研究指出，短视频成瘾不仅可能直接影响学业拖延，还可能通过注意力控制产生间接影响。这篇文献与“学习专注度”关系最为接近，因为注意力控制是学习专注的重要心理基础，学业拖延也常常表现为无法持续投入学习任务。

Li、Geng和Wu等学者在《Effects of short-form video app addiction on academic anxiety and academic engagement: The mediating role of mindfulness》一文中分析了短视频应用成瘾对学业焦虑和学业投入的影响。该研究认为，短视频应用成瘾会增加学业焦虑、降低学业投入，并且正念在其中具有中介作用。该文可以帮助解释短视频使用影响学习专注度的另一条路径：短视频成瘾可能通过降低个体当下觉察和调节能力，使学生更难稳定投入学习过程。

王兴超、田芳芳学者在《大学生短视频成瘾与学业成绩的关系——学习投入的中介作用和学业自我效能感的调节作用》一文中，以大学生为研究对象，讨论了短视频成瘾与学业成绩之间的关系。该研究指出，短视频成瘾负向预测学业成绩，学习投入在二者之间起部分中介作用，学业自我效能感对学习投入与学业成绩之间的关系具有调节作用。该文可以作为本研究的重要支撑，因为它把短视频成瘾、学习投入和学业结果联系起来，说明短视频使用对学习的影响可能并不只体现在短期注意力分散上，也可能通过学习投入持续下降影响学业表现。

综合上述候选文献可以看出，关于大学生短视频使用与学习状态的研究已经形成了若干相互关联的线索。第一，短视频成瘾已有一定的测量基础，研究者可以从失控、逃避、戒断和低效等维度识别问题性使用。第二，短视频使用对大学生的影响并不局限于娱乐时间占用，还可能通过自我控制、学习动机、正念和注意力控制等心理机制影响学习过程。第三，学习投入、学业拖延、课堂沉默和学业成绩等变量为观察学习专注度提供了可操作的结果指标。对于“大学生短视频使用对学习专注度的影响”这一选题，后续研究可以在既有文献基础上，进一步区分一般短视频使用与成瘾性使用，并重点考察注意力控制、自我控制和学习投入在其中的作用机制。

## 第 7 步：文献覆盖简表

| 文献 | 是否写入综述 | 正文位置 | 核验状态 |
| --- | --- | --- | --- |
| 秦浩轩等（2019）《大学生短视频成瘾量表的初步编制》 | 是 | 第 2 段 | 待核验 |
| 王小凤等（2022）《大学生短视频使用特点及对主观幸福感的影响研究》 | 是 | 第 3 段 | 待核验 |
| Ye等（2022）《Effects of Short Video Addiction on the Motivation and Well-Being of Chinese Vocational College Students》 | 是 | 第 4 段 | 待核验 |
| Zhang等（2023）《A cross-national study on the excessive use of short-video applications among college students》 | 是 | 第 5 段 | 待核验 |
| Ye等（2023）《Predicting the Learning Avoidance Motivation, Learning Commitment, and Silent Classroom Behavior...》 | 是 | 第 6 段 | 待核验 |
| Xie等（2023）《The effect of short-form video addiction on undergraduates' academic procrastination...》 | 是 | 第 7 段 | 待核验 |
| Li等（2024）《Effects of short-form video app addiction on academic anxiety and academic engagement...》 | 是 | 第 8 段 | 待核验 |
| 王兴超、田芳芳（2025）《大学生短视频成瘾与学业成绩的关系——学习投入的中介作用和学业自我效能感的调节作用》 | 是 | 第 9 段 | 待核验 |

## 第 8 步：正式使用前的核验清单

- 回到 CNKI、万方、维普、学校图书馆、期刊官网或 DOI 页面核对题录。
- 下载原文或至少阅读正式摘要，不要只依赖搜索结果页。
- 核对中文文献是否有页码、卷期、期号和 DOI。
- 英文文献按学校要求转换为 GB/T 7714 或 APA 等引用格式。
- 如果某篇文献无法核验全文或正式题录，只能作为检索线索，不应进入正式参考文献。
- 综述正文中的“提出、指出、认为”必须与原文摘要、结论或正文一致。

## 这个案例适合怎么推广

对外分享时，可以直接使用这句话：

> 这个案例演示了：用户一篇文献都没有时，如何先从题目拆关键词，找到 8 篇真实可追溯的公开候选文献，再生成一版待核验文献综述。重点不是代写，而是把“找文献 → 核验 → 生成综述”的流程固定下来。
