# 三张核心报表逐行解读指南

---

## 一、损益表（Income Statement / P&L）

损益表回答：**公司这一期赚了多少钱？**

```
Revenue（营收/总收入）
  └─ 减：Cost of Revenue / COGS（营业成本）
        = Gross Profit（毛利润）
            毛利率 = 毛利润 / 营收

  └─ 减：Operating Expenses（运营费用）
        ├─ R&D（研发费用）          ← 科技公司重点关注
        ├─ Sales & Marketing（销售费用）← 获客成本是否可控
        └─ G&A（行政管理费用）       ← 通常相对固定

        = Operating Income（营业利润）
            营业利润率 = 营业利润 / 营收

  └─ 加减：Other Income/Expense
        ├─ Interest Expense（利息支出）← 负债成本
        ├─ Interest Income（利息收入）
        └─ Other（汇率损益等）

        = Pre-tax Income（税前利润）

  └─ 减：Income Tax Expense（所得税）
        有效税率 = 所得税 / 税前利润（美国通常 18-25%）

        = Net Income（净利润）

  └─ 除：Diluted Shares Outstanding（摊薄股数）
        = Diluted EPS（摊薄每股收益）← 最关注的数字
```

### 损益表关键观察点

**1. 收入质量**
- 营收构成：产品收入 vs 服务收入（服务通常更高毛利、更稳定）
- 有无一次性大额收入（剥离业务、授权费等）
- 延递收入（Deferred Revenue）增长 = 预收款增加 = 未来收入可见性高 ✅

**2. 费用趋势**
- 费用率（费用/营收）是否在下降 = 规模效应显现
- R&D 占比过低可能透支未来增长
- SG&A 突然大增需查原因

**3. GAAP vs Non-GAAP**
公司通常同时披露两个口径：

| 项目 | GAAP | Non-GAAP（Adjusted）|
|------|------|---------------------|
| 含义 | 遵循会计准则的真实数字 | 剔除"非现金/一次性"项目 |
| 常见调整 | 股权激励、摊销、重组费用 | 被加回去 |
| 使用建议 | 看盈利质量用 GAAP | 看经营能力用 Non-GAAP |

> ⚠️ Non-GAAP 不是陷阱，但要检查调整项是否合理。
> 详见 `references/non-gaap-guide.md`

---

## 二、现金流量表（Cash Flow Statement）

现金流量表回答：**公司实际收到/付出了多少真金白银？**

> 这是比损益表更难造假的报表。巴菲特优先看现金流。

```
Operating Activities（经营活动现金流）
  净利润
  + 折旧与摊销（非现金支出，加回）
  + 股权激励费用（非现金，加回）
  ± 营运资本变化：
      应收账款变化（增加 = 占用现金，减分）
      库存变化（增加 = 占用现金，减分）
      应付账款变化（增加 = 占用供应商资金，加分）
      预收账款变化（增加 = 提前收款，加分）
  = 经营活动现金流（CFO）← 核心数字

Investing Activities（投资活动现金流）
  - 资本支出 CapEx（购买设备/厂房/服务器）
  ± 并购/出售业务
  ± 购买/出售证券投资
  = 投资活动现金流（通常为负，是正常投入）

Financing Activities（融资活动现金流）
  ± 发债/还债
  ± 发行/回购股票
  - 支付股息
  = 融资活动现金流

自由现金流（FCF）= CFO - CapEx  ← 最重要的自算指标
```

### 现金流关键观察点

**黄金法则：CFO 应该 > 净利润（长期）**

| CFO vs 净利润 | 含义 |
|-------------|------|
| CFO >> 净利润 | 利润质量极高，现金转化超强 ✅ |
| CFO ≈ 净利润 | 正常健康 ✅ |
| CFO < 净利润 | 应收账款堆积？警惕 ⚠️ |
| CFO << 净利润 | 可能存在收入确认问题 🚨 |
| CFO 持续为负 | 烧钱模式，需判断是否正常（早期公司 vs 成熟公司）|

