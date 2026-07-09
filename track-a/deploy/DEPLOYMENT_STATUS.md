# 部署状态（Staging / Production）

> Moses 关机前在 [`MOSES_BEFORE_SHUTDOWN.md`](../../MOSES_BEFORE_SHUTDOWN.md) 步骤 4 填写；agent 可更新「最后验证」等字段。**勿在此写 API key。**

| 字段 | 值 |
|------|-----|
| **Staging URL** | _（待填，例 `https://xxx.up.railway.app`）_ |
| **Railway 项目** | _（可选，项目名）_ |
| **Root Directory** | `track-a` |
| **最后 `/health` 检查** | _（日期 + ok/fail，由 agent 或 Moses 填）_ |
| **KEEL_STAGING_URL（GitHub Variable）** | _（已填 / 未填）_ |
| **备注** | Railway GitHub 集成完成后，`main` push 触发自动部署 |

