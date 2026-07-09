# Track A 部署手册（Railway 主路径 + Fly.io 备选）

目标：部署后只剩 3 件人工动作：Moses 填 key、点部署、把 URL/API Key 填进快捷指令。

---

## 0. 环境变量清单（两平台通用）

必填：

- `KEEL_API_KEY`：你自定义的一串随机字符串（快捷指令用 `X-API-Key` 带上）
- `DEEPSEEK_API_KEY` 或 `DASHSCOPE_API_KEY`：至少填一个

可选：

- `DEEPSEEK_MODEL_DEFAULT=deepseek-chat`
- `DEEPSEEK_MODEL_DEEP=deepseek-reasoner`（仅 `/max` 或深度模式使用）
- `QWEN_MODEL_DEFAULT=qwen-plus`
- `QWEN_MODEL_MAX=qwen-max`
- `DEEP_TOPIC_SLUGS=deep,strategic,重大`

---

## 1) Railway（主路径，推荐）

### 步骤 1：创建项目

1. 登录 Railway，新建 Project
2. 连接本仓库
3. Railway 会读取 `track-a/railway.toml` 和 `track-a/server/Dockerfile`

### 步骤 2：设置 Root Directory

在服务设置里把 Root Directory 设为：

`track-a`

### 步骤 3：填写环境变量

在 Variables 里填写上面的必填项（至少 3 个）：

- `KEEL_API_KEY`
- `DEEPSEEK_API_KEY`（或 `DASHSCOPE_API_KEY`）

### 步骤 4：部署并拿 URL

1. 点击 Deploy
2. 成功后获得公网 URL，例如：`https://xxx.up.railway.app`
3. 快捷指令里把 `{{KEEL_API_URL}}` 替换为：
   - `https://xxx.up.railway.app/v1/entry`

### 步骤 5：在线验证

```bash
curl -sS "{{KEEL_API_URL}}" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: {{KEEL_API_KEY}}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"部署后首测：请给我一条稳妥+一条disruptive建议"}'
```

---

## 2) Fly.io（备选路径）

> 用于 Railway 不稳定或希望长期固定域名时。

### 步骤 1：初始化（在 `track-a/` 下）

```bash
cd "track-a"
fly auth login
fly launch --no-deploy
```

建议配置：

- Build context：`track-a`
- Dockerfile：`server/Dockerfile`
- Internal port：`8787`

### 步骤 2：写 secrets

```bash
fly secrets set KEEL_API_KEY="你的随机key"
fly secrets set DEEPSEEK_API_KEY="你的deepseek-key"
# 或 fly secrets set DASHSCOPE_API_KEY="你的qwen-key"
```

### 步骤 3：部署

```bash
fly deploy
```

部署完成后获得 URL：

- `https://<your-app>.fly.dev/v1/entry`

### 步骤 4：在线验证

```bash
curl -sS "https://<your-app>.fly.dev/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: {{KEEL_API_KEY}}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"Fly 部署验证"}'
```

---

## 3) 健康检查

- `GET /health`（建议平台 health check）
- `GET /healthz`（兼容旧脚本）

示例：

```bash
curl -sS "https://<your-domain>/health"
```
