# GitHub Actions Secrets（mosesdai/keel）

> **填写位置**：https://github.com/mosesdai/keel → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**  
> **原则**：只在本文件列**名称与说明**；**值永远不要**提交进 git 或粘贴到 Cursor 聊天。

---

## 现在就要填（S0 / Bridge Track）

| Secret 名称 | 说明 |
|-------------|------|
| `KEEL_API_KEY` | Bridge API 鉴权（`X-API-Key`）；须与 Railway Variables 及九叔快捷指令里的一致 |
| `DEEPSEEK_API_KEY` | DeepSeek 模型调用；上线前建议轮换新 key |
| `RAILWAY_TOKEN` | （可选）供 `deploy-server.yml` 用 Railway CLI 部署；若只用 **Railway Dashboard → Deploy from GitHub**，可不填，workflow 会 skip deploy 并打 notice |
| `DASHSCOPE_API_KEY` | （可选）Qwen / DashScope 备选路由 |

### Repository variable（非 Secret）

| 名称 | 说明 |
|------|------|
| `KEEL_STAGING_URL` | 部署后的 API 根 URL，例如 `https://xxx.up.railway.app`（**无**尾斜杠）；供 `deploy-server.yml` 可选 `/health` 检查 |

---

## 如何从本地复制 `KEEL_API_KEY`（不暴露完整 key）

1. 在终端打开本地 env（勿把输出贴到聊天）：

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a/server"
grep '^KEEL_API_KEY=' .env
```

2. 复制 **等号后面**整段字符串（无引号则整行后半部分）。
3. 在 GitHub Actions **New repository secret** 中：Name = `KEEL_API_KEY`，Secret = 粘贴该值。
4. 同样在 **Railway** → Project → **Variables** 添加同名 `KEEL_API_KEY`。

`DEEPSEEK_API_KEY`：在 `track-a/server/.env` 中同样用 `grep '^DEEPSEEK_API_KEY=' .env` 查看行，**只复制到 GitHub/Railway UI**，不要发给 agent，不要 commit。

DeepSeek 新 key 生成见 `track-a/deploy/DEEPSEEK_SETUP.md`。

---

## 获取 `RAILWAY_TOKEN`（若走 Actions 部署）

1. 登录 https://railway.app  
2. 右上角头像 → **Account Settings**（或 **Settings**）  
3. 找到 **Tokens** / **Create Token**（名称如 `keel-github-actions`）  
4. 复制 token **一次**，粘贴到 GitHub Secret `RAILWAY_TOKEN`

**更省事的路径（推荐 Moses 7/15 前）**：Railway 项目用 **Deploy from GitHub** 连 `mosesdai/keel`，Root Directory = `track-a`，在 Railway 填 Variables；`main` push 由 Railway 自动部署，可不配置 `RAILWAY_TOKEN`。

---

## 日后阶段（勿提前填）

| Secret | 阶段 |
|--------|------|
| `IOS_DIST_CERT_BASE64`、`IOS_DIST_CERT_PASSWORD`、`IOS_ADHOC_PROFILE_BASE64`、`KEYCHAIN_PASSWORD` | S2 Ad Hoc（约 7/16 后） |
| `APP_STORE_CONNECT_API_KEY_ID`、`APP_STORE_CONNECT_ISSUER_ID`、`APP_STORE_CONNECT_PRIVATE_KEY`、`MATCH_PASSWORD` | S3 TestFlight（约 7/25 前） |
| `FLY_API_TOKEN` | 仅当选用 Fly.io 备选部署 |

---

## 安全自检（push 前/填 secret 后）

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git status --short
git check-ignore -v track-a/server/.env
```

不得将 `.env`、`.venv`、证书、profile 纳入 commit。
