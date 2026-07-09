# 部署状态（Staging / Production）

> Moses 关机前在 [`MOSES_BEFORE_SHUTDOWN.md`](../../MOSES_BEFORE_SHUTDOWN.md) 步骤 4 填写；agent 可更新「最后验证」等字段。**勿在此写 API key。**

| 字段 | 值 |
|------|-----|
| **Staging URL** | `https://keel-production-be1c.up.railway.app`（`/health`：[链接](https://keel-production-be1c.up.railway.app/health)） |
| **Railway 项目** | keel-production（Moses 部署） |
| **Root Directory** | `track-a` |
| **最后 `/health` 检查** | **2026-07-10 07:15 JST** — **ok** HTTP **200**，`"status":"ok"`，**`"api_key_configured":true`** |
| **最后 `/v1/entry` 检查** | **2026-07-10 07:15 JST** — **ok** HTTP **200**（有效 `X-API-Key`）；无效 Key → **401**。Smoke 回复曾含「本地兜底」→ 建议确认 Railway **`DEEPSEEK_API_KEY`** 有效 |
| **KEEL_STAGING_URL（GitHub Variable）** | **待填** → `https://keel-production-be1c.up.railway.app`（**无尾斜杠**） |
| **备注** | 九叔 POST URL：[`../shortcuts/KEEL_URL.txt`](../shortcuts/KEEL_URL.txt)；变量：[`../server/RAILWAY_VARIABLES_傻瓜版.md`](../server/RAILWAY_VARIABLES_傻瓜版.md) |

### curl 验收命令（不含 key）

```bash
# Health
curl -sS "https://keel-production-be1c.up.railway.app/health"

# Entry（需替换 YOUR_KEEL_API_KEY）
curl -sS -X POST "https://keel-production-be1c.up.railway.app/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEEL_API_KEY" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"smoke test","advice_intensity":3}'
```

**Moses 可选下一步**：确认 Railway `DEEPSEEK_API_KEY` → Redeploy → entry 回复应为真实 DeepSeek 而非 mock。
