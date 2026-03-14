---
name: earnings-report-decoder
description: >
  解读美股财报文件，包括 10-K（年报）、10-Q（季报）、8-K（重大事项）、
  以及财报电话会议记录（Earnings Call Transcript）。
  当用户说"帮我读这份财报"、"10-K 怎么看"、"这个季度业绩好不好"、
  "财报发布了帮我解读一下"、"earnings 出来了分析一下"时立即触发。
  用户上传 PDF 或粘贴财报内容时也应触发。
  输出结构化的财报解读笔记，让新手也能快速抓住核心信息。
---

# 财报快速解读 Skill

> ⚠️ 本 Skill 为财报理解辅助工具，不构成投资建议。
> 财务数据请以 SEC EDGAR 官方文件为准。

---

## 第一步：识别文件类型

拿到财报后，先判断是哪种文件，然后跳转到对应的解读流程：

| 文件类型 | 频率 | 核心用途 | 跳转章节 |
|---------|------|---------|---------|
| **10-K** | 年度 | 完整年度经营情况 | → 见「10-K 解读流程」 |
| **10-Q** | 季度（Q1/Q2/Q3）| 季度经营更新 | → 见「10-Q 解读流程」 |
| **8-K** | 不定期 | 重大事项公告 | → 见「8-K 解读流程」 |
| **Earnings Call** | 随财报 | 管理层解读 + 分析师问答 | → 见「电话会议解读流程」 |

如果用户只说"最新财报"，先用 web_search 确认：
```
[TICKER] latest 10-K 10-Q SEC filing 2024
[TICKER] earnings call transcript latest quarter
```

---

## 10-K 解读流程（年报）

10-K 通常 100-300 页，不需要全读。按以下优先级精准定位。

### 必读章节地图

```
10-K 文件结构
│
├── Part I
│   ├── Item 1   Business          ★★★ 必读：理解业务模式
│   ├── Item 1A  Risk Factors      ★★  必读：公司自己承认的风险
│   ├── Item 1B  Unresolved Comments（通常跳过）
│   └── Item 2   Properties（通常跳过）
│
├── Part II
│   ├── Item 5   Market Info / Stockholder Matters  ★ 看回购/股息政策
│   ├── Item 6   Selected Financial Data（跳过，看 Item 8）
│   ├── Item 7   MD&A                ★★★ 必读：管理层自己的解释
│   ├── Item 7A  Quantitative Disclosures（高级用户）
│   └── Item 8   Financial Statements ★★★ 必读：三张核心报表
│
└── Part III / IV
    ├── Item 10-13  董事、薪酬、关联交易  ★ 扫一眼
    └── Item 15     Exhibits（合同、子公司列表）
```

### Item 1 — Business（业务描述）
**目标**：提炼公司的商业模式，3 分钟内完成。

重点提取：
- [ ] 公司如何描述自己的竞争优势（原文用词很重要）
- [ ] 收入来源有哪几条线？哪条最大？
- [ ] 客户集中度：前 N 大客户占比多少？（高集中=高风险）
- [ ] 有无提到"subscription"、"recurring"、"renewal rate"（预示收入质量）
- [ ] 员工人数变化（扩张 or 收缩的信号）

### Item 1A — Risk Factors（风险因素）
**目标**：找到公司自己最担心的 3 件事。

技巧：
- 全文搜索"may"、"could"、"might"密度最高的段落
- 新增风险因素（对比上年）是市场最关注的信号
- 顺序有含义：通常越靠前的风险越被管理层重视
- 读完后问：**这些风险有没有在过去一年内实际发生？**

### Item 7 — MD&A（管理层讨论与分析）
**这是整份 10-K 最重要的章节。** 管理层在这里用自己的语言解释数字。

重点阅读顺序：

**① 收入增长归因**
```
寻找管理层对营收变化的解释，格式通常是：
"Revenue increased $X million, primarily due to [原因]，
 partially offset by [反向因素]"

提取：
- 增长主要来自：有机增长 / 并购 / 汇率？
- 哪个业务线贡献最大？哪个在拖累？
- 有无一次性收入（剔除后真实增速是多少）
```

**② 利润率变化解释**
```
寻找 gross margin、operating margin 的变化解释：
- 毛利率下降：是因为产品结构变化？原材料涨价？促销加大？
- 费用率变化：销售费用/研发费用/管理费用各自的趋势
- 有无提到"operating leverage"（规模效应，是好事）
```

