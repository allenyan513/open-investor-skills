# Open Investor Skills

> A collection of Claude Skills for US stock market analysis —
> from fundamental research to earnings decoding to real-time news sentiment.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Claude Skills](https://img.shields.io/badge/Claude-Skills-8B5CF6)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)

---

## What is this?

**open-investor-skills** is an open-source collection of [Claude Skills](https://docs.anthropic.com/en/docs/claude-code/skills) designed to make US stock market analysis faster, more structured, and more consistent.

Each Skill teaches Claude a professional analysis framework — so instead of asking Claude the same questions from scratch every time, you get a repeatable, high-quality workflow that triggers automatically.

> ⚠️ **Disclaimer**: All outputs are for educational and research purposes only.
> Nothing in this repository constitutes financial or investment advice.
> Always do your own due diligence before making any investment decisions.

---

## Skills Overview

| Skill | Trigger | Output |
|-------|---------|--------|
| [`stock-fundamental-research`](#-stock-fundamental-research) | "Analyze NVDA" / "Is AAPL worth buying?" | 4-step research report (Business + Financials + Valuation + Moat) |
| [`earnings-report-decoder`](#-earnings-report-decoder) | "Read this earnings report" / "How was Q3?" | Structured earnings notes (10-K / 10-Q / 8-K / Transcript) |
| [`news-sentiment-analyzer`](#-news-sentiment-analyzer) | "Is this news bullish or bearish?" | Sentiment scorecard (-3 to +3) + recommended action |
| [`technical-analysis-primer`](#-technical-analysis-primer) | "Is now a good entry?" / "Where's the support?" | Technical report (Trend + Levels + MA + Momentum) |
| [`weekly-portfolio-review`](#-weekly-portfolio-review) | "Review my portfolio" / "Should I still hold this?" | Structured review report (Hold / Trim / Exit) |

### How they work together

```
A news event arrives
      │
      ▼
news-sentiment-analyzer        ← Quick signal vs noise check. Score ≥ ±2?
      │
      ▼  (score triggers deeper research)
earnings-report-decoder        ← Read the raw filing, verify the numbers
      │
      ▼  (re-evaluate fundamentals)
stock-fundamental-research     ← Full valuation + moat analysis, decide on position
      │
      ▼  (entry timing)
technical-analysis-primer      ← Assess current price position, find entry zone
      │
      ▼  (ongoing management)
weekly-portfolio-review        ← Verify buy thesis still holds, manage position sizing
```

---

## Skills Detail

### 📊 stock-fundamental-research

Systematic fundamental research on any US stock across four dimensions:

| Step | Focus | Key Output |
|------|-------|------------|
| Step 1 | Business Snapshot | Business model, revenue mix, growth drivers |
| Step 2 | Financial Quality | Profitability, growth, balance sheet, red flags |
| Step 3 | Valuation | Relative valuation + DCF three-scenario range |
| Step 4 | Moat Assessment | Morningstar 5-source framework scoring |

**Auto output**: Research report `.md` + `.pdf`, with optional Gmail delivery.

**Reference files**:
- `references/financial-metrics.md` — Excellent / acceptable / warning thresholds for key metrics
- `references/valuation-methods.md` — Step-by-step DCF calculation guide
- `references/sector-benchmarks.md` — Valuation benchmarks for 10+ sectors

**Trigger examples**:
```
Analyze NVDA's fundamentals
Is AAPL's valuation reasonable right now?
Help me research MSFT — is it worth holding long term?
```

---

### 📋 earnings-report-decoder

Decode SEC filings across four formats: 10-K, 10-Q, 8-K, and earnings call transcripts.
**Core value**: tells you where to look, what to look for, and how to judge it.

| Filing Type | Analysis Framework |
|-------------|-------------------|
| 10-K Annual | Must-read section map → MD&A four key areas → 3-statement quick scan |
| 10-Q Quarterly | 5-minute framework: result vs estimate → variance explanation → cash flow |
| 8-K Material Event | 17 Item type quick-ref + 60-second triage method |
| Earnings Call | Management commentary highlights + Q&A signal identification |

**Auto output**: Earnings notes `.md` + `.pdf`, with optional Gmail delivery.

**Reference files**:
- `references/three-statements.md` — Line-by-line breakdown of all three statements + linkages
- `references/non-gaap-guide.md` — Identifying Non-GAAP adjustments and common traps
- `references/sec-edgar-howto.md` — SEC EDGAR navigation guide

**Trigger examples**:
```
NVDA's latest quarterly report is out — decode it for me
What does the MD&A section say in this 10-K? (upload PDF)
Did META beat estimates this quarter? What's the guidance?
```

---

### 📰 news-sentiment-analyzer

Quickly assess a news item's impact direction and duration. Outputs a standardized sentiment scorecard.

**7 News Frameworks**:

| Framework | Type | Core Logic |
|-----------|------|------------|
| A | Financial Results | Result vs estimate × guidance vs estimate × KPI trend |
| B | Business Events | M&A premium rationality / contract size / product TAM |
| C | Regulatory | 4-level severity scale (substantive impact vs sentiment shock) |
| D | Macro | Interest rate sensitivity × sector attribute mapping |
| E | Industry | Competitive landscape shift / supply chain propagation |
| F | Management | Sudden departure signal decoding / insider trading analysis |
| G | Market Sentiment | Analyst upgrades / short report credibility / meme risk |

**Sentiment score**: `-3` (strong bearish) to `+3` (strong bullish) — consistent scale for cross-time comparison.

**Auto output**: Sentiment report `.md` + `.pdf` (color-coded by score), with optional Gmail delivery.

**Reference files**:
- `references/sector-sensitivity.md` — Sector sensitivity matrix for different news types
- `references/historical-patterns.md` — Historical market reaction patterns for comparable events
- `references/source-credibility.md` — News source credibility tiers + tool recommendations

**Trigger examples**:
```
Adobe's CEO suddenly resigned — how should I read this?
Walk me through today's key market news, one by one
How much does rising Fed rate expectations affect my tech holdings?
```

---

### 📈 technical-analysis-primer

Read technical indicators to assess current price position and identify entry/exit zones.

**Five-Layer Analysis Framework**:

| Layer | Focus | Key Output |
|-------|-------|------------|
| Layer 1 | Trend | Primary/intermediate trend direction, trend strength |
| Layer 2 | Key Levels | Support and resistance (historical pivots / MAs / round numbers) |
| Layer 3 | Moving Averages | Bullish/bearish alignment, golden/death cross status |
| Layer 4 | Momentum | RSI overbought/oversold + MACD divergence signals |
| Layer 5 | Volume Confirmation | Price-volume relationship, valid breakout vs false breakout |

**Auto output**: Technical analysis report `.md`, saved to `output/[TICKER]/`.

**Reference files**:
- `references/candlestick-patterns.md` — 40+ candlestick patterns with annotations
- `references/indicator-settings.md` — Indicator parameter configs and use cases
- `references/ta-checklist.md` — Pre-buy / pre-sell technical checklist

**Trigger examples**:
```
Is now a good time to buy NVDA?
The MA just had a death cross — what should I do?
Is RSI overbought a sell signal?
Where's the support level for AAPL?
```

---

### 📋 weekly-portfolio-review

Periodic review of your holdings — verify that each stock's buy thesis still holds.

**Four-Question Framework**:

| Question | Core Check | Verdict |
|----------|-----------|---------|
| Does the buy thesis still hold? | Growth / valuation / catalyst / moat logic check | ✅ Hold / ⚠️ Trim & Watch / 🚨 Consider Exit |
| Are there new risks? | Company / valuation / macro risk scan | Low / Medium / High |
| Is the position size appropriate? | Single-name concentration limits + rebalance triggers | Maintain / Trim / Add |
| How does the risk/reward compare to entry? | Price change × thesis change 2×2 matrix | Improved / Unchanged / Deteriorated |

**Auto output**: Portfolio review report `.md`, saved to `output/`.

**Reference files**:
- `references/risk-checklist.md` — Comprehensive holding risk checklist
- `references/portfolio-health.md` — Portfolio health assessment framework
- `references/review-log.md` — Historical review log format (for tracking decision accuracy)

**Trigger examples**:
```
Review my portfolio for me
Should I still hold NVDA?
Check my positions — which ones should I sell?
(paste your holdings table)
```

---

## Installation

### 1. Install Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/open-investor-skills.git
```

### 3. Verify installation

```bash
claude
> /context    # check loaded Skills list
```

---

## Usage Examples

### Basic: trigger by chatting naturally

```bash
claude

# Fundamental research
> Help me research NVDA — is it worth buying now?

# Earnings decoding
> AAPL Q1 2026 earnings just dropped — decode it for me

# News analysis
> Adobe CEO just announced their resignation — how does this affect ADBE?

# Technical analysis
> What does NVDA's technical picture look like? Where's the support?

# Portfolio review
> Review my holdings: NVDA/AAPL/MSFT at 30%/40%/30%
```

---

## Output Structure

Each analysis automatically generates files in the `outputs/` directory

## License

MIT License — free to use, modify, and distribute.
See [LICENSE](LICENSE) for details.

---

## Acknowledgements

Built with [Claude](https://claude.ai) by Anthropic.
Investment frameworks inspired by Warren Buffett, Charlie Munger, and the Morningstar moat methodology.

> *"The stock market is a device for transferring money from the impatient to the patient."*
> — Warren Buffett
