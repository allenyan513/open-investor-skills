---
name: daily-close-report
description: >
  每日收盘投研复盘报告。读取持仓 CSV，通过 yfinance 获取收盘价格，
  计算当日和总体盈亏，结合市场表现、情绪指标和新闻，生成收盘报告并发送到 Telegram。
  当用户说"收盘报告"、"日报"、"今天收盘情况"、"today's recap"时触发。
  也可由 cron 在每个交易日 16:30 EST 自动触发。
---

# 每日收盘报告 Skill

> 目标：复盘当日表现，记录关键变化，为明日做准备。

---

## 执行步骤

### Step 1：获取市场收盘数据

```bash
cd {项目根目录} && python3 .claude/skills/daily-open-report/scripts/fetch_market_data.py close
```

解析输出的 JSON，提取：
- `holdings[]`：每只持仓的收盘价、当日涨跌幅、总收益率、市值、未实现盈亏
- `indices{}`：SPY / QQQ / DIA 当日涨跌
- `sentiment{}`：VIX / 黄金 / 国债 / 美元

计算组合层面汇总：
- 组合总市值 = sum(market_value)
- 组合当日盈亏 = sum(change * shares)（需用 change × shares 估算）
- 组合总未实现盈亏 = sum(unrealized_pnl)

---

### Step 2：搜索今日市场表现

```
US stock market today recap {date}
S&P 500 today performance sectors {date}
```

提取：
- 今日市场整体涨跌驱动因素（1-2 句话）
- 领涨/领跌板块

---

### Step 3：搜索持仓当日新闻

对每只持仓，若 `change_pct` 绝对值 > 2%，搜索：

```
{TICKER} stock news today {date}
{TICKER} earnings analyst rating today
```

提取当日重要新闻/事件。无显著异动（< 2%）跳过，标注"—"。

---

### Step 4：搜索明日事件预告

```
earnings report tomorrow {next_date}
US economic calendar tomorrow {next_date}
```

提取：
- 明日有财报的持仓公司（重点关注）
- 明日重要经济数据

---

### Step 5：生成报告

按以下模板生成报告（中文）：

```
════════════════════════════════════
  📉 收盘日报 {YYYY-MM-DD} 16:30 EST
════════════════════════════════════

【大盘表现】
  SPY  {+/-X.XX%}  |  QQQ  {+/-X.XX%}  |  DIA  {+/-X.XX%}
  VIX {value} ({+/-X%})  |  黄金 {+/-X%}  |  国债 {+/-X%}
  → [一句话今日市场定性：反弹 / 下跌 / 震荡 + 驱动因素]
  → 领涨板块：{XX}  | 领跌板块：{XX}

【持仓今日表现】
  涨跌幅从高到低排列：

  {TICKER}  ${price}  今日{+/-X.XX%}  总收益{+/-X%}  [📰异动原因 或 —]
  ...

  ──────────────────────────────
  组合今日估算盈亏：{+/-$X,XXX}
  组合总未实现盈亏：{+/-$X,XXX}
  组合总市值（估算）：${XXX,XXX}

【今日亮点 / 警示】
  📗 表现最佳：{TICKER} {+X.XX%} — {原因或"—"}
  📕 表现最差：{TICKER} {-X.XX%} — {原因或"—"}
  ⚠️ 需关注：{有异动或触及风险点的持仓，简述原因}
  （若无需特别关注：今日各持仓无重大异常）

【明日关注】
  📋 财报：{持仓公司 + 预计时间，或"无持仓公司财报"}
  📊 经济数据：{事件名 + 时间，或"无重大数据"}
  🔍 重点观察：{需要明日重点跟踪的仓位或事件}

【今日小结】
  [2-3 句话：今日组合相对大盘表现如何，有无持仓逻辑需要重新审视，明日操作基调]

════════════════════════════════════
⚠️ 仅供参考，不构成投资建议
```

---

### Step 6：保存

**保存文件**：
```bash
mkdir -p {项目根目录}/outputs/daily
```
文件名：`close_report_{YYYYMMDD}.md`
路径：`{项目根目录}/outputs/daily/`

---

## 与其他 Skill 的衔接

```
持仓有重大新闻事件  → news-sentiment-analyzer（深度解读）
持仓跌幅较大       → weekly-portfolio-review（复核买入逻辑）
明日有财报         → earnings-report-decoder（提前准备）
持仓触及技术关键位  → technical-analysis-primer（技术面研判）
```
