---
name: daily-open-report
description: >
  每日开盘前投研简报。读取持仓 CSV，通过 yfinance 获取盘前价格和期货数据，
  结合网络搜索获取宏观事件和持仓新闻，生成开盘报告并发送到 Telegram。
  当用户说"开盘报告"、"早报"、"morning brief"、"今天开盘情况"时触发。
  也可由 cron 在每个交易日 09:15 EST 自动触发。
---

# 每日开盘报告 Skill

> 目标：在开盘前 15 分钟，给出今日交易方向的全景判断。

---

## 执行步骤

### Step 1：获取市场数据

```bash
cd {项目根目录} && python3 .claude/skills/daily-open-report/scripts/fetch_market_data.py open
```

解析输出的 JSON，提取：
- `holdings[]`：每只持仓的盘前价格、当日涨跌幅、总收益率
- `futures{}`：ES=F / NQ=F / YM=F 期货涨跌
- `indices{}`：SPY / QQQ / DIA 昨收
- `sentiment{}`：VIX / 黄金 / 国债 / 美元

若脚本执行失败，输出 `❌ 数据获取失败：{错误信息}`，终止流程。

---

### Step 2：搜索今日宏观事件

搜索以下内容（用 WebSearch）：

```
today economic calendar US market {date}
Fed speech today {date}
US economic data release today {date}
```

提取：
- 今日重要经济数据（CPI、非农、PMI、GDP、就业数据等）
- Fed 官员讲话安排
- 重大政策/地缘事件

---

### Step 3：搜索持仓盘前异动

对每只持仓，若 `change_pct` 绝对值 > 1.5%，搜索：

```
{TICKER} premarket news today
{TICKER} stock news {date}
```

提取异动原因（财报/分析师评级/行业事件等）。

无显著异动（< 1.5%）的持仓跳过搜索，统一标注"无异动"。

---

### Step 4：生成报告

按以下模板生成报告（中文）：

```
════════════════════════════════════
  📊 开盘简报 {YYYY-MM-DD} 09:15 EST
════════════════════════════════════

【期货预判】
  S&P 500 期货  {price}  {+/-X.XX%}
  Nasdaq 期货   {price}  {+/-X.XX%}
  Dow 期货      {price}  {+/-X.XX%}
  → 综合判断：[偏多 / 偏空 / 中性]

【市场情绪】
  VIX {value}  （{↑恐慌升温 / ↓情绪平稳 / 持平}）
  黄金 {+/-X%}  | 国债(TLT) {+/-X%}  | 美元 {+/-X%}
  → [一句话情绪解读]

【今日宏观事件】
  {时间} {事件名}（重要度：🔴高 / 🟡中 / ⚪低）
  {时间} {事件名}
  （若无重要事件：今日无重大宏观事件，关注盘中消息面）

【持仓盘前概况】
  涨跌幅从高到低排列：

  {TICKER}  ${price}  {+/-X.XX%}  总收益 {+/-X%}  {⚠️异动原因 或 —}
  ...

  今日需关注：
  ⚠️ {有异动的 TICKER}：{原因简述}
  （无异动则写：各持仓盘前平稳，无重大异动）

【今日交易提示】
  [2-3 句话：结合期货+宏观+持仓异动，给出今日操作基调]
  例："期货偏弱，VIX 升温，建议今日谨慎，重点关注 XX 的开盘走势"

════════════════════════════════════
⚠️ 仅供参考，不构成投资建议
```

---

### Step 5：保存

**保存文件**：
```bash
mkdir -p {项目根目录}/outputs/daily
```
文件名：`open_report_{YYYYMMDD}.md`
路径：`{项目根目录}/outputs/daily/`

---

## 与其他 Skill 的衔接

```
持仓有重大盘前新闻 → news-sentiment-analyzer（深度解读）
持仓触及技术关键位 → technical-analysis-primer（技术面判断）
今日有财报公布     → earnings-report-decoder（财报解读）
```
