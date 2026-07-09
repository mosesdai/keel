# 无人值守持续开发 · Keel / 军师

> 日期：2026-07-10  
> 仓库：https://github.com/mosesdai/keel  
> 读者：Cursor Agent、GitHub Actions、Moses（偶尔 review）

---

## 1. 目标

Moses 关机后，工程在 **GitHub + CI + Railway** 上继续推进；只有 `PLAYBOOK.md` §5 决策门禁才需要叫醒 Moses。

---

## 2. 触发器

| 触发 | 谁执行 | 做什么 |
|------|--------|--------|
| **push to `main`** | GitHub Actions | `server-ci.yml` 跑 server 测试；`docs-check.yml` 检查文档；`deploy-server.yml` 记录部署状态（Railway GitHub 集成时自动部署，无需 `RAILWAY_TOKEN`） |
| **schedule 每周一 09:00 UTC** | `agent-backlog.yml` | 自动创建「本周 S0/S1 进度检查」issue（纯 github-script，**不调用 LLM**） |
| **Issue label `agent`** | Cursor Cloud Agent / Moses 开机 Agent | 按 issue 正文开分支 → PR → 合并（无门禁时） |
| **Moses 开机 + Cursor** | 本地 Agent | 读 RESUME → SESSION_LOG → open issues，继续 backlog |

---

## 3. Agent 每轮启动（读序）

1. [`MOSES_STATUS.md`](./MOSES_STATUS.md) — Moses 还要做什么、Railway 是否在线
2. [`PLAYBOOK.md`](./PLAYBOOK.md) — 当前阶段 S0/S1/S2…
3. [`RESUME.md`](./RESUME.md) + [`SESSION_LOG.md`](./SESSION_LOG.md) — 上轮 handoff
4. GitHub **open issues**（优先 label `agent` 或 `issues/*.md` 草稿）
5. [`GITHUB_STATUS.md`](./GITHUB_STATUS.md) — CI / remote 状态
6. [`CLOUD_DEV.md`](./CLOUD_DEV.md) §6b — 关机后 SOP 细节

---

## 4. Agent 做什么

- 修 CI 红（workflow、import、health smoke）
- 改进 `track-a/demo`、`ios/` 文档与脚手架
- 写/补 server 测试、QUALITY_TESTS 脚本化草稿
- 更新 `ROADMAP.md` 进度、`SESSION_LOG.md` handoff
- Issue 拆分、PR、Dependabot、非敏感依赖升级
- Railway 相关：**文档化** Root Directory、验收清单；staging URL 可用时跑 `/health` 与 QUALITY_TESTS

---

## 5. Agent 不做

| 禁止 | 原因 |
|------|------|
| 花 Moses 钱的**大模型 API 调用**（DeepSeek/Qwen 等） | 密钥在 Secrets；CI 只用 mock/smoke |
| 改 GitHub / Railway **Secrets 的值** | 需 Moses Dashboard |
| 发给九叔（装快捷指令、真机验收、微信说明） | 需 Moses 或九叔本人 |
| Apple 签名、TestFlight 提交、Developer 付费 | 决策门禁 |
| 登录 Moses 的 Railway / GitHub 账号代填 UI | 无凭据、无浏览器 session |
| commit `.env`、证书、profile、API key 明文 | 安全 |

---

## 6. 决策门禁（必须等 Moses）

摘自 `PLAYBOOK.md` §5，命中则 **暂停该 PR/issue**，在评论写清「需要 Moses：…」，其他非阻塞任务继续：

1. Apple Developer 年费、Team、Bundle ID、证书策略  
2. 九叔真机分发路径（Ad Hoc / TestFlight / 企业签）与 UDID  
3. 隐私政策、Beta/App Store 文案终审  
4. 模型供应商变更、利益冲突路由、单月费用预计 **> ¥800**  
5. 交给九叔前的 go/no-go；九叔真实商业敏感内容的外部分享/截图  
6. 架构级变更（CloudKit vs 自建 Hub、日志保留策略）  
7. 外显名、图标、discreet 文案最终拍板  

---

## 7. 现实约束（诚实说明）

### GitHub Actions **不能**替 Cursor Agent 写 Swift / 复杂 PR

标准 `ubuntu-latest` / `macos-latest` runner 只能跑：**测试、lint、部署脚本、issue 创建、文档检查**。  
除非额外接入 **Codex API**、**self-hosted runner + Cursor Cloud Agent**，否则 **无人写代码**。

### 可无人值守的

- CI 绿/红反馈  
- `main` push → **Railway GitHub 集成**自动部署 API（Moses 关机也在线）  
- Issue 管理、每周进度 issue（`agent-backlog.yml`）  
- 文档生成（workflow 内脚本，非 LLM）  
- changelog、Dependabot PR  

### 推荐路径（按优先级）

1. **Railway GitHub 集成** — Moses 一次性设 Root Directory = `track-a`；之后 push `main` 即 24/7 API  
2. **Cursor Cloud Agent**（若 Moses 订阅可用）— 对 label `agent` 的 issue 开 PR  
3. **Moses 定期 5 分钟** — review 绿 CI 的 PR、点 merge  
4. **GitHub Actions + 脚本** — 测试、lint、staging health check、backlog issue  

---

## 8. 借鉴 ipitch 的模式

`~/.cursor/skills/ipitch/SKILL.md` 的核心不是某个云平台，而是：

- **固定轮次 + 固定门禁 + 固定产物 + handoff**（R0→R3，每轮有模板与 Gates）  
- 研究沉 `research/`，对外交付短而锋利  
- bespoke 与货架分轨，避免临时定制当标准产品  

军师项目映射：

| ipitch | Keel |
|--------|------|
| R0 charter | S0 云上底座（repo、CI、Railway） |
| R1 研究 + 刀 | `research/` + Bridge Track 验收 |
| R2 货架 | `issues/` backlog + ROADMAP 里程碑 |
| R3 收口 | 7/15 Bridge / TestFlight go-no-go |
| Gates | `PLAYBOOK.md` §5 决策门禁 |
| handoff | `SESSION_LOG.md` + `RESUME.md` |

---

## 9. 标准 Issue → PR 流程

1. 从 `issues/*.md` 或 GitHub New Issue（模板 **Agent task**）创建任务  
2. 分支名：`agent/<issue-num>-<short-slug>`  
3. PR 必填：Summary、Acceptance（见 `.github/pull_request_template.md`）  
4. 同步更新 `SESSION_LOG.md`；里程碑变化更新 `ROADMAP.md`  
5. CI 绿 + 无门禁 → merge；有门禁 → 留 PR 待 Moses  

---

## 10. 相关文件

- [`CURSOR_CLOUD_AGENT_SETUP.md`](./CURSOR_CLOUD_AGENT_SETUP.md) — Cursor Cloud Agent 绑定 GitHub issue 设置指南
- [`CLOUD_DEV.md`](./CLOUD_DEV.md) — Actions 设计、Secrets 分层  
- [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md) — 关机前清单  
- [`MOSES_STATUS.md`](./MOSES_STATUS.md) — Moses 一页纸状态  
- [`issues/`](./issues/) — 可粘贴 issue 草稿  