**③ 流动性与资本资源（Liquidity）**
```
关键数字：
- 现金及等价物余额
- 可用信贷额度（Revolving Credit Facility）
- 未来 12 个月到期债务
- 自由现金流（Operating CF - CapEx）
- 管理层对现金消耗的说明
```

**④ 前瞻性陈述（Forward-looking Statements）**
```
寻找 Guidance 或 Outlook 段落：
- 下一年/季度的营收、利润指引
- 对比分析师共识：是否超预期？
- 注意管理层是否主动下调预期（非常关键）
```

### Item 8 — Financial Statements（三张报表）

**详细解读见** `references/three-statements.md`

快速扫描检查清单（5 分钟内完成）：

**损益表（Income Statement）**
- [ ] 营收 YoY 增速：____%
- [ ] 毛利率：____% （vs 上年 ____%）
- [ ] 营业利润率：____% （vs 上年 ____%）
- [ ] EPS（摊薄）：$____ （vs 上年 $____）
- [ ] 有无大额一次性费用/收益（重组费用、资产减值等）

**现金流量表（Cash Flow Statement）**
- [ ] 经营活动现金流：$____ （正数才是真赚钱）
- [ ] 资本支出 CapEx：$____
- [ ] 自由现金流 = 经营CF - CapEx：$____
- [ ] FCF vs 净利润对比（差距大需警惕）

**资产负债表（Balance Sheet）**
- [ ] 现金余额：$____
- [ ] 总债务：$____
- [ ] 净现金（债）= 现金 - 总债务：$____
- [ ] 商誉 Goodwill 占总资产比：____% （>30% 需注意）
- [ ] 股东权益是否为正

---

## 10-Q 解读流程（季报）

10-Q 比 10-K 精简，重点关注变化而非全貌。

**核心问题**：这个季度相比上个季度/去年同期，发生了什么变化？

### 季报 5 分钟速读框架

**Step 1：看数字结果（2 分钟）**
```
对比三个维度：
① vs 上季度（环比 QoQ）
② vs 去年同季度（同比 YoY）
③ vs 分析师预期（Beat / Miss / In-line）

核心指标：
- 营收：$____ （预期 $____，超/低 ____%）
- EPS：$____ （预期 $____，超/低 ____%）
- 毛利率：____% （预期 ____%）
- 公司下季度指引：营收 $____，EPS $____
```

**Step 2：找 MD&A 中的变化解释（2 分钟）**
```
重点寻找：
- 为什么超预期/低预期？
- 有没有新的风险或机遇被提及？
- 管理层语气是否比上季度更乐观/谨慎？
```

**Step 3：看现金流和负债变化（1 分钟）**
```
- 现金余额有没有大幅减少？
- 有没有新增债务或回购？
- 库存变化（大幅增加 = 可能销售放缓）
```

### 季报红旗清单 🚨
触发以下任意一条，需要深入研究原因：

- [ ] 营收 Miss 超过 3%
- [ ] 下季度指引低于分析师预期（Guidance cut）
- [ ] 毛利率连续两季度下滑
- [ ] 经营现金流为负但净利润为正
- [ ] 管理层下调全年指引
- [ ] CFO 或 CEO 突然离职（8-K 公告）
- [ ] 审计师发出"持续经营"疑虑

---

## 8-K 解读流程（重大事项公告）

8-K 是公司发生重大事件时必须在 4 个工作日内提交的报告。

### 常见 8-K 类型及解读重点

| Item 编号 | 事件类型 | 关注要点 |
|----------|---------|---------|
| Item 1.01 | 重大合同签署 | 合同金额、期限、对方是谁 |
| Item 1.02 | 重大合同终止 | 损失多少收入？原因？ |
| Item 1.03 | 破产/接管 | 🚨 极端风险 |
| Item 2.01 | 重大资产收购/出售 | 收购价格合理吗？协同效应？ |
| Item 2.02 | **季度/年度业绩公告** | ★ 最常见，就是 Earnings Release |
| Item 2.05 | 大规模裁员 | 规模多大？是降本还是业务萎缩？ |
| Item 2.06 | 资产减值 | 减值多少？哪部分资产？ |
| Item 3.01 | 退市警告 | 🚨 危险信号 |
| Item 5.02 | **高管变动** | ★ CEO/CFO 离职原因很重要 |
| Item 5.03 | 章程修改 | 注意反收购条款 |
| Item 7.01 | 自愿披露信息 | 可能是提前发布的好/坏消息 |
| Item 8.01 | 其他重大事项 | 需具体判断 |

