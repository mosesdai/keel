# 部署状态（Staging / Production）

> Moses 关机前在 [`MOSES_BEFORE_SHUTDOWN.md`](../../MOSES_BEFORE_SHUTDOWN.md) 步骤 4 填写；agent 可更新「最后验证」等字段。**勿在此写 API key。**

| 字段 | 值 |
|------|-----|
| **Staging URL** | `https://keel-production-be1c.up.railway.app`（Port 8080，Railway 反代） |
| **Railway 项目** | keel-production（Moses 部署） |
| **Root Directory** | `track-a` |
| **最后 `/health` 检查** | **2026-07-10 07:01 JST** — **ok** HTTP 200，`status":"ok"`；`api_key_configured":false`（服务端未读到 `KEEL_API_KEY`） |
| **最后 `/v1/entry` 检查** | **2026-07-10 07:01 JST** — **fail** HTTP 503，`服务端未配置 KEEL_API_KEY`（Railway Variables 需补 `KEEL_API_KEY` 并 Redeploy） |
| **KEEL_STAGING_URL（GitHub Variable）** | **待填** → 应填 `https://keel-production-be1c.up.railway.app`（**无尾斜杠**，非 `/v1/entry`） |
| **备注** | Railway GitHub 集成完成后，`main` push 触发自动部署；九叔快捷指令 POST URL 见 `track-a/shortcuts/KEEL_URL.txt` |

