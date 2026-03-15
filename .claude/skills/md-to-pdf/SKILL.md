---
name: md-to-pdf
description: >
  将指定的 Markdown 文件转换为美观的 PDF。
  当用户说 "/md-to-pdf"、"转成 PDF"、"导出 PDF"、"生成 PDF" 时触发。
  用户可以指定文件路径，不指定时默认转换当前对话中最近提到的 .md 文件。
  依赖本地安装的 pandoc + wkhtmltopdf（或 Chrome headless）。
---

# MD → PDF 美化转换 Skill

## 执行流程

### Step 1：确定输入文件

按以下优先级确定要转换的文件：

1. 用户在命令中直接指定了路径 → 使用该路径
2. 当前对话中最近读取或生成的 `.md` 文件 → 使用该文件
3. 以上都没有 → 询问用户："请告诉我要转换哪个 .md 文件的路径"

读取该 MD 文件内容，观察其结构（标题层级、是否有表格、是否有代码块、是否含中文）。

### Step 2：检查依赖

```bash
pandoc --version
```

若命令不存在，输出：
```
❌ 未检测到 pandoc，请先安装：
   brew install pandoc        # macOS
   sudo apt install pandoc    # Ubuntu/Debian
```
然后终止。

检测可用 PDF 引擎（按优先级）：
```bash
which wkhtmltopdf
which google-chrome || which chromium || which "Google Chrome"
```

### Step 3：确定输出路径

- 目录：与输入文件**相同目录**
- 文件名：与输入文件**相同文件名**，扩展名改为 `.pdf`
- 临时 HTML 文件：同目录，文件名加 `_styled` 后缀，扩展名 `.html`

示例：
```
输入：outputs/PORTFOLIO/portfolio_review_20260314.md
临时：outputs/PORTFOLIO/portfolio_review_20260314_styled.html
输出：outputs/PORTFOLIO/portfolio_review_20260314.pdf
```

### Step 4：写入 CSS 样式文件

在输入文件**同目录**创建 `_report_style.css`，内容如下（直接用 Write 工具写入，不要用 bash echo）：

```css
/* ===== 全局基础 ===== */
*, *::before, *::after { box-sizing: border-box; }

body {
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
               "Helvetica Neue", Arial, sans-serif;
  font-size: 13px;
  line-height: 1.75;
  color: #1a1a2e;
  background: #ffffff;
  margin: 0;
  padding: 28px 36px;
  max-width: 860px;
  margin: 0 auto;
}

/* ===== 标题系统 ===== */
h1 {
  font-size: 22px;
  font-weight: 700;
  color: #0f3460;
  border-bottom: 3px solid #0f3460;
  padding-bottom: 8px;
  margin: 0 0 20px 0;
  letter-spacing: 0.02em;
}

h2 {
  font-size: 16px;
  font-weight: 600;
  color: #16213e;
  border-left: 4px solid #e94560;
  padding-left: 10px;
  margin: 28px 0 12px 0;
}

h3 {
  font-size: 14px;
  font-weight: 600;
  color: #0f3460;
  margin: 20px 0 8px 0;
}

h4 { font-size: 13px; font-weight: 600; color: #533483; margin: 16px 0 6px 0; }

/* ===== 段落与文字 ===== */
p { margin: 0 0 10px 0; }

strong { color: #0f3460; font-weight: 700; }

em { color: #533483; }

a { color: #0f7abf; text-decoration: none; }

/* ===== 分隔线 ===== */
hr {
  border: none;
  border-top: 1px solid #e0e6f0;
  margin: 20px 0;
}

/* ===== 表格 ===== */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0 18px 0;
  font-size: 12.5px;
}

thead tr {
  background: #0f3460;
  color: #ffffff;
}

thead th {
  padding: 8px 12px;
  text-align: left;
  font-weight: 600;
  letter-spacing: 0.03em;
}

tbody tr:nth-child(even) { background: #f4f7fc; }
tbody tr:nth-child(odd)  { background: #ffffff; }
tbody tr:hover           { background: #eaf0fb; }

tbody td {
  padding: 7px 12px;
  border-bottom: 1px solid #e0e6f0;
  vertical-align: middle;
}

/* ===== 引用块 ===== */
blockquote {
  background: #f0f4ff;
  border-left: 4px solid #0f7abf;
  margin: 12px 0;
  padding: 10px 16px;
  border-radius: 0 6px 6px 0;
  color: #2a3f6f;
  font-size: 12.5px;
}

blockquote p { margin: 0; }

/* ===== 代码块 ===== */
pre {
  background: #1e1e2e;
  color: #cdd6f4;
  padding: 14px 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 12px;
  line-height: 1.6;
  margin: 12px 0;
}

code {
  font-family: "JetBrains Mono", "Fira Code", "Source Code Pro", monospace;
  font-size: 12px;
}

p > code, li > code {
  background: #eef2ff;
  color: #e94560;
  padding: 1px 5px;
  border-radius: 3px;
}

/* ===== 列表 ===== */
ul, ol {
  padding-left: 1.6em;
  margin: 8px 0 12px 0;
}

li { margin-bottom: 4px; }

/* ===== emoji 与特殊符号对齐 ===== */
.emoji { font-style: normal; }

/* ===== 页面打印设置 ===== */
@media print {
  body { padding: 0; }
  h2   { page-break-after: avoid; }
  table, blockquote { page-break-inside: avoid; }
}
```