### Item 2.02 Earnings Release 速读（最常用）

这是财报季最核心的 8-K，通常包含：
1. 新闻稿正文（Highlights）
2. 财务报表摘要
3. 下季度/全年指引

**60 秒判断法**：
```
① 标题数字：营收和EPS是否超预期？
② Guidance：下季度指引 vs 市场预期
③ 管理层引语：CEO 第一句话是"strong"还是"challenging"？
④ 非GAAP调整：剔除了哪些费用？金额大吗？
```

---

## 电话会议（Earnings Call）解读流程

电话会议分两部分：管理层陈述 + 分析师问答。**问答环节往往比陈述更有价值。**

### 管理层陈述（Prepared Remarks）

重点捕捉：
- [ ] 业务亮点：管理层主动强调了什么？
- [ ] 刻意回避了什么？（对比上季度没再提的指标）
- [ ] 新战略或新产品的具体细节
- [ ] 对宏观环境的判断

### 分析师问答（Q&A）

**这是金矿。** 分析师的问题通常针对市场最担心的点。

重点听：
```
1. 分析师重复问同一个问题 → 管理层在回避什么
2. 管理层的回答是否具体 → 模糊回答通常不是好消息
3. 指引措辞变化：
   "confident" → "cautiously optimistic" → "uncertain"
   这种措辞降级是重要信号
4. 分析师问题的语气：是挑战性的还是恭维性的？
```

**搜索电话会议记录**：
```
[TICKER] earnings call transcript Q[X] [年份] site:seekingalpha.com
[TICKER] Q[X] [年份] earnings call transcript
```

### 电话会议关键词速查

| 正面信号 ✅ | 负面信号 🚨 |
|-----------|-----------|
| "record revenue / bookings" | "headwinds", "challenging environment" |
| "expanding margins" | "margin pressure", "investment phase" |
| "strong pipeline" | "elongated sales cycles" |
| "increasing guidance" | "lowering / withdrawing guidance" |
| "share buyback" | "preserving cash / liquidity" |
| "new customer wins" | "customer churn", "downgrades" |
| "operating leverage" | "cost optimization program"（=裁员）|

---

## 数据获取快速通道

```
SEC EDGAR 官方原始文件（最权威）：
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K

财报摘要和分析师预期对比：
搜索：[TICKER] earnings results vs estimates [季度]

电话会议文字记录：
搜索：[TICKER] earnings call transcript [季度年份]

财报日历（提前知道发布时间）：
搜索：[TICKER] earnings date next quarter
```

---

## 最终输出模板

```
════════════════════════════════════
  [公司]（[代码]）财报解读笔记
  文件类型：[10-K / 10-Q Q_/ 8-K]
  财报期间：[覆盖时间段]
  解读日期：[今天日期]
════════════════════════════════════

【一句话总结】
[用一句话说明这份财报的核心结论，好/差/符合预期]

【关键数字对比】
                本期        上期       预期(若有)   同比变化
营收           $____       $____       $____        ±____%
毛利率          ____%       ____%       ____%        ±____pp
EPS(摊薄)      $____       $____       $____        ±____%
自由现金流      $____       $____         -          ±____%

【亮点 ✅】
1. ...
2. ...
3. ...

【隐患 / 红旗 ⚠️】
1. ...
2. ...

【管理层指引】
下季度营收：$____ - $____ （市场预期 $____，[超/符合/低于]预期）
下季度EPS ：$____ - $____
全年指引变化：[维持/上调/下调]

【值得深挖的问题】
（读完财报后仍未解答的疑问，可带入下一步研究）
1. ...
2. ...

【与上期报告对比】
[本次财报相比上季度/上年，最大的变化是什么]

【数据来源】
- [SEC EDGAR 链接]
- [财报发布日期]
════════════════════════════════════
⚠️ 以上为财报解读辅助，不构成投资建议
如需完整个股分析，请使用 stock-fundamental-research Skill
```

---

## 参考文件索引

- `references/three-statements.md` — 三张报表逐行解读指南
- `references/non-gaap-guide.md` — Non-GAAP 调整项解读与陷阱识别
- `references/sec-edgar-howto.md` — SEC EDGAR 导航与文件下载手册
