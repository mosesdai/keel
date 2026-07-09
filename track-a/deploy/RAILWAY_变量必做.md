# Railway 变量必做（Keel / keel-production）

> **症状**：打开 `https://keel-production-be1c.up.railway.app/health` 看到 `"status":"ok"`，但 **`"api_key_configured": false`**。  
> **含义**：容器在跑，但进程里**没有读到非空的 `KEEL_API_KEY`** → `POST /v1/entry` 会 **503**（「服务端未配置 KEEL_API_KEY」）。  
> **预计时间**：约 5 分钟（填变量 + Redeploy + 验收）。

---

## 一、代码到底检查什么？（`track-a/server/app.py`）

| 位置 | 行为 |
|------|------|
| **`GET /health`** | `"api_key_configured": bool(os.getenv("KEEL_API_KEY", "").strip())` —— **只认 `KEEL_API_KEY` 这一个名字**，且去掉首尾空格后不能为空。 |
| **`require_api_key`（/v1/entry 等）** | 同样读 **`KEEL_API_KEY`**；请求头 **`X-API-Key`** 必须与此值完全一致。 |
| **调 DeepSeek** | 读 **`DEEPSEEK_API_KEY`**（无 key 会走 mock 或报错，视路径而定）。 |
| **调 Qwen 后备** | 读 **`DASHSCOPE_API_KEY`**（可选）。 |
| **`DEFAULT_PROVIDER`** | **当前 `app.py` 不读取此变量**。模型路由只看是否配置了 `DEEPSEEK_API_KEY` / `DASHSCOPE_API_KEY`。在 Railway 写上 `DEFAULT_PROVIDER=deepseek` **无害**，便于与旧文档对齐，但 **不能代替 `DEEPSEEK_API_KEY`**，也 **不会** 让 `api_key_configured` 变 true。 |

本地开发时，`load_dotenv()` 会加载 `track-a/server/.env`；**Railway 上只靠平台注入的环境变量**，不会读你 GitHub 里的 `.env` 文件。

---

## 二、GitHub Secrets ≠ Railway Variables（两套都要填，各管各的）

很多人只配了 GitHub，以为部署会自动带上 Key —— **不会**。

| 存放位置 | 用途 | 和 Keel API 的关系 |
|----------|------|---------------------|
| **GitHub → Repository → Settings → Secrets and variables → Actions** | CI/CD、GitHub Actions 流水线 | 仅当 workflow **显式**把 secret 传给 Railway CLI 或写入部署时才有用；**不会**自动出现在已运行容器的进程环境里。 |
| **Railway → 具体 Service → Variables** | 该服务**运行时** `os.getenv(...)` 读到的值 | **必须在这里配 `KEEL_API_KEY`**，`/health` 才会 `api_key_configured: true`。 |

**结论**：  
- GitHub 里的 `KEEL_API_KEY`：给 Action / 本地脚本 / 文档对齐用。  
- Railway Service Variables 里的 `KEEL_API_KEY`：**线上 health 与鉴权真正看的**。

两套的值**建议相同**（与九叔快捷指令 `X-API-Key`、本地 `track-a/server/.env` 一致），但**必须在 Railway 再填一遍**。

---

## 三、填在哪里？（最常见错因：填错层级）

### 正确位置

