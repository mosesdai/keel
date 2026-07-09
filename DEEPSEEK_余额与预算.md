# DeepSeek 余额与预算 · 主见 Keel

> 更新：**2026-07-10**  
> 配置细节见 [`track-a/deploy/DEEPSEEK_SETUP.md`](./track-a/deploy/DEEPSEEK_SETUP.md) · 决策 4 见 [`DECISIONS.md`](./DECISIONS.md)

---

## 1. 你要管什么？

| 项目 | 说明 |
|------|------|
| **DeepSeek 账户余额** | [DeepSeek 开放平台](https://platform.deepseek.com/) → 余额 / 用量 |
| **Railway 平台费** | [Railway Dashboard](https://railway.app/) → 项目 `keel-production` 用量（与模型费分开） |
| **GitHub Actions** | 当前 workflow 无 LLM 调用；主要是 CI，费用可忽略 |

**原则（DECISIONS 决策 4）**：智能优先、单人可控。日常走便宜模型；`/max` 或深度模式才升档。

---

## 2. 模型路由（省钱核心）

| 场景 | 模型 | 触发条件 |
|------|------|----------|
| 日常 entry | `deepseek-chat` | 默认（`DEEPSEEK_MODEL_DEFAULT`） |
| 深度判断 | `deepseek-reasoner` | 消息含 `/max`、`depth: deep`、或 topic 深度模式 |
| 后备 | Qwen / mock | DeepSeek 不可用时的降级 |

**九叔日常用法**：不加 `/max` → 几乎全是 `deepseek-chat`。

---

## 3. 单人月费估算

**假设**（可按实际替换）：

- 每天 **30 次** entry（九叔三段话 × 10 天活跃 ≈ 保守上限）
- 每次约 **1.3K tokens**（输入 + 输出）
- 月总量 ≈ **1.17M tokens**

| 场景 | `/max` 占比 | 月费量级（人民币） | 说明 |
|------|-------------|-------------------|------|
| **A · 日常** | ≤ 10% | 低个位数 ~ 十几元 | 推荐默认 |
| **B · 混合** | ~ 30% | 十几 ~ 三十元 | 关键周谈判期 |
| **C · 频繁深度** | ~ 50% | 数十元 | 需刻意控制 |

> 单价随 DeepSeek 官方调整；上表按「便宜模型为主」估算，非精确账单。

**Railway**：Hobby/Pro 按平台计费，Track A 轻量 API 通常 **$5–20/月** 量级（视 sleep、请求量而定）。

---

## 4. 预算告警线（建议）

| 层级 | 阈值 | 动作 |
|------|------|------|
| **正常** | DeepSeek < ¥200/月 | 无需动作 |
| **关注** | ¥200–500/月 | 查是否 `/max` 过频、topic 是否误开深度 |
| **告警** | **> ¥800/月** | [`PLAYBOOK.md`](./PLAYBOOK.md) 决策门禁：暂停升档、复盘路由 |
| **Railway** | 平台费突增 | 查日志量、是否多实例、Volume 挂载 |

Moses 可在 DeepSeek 控制台设 **余额不足提醒**（若平台支持）。

---

## 5. 上线前必做（安全 + 成本）

1. **轮换 API Key**：开发环境用过的 `DEEPSEEK_API_KEY` 上线前在控制台换新 → 同步 **GitHub Secret + Railway Variable**（勿 commit `.env`）。
2. **确认 Railway Variables**：`KEEL_API_KEY`、`DEEPSEEK_API_KEY`、`DEEPSEEK_MODEL_DEFAULT=deepseek-chat`（见 [`track-a/server/RAILWAY_VARIABLES_傻瓜版.md`](./track-a/server/RAILWAY_VARIABLES_傻瓜版.md)）。
3. **验收**：`/health` → `api_key_configured: true`；`POST /v1/entry` → **200**（非 mock 需 DeepSeek key 有效）。

---

## 6. 怎么看「是不是在烧钱」？

**每周 2 分钟**：

1. DeepSeek 控制台 → 用量曲线（是否突刺）
2. Railway → Metrics（CPU/内存/请求）
3. 若 entry 回复含「本地兜底 / mock」→ **模型 key 无效或未注入**，先修配置再谈用量

**不要**：把 key 贴进 issue、文档或 Cursor 对话。

---

## 7. 相关入口

- 环境变量清单：[`GITHUB_SECRETS.md`](./GITHUB_SECRETS.md)
- 部署状态：[`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md)
- 团队角色（月费监控）：[`TEAM.md`](./TEAM.md) § 模型路由
