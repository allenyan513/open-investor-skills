# Non-GAAP 调整项解读与陷阱识别

---

## 什么是 Non-GAAP？

GAAP（Generally Accepted Accounting Principles）是美国通用会计准则，所有上市公司必须遵守。

Non-GAAP（也叫 Adjusted 或 Pro Forma）是公司在 GAAP 基础上剔除某些项目后的"自定义"利润，**不受 SEC 强制要求**，但公司自愿披露并认为更能反映"核心业务表现"。

---

## 常见调整项及合理性判断

### ✅ 通常合理的调整（加回）

| 调整项 | 英文 | 合理性 | 说明 |
|--------|------|--------|------|
| 股权激励费用 | Stock-based Compensation (SBC) | 有争议但普遍接受 | 非现金支出，但确实是真实成本 |
| 收购相关无形资产摊销 | Amortization of acquired intangibles | 合理 | 会计准则要求，与实际经营无关 |
| 重组费用 | Restructuring charges | 看频率 | 一次性裁员/关厂成本 |
| 并购交易费用 | M&A transaction costs | 合理 | 一次性法律/顾问费 |
| 资产减值 | Impairment charges | 合理 | 非现金，一次性 |

### ⚠️ 需要警惕的调整

| 调整项 | 警示信号 |
|--------|---------|
| **SBC 金额巨大（>10% 营收）** | 实质上在大量稀释股东。科技公司 SBC 通常 5-15%，超过要注意 |
| **重组费用连续多年出现** | 如果每年都有"一次性"重组费用，就不是一次性了 |
| **"Legal settlements"被加回** | 若频繁出现，说明业务有系统性法律风险 |
| **Revenue-related adjustments** | 公司调整收入确认方式，非常罕见但最危险 |
| **Adjusted EBITDA 与 FCF 差距极大** | EBITDA 好看但 FCF 很差，说明大量现金被吸走（CapEx、营运资本）|

---

## 最重要的非GAAP指标详解

### Adjusted EBITDA
```
EBITDA = 净利润 + 所得税 + 利息 + 折旧 + 摊销
Adjusted EBITDA = EBITDA + 其他调整项（SBC、重组等）

用途：衡量运营盈利能力，排除资本结构和会计政策影响
常用于：债务/EBITDA 杠杆比率计算
```

### Non-GAAP Operating Income / EPS
```
通常 = GAAP 基础上加回 SBC + 收购摊销 + 重组费用

判断：Non-GAAP EPS - GAAP EPS 的差距有多大？
  差距 < 20%：调整合理
  差距 > 50%：要仔细审查调整项
```

### Rule of 40（SaaS 专用）
```
Rule of 40 = 营收增速(%) + FCF Margin(%)

> 40 = 优秀
20-40 = 良好
< 20 = 需关注

注意：一定要用 FCF Margin 而不是 Adjusted EBITDA Margin
```

---

## 快速检验公式

**Non-GAAP 可信度测试**：

```
① SBC / 营收 < 15%？（否则稀释严重）
② 调整项同比变化不大？（否则在移动目标）
③ Non-GAAP 净利润 ≈ FCF？（最终要落地为现金）
④ GAAP 净利润趋势与 Non-GAAP 方向一致？
   （如果 Non-GAAP 上升但 GAAP 持续恶化，要警惕）
```

---

## 实战举例

**案例：某 SaaS 公司**
```
GAAP Net Income:       -$50M（亏损）
调整：
  + SBC:              +$80M
  + 摊销:             +$20M
  + 重组:             +$10M
Non-GAAP Net Income:   +$60M（盈利）

分析：
- 差距高达 $110M
- SBC $80M 占营收比需计算
- 如果营收 $500M，SBC = 16%，偏高
- 需关注股权稀释速度：股数每年增加多少？
```

---

## 关键原则

1. **Non-GAAP 不是谎言**，是公司提供的补充视角
2. **FCF 才是最终检验**：再漂亮的 Non-GAAP 都要对应真实现金流
3. **横向比较要统一口径**：对比两家公司时确保用同一个指标定义
4. **看趋势比看绝对值更重要**：调整项的绝对金额不如它占营收的比率趋势有价值
