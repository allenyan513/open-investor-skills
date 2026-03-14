# SEC EDGAR 导航与文件下载手册

---

## EDGAR 是什么？

SEC EDGAR（Electronic Data Gathering, Analysis, and Retrieval）是美国证券交易委员会的官方财报数据库。所有在美上市公司必须在此提交原始文件，**免费公开、数据权威、无广告**。

主入口：https://www.sec.gov/cgi-bin/browse-edgar

---

## 如何找到一家公司的所有文件

### 方法一：直接搜索（最简单）
```
URL 公式：
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[股票代码]&type=10-K&dateb=&owner=include&count=10

把 [股票代码] 替换成 AAPL、MSFT、NVDA 等

或者直接 Google：
[TICKER] 10-K SEC EDGAR
```

### 方法二：EDGAR 全文搜索
```
https://efts.sec.gov/LATEST/search-index?q="公司名"&dateRange=custom&startdt=2024-01-01
```

---

## 各文件类型的直接获取方式

### 10-K（年报）
```
最新年报：
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K&dateb=&owner=include&count=5

通常在财年结束后 60-90 天内提交
苹果举例：
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AAPL&type=10-K
```

### 10-Q（季报）
```
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-Q&dateb=&owner=include&count=10

通常在季度结束后 40 天内提交（大公司）或 45 天（小公司）
```

### 8-K（重大事项）
```
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=8-K&dateb=&owner=include&count=20

财报季期间每天都有，设置 RSS 可及时追踪
```

### DEF 14A（代理委托声明，含高管薪酬）
```
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=DEF+14A

查看 CEO/CFO 薪酬、股权激励计划、董事会构成
```

---

## 打开文件后的导航技巧

EDGAR 文件通常是 HTML 或 XBRL 格式，打开后：

**快速跳转章节**：
- 用浏览器 Ctrl+F 搜索章节标题
- 搜索 "Item 7" 直接跳到 MD&A
- 搜索 "CONSOLIDATED STATEMENTS" 直接找到三张报表

**关键数字定位**：
```
搜索关键词           找到什么
──────────          ──────
"net revenue"       营收汇总表
"gross profit"      毛利润行
"free cash flow"    自由现金流（公司自算）
"stock repurchase"  回购信息
"guidance"          指引（不总是在财报里）
"risk factors"      风险章节开头
"material weakness" 🚨 内控重大缺陷
"going concern"     🚨 持续经营疑虑
```

---

## 更友好的第三方工具

EDGAR 原始文件格式较旧，以下工具提供更好的阅读体验：

| 工具 | 用途 | 费用 |
|------|------|------|
| **Macrotrends.net** | 历史财务数据图表化 | 免费 |
| **Wisesheets / Koyfin** | 财务数据提取 | 部分免费 |
| **Seeking Alpha** | 财报摘要 + 电话会议文字 | 有免费额度 |
| **SEC 官方 XBRL Viewer** | 结构化数据展示 | 免费 |

**原则**：分析用第三方工具辅助，但**核实关键数字永远回到 EDGAR 原始文件**。

---

## 财报发布时间规律

| 公司规模 | 10-K 截止 | 10-Q 截止 |
|---------|----------|----------|
| 大型加速申报人（市值 >$700M）| 财年末后 60 天 | 季末后 40 天 |
| 加速申报人（市值 $75M-$700M）| 财年末后 75 天 | 季末后 40 天 |
| 非加速申报人（小公司）| 财年末后 90 天 | 季末后 45 天 |

大多数科技巨头（AAPL、MSFT、GOOGL）财年末在 9 月-12 月，10-K 通常在次年 1-2 月发布。

---

## RSS 订阅（自动追踪特定公司文件）

```
任意公司的最新 SEC 文件 RSS：
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=&dateb=&owner=include&count=40&search_text=&action=getcompany

加入 RSS 阅读器，新文件提交时自动通知
```
