# Railway Variables 傻瓜版（补 Key 让 `/v1/entry` 可用）

> **适用场景**：浏览器打开 `https://keel-production-be1c.up.railway.app/health` 看到 `"status":"ok"`，但 **`"api_key_configured":false`**。  
> **预计时间**：约 3 分钟（填变量 + Redeploy）。  
> **勿把 key 写进本仓库、勿贴到聊天。**

---

## 这说明什么？

| 字段 | 含义 |
|------|------|
| `status: ok` | 容器在跑，域名可达，**部署成功**。 |
| `api_key_configured: false` | 进程里**没有**读到环境变量 **`KEEL_API_KEY`**（或值为空）。此时 `POST /v1/entry` 会 **503**，提示「服务端未配置 KEEL_API_KEY」。 |

代码依据（`app.py` 的 `/health`）：`api_key_configured` = 是否设置了非空的 **`KEEL_API_KEY`**。  
`/v1/entry` 还需要 **`DEEPSEEK_API_KEY`** 才能调 DeepSeek 生成回复（变量名与 `track-a/server/.env.example`、`track-a/deploy/DEPLOY.md` 一致）。

---

## 逐步操作

### 1. 打开 Railway 项目

1. 浏览器打开 **https://railway.app** 并登录  
2. 进入项目 **keel-production**（或你部署 Keel 的那个项目）  
3. 点进 **跑 API 的那个 Service**（不是数据库）

### 2. 打开 Variables 页

1. 顶部或左侧点 **Variables**（环境变量）  
2. 确认列表里**还没有**下面三个名字，或值为空——需要新增/补全

### 3. 添加 3 个变量（名字必须一字不差）

点 **+ New Variable**（或 **Add Variable**），逐个添加：

| 变量名 | 值从哪来 | 说明 |
|--------|----------|------|
| **`KEEL_API_KEY`** | 与本地 **`track-a/server/.env`** 里同一串；或与 GitHub → Settings → Secrets → **`KEEL_API_KEY`** 相同 | 九叔快捷指令请求头 **`X-API-Key`** 必须与此一致 |
| **`DEEPSEEK_API_KEY`** | 与本地 `.env` 相同；或 [DeepSeek 开放平台](https://platform.deepseek.com/) 的 API Key（`sk-…`） | 服务端调用模型用；勿 commit |
| **`DEEPSEEK_MODEL_DEFAULT`** | 填 **`deepseek-chat`**（与 `.env.example` 默认一致） | 日常 entry 用的便宜模型；不填时代码也会默认 `deepseek-chat`，但建议在 Railway 显式写上 |

可选（一般不用改）：`DEEPSEEK_MODEL_DEEP=deepseek-reasoner`（仅 `/max` 或深度模式）。

**不要**在变量名里加空格；**不要**把 key 写进 markdown 或 push 到 Git。

### 4. 保存后必须 Redeploy

仅保存 Variables **不会**让正在跑的旧容器立刻读到新值。

1. 打开 **Deployments**  
2. 点最新部署右侧 **⋯** → **Redeploy**（或 **Deploy** 重新部署）  
3. 等到状态 **Success / Active**（约 1–3 分钟）

### 5. 验收

浏览器或终端：

```bash
curl -sS "https://keel-production-be1c.up.railway.app/health"
```

**期望**：JSON 里 **`"api_key_configured":true`**（且仍为 `"status":"ok"`）。

再测业务（在本机终端，用你自己的 key，勿贴到聊天）：

```bash
export KEEL_STAGING_URL="https://keel-production-be1c.up.railway.app"
export KEEL_API_KEY="你的KEEL_API_KEY"

curl -sS "${KEEL_STAGING_URL}/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${KEEL_API_KEY}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"Railway 变量补全后首测","advice_intensity":3}'
```

**期望**：HTTP **200**，JSON 含非空 **`reply`**。

---

## 仍失败时

| 现象 | 处理 |
|------|------|
| 还是 `api_key_configured: false` | 检查变量名是否为 **`KEEL_API_KEY`**（不是 `API_KEY`）；Redeploy 是否完成 |
| 401 | `X-API-Key` 与 Railway 里 **`KEEL_API_KEY`** 不一致 |
| 500 + DeepSeek 相关 | 检查 **`DEEPSEEK_API_KEY`** 是否有效、是否 Redeploy |
| 503 未配置 key | 同上，确认 **`KEEL_API_KEY`** 已保存并 Redeploy |

更多验收步骤：[`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`](../deploy/RAILWAY_STAGING_CHECKLIST.md) · 部署总览：[`track-a/deploy/DEPLOYMENT_STATUS.md`](../deploy/DEPLOYMENT_STATUS.md)
