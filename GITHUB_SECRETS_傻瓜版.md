# GitHub Secrets 傻瓜版（Moses 专用）

> **不懂请看本文件** · 详细版见 [`GITHUB_SECRETS.md`](./GITHUB_SECRETS.md)

---

## 这是什么

**一句话**：给 GitHub 上的机器人存密码，这样你关电脑它也能自动部署。

---

## 你要填几个

| 类型 | 数量 | 名称 |
|------|------|------|
| **必填** | 2 个 | `KEEL_API_KEY`、`DEEPSEEK_API_KEY` |
| **可选** | 1 个 | `RAILWAY_TOKEN`（先跳过，等 Railway 建好再填） |

---

## 逐步操作（跟着点就行）

### 1. 打开 Secrets 页面

在浏览器地址栏粘贴并回车：

**https://github.com/mosesdai/keel/settings/secrets/actions**

（若未登录 GitHub，先登录账号 `mosesdai`。）

---

### 2. 点绿色按钮

页面上方找到绿色按钮 **New repository secret**，点一下。

---

### 3. 填第一个 Secret：`KEEL_API_KEY`

| 字段 | 填什么 |
|------|--------|
| **Name** | `KEEL_API_KEY`（一字不差，全大写） |
| **Secret** | 见下方 |

**Secret 填什么：**

- 打开本机文件：`track-a/server/.env`（用「文本编辑」或 VS Code 打开）
- 找到这一行：`KEEL_API_KEY=……`
- 复制 **等号 `=` 后面** 那一整串（不要带引号）

若你本地就是 `114c173b44a498e621b8c807e2d320d2`，直接填这个也行（这是本项目的鉴权 key，不是 DeepSeek 的 key）。

填完后点绿色 **Add secret**。

---

### 4. 填第二个 Secret：`DEEPSEEK_API_KEY`

再次点 **New repository secret**。

| 字段 | 填什么 |
|------|--------|
| **Name** | `DEEPSEEK_API_KEY` |
| **Secret** | 从 `.env` 里 `DEEPSEEK_API_KEY=` 后面复制 |

**怎么复制（二选一）：**

- **方法一**：打开 `track-a/server/.env`，找到 `DEEPSEEK_API_KEY=` 那一行，复制等号后面的值
- **方法二**：终端执行（只在自己屏幕上看，**不要贴到 Cursor 聊天**）：
  ```bash
  grep DEEPSEEK_API_KEY track-a/server/.env
  ```

填完后点 **Add secret**。

> ⚠️ DeepSeek 的 key 是第三方 API 密码，**不要**发给任何人，也**不要**写进 git。

---

### 5. 第三个（可选）：`RAILWAY_TOKEN`

**现在先跳过。** 等 Railway 项目建好、需要 Actions 自动部署时再回来填。详见 [`GITHUB_SECRETS.md`](./GITHUB_SECRETS.md) 的「获取 RAILWAY_TOKEN」一节。

---

### 6. 填完应该长什么样

回到 Secrets 列表页，你应该看到 **至少 2 行名字**：

- `KEEL_API_KEY`
- `DEEPSEEK_API_KEY`

**值看不见是正常的**——GitHub 故意隐藏，只有机器人能用。

---

## 常见困惑 FAQ

### Secret 和 Password 不是一回事？

对。**Secret** 是存给 GitHub 机器人（Actions）用的「后台密码」；不是你登录 GitHub 的账号密码。你在网页上填一次，机器人跑流水线时自动读取。

### 填错了怎么办？

- 点该 Secret 右边的 **Update**，改新值；或
- 点 **Remove** 删掉，再 **New repository secret** 重建

改完保存即可，不用重启电脑。

### 不需要填到 Railway 吗？

**要，但那是下一步。** GitHub Secrets 给 GitHub Actions 用；Railway 要在它自己的 **Variables** 里再填一遍同名变量。两件事分开做，别混在一起。Railway 步骤见 [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md) 步骤 2。

---

## 填完怎么确认成功

1. 打开：https://github.com/mosesdai/keel/settings/secrets/actions  
2. 列表里能看到 `KEEL_API_KEY` 和 `DEEPSEEK_API_KEY` 两个名字 → **成功**  
3. 回到 Cursor 回复 agent：**「secrets 填好了」**

（值永远看不到；只要名字在列表里就对了。）