### Step 5：生成带样式的 HTML

```bash
pandoc "{输入文件路径}" \
  --standalone \
  --embed-resources \
  --css "{CSS文件路径}" \
  --metadata title="" \
  --from markdown+smart \
  -o "{临时HTML文件路径}"
```

若 pandoc 版本较旧不支持 `--embed-resources`，改用 `--self-contained`：

```bash
pandoc "{输入文件路径}" \
  --standalone \
  --self-contained \
  --css "{CSS文件路径}" \
  --metadata title="" \
  --from markdown+smart \
  -o "{临时HTML文件路径}"
```

### Step 6：将 HTML 转换为 PDF

按可用引擎依次尝试：

**方案 A — wkhtmltopdf（推荐，最稳定）**
```bash
wkhtmltopdf \
  --page-size A4 \
  --margin-top 18mm \
  --margin-bottom 18mm \
  --margin-left 16mm \
  --margin-right 16mm \
  --encoding utf-8 \
  --enable-local-file-access \
  --print-media-type \
  "{临时HTML文件路径}" \
  "{输出PDF文件路径}"
```

**方案 B — Chrome headless（备选）**

检测 Chrome 路径（按顺序）：
- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- `google-chrome`
- `chromium`

```bash
"{chrome路径}" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="{输出PDF文件路径}" \
  --print-to-pdf-no-header \
  "file://{临时HTML文件的绝对路径}"
```

**方案 C — pandoc + xelatex（最后回退，中文排版）**
```bash
pandoc "{输入文件路径}" \
  -o "{输出PDF文件路径}" \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V CJKmainfont="PingFang SC" \
  -V mainfont="PingFang SC" \
  -V fontsize=11pt \
  -V linestretch=1.6
```

### Step 7：清理临时文件并报告

删除临时 HTML 文件和 CSS 文件：
```bash
rm -f "{临时HTML文件路径}" "{CSS文件路径}"
```

转换成功后输出：
```
✅ PDF 已生成：{输出PDF文件路径}
   引擎：{使用的引擎名称}
```

若所有引擎均失败，保留临时 HTML 文件（供用户手动打印），并输出：
```
⚠️  PDF 引擎不可用，已保留样式化 HTML：{临时HTML文件路径}
   可在浏览器中打开后手动「打印 → 存储为PDF」
```

---

## 依赖说明

| 工具 | 用途 | 安装命令 |
|------|------|---------|
| `pandoc` | Markdown → HTML 转换 | `brew install pandoc` |
| `wkhtmltopdf` | HTML → PDF（推荐） | `brew install wkhtmltopdf` |
| `Google Chrome` | HTML → PDF（备选） | 通常已安装 |
| `xelatex` | 纯 LaTeX 方案（回退） | `brew install --cask mactex-no-gui` |

> 推荐组合：`pandoc` + `wkhtmltopdf`，中英文均支持，CSS 样式完整呈现。