**CapEx 性质判断**
- Maintenance CapEx（维持性支出）：维持现有业务运转，是"必须"支出
- Growth CapEx（扩张性支出）：为了未来增长，是"主动"投入
- 区分方法：看公司披露，或对比折旧额（CapEx << 折旧 = 收缩投资）

**回购 vs 股息**
- 大规模回购 + 股价合理 = 管理层认为股票被低估 ✅
- 回购同时股权稀释（股票数未减少）= 在用左手抵右手，无效回购 ⚠️

---

## 三、资产负债表（Balance Sheet）

资产负债表回答：**公司现在的家底如何？**
公式：资产 = 负债 + 股东权益

```
ASSETS（资产）
  Current Assets（流动资产）
    Cash & Equivalents（现金及等价物）← 最关注
    Short-term Investments（短期投资）
    Accounts Receivable（应收账款）
    Inventory（库存）← 制造/零售重点
    Prepaid Expenses（预付费用）
  ─────────────────────────────────
  Total Current Assets

  Non-current Assets（非流动资产）
    PP&E（厂房、设备、土地）← CapEx 累积
    Goodwill（商誉）← 并购溢价，需重点关注
    Intangible Assets（无形资产/专利）
    Long-term Investments
  ─────────────────────────────────
  TOTAL ASSETS

LIABILITIES（负债）
  Current Liabilities（流动负债）
    Accounts Payable（应付账款）
    Deferred Revenue（延递收入）← 增长是好事
    Short-term Debt（一年内到期债务）← 流动性风险
    Accrued Expenses（应计费用）
  ─────────────────────────────────
  Total Current Liabilities

  Long-term Liabilities（长期负债）
    Long-term Debt（长期借款/债券）
    Deferred Tax Liabilities
    Operating Lease Obligations（经营性租约）
  ─────────────────────────────────
  TOTAL LIABILITIES

SHAREHOLDERS' EQUITY（股东权益）
  Common Stock + APIC（普通股 + 资本公积）
  Retained Earnings（留存收益）← 累积盈利
  Treasury Stock（库藏股）← 回购累积，负值
  AOCI（其他综合收益）
  ─────────────────────────────────
  TOTAL EQUITY
```

### 资产负债表关键比率

**流动性**
```
流动比率 = 流动资产 / 流动负债（>1.5 安全）
速动比率 = (流动资产 - 库存) / 流动负债（>1 安全）
现金比率 = (现金 + 短期投资) / 流动负债（越高越安全）
```

**资本结构**
```
净现金（债）= 现金及等价物 + 短期投资 - 总债务
  净现金为正 = 现金多于债务，财务灵活 ✅
  净债务较高 = 需关注偿债能力和利息支出

债务/EBITDA = 总债务 / EBITDA（<2x 健康）
```

**商誉风险**
```
商誉/总资产 > 30% → 需关注
风险：若收购的业务表现不及预期，会发生"商誉减值"
商誉减值 = 一次性大额亏损冲击利润表
```

**股东权益**
```
股东权益为负 → 不一定是坏事（大量回购导致），但需判断原因
  正常情况：大量回购 + 持续盈利（如 AAPL）
  危险情况：长期亏损侵蚀 + 高负债
```

---

## 三张报表的联动关系

```
损益表                    现金流量表               资产负债表
────────                 ──────────              ────────────
净利润 ──────────────→  净利润（起点）
                         + 非现金调整
                         ± 营运资本变化
                         = CFO
                               │
                               ↓
                         投资活动（CapEx 等）  →  PP&E 变化
                               │
                               ↓
                         融资活动（回购/债务） →  债务/权益变化
                                                      │
                         期末现金 ─────────────────→  Cash 余额
                                                      │
净利润 ─────────────────────────────────────────→  留存收益累积
```

理解这个联动，就能发现报表之间的不一致（造假往往就藏在这里）。
