# Railway Staging 验收清单（Agent 用）

> Moses 部署完成后，用本文件对公网 API 做 curl 验收。  
> **勿在此文件写入 API key**；key 从环境变量或本地 `.env` 读取。

---

## 前置

| 项 | 值 |
|----|-----|
| **Staging URL** | 从 `DEPLOYMENT_STATUS.md` 或 Moses 消息 `Railway URL: …` 获取 |
| **KEEL_API_KEY** | 本地 `track-a/server/.env` 或 Railway Variables（勿 commit） |

```bash
# 设置变量（在本机终端执行，勿贴到聊天）
export KEEL_STAGING_URL="https://xxx.up.railway.app"
export KEEL_API_KEY="你的key"
```

---

## 1. 健康检查

```bash
curl -sS "${KEEL_STAGING_URL}/health"
```

**期望**：返回 JSON 含 `ok` 或 `status` 为 healthy。

```bash
curl -sS -o /dev/null -w "%{http_code}" "${KEEL_STAGING_URL}/health"
```

**期望**：`200`

---

## 2. 兼容健康端点

```bash
curl -sS "${KEEL_STAGING_URL}/healthz"
```

**期望**：与 `/health` 同等可用（200）。

---

## 3. 鉴权失败（应 401）

```bash
curl -sS -o /dev/null -w "%{http_code}" \
  -X POST "${KEEL_STAGING_URL}/v1/entry" \
  -H "Content-Type: application/json" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"test"}'
```

**期望**：`401`（无 `X-API-Key` 时拒绝）。

---

## 4. 业务接口首测

```bash
curl -sS "${KEEL_STAGING_URL}/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${KEEL_API_KEY}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"部署后首测：请给我一条稳妥+一条disruptive建议","advice_intensity":3}'
```

**期望**：

- HTTP `200`
- JSON 含 `reply` 字段（非空字符串）
- 可选：`timestamp`、`living_position_summary`

快速检查 reply 是否存在：

```bash
curl -sS "${KEEL_STAGING_URL}/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${KEEL_API_KEY}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"部署后首测","advice_intensity":3}' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('reply_len:', len(d.get('reply','')))"
```

---

## 5. Topic 查询

```bash
curl -sS "${KEEL_STAGING_URL}/v1/topic/tencent-ali-renewal" \
  -H "X-API-Key: ${KEEL_API_KEY}"
```

**期望**：HTTP `200`，JSON 含 `display_name` 或 `living_position`。

---

## 6. 记录验收结果

验收通过后更新 [`DEPLOYMENT_STATUS.md`](./DEPLOYMENT_STATUS.md)：

| 字段 | 示例 |
|------|------|
| Staging URL | `https://xxx.up.railway.app` |
| 最后 `/health` 检查 | `2026-07-09 ok` |
| KEEL_STAGING_URL（GitHub Variable） | 已填 / 未填 |

---

## 失败排查

| HTTP | 可能原因 |
|------|----------|
| 502 / 503 | 部署未完成或容器崩溃；查 Railway Deployments 日志 |
| 401 | `KEEL_API_KEY` 不匹配 |
| 500 + 模型错误 | `DEEPSEEK_API_KEY` 无效或 `DEFAULT_PROVIDER` 未设 |
| 连接超时 | 域名未 Generate 或 URL 填错 |

---

*创建：2026-07-09 · Agent 自主维护*