1. 打开 [Railway Dashboard](https://railway.app) → 项目（如 **keel-production**）。  
2. 在架构图里点 **跑 FastAPI 的那个 Service**（名称常为 **`keel`** 或类似，**不是** Postgres/Redis 插件）。  
3. 进入该 Service 后，点 **Variables** 标签页。  
4. 在此 **Service 的 Variables** 里新增/修改变量。

### 错误位置（填了也白填）

| 错误做法 | 为什么不行 |
|----------|------------|
| 只在 **Project Settings → Shared Variables** 里填，但 **没有 Link / 关联到 keel Service** | 未 link 的 Shared 变量**不会**注入该容器。 |
| 填在 **另一个 Service**（例如只开了数据库的那个） | 每个 Service 环境隔离；API 容器读不到。 |
| 只在 **GitHub Secrets** 填，Railway Variables 为空 | 见第二节。 |
| 只点 **Save**，没有 **Redeploy** | 旧容器仍用旧环境快照，见第五节。 |

**截图自检**：Variables 页顶栏应显示 **当前 Service 名**（如 `keel`），列表里应能看到你刚加的名字。

---

## 四、变量名与值（大小写、空格、引号）

### 必配（让 health 与 entry 可用）

| 变量名 | 必须完全一致 | 值说明 |
|--------|----------------|--------|
| **`KEEL_API_KEY`** | 全大写，中间是下划线 | 任意足够长的随机串；与快捷指令 **`X-API-Key`**、本地 `.env` 相同。**health 只看这一项。** |
| **`DEEPSEEK_API_KEY`** | 全大写 | DeepSeek 控制台 API Key（通常 `sk-…`）。**勿提交到 Git。** |

### 建议配（与仓库文档一致）

| 变量名 | 建议值 | 说明 |
|--------|--------|------|
| **`DEFAULT_PROVIDER`** | `deepseek` | 旧文档/清单沿用；**代码不读**，可写可不写。 |
| **`DEEPSEEK_MODEL_DEFAULT`** | `deepseek-chat` | 不填时代码默认也是 `deepseek-chat`。 |

### 可选

- **`DEEPSEEK_MODEL_DEEP`** = `deepseek-reasoner`（深度模式）  
- **`DASHSCOPE_API_KEY`**（Qwen 后备）  
- **`DEEP_TOPIC_SLUGS`** 等见 `track-a/server/.env.example`

### 常见填错

1. **变量名**：`Keel_Api_Key`、`KEEL-API-KEY`、` keel_api_key `（前后空格）—— 进程读不到。  
2. **值两侧多引号**：Railway 一般**不要**包一层 `"..."`；若把 `"sk-xxxx"` 整段粘贴，引号可能变成值的一部分。  
3. **值中间换行或复制了半串 Key**。  
4. **Shared Variable 未 link 到 keel Service**（见第三节）。  
5. **填完只 Save，未 Redeploy**（见第五节）。

---

## 五、保存后必须 Redeploy（不是「只 Save」）

Railway 在**新部署**时把 Variables 注入容器。正在运行的旧实例**不会**因为你点了 Save 就热更新环境变量。

1. 在同一 Service 打开 **Deployments**。  
2. 最新一条部署右侧 **⋯** → **Redeploy**（或触发一次新 deploy）。  
3. 等到状态 **SUCCESS / ACTIVE**（常见 1–3 分钟，视构建而定）。  
4. **再**访问 health。

---

## 六、验收

### 1）Health

```bash
curl -sS "https://keel-production-be1c.up.railway.app/health"
```

**期望 JSON**（示例字段）：

```json
{
  "status": "ok",
  "api_key_configured": true,
  "data_dir": "/app/data",
  "seed_topics": ["tencent-ali-renewal", "lining-pitch", "baijiu-wly-lzlj"]
}
```

若仍为 `"api_key_configured": false`：回到第三节确认 Service、第五节确认 Redeploy 已 ACTIVE。

### 2）Entry（勿把真实 key 贴到聊天）

```bash
export KEEL_STAGING_URL="https://keel-production-be1c.up.railway.app"
export KEEL_API_KEY="你的KEEL_API_KEY"

curl -sS "${KEEL_STAGING_URL}/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${KEEL_API_KEY}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"Railway 变量验收","advice_intensity":3}'
```

期望 HTTP **200**，JSON 含非空 **`reply`**。

---

## 七、Raw Editor 粘贴格式示例（无真实 Key）

在 Service → **Variables** → **Raw Editor** 中，可按行 `KEY=value` 粘贴（**把占位符换成你自己的值**）：

```env
KEEL_API_KEY=请换成与快捷指令一致的随机串
DEEPSEEK_API_KEY=sk-请从DeepSeek控制台复制完整key
DEFAULT_PROVIDER=deepseek
DEEPSEEK_MODEL_DEFAULT=deepseek-chat
```

规则：

- 一行一个变量，**不要** `export`。  
- **不要**在 value 外加 JSON 引号。  
- 粘贴后点保存，然后 **Deployments → Redeploy**。

---

## 八、Variables 截图里应看到的名字（核对清单）

在 **Service keel（或你的 API 服务）→ Variables** 列表中，至少应出现：

1. **`KEEL_API_KEY`**（必填，决定 `api_key_configured`）  
2. **`DEEPSEEK_API_KEY`**（必填，才能真调模型）  
3. **`DEFAULT_PROVIDER`**（可选，建议 `deepseek`，与 MOSES 清单一致）  

若还按 `.env.example` 显式配置模型，可能另有 **`DEEPSEEK_MODEL_DEFAULT`** 等。

**不应**指望在 Project 级 Shared Variables 里「只保存不 link」就能让 health 变 true。

---

## 九、相关文档

- `track-a/server/.env.example` — 本地变量名权威列表  
- `track-a/server/RAILWAY_VARIABLES_傻瓜版.md` — 短版三步  
- `track-a/deploy/RAILWAY_WALKTHROUGH.md` — 全流程  
- `track-a/deploy/DEPLOY.md` — 部署总览  

**安全**：任何 `sk-…`、真实 `KEEL_API_KEY` 勿 commit、勿写进 markdown 再 push。
