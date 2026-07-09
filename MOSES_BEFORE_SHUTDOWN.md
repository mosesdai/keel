# Moses 关机前必做清单（复制即用）

> **不懂 GitHub Secrets 怎么填？请看** [`GITHUB_SECRETS_傻瓜版.md`](./GITHUB_SECRETS_傻瓜版.md)  
> **不懂 Railway 怎么部署？请看** [`RAILWAY_傻瓜版.md`](./RAILWAY_傻瓜版.md)

> **仓库**：https://github.com/mosesdai/keel  
> **工作区**：`/Users/Eliam-Code/20260701 军师 app/`  
> **目标**：做完下面「关机前必须做」（约 **15–20 分钟**）即可关电脑；之后在 GitHub / 云上由 agent 继续开发，**只有决策门禁**才再叫醒你。

---

## 进度速览

| 步骤 | 状态 |
|------|------|
| GitHub Secrets（`KEEL_API_KEY`、`DEEPSEEK_API_KEY`） | ✅ Moses 已完成 |
| Railway 部署 + `/health` 公网可访问 | ⏳ **待做**（见步骤 2） |
| `KEEL_STAGING_URL` 回填 GitHub Variable | ⏳ Railway 域名生成后 |
| URL 告诉 Agent | ⏳ Railway 完成后 |

---

## 一、关机前必须做（做完可关电脑）

### 步骤 1 · GitHub Secrets（约 5 分钟）✅ 已完成

1. 打开：https://github.com/mosesdai/keel → **Settings** → **Secrets and variables** → **Actions**
2. 点 **New repository secret**，按 [`GITHUB_SECRETS.md`](./GITHUB_SECRETS.md) 填下面 **3 项必填**（值从本机 `track-a/server/.env` 复制，**勿粘贴到 Cursor 聊天**）：

| # | 名称 | 类型 | 说明 |
|---|------|------|------|
| 1 | `KEEL_API_KEY` | Secret | Bridge API 鉴权；须与 Railway Variables、九叔快捷指令一致 |
| 2 | `DEEPSEEK_API_KEY` | Secret | DeepSeek 模型；上线前建议换新 key（见 `track-a/deploy/DEEPSEEK_SETUP.md`） |
| 3 | `KEEL_STAGING_URL` | **Variables**（非 Secret） | Railway 公网 API 根 URL，如 `https://xxx.up.railway.app`（**无**尾斜杠）；**Generate Domain 后再填** |

> `RAILWAY_TOKEN`：**可选**。若 Railway 已用 **Deploy from GitHub** 连 repo，可不填；Actions 的 `deploy-server.yml` 会 skip CLI 部署，由 Railway 自动部署。

本地复制 key 的命令见 [`GITHUB_SECRETS.md`](./GITHUB_SECRETS.md) §「如何从本地复制 `KEEL_API_KEY`」。

---

### 步骤 2 · Railway 连 GitHub 并部署（约 8–12 分钟）⏳ **下一步**

> **零基础逐步**：[`RAILWAY_傻瓜版.md`](./RAILWAY_傻瓜版.md)

1. 登录 https://railway.app（建议用 GitHub 登录）
2. **New Project** → **Deploy from GitHub repo** → 选 **`mosesdai/keel`**
3. 进入该 Service → **Settings** → **Root Directory** 填：**`track-a`**
4. **Variables** → 新增（与 GitHub / 本地 `.env` 对齐，勿写入 git）：
   - `KEEL_API_KEY`（与步骤 1 相同）
   - `DEEPSEEK_API_KEY`（与步骤 1 相同）
   - `DEFAULT_PROVIDER` = `deepseek`
   - `DEEPSEEK_MODEL_DEFAULT` = `deepseek-chat`
   - `DEEPSEEK_MODEL_DEEP` = `deepseek-reasoner`
5. **Settings → Networking → Generate Domain**，得到形如 `https://….up.railway.app` 的 URL
6. 浏览器打开：`https://你的域名/health`，应返回 ok
7. 回到 GitHub → **Settings → Secrets and variables → Actions → Variables**，把该 URL 写入 **`KEEL_STAGING_URL`**

详细版：`track-a/deploy/RAILWAY_WALKTHROUGH.md` · 部署后验收：`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`

---

### 步骤 3 ·（可选，约 2 分钟）GitHub Issue #1

在 https://github.com/mosesdai/keel/issues/new 创建 issue：

- **标题**：`S0 · Railway 部署 + Bridge Track 7/15`
- **正文**：复制粘贴 [`issues/001-S0-railway-bridge.md`](./issues/001-S0-railway-bridge.md) 全文

