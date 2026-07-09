# GitHub 初始化与一次性设置

> 日期：2026-07-09  
> 目的：让 agent/CI 在云上推进，Moses 电脑不必常开。  
> 当前状态：本工作区根目录尚未检测到 Git repo；`track-a/MOSES_CHECKLIST.md` 曾提到 Track A Git 已 init，但以当前根目录为准，需要重新确认/初始化。

---

## 1. Moses 一次性 5 步

### Step 1：创建 GitHub repo

建议 repo 名：

```text
keel
```

或：

```text
zhujian-keel
```

建议设置：
- Private repo。
- 不初始化 README/gitignore/license，避免和本地文件冲突。
- 只给必要 collaborators 权限。

### Step 2：本地初始化并 push

在工作区根目录执行：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git init
git branch -M main
git add .
git commit -m "Initialize Keel project"
git remote add origin git@github.com:<YOUR_ORG_OR_USER>/<REPO>.git
git push -u origin main
```

如果已经存在 git repo：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git status
git remote -v
git remote add origin git@github.com:<YOUR_ORG_OR_USER>/<REPO>.git
git push -u origin main
```

推送前必须确认：

```bash
git status --short
```

不得出现：
- `.env`
- `.venv`
- Apple certificates
- provisioning profiles
- API key 文本
- 私人聊天原文或九叔真实敏感内容

### Step 3：填 GitHub Secrets

GitHub -> Settings -> Secrets and variables -> Actions -> New repository secret。

7/15 前最小必填：

| Secret | 用途 |
|---|---|
| `KEEL_API_KEY` | Bridge Track API 鉴权 |
| `DEEPSEEK_API_KEY` | DeepSeek 模型 |
| `DASHSCOPE_API_KEY` | Qwen 备选，可后填 |
| `RAILWAY_TOKEN` | GitHub Actions 部署 Railway |

7/16 后 Ad Hoc AirDrop 需要：

| Secret | 用途 |
|---|---|
| `IOS_DIST_CERT_BASE64` | 分发证书 `.p12`（Base64）|
| `IOS_DIST_CERT_PASSWORD` | `.p12` 密码 |
| `IOS_ADHOC_PROFILE_BASE64` | Ad Hoc 描述文件（含九叔 UDID）|
| `KEYCHAIN_PASSWORD` | CI 临时钥匙串密码 |

7/25 前 TestFlight 额外需要：

| Secret | 用途 |
|---|---|
| `APP_STORE_CONNECT_API_KEY_ID` | 上传 TestFlight |
| `APP_STORE_CONNECT_ISSUER_ID` | 上传 TestFlight |
| `APP_STORE_CONNECT_PRIVATE_KEY` | 上传 TestFlight |
| `MATCH_PASSWORD` 或等价签名 secret | 如果使用 fastlane match |

不要把 Apple ID 密码、`.p12`、`.mobileprovision` 放入 repo。优先用 App Store Connect API key。Ad Hoc 流程见 `DISTRIBUTION.md` §5。

### Step 4：连接 Railway

Railway Dashboard：

1. New Project。
2. Deploy from GitHub repo。
3. 选择 `keel` repo。
4. Root Directory 填：

```text
track-a
```

5. Variables 填：

```text
KEEL_API_KEY
DEEPSEEK_API_KEY
DASHSCOPE_API_KEY
DEFAULT_PROVIDER=deepseek
```

6. Deploy。
7. Generate Domain。
8. 验证：

```bash
curl -sS "https://<your-domain>/health"
```

如果 Railway 卡住，按 `track-a/deploy/DEPLOY.md` 切 Fly.io。

### Step 5：Apple Developer / App Store Connect

7/15 前不阻塞 Bridge Track；**7/16 后 Ad Hoc AirDrop 需要**。

需要 Moses 决策/执行：
- 是否已有 Apple Developer Program（**$99/年**）。
- Team 名称用个人还是公司。
- Bundle ID：建议 `com.eliam.keel` 或 Moses 公司域名反写。
- App 显示名：中文“主见”，英文/产品名“Keel”。
- TestFlight Beta App Review 信息与隐私说明（08-02 路径）。
- **九叔 iPhone UDID** 注册到 Developer Portal（Ad Hoc 必需）。

**Ad Hoc + AirDrop**（Moses 已接受）：见 `DISTRIBUTION.md`。

---

## 2. agent 初始化 PR 应做什么

GitHub repo 建好后，agent 开第一批 PR：

### PR 1：CI scaffold

新增：

```text
.github/workflows/server-ci.yml
.github/workflows/docs-check.yml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/feature.yml
.github/ISSUE_TEMPLATE/decision-gate.yml
.github/ISSUE_TEMPLATE/release-check.yml
```

DoD：
- PR 自动跑 docs check。
- server CI 至少能安装依赖并 import FastAPI app。

### PR 2：Cloud deploy

新增：

```text
.github/workflows/deploy-server.yml
```

DoD：
- main 合并后可部署 Railway staging。
- 部署后自动检查 `/health`。

### PR 3：iOS scaffold

新增：

```text
ios/
ios/ExportOptionsAdHoc.plist
.github/workflows/ios-ci.yml
.github/workflows/ios-adhoc.yml
```

DoD：
- SwiftUI 空壳 app 能在 simulator build。
- `ios-adhoc.yml` 手动触发可产出 Ad Hoc IPA artifact（Moses 下载后 AirDrop）。
- 不要求签名阻塞 7/15 Bridge Track。

### PR 4：Bridge Track release

更新：

```text
track-a/shortcuts/SETUP.md
track-a/JIUSHU_ONBOARDING.md
ACCEPTANCE.md
ROADMAP.md
SESSION_LOG.md
```

DoD：
- Moses 能把说明微信发给九叔。
- 九叔不需要 Cursor。

---

## 3. Branch 与保护规则

建议：
- `main` 为稳定分支。
- 每个 issue 一个 branch：`agent/<issue-number>-short-name`。
- 开启 branch protection：
  - Require PR before merge。
  - Require status checks。
  - Require conversation resolution。
  - 不强制 Moses 每个 PR review；只有 `decision-gate` label 必须 Moses review。

Labels：

```text
decision-gate
bridge-track
ios
server
docs
ci
privacy
release
blocked-by-moses
```

---

## 4. Moses 只会被打断的 GitHub 事件

- PR 带 `decision-gate`。
- PR 带 `release` 且目标是发给九叔。
- CI 需要付费 runner / Apple 账号 / 云平台账单。
- 隐私、模型供应商、利益冲突路由变化。
- App Store/TestFlight 文案需要人类背书。

其他 issue/PR 由 agent 自主推进。

---

## 5. 初始 issue 清单

建 repo 后建议立即创建：

1. `S0: Add GitHub Actions server CI`
2. `S0: Connect Railway deploy from GitHub`
3. `S1: Prepare Jiushu Bridge Track install flow`
4. `S1: Run cloud quality tests`
5. `S2: Scaffold SwiftUI iPhone app`
6. `S2: Define CloudKit schema`
7. `S3: Prepare TestFlight signing and beta metadata`

只有第 2、7 可能需要 Moses 填账号或 secret；其余 agent 可先做。
