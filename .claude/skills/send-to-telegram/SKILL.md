---
name: send-to-telegram
description: >
  通过 Telegram 将文件发送到手机。
  当用户说 "/send-to-telegram"、"发送文件到tg"、"发到手机"、"发给我" 时触发。
  用户可以指定文件路径，不指定时默认发送当前对话中最近提到的文件。
  依赖项目根目录 .env 中的 TELEGRAM_BOT_TOKEN 和 TELEGRAM_CHAT_ID。
---

# 发送文件到 Telegram

## 执行步骤

### Step 1：确定文件路径

1. 用户命令中指定了路径 → 使用该路径
2. 对话中最近生成/提到的文件 → 使用该文件
3. 都没有 → 询问用户

### Step 2：读取 .env 并发送

```bash
source .env && curl -s \
  -F document=@"<文件路径>" \
  "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument?chat_id=${TELEGRAM_CHAT_ID}"
```

若 `.env` 不存在或变量为空，提示：
```
❌ 请在项目根目录 .env 中添加：
   TELEGRAM_BOT_TOKEN=...
   TELEGRAM_CHAT_ID=...
```

### Step 3：输出结果

API 返回 `"ok":true` → `✅ 已发送：<文件名>`
否则输出错误描述。