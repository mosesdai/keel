# GitHub 初始化状态

> 更新：2026-07-09  
> 工作区：`/Users/Eliam-Code/20260701 军师 app/`

## ✅ Moses：GitHub push 完成（2026-07-09）

| 项 | 结果 |
|----|------|
| 仓库 | **https://github.com/mosesdai/keel** |
| 命令 | `git push -u origin main` 成功，`main -> main` |
| 跟踪 | `branch 'main' set up to track 'origin/main'` |
| 下一步 | GitHub Actions Secrets → Railway 连 repo → issue #1（见 `issues/001-S0-railway-bridge.md`） |

---

## ⚠️ 不要用尖括号占位符原样粘贴

教程或文档里的 **`<你的用户名>`**、**`<YOUR_USER>`** 只是占位示意，**不能**整段复制进终端。

- 若原样输入 `https://github.com/<你的用户名>/keel.git`，zsh/bash 会把 `<` 当成**输入重定向**，命令会乱掉，`origin` 往往**加不上**。
- 随后执行 `git push -u origin main` 会报：`fatal: 'origin' does not appear to be a git repository`。

**正确做法**：换成你在 [github.com](https://github.com) 右上角头像旁看到的用户名，或新建仓库页 Quick setup 里显示的 URL。GitHub 用户名为 **mosesdai** 时，HTTPS 示例为：

```bash
git remote add origin https://github.com/mosesdai/keel.git
```

若仍不确定用户名，在 GitHub 打开 **Your repositories** 或 **Create a new repository**，地址栏/页面上的 `github.com/某某/keel` 中 **`某某` 就是你的用户名**。

---

## 本机检测（2026-07-09）

| 项 | 结果 |
|----|------|
| `git` | `/usr/bin/git`，`git version 2.50.1 (Apple Git-155)` |
| 分支 / 工作区 | `main`，已跟踪 `origin/main`（push ✅） |
| `origin` | `https://github.com/mosesdai/keel.git`（fetch/push） |
| 本地 commit | `6964c5c` — Initialize Keel monorepo with CI scaffold and safe gitignore. |
| `brew` / `gh` | **未安装**（`command not found`）→ 原 `GITHUB_SETUP` 中 `brew install gh` 会失败 |
| 凭据 | 系统 `credential.helper=osxkeychain`；钥匙串中已有 `github.com` 条目（用户 `mosesdai`）。HTTPS push 时可能自动用钥匙串；若被拒，请用 **Personal Access Token** 作密码（勿贴到聊天）。 |

**常见笔误**：命令行里不要多打 `[`，正确是 `gh repo create ...`，不是 `[gh repo create ...`（无 `gh` 时请用下方「无 brew 方案」）。

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
- [x] 本地初始 commit `6964c5c`
- [x] Moses：`git push -u origin main` → https://github.com/mosesdai/keel

## 无 brew 方案（推荐 Moses 用此推送）

不安装 Homebrew 也可上 GitHub。建议仓库名：`keel`（或 `zhujian-keel`）。

### 方案 A（推荐）：网页建库 + 纯 `git`

**第 0 步 — 推送前自检（复制即用）**

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git status --short
git check-ignore -v track-a/server/.env
```

不得出现 `.env`、`.venv`、`.p12`、`.mobileprovision`、API key 明文。

**第 1 步 — GitHub 网页**

1. 打开 https://github.com/new  
2. Repository name：`keel`（自定亦可）  
3. 选 **Private**  
4. **不要**勾选 Add a README / .gitignore / license（保持空仓库）  
5. 点 **Create repository**

**第 2 步 — 添加 remote（把 `<YOUR_USER>` 换成你的 GitHub 用户名）**

HTTPS（配合 PAT，见下）：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git remote add origin https://github.com/<YOUR_USER>/keel.git
```

或 SSH（需本机已配置 GitHub SSH key，见 https://docs.github.com/en/authentication/connecting-to-github-with-ssh ）：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git remote add origin git@github.com:<YOUR_USER>/keel.git
```

若误加过 remote，先：`git remote remove origin`，再执行上面 `git remote add`。

**第 3 步 — 推送**

```bash
git push -u origin main
```

- **HTTPS**：用户名填 GitHub 用户名；密码处填 **Personal Access Token**（不是登录密码）。  
- **获取 Token（勿把 token 发给 agent）**：GitHub 右上角头像 → **Settings** → 左侧最下 **Developer settings** → **Personal access tokens** → **Tokens (classic)** 或 **Fine-grained tokens** → Generate；至少勾选 repo 权限。  
- **SSH**：`git push` 一般不再要 token。

**推送成功后**在聊天告诉 agent（示例）：

```text
GitHub 已 push 成功，仓库 URL：https://github.com/<YOUR_USER>/keel
请继续：创建 issue #1（S0 CI/Railway）并更新 GITHUB_STATUS.md 的 Remote URL。
```

### 方案 B：不装 brew，直接安装 `gh`（可选）

从 GitHub 官方 Release 下载 macOS 安装包（无需 Homebrew）：

1. 打开 https://github.com/cli/cli/releases/latest  
2. 下载适合本机的文件，例如 Apple Silicon：`gh_*_macOS_arm64.zip`（Intel 选 `amd64`）  
3. 解压后将 `gh` 放到 PATH，例如：

```bash
mkdir -p "$HOME/bin"
unzip -o ~/Downloads/gh_*_macOS_arm64.zip -d /tmp/gh-unpack
cp /tmp/gh-unpack/gh_*/bin/gh "$HOME/bin/gh"
chmod +x "$HOME/bin/gh"
export PATH="$HOME/bin:$PATH"
gh --version
```

4. 登录并创建仓库（**注意**：不要多打 `[`）：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
gh auth login
gh repo create keel --private --source=. --remote=origin --push
```

持久 PATH：在 `~/.zshrc` 增加一行 `export PATH="$HOME/bin:$PATH"`，然后 `source ~/.zshrc`。

---

## ⏳ 待 Moses（有 brew/gh 时的原流程）

若日后安装了 Homebrew + `gh`，仍可用：

```bash
brew install gh
gh auth login
cd "/Users/Eliam-Code/20260701 军师 app"
gh repo create keel --private --source=. --remote=origin --push
```

### GitHub Actions Secrets（Settings → Secrets and variables → Actions）

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

### Railway（`GITHUB_SETUP.md` Step 4）

Dashboard → Deploy from GitHub → Root Directory：`track-a` → 填 Variables → Deploy → 验证 `/health`。

### push 后创建首个 agent issue（若 agent 未创建）

标题示例：`S0: Add GitHub Actions server CI 与 Railway 联通`

或在 repo 建好后让 agent 开 issue #1（PLAYBOOK S0）。

## Git 本地

- 分支：`main`
- Remote：`https://github.com/mosesdai/keel.git`
- 初始 commit：`6964c5c`

## Remote URL

（Moses push ✅；浏览器可打开确认）

```text
https://github.com/mosesdai/keel
```

## 阻塞说明

- 本机无 `brew`、`gh`（issue 需网页 New Issue 或安装 `gh`）。
- **S0 剩余**：GitHub Secrets、`RAILWAY_TOKEN` 或 Railway GitHub 集成、staging `/health`；见 `GITHUB_SECRETS.md` 与 `issues/001-S0-railway-bridge.md`。

---

## 🔍 找不到时看这里

> 给 Moses：按指引操作时，若**钥匙串里搜不到 `github.com`**，或 **Settings 里找不到 Personal access tokens**，用本章。  
> **最短路径（现在就试）**见文末 [D. 现在就试](#d-现在就试最短路径)。

### A. GitHub PAT（2026 界面）

#### 直接链接（浏览器地址栏粘贴即可）

| 用途 | 链接 |
|------|------|
| PAT 总入口（classic + fine-grained 列表） | https://github.com/settings/tokens |
| 新建 **Fine-grained** token | https://github.com/settings/personal-access-tokens/new |
| 新建 **Classic** token（推荐 Moses 先用这个） | https://github.com/settings/tokens/new |

若某个链接打开后提示 404 或跳转到登录页：先登录 **mosesdai** 账号，再点一次链接。

#### 推荐 Moses 用哪种 token

| 类型 | 适合谁 | 怎么配 |
|------|--------|--------|
| **Tokens (classic)** ✅ 推荐 | 第一次 push、想最少点击 | Generate → Note 填 `keel-push` → Expiration 自选 → 勾选 **`repo`**（整组）→ Generate → **复制 token** |
| **Fine-grained tokens** | 只想授权单个仓库 | Resource owner：`mosesdai` → Repository access：**Only select repositories** → 选 **`keel`** → Permissions → **Contents: Read and write** → Generate |

Classic 勾 **`repo`** 最简单；Fine-grained 记得仓库选 **`mosesdai/keel`** 且 Contents 要有写权限。

#### 逐步点击路径（截图级文字）

1. **打开 GitHub 并确认账号**  
   - 浏览器打开 https://github.com  
   - 看页面**右上角圆形头像**：点开应显示 **mosesdai**（或你的 GitHub 用户名）。若不是，先 Sign out 再 Sign in 正确账号。

2. **进入 Settings（设置）**  
   - 点击**右上角头像**（不要点仓库里的 Settings）  
   - 下拉菜单里点 **Settings**（齿轮图标旁的文字「Settings」）  
   - 地址栏应变为：`https://github.com/settings/profile`

3. **找到 Developer settings（开发者设置）**  
   - 看页面**左侧竖向菜单**，**一直滚到最底部**  
   - 最后一项通常是 **<> Developer settings**（带尖括号图标，在「Archived repositories」等条目下面）  
   - 若左侧菜单很长、没滚到底：容易误以为「没有 Developer settings」——**务必滚到最底**  
   - 点击 **<> Developer settings**  
   - 地址栏变为：`https://github.com/settings/apps` 或类似 `/settings/...` 下的开发者区

4. **进入 Personal access tokens**  
   - 左侧子菜单里点 **Personal access tokens**（会展开两项）  
   - 二选一：  
     - **Fine-grained tokens** → 列表页右上角 **Generate new token**  
     - **Tokens (classic)** → **Generate new token (classic)**（Moses 推荐走这条）

5. **生成并复制**  
   - 按上表勾选权限 → 点绿色 **Generate token**  
   - 页面上 **`ghp_...` 或 `github_pat_...` 只显示一次** → 立刻复制到备忘录/密码管理器  
   - **勿**粘贴到 Cursor 聊天、勿提交进 git

#### 左侧没有 Developer settings 时

- **最常见原因**：Settings 左侧栏**没滚到底**；Developer settings 在**最下方**，不在中间。  
- **确认进对了 Settings**：必须是 **头像 → Settings**（个人设置），不是仓库页 `github.com/mosesdai/keel` 顶部的 **Settings**（那是仓库设置，没有 PAT）。  
- **仍找不到**：直接用链接 https://github.com/settings/tokens/new（classic 新建页），跳过菜单点击。  
- **公司/学校账号**：部分组织会禁用 PAT；个人账号 **mosesdai** 一般无此限制。若页面写「disabled by organization」，需用 SSH 或联系组织管理员。

---

### B. 钥匙串找不到 `github.com` 时

文档里写「钥匙串搜 github.com 删除」——有时**确实搜不到**（从未保存、条目名不是 `github.com`、或在「登录」钥匙串里）。**不必纠结钥匙串**，优先用下面终端命令。

#### 打开「钥匙串访问 / Keychain Access」（若仍想手动查）

任选一种：

1. **Spotlight**：按 `⌘ + 空格` → 输入 **`钥匙串`** 或 **`Keychain Access`** → 回车  
2. **启动台**：打开 **其他** → **钥匙串访问**  
3. **Finder**：**应用程序 → 实用工具 → 钥匙串访问**  
4. **终端**：`open -a "Keychain Access"`

#### 在钥匙串里怎么搜

1. 窗口**左上角「钥匙串」**下拉：选 **登录**（login）  
2. **左下角「类别」**：选 **密码**（Passwords），**不要**选「证书」或「我的证书」  
3. 右上角搜索框依次试：**`github`**、**`git`**、**`github.com`**（不要只搜一种）  
4. 条目「种类」为 **互联网密码** 的，可能与 Git 有关；右键 **删除** 前确认不是别的网站  
5. 若**完全没有结果**：说明 push 时可能还没写入钥匙串，或凭据在别处——**直接用下方终端 erase，效果一样**

#### 更简单替代：一条终端命令（不用找钥匙串）✅

在 **终端.app** 里复制粘贴（整段一行），**回车**即可；**不会**打印成功字样，无报错即表示已尝试清除：

```bash
printf "protocol=https\nhost=github.com\n\n" | git credential-osxkeychain erase
```

然后推送，系统会**重新询问**用户名和密码：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git push -u origin main
```

- **Username**：`mosesdai`  
- **Password**：粘贴 **PAT**（不是 GitHub 登录密码；输入时屏幕不显示字符是正常的）

#### 若 erase + 新 PAT 仍 403：改用 SSH（完整步骤）

1. **生成 SSH 密钥**（邮箱换成你的 GitHub 邮箱，一路回车即可）：

```bash
ssh-keygen -t ed25519 -C "你的邮箱@example.com" -f ~/.ssh/id_ed25519_github
```

2. **启动 agent 并添加私钥**：

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github
```

3. **复制公钥**（整行，从 `ssh-ed25519` 到邮箱）：

```bash
pbcopy < ~/.ssh/id_ed25519_github.pub
```

4. **加到 GitHub**  
   - 打开 https://github.com/settings/keys  
   - **New SSH key** → Title 填 `MacBook` → Key 粘贴 → **Add SSH key**

5. **测试连接**：

```bash
ssh -T git@github.com
```

   首次会问 `Are you sure you want to continue connecting?` → 输入 **`yes`**。成功时大致出现：`Hi mosesdai! You've successfully authenticated...`

6. **改 remote 并推送**：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git remote set-url origin git@github.com:mosesdai/keel.git
git push -u origin main
```

SSH 配置好后，一般**不再需要 PAT**。

---

### C. 终极备选（完全不想碰 PAT / 钥匙串）

| 方式 | 说明 | 链接 / 操作 |
|------|------|-------------|
| **GitHub 网页上传** | 仓库页 **Add file → Upload files**，拖文件上传。适合少量文件；**不适合**整个 monorepo + 大历史，仅作应急。 | https://github.com/mosesdai/keel |
| **GitHub Desktop** | 图形界面：安装 → Sign in **mosesdai** → File → Add Local Repository → 选本机文件夹 → **Publish repository** / Push。免手输 PAT（走 Desktop 登录）。 | https://desktop.github.com |

---

### D. 现在就试（最短路径）

按顺序做，**约 5 分钟**：

1. **终端清除旧凭据**（不用开钥匙串）：

```bash
printf "protocol=https\nhost=github.com\n\n" | git credential-osxkeychain erase
```

2. **浏览器新建 Classic PAT**：  
   https://github.com/settings/tokens/new  
   → Note：`keel-push` → 勾选 **`repo`** → **Generate token** → **复制 token**

3. **推送**：

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git push -u origin main
```

   Username：`mosesdai` | Password：粘贴 token

4. **成功标志**：终端无 fatal 报错；浏览器打开 https://github.com/mosesdai/keel 能看到代码。

5. **若第 3 步仍失败**：二选一——装 [GitHub Desktop](https://desktop.github.com) 登录后 Push，或按 [B 节 SSH 步骤](#若-erase--新-pat-仍-403改用-ssh完整步骤) 改 SSH。

---

## 403 修复

`git push` 报 **403 Permission denied**（例如 `denied to mosesdai`）时，通常表示：**GitHub 已收到请求，但当前使用的账号/凭据无权写入该仓库**。与「Repository not found」（404，常见为**用户名拼错**，如 `mosesdye`）不同。

| 现象 | 含义 |
|------|------|
| `Repository not found` | 仓库不存在，或 URL 用户名错误，或私有库且当前身份无读权限 |
| `403 Permission denied` | 远程 URL 往往正确（如 `mosesdai/keel`），但 **HTTPS 用了错误或过期凭据**（旧 token、别的 GitHub 账号、或把登录密码当密码） |
| `git push -u origin ma` | 分支名笔误，应为 **`main`** |

### 常见原因（macOS + HTTPS）

1. **钥匙串（osxkeychain）里缓存了旧的 GitHub 密码或 PAT**  
   系统 `credential.helper=osxkeychain` 会在 push 时自动提交旧凭据，GitHub 已撤销或权限不足的 token 会导致 403。

2. **HTTPS 不再接受账号登录密码**  
   Push 时「密码」栏必须填 **Personal Access Token（PAT）**，不是 github.com 的登录密码。

3. **Token 权限或账号不匹配**  
   PAT 须对 `mosesdai/keel` 有 **repo**（classic）或对应 fine-grained 仓库写权限；生成 token 的 GitHub 账号须是仓库所有者或协作者。

4. **仓库侧**  
   确认 https://github.com/mosesdai/keel 已创建且当前登录网页的账号是 **mosesdai**。

### 步骤 1：确认 remote（勿改用户名）

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git remote -v
```

期望输出（fetch/push 一致）：

```text
origin	https://github.com/mosesdai/keel.git (fetch)
origin	https://github.com/mosesdai/keel.git (push)
```

若不对：`git remote set-url origin https://github.com/mosesdai/keel.git`

### 步骤 2：清除 macOS 里旧的 `github.com` 凭据

**方式 A — 终端（推荐，按提示输入后回车）**

```bash
printf "protocol=https\nhost=github.com\n\n" | git credential-osxkeychain erase
```

**方式 B — 钥匙串访问（Keychain Access）**

1. 打开「钥匙串访问」  
2. 搜索 **`github.com`**  
3. 删除与 GitHub 相关的「互联网密码」条目（尤其是旧 token / 错误账号）

清除后，下次 `git push` 会重新询问用户名与密码（密码处填 **新 PAT**）。

### 步骤 3：生成新 PAT（勿发给 agent、勿提交进 repo）

1. 浏览器登录 **mosesdai** 账号  
2. GitHub → **Settings** → **Developer settings** → **Personal access tokens**  
3. **Tokens (classic)**：Generate，勾选 **`repo`**；或 **Fine-grained**：仅授权 `keel` 仓库的 Contents 读写  
4. 复制 token（只显示一次），本地保存到密码管理器

### 步骤 4：再次推送

```bash
cd "/Users/Eliam-Code/20260701 军师 app"
git push -u origin main
```

- **Username**：`mosesdai`  
- **Password**：粘贴 **PAT**（终端不显示字符属正常）

成功后可访问：https://github.com/mosesdai/keel

### 备选：SSH（免每次 PAT）

1. 本机生成/使用已有 SSH key，公钥加到 GitHub → **Settings → SSH and keys**  
2. 文档：https://docs.github.com/en/authentication/connecting-to-github-with-ssh  
3. 改 remote：

```bash
git remote set-url origin git@github.com:mosesdai/keel.git
git push -u origin main
```

### 与本机检测对齐（2026-07-09）

- `origin` 已为 `https://github.com/mosesdai/keel.git`  
- 钥匙串中曾有 `github.com`（用户 `mosesdai`）；若 403，优先 **erase + 新 PAT** 或改 **SSH**。

