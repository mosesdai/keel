# S0 · Railway 部署 + Bridge Track 7/15

> **GitHub Issue 标题（复制到 New Issue）**：`S0 · Railway 部署 + Bridge Track 7/15`  
> **仓库**：https://github.com/mosesdai/keel

---

## 背景

Monorepo 已 push 到 `main`（commit `6964c5c`+）。7/15 前交付路径为 **Bridge Track**（`track-a/`：FastAPI + 快捷指令 + 主屏入口），不做虚假 TestFlight 承诺。本 issue 收口 **PLAYBOOK.md S0** 剩余项并衔接到 **S1 7/15 过渡交付**。

---

## 任务清单

### A. GitHub / CI（agent）

- [ ] 确认 `server-ci.yml` 在 PR/push 上绿（import + `/health` smoke）
- [ ] 确认 `docs-check.yml` 通过
- [ ] PR：将 `deploy-server.yml` 从占位改为可部署（Railway CLI 或文档化「仅用 Railway GitHub 集成」二选一，与 Moses 已选路径一致）
- [ ] 部署后设置 repo **Variable** `KEEL_STAGING_URL`（staging 根 URL，无尾斜杠）
- [ ] 更新 `GITHUB_STATUS.md` / `SESSION_LOG.md` 于同一 PR

### B. Railway（Moses + agent）

- [ ] Railway：New Project → **Deploy from GitHub** → repo `mosesdai/keel` → **Root Directory：`track-a`**
- [ ] Railway Variables（与本地 `track-a/server/.env` 对齐，**勿写入 git**）：
  - `KEEL_API_KEY`
  - `DEEPSEEK_API_KEY`
  - `DEFAULT_PROVIDER=deepseek`
  - （可选）`DASHSCOPE_API_KEY`
- [ ] Generate Domain → 公网 `GET /health` 返回 ok
- [ ] 跑 `track-a/server/QUALITY_TESTS.md` 三条用例（对 staging URL）

### C. Bridge Track 7/15（agent + Moses）

- [ ] 快捷指令：`{{KEEL_API_URL}}` / `{{KEEL_API_KEY}}` 替换为 staging（`track-a/shortcuts/SETUP.md`）
- [ ] 九叔视角安装说明：`track-a/JIUSHU_ONBOARDING.md`
- [ ] Moses：九叔手机装快捷指令 + 首测「腾讯阿里续约」真实输入
- [ ] `ACCEPTANCE.md` A0 Bridge 验收项勾选

---

## Definition of Done（本 issue）

1. `main` 合并后 CI 绿；staging API `/health` 可从公网访问。
2. GitHub Secrets 已配置（名称见 `GITHUB_SECRETS.md`）；无 secret 进 repo。
3. 至少一次端到端：文字/语音入口 → 军师回复 → 记录落盘；军师给出反对意见或 disruptive 备选，语气不冒犯。
4. 文档 handoff：`SESSION_LOG.md` 记录 staging URL 的**存放位置**（仅 Moses 本地/密码管理器，不写 key 明文进 repo）。

---

## Agent 可自主完成

- Workflow 修复、Railway deploy 脚本接线、QUALITY_TESTS 自动化草稿、文档与 `ROADMAP.md` 同步
- Issue/PR 拆分：CI 绿 → deploy → Bridge 文档/快捷指令模板检查

## Moses 只需做（真人判断 / secrets）

- GitHub：**Settings → Secrets and variables → Actions** 填 `KEEL_API_KEY`、`DEEPSEEK_API_KEY`、（可选）`RAILWAY_TOKEN`、`DASHSCOPE_API_KEY`
- Railway：连 GitHub、填 Variables、确认域名
- 九叔手机：装快捷指令 + 一次首测（或远程指导）

---

## 参考

- `PLAYBOOK.md` § S0 / S1
- `CLOUD_DEV.md` § deploy-server
- `track-a/deploy/RAILWAY_WALKTHROUGH.md`
- `GITHUB_SECRETS.md`
