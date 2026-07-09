# Track A 轻后端（FastAPI）

这个服务负责 7/15 前过渡闭环：

1. 接收快捷指令文本输入
2. 注入军师 system prompt + topic 活文档
3. 模型路由默认用便宜 `deepseek-chat`，仅在 `/max`、`depth: deep` 或 topic 深度模式时升到深度模型
4. 持久化到 `track-a/data/topics/<slug>/`（JSONL + Markdown）

---

## 本地启动（5 分钟）

```bash
cd "track-a/server"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

`.env` 必填：

- `KEEL_API_KEY=...`（快捷指令通过 `X-API-Key` 传入）
- `DEEPSEEK_API_KEY=...` 或 `DASHSCOPE_API_KEY=...`

启动：

```bash
uvicorn app:app --host 0.0.0.0 --port 8787 --reload
```

---

## 接口

- `GET /health`：健康检查（推荐平台探活）
- `GET /healthz`：兼容旧探活
- `POST /v1/entry`：写入一条输入并返回回复
- `GET /v1/topic/{slug}`：查看 topic 当前状态

> `/v1/*` 全部要求 `X-API-Key`，若未配置 `KEEL_API_KEY` 会返回 503。

---

## 话题 seed（启动自动创建）

- `tencent-ali-renewal`
- `lining-pitch`
- `baijiu-wly-lzlj`

---

## 部署

- Railway 主路径：见 `track-a/deploy/DEPLOY.md`（已配 `track-a/railway.toml`）
- Fly.io 备选：同文档内有完整步骤
- Docker：使用 `track-a/server/Dockerfile`

---

## 本地验证示例

```bash
curl -sS "http://127.0.0.1:8787/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: 你在.env里配置的KEEL_API_KEY" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"本地联调：请给我稳妥+disruptive两条建议"}'
```
