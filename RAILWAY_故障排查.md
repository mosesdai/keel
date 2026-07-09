# Railway 部署故障排查（Moses）

> 仓库：`mosesdai/keel` · 服务代码在 **`track-a/`**  
> 傻瓜步骤见 [`RAILWAY_傻瓜版.md`](./RAILWAY_傻瓜版.md)

---

## 1. 先看失败日志（必做）

1. 打开 [Railway Dashboard](https://railway.app) → 进入 **Project** → 点你的 **Service**
2. 点 **Deployments** 标签
3. 找到红色 **Deployment failed** 的那条 → 点进去
4. 点 **View logs**（或 **Build Logs** / **Deploy Logs** 两个都看）

### 日志里常见关键字 → 含义

| 日志片段 | 多半原因 |
|----------|----------|
| `Dockerfile not found` / `no such file` | **Root Directory** 没设为 `track-a`，且根目录构建也未命中 Dockerfile |
| `COPY failed` / `file not found in build context` | Root Directory 与 Dockerfile 路径不一致 |
| `pip install` 失败 | `requirements.txt` 路径错（应用 `track-a` 为根） |
| 构建成功但 **Healthcheck failed** | 进程没监听 `$PORT`，或 `/health` 不可达 |
| `Application failed to respond` | 容器启动后崩溃；看 **Deploy Logs** 里 Python traceback |
| `401` 仅出现在业务接口 | 正常；`/health` 不需 API Key |

---

## 2. 必须检查的三项设置

### ① Root Directory（最关键）

**Settings** → **Root Directory** → 填 **`track-a`**（仅这四个字符，无斜杠）→ 保存。

- 正确时：Railway 使用 `track-a/railway.toml` + `track-a/Dockerfile`
- 若暂时留空：会使用仓库根的 `railway.toml` + 根 `Dockerfile`（已加回退，但仍推荐 `track-a`）

### ② Variables（环境变量）

**Variables** 标签 → 确认至少有以下项（值从本机 `track-a/server/.env` 复制，**勿发到聊天**）：

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `KEEL_API_KEY` | 是 | 与 iPhone 快捷指令 `X-API-Key` 一致 |
| `DEEPSEEK_API_KEY` | 是 | DeepSeek 控制台密钥 |
| `DEFAULT_PROVIDER` | 是 | 填 `deepseek` |
| `DEEPSEEK_MODEL_DEFAULT` | 建议 | `deepseek-chat` |
| `DEEPSEEK_MODEL_DEEP` | 建议 | `deepseek-reasoner` |

Railway 会自动注入 **`PORT`**，无需手填。

可选：

| 变量名 | 说明 |
|--------|------|
| `TRACK_A_DATA_DIR` | 默认 `/app/data`（Docker 内已设） |
| `PERSONALITY_CHARTER_PATH` | 人格宪章路径（默认有内置 fallback） |

### ③ 重新部署

改完 Root Directory 或 Variables 后：

1. 打开 **Deployments**
2. 点右上角 **Deploy** → **Redeploy**（或 **Deploy latest commit**）
3. 等 2–5 分钟，直到状态为 **Success** / **Active**

---

## 3. 部署成功怎么验

1. **Settings** → **Networking** → **Generate Domain**（若还没有公网域名）
2. 浏览器打开：`https://你的域名.up.railway.app/health`
3. 应看到 JSON，含 `"status":"ok"`

业务接口验收见：`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`

---

## 4. 本仓库里的 Railway 相关文件

| 路径 | 何时生效 |
|------|----------|
| `track-a/railway.toml` | Root Directory = **`track-a`**（推荐） |
| `track-a/Dockerfile` | 同上 |
| `track-a/Procfile` | Nixpacks 回退用；Docker 构建以 Dockerfile 为准 |
| `railway.toml` + `Dockerfile`（仓库根） | Root Directory 为空时的回退 |

---

## 5. 仍失败时发给 Agent 的信息

（**不要**包含 API Key）

1. Build Logs 最后 **30 行**（复制文本）
2. Deploy Logs 里第一段 **traceback**（若有）
3. 截图：**Settings → Root Directory** 当前值
4. Variables 里**变量名列表**（不要值）

---

*更新：2026-07-09 · 与 `track-a` Docker/Railway 配置同步*
