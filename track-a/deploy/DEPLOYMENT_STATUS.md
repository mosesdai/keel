# 部署状态（Staging / Production）

> Moses 关机前在 [`MOSES_BEFORE_SHUTDOWN.md`](../../MOSES_BEFORE_SHUTDOWN.md) 步骤 4 填写；agent 可更新「最后验证」等字段。**勿在此写 API key。**

| 字段 | 值 |
|------|-----|
| **Staging URL** | `https://keel-production-be1c.up.railway.app`（`/health`：[链接](https://keel-production-be1c.up.railway.app/health)） |
| **Railway 项目** | keel-production（Moses 部署） |
| **Root Directory** | `track-a` |
| **最后 `/health` 检查** | **2026-07-10 07:03 JST** — **ok** HTTP 200，`"status":"ok"`；**`"api_key_configured":false`**（Railway 未注入 `KEEL_API_KEY`） |
| **最后 `/v1/entry` 检查** | **2026-07-10 07:03 JST** — **fail** HTTP 503（无 `KEEL_API_KEY` 时连无头 POST 也 503；补 key + Redeploy 后期望 401/200） |
| **KEEL_STAGING_URL（GitHub Variable）** | **待填** → `https://keel-production-be1c.up.railway.app`（**无尾斜杠**） |
| **备注** | 补 Variables 步骤：[`track-a/server/RAILWAY_VARIABLES_傻瓜版.md`](../server/RAILWAY_VARIABLES_傻瓜版.md)；九叔 POST URL：`track-a/shortcuts/KEEL_URL.txt` |

**Moses 下一步**：Railway Variables 添加 `KEEL_API_KEY`、`DEEPSEEK_API_KEY`、`DEEPSEEK_MODEL_DEFAULT` → **Redeploy** → `/health` 应出现 `api_key_configured: true`。