不创建也可以；agent 会按该文件内容推进。

---

### 步骤 4 · 确认 staging URL（约 1 分钟）

任选其一（agent 需要知道公网 API 地址才能跑验收 / 更新文档）：

- 在本 Cursor 对话里发一句：`Railway URL: https://….up.railway.app`（**不要**发 key）
- 或编辑 [`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md)，在「Staging URL」一行填域名（agent 可后续补全其余字段）

---

### 关机前自检（30 秒）

- [x] GitHub 已有 `KEEL_API_KEY`、`DEEPSEEK_API_KEY`（Secrets）
- [ ] Railway Root = `track-a`，Variables 已填，`/health` 公网可访问
- [ ] （建议）`KEEL_STAGING_URL` 已填
- [ ] URL 已告诉 agent 或写入 `DEPLOYMENT_STATUS.md`

**做完以上即可关机。**

---

## 二、诚实说明：没配 Railway 时 agent 能做什么

截至文档编写时，**Railway 尚未在 repo 侧记录为已联通**（见 `GITHUB_STATUS.md`）。

| 你已做完 | agent 关机后可做 |
|----------|------------------|
| 仅 push 过代码，**未**做步骤 1–2 | **只能**：改代码、文档、Issue/PR、修 CI、push 到 `main`。**不能**：替你登录 Railway、不能部署 API、不能替你在 Dashboard 填 Variables |
| 步骤 1–2 做完（GitHub Secrets + Railway GitHub 集成） | **可以**：合并 PR 后 Railway **自动**部署；用 `KEEL_STAGING_URL` / `DEPLOYMENT_STATUS` 跑 staging 验收草稿 |
| 另填了 `RAILWAY_TOKEN` | **可以**：GitHub Actions `deploy-server.yml` 用 CLI 部署（与 Dashboard 集成二选一即可） |

**没有** `KEEL_API_KEY` / `DEEPSEEK_API_KEY` 进 GitHub 或 Railway 时，云端 **无法** 跑通真实模型调用；agent 只会推进不依赖线上密钥的工作。

---

## 三、可以不做 · agent 会继续推进

关机后 **不必** 等你再做这些事，agent 自主处理即可：

- `track-a/demo` 体验与 UI 微调
- 文档维护：`SESSION_LOG.md`、`ROADMAP.md`、`ACCEPTANCE.md`、`GITHUB_STATUS.md`
- `ios/` 骨架、simulator CI、workflow 修复
- Issue 拆分、PR、Dependabot、非门禁型 CI 失败修复
- 快捷指令 / onboarding 文案检查（**不含**替九叔真机安装）
- `QUALITY_TESTS.md` 脚本化草稿（staging 可用后再对 URL 跑）

---

## 四、只有这些情况才再叫醒 Moses（决策门禁）

摘自 [`PLAYBOOK.md`](./PLAYBOOK.md) §5；**除此以外 agent 不打扰**。

1. **Apple Developer**：年费 $99、团队角色、Bundle ID、证书与签名策略。
2. **九叔真机分发**：收集 **UDID**、Ad Hoc vs TestFlight vs 企业签等路径拍板（Ad Hoc AirDrop 已为可接受路径之一，见 `DISTRIBUTION.md`）。
3. **隐私与对外文案**：隐私政策、Beta / App Store 文案中关于数据保留、模型供应商、敏感内容的**措辞终审**。
4. **费用与供应商**：单月 API/云费用预计超过 **¥800**；或模型供应商/路由重大变更（含腾讯、阿里、字节、DeepSeek/Qwen 与利益冲突通道）。
5. **交给九叔前的 go/no-go**：是否今晚/本周把某 build 或 Bridge 装给九叔；涉及九叔真实商业敏感内容的**外部分享、截图、演示**。
6. **架构级变更**（若 agent 提出）：CloudKit vs 自建 Hub、端侧存储、日志保留策略等需你拍板时再问。
7. **外显名最终确认**：App 图标名、锁屏 discreet 文案的最终拍板（候选见 `NAMING.md`，日常文档 agent 可先写草稿）。

---

## 五、agent 恢复工作时先读

1. 本文件 `MOSES_BEFORE_SHUTDOWN.md`
2. `RESUME.md` → `SESSION_LOG.md`
3. `issues/001-S0-railway-bridge.md` 或 GitHub open issues
4. `CLOUD_DEV.md` §「Moses 关机后 agent 自主推进 SOP」

---

*最后更新：2026-07-09 · Secrets ✅，Railway 待做*
