# Railway 部署手把手（Track A 军师 Server）

预计 **5–10 分钟**。本机已安装 `@railway/cli`；Agent 环境无法替你完成浏览器登录，请按下面步骤在 **Moses 的 Mac** 上操作。

---

## 前置

- 代码目录：`track-a/`（已含 `railway.toml`、`server/Dockerfile`）
- 本地 `.env` 在 `server/.env`（**勿提交 Git**）；密钥只在 Railway Dashboard 粘贴，不要写进任何文档或 commit
- 你需要：`KEEL_API_KEY`（可与本地一致）、`DEEPSEEK_API_KEY`（从 DeepSeek 控制台复制）、`DEFAULT_PROVIDER=deepseek`

---

## 路径 A：Railway CLI 从本机部署（推荐，无需先 push GitHub）

### 1. 注册 / 登录 Railway

1. 打开 [https://railway.app](https://railway.app) 用 GitHub 或邮箱注册
2. 终端执行：

```bash
railway login
```

浏览器会打开授权页，点 **Authorize** 即可。

### 2. 进入项目目录并关联服务

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a"
railway init
```

- 选 **Create new project**，名称例如 `keel-track-a`
- 若已有项目：`railway link` 选对应 Project

### 3. 确认构建根目录

Railway 会以 **当前目录**（`track-a/`）为根，自动读：

- `railway.toml` → Docker 构建 `server/Dockerfile`
- 健康检查：`GET /health`

若在 Dashboard 从 GitHub 部署，请在 **Service → Settings → Root Directory** 填：`track-a`（仓库根在上一级时）。

### 4. 配置环境变量（Dashboard 或 CLI）

**Dashboard**：Project → 你的 Service → **Variables** → **New Variable**

| 变量名 | 说明 |
|--------|------|
| `KEEL_API_KEY` | 与快捷指令 `X-API-Key` 一致（例：`114c173b44a498e621b8c807e2d320d2`） |
| `DEEPSEEK_API_KEY` | 在 Dashboard 粘贴 DeepSeek 密钥，**勿写入文档** |
| `DEFAULT_PROVIDER` | `deepseek` |

可选：`DEEPSEEK_MODEL_DEFAULT=deepseek-chat`、`DEEPSEEK_MODEL_DEEP=deepseek-reasoner`

**CLI 示例**（DeepSeek 密钥请在本机终端粘贴，不要提交到 shell 历史共享处）：

```bash
railway variables set KEEL_API_KEY="114c173b44a498e621b8c807e2d320d2"
railway variables set DEFAULT_PROVIDER=deepseek
# DEEPSEEK_API_KEY 建议在 Dashboard 粘贴，或：
# railway variables set DEEPSEEK_API_KEY="你的密钥"
```

### 5. 部署

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a"
railway up
```

等待构建完成（Docker 约 2–5 分钟）。在 **Settings → Networking → Generate Domain** 生成公网域名，形如：

`https://keel-track-a-production-xxxx.up.railway.app`

记下 **不含路径** 的域名，下文称 `YOUR_RAILWAY_URL`。

### 6. 用 curl 验证

健康检查：

```bash
curl -sS "https://YOUR_RAILWAY_URL/health"
```

业务接口（把 `YOUR_RAILWAY_URL` 和 `KEEL_API_KEY` 换成你的）：

```bash
curl -sS "https://YOUR_RAILWAY_URL/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEEL_API_KEY" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"部署后首测：请给我一条稳妥+一条disruptive建议"}'
```

应返回 JSON，含 `reply` 等字段。

### 7. 填进 iPhone 快捷指令

打开 `shortcuts/SETUP.md`：

- `{{KEEL_API_URL}}` → `https://YOUR_RAILWAY_URL/v1/entry`（**必须带** `/v1/entry`）
- `{{KEEL_API_KEY}}` → 与 Railway 里 `KEEL_API_KEY` 相同

然后按 `JIUSHU_ONBOARDING.md` 在九叔 iPhone 上安装并首测。

---

## 路径 B：Deploy from GitHub（备选）

1. 将 `track-a/` 所在仓库 push 到 GitHub（确保 `.env` 在 `.gitignore` 内）
2. Railway → **New Project** → **Deploy from GitHub repo** → 选仓库
3. **Root Directory** = `track-a`
4. Variables 同路径 A 第 4 步
5. Deploy 后 **Generate Domain**，验证同第 6 步

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 502 / 部署失败 | 看 **Deployments → View Logs**；确认 `PORT` 由 Railway 注入（Dockerfile 已用 `${PORT:-8787}`） |
| 401 Unauthorized | `X-API-Key` 与 `KEEL_API_KEY` 不一致 |
| 模型报错 | 检查 `DEEPSEEK_API_KEY`、`DEFAULT_PROVIDER=deepseek` |
| CLI `Unauthorized` | 重新 `railway login` |

---

## 部署成功后（可选）

在 `deploy/DEPLOYMENT_STATUS.md` 记录公网 URL 与部署日期（**不要写 API 密钥**），并勾选 `MOSES_CHECKLIST.md` 第 4、7 项。
