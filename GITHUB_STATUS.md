# GitHub 初始化状态

> 更新：2026-07-09  
> 工作区：`/Users/Eliam-Code/20260701 军师 app/`

## ✅ 已完成（agent）

- [x] 阅读并对齐 `GITHUB_SETUP.md`、`PLAYBOOK.md`、`CLOUD_DEV.md`、`RESUME.md`
- [x] 根目录 `git init`，分支 `main`
- [x] 移除 `track-a/.git` 嵌套空仓库，统一为 monorepo
- [x] 根目录 `.gitignore`：`.env`、`.venv`、证书、profile、Track A 活数据（`entries.jsonl`、snapshots 等）
- [x] 确认 `track-a/server/.env` 与 `.venv` 被 ignore，未进入暂存区
- [x] GitHub Actions 骨架：
  - `.github/workflows/server-ci.yml`
  - `.github/workflows/docs-check.yml`
  - `.github/workflows/deploy-server.yml`（Railway 占位，无真实 secret）
  - `.github/pull_request_template.md`
  - `.github/ISSUE_TEMPLATE/feature.yml`、`decision-gate.yml`、`release-check.yml`
- [x] 本地初始 commit（见下方「Git 本地」）

## ⏳ 待 Moses（复制即用）

### 1. 安装并登录 GitHub CLI

```bash
brew install gh
gh auth login
```

### 2. 创建 private repo 并 push

建议仓库名：`keel`（或 `zhujian-keel`）。**不要**在 GitHub 网页勾选「Add README / .gitignore / license」。

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
gh repo create keel --private --source=. --remote=origin --push
```

若 repo 名或 owner 不同，改 `keel` 为你的名字；或先网页建空 repo 再：

```bash
git remote add origin git@github.com:<YOUR_USER>/keel.git
git push -u origin main
```

推送前再确认：

```bash
git status --short
git check-ignore -v track-a/server/.env
```

不得出现 `.env`、`.venv`、`.p12`、`.mobileprovision`、API key 明文。

### 3. GitHub Actions Secrets（Settings → Secrets and variables → Actions）

只填名称，**值在 GitHub UI 填写，勿写入 repo**：

| Secret | 用途 |
|--------|------|
| `KEEL_API_KEY` | Bridge Track API 鉴权 |
| `DEEPSEEK_API_KEY` | DeepSeek 模型 |
| `DASHSCOPE_API_KEY` | Qwen 备选（可后填） |
| `RAILWAY_TOKEN` | Actions 部署 Railway（可选，亦可用 Railway GitHub 集成） |

7/16 后 Ad Hoc：`IOS_DIST_CERT_BASE64`、`IOS_DIST_CERT_PASSWORD`、`IOS_ADHOC_PROFILE_BASE64`、`KEYCHAIN_PASSWORD`

7/25 前 TestFlight：`APP_STORE_CONNECT_API_KEY_ID`、`APP_STORE_CONNECT_ISSUER_ID`、`APP_STORE_CONNECT_PRIVATE_KEY`、`MATCH_PASSWORD`（若用 fastlane match）

可选 **Repository variable**：`KEEL_STAGING_URL`（部署后 `/health` 检查用）

### 4. Railway（`GITHUB_SETUP.md` Step 4）

Dashboard → Deploy from GitHub → Root Directory：`track-a` → 填 Variables → Deploy → 验证 `/health`。

### 5. push 后创建首个 agent issue（若 agent 未创建）

标题示例：`S0: Add GitHub Actions server CI 与 Railway 联通`

或在 repo 建好后让 agent 开 issue #1（PLAYBOOK S0）。

## Git 本地

- 分支：`main`
- Remote：**未配置**（本机未检测到 `gh` CLI）
- 初始 commit：agent 本轮提交

## Remote URL

（待 `gh repo create` 或 `git push` 成功后填写）

```text
https://github.com/<YOUR_USER>/keel
```

## 阻塞说明

- 执行环境未安装 `gh`，无法非交互创建 GitHub repo、push、开 issue #1。
- Moses 完成 Step 1–2 后，可在新会话让 agent 创建 issue #1 并开 PR 1（CI scaffold 已在本 commit）。
