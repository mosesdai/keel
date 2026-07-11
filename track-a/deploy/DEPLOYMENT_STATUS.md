# 部署状态（Staging / Production）

> Moses 关机前在 [`MOSES_BEFORE_SHUTDOWN.md`](../../MOSES_BEFORE_SHUTDOWN.md) 步骤 4 填写；agent 可更新「最后验证」等字段。**勿在此写 API key。**

| 字段 | 值 |
|------|-----|
| **Staging URL** | `https://keel-production-be1c.up.railway.app`（`/health`：[链接](https://keel-production-be1c.up.railway.app/health)） |
| **Railway 项目** | keel-production（Moses 部署） |
| **Root Directory** | `track-a` |
| **最后 `/health` 检查** | **2026-07-11 10:17 JST** — **ok** HTTP **200**，`deepseek_configured: true` |
| **最后 `/v1/entry` 检查** | **2026-07-11 10:17 JST** — **`used_mock: false`**，`deepseek:deepseek-chat`，两条 tencent-ali-renewal 验收回复结构完整（主见/反对/下一步） |
| **KEEL_STAGING_URL（GitHub Variable）** | **待填** → `https://keel-production-be1c.up.railway.app`（**无尾斜杠**） |
| **备注** | 九叔 POST URL：[`../shortcuts/KEEL_URL.txt`](../shortcuts/KEEL_URL.txt)；变量：[`../server/RAILWAY_VARIABLES_傻瓜版.md`](../server/RAILWAY_VARIABLES_傻瓜版.md) |

### 2026-07-11 大脑修复摘要

- `system.txt` 注入 PERSONALITY_CHARTER 核心（树洞/诤友/镜子、反昏君、disruptive、力谏档位）
- DeepSeek 端点改为 `https://api.deepseek.com/chat/completions`；失败时 `metadata.error` 含 HTTP 状态码，不再静默 mock
- 矛盾检测升级：关键词辅助 + 模型对照 `living_position` 解释转变（`tension_detected`）
- reply 放宽至 200~600 字结构化（主见/反对/disruptive/下一步）

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

**下一步**：九叔 iPhone 装机（[`JIUSHU_5MIN.md`](../shortcuts/JIUSHU_5MIN.md)）。
