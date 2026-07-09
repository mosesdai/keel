# Railway 部署傻瓜版（Moses 专用）

> **不懂请看本文件** · 详细版见 [`track-a/deploy/RAILWAY_WALKTHROUGH.md`](./track-a/deploy/RAILWAY_WALKTHROUGH.md)

---

## 这是什么

**一句话**：把军师 API 放到公网，让九叔的 iPhone 快捷指令能连上，不用你电脑一直开着。

**预计时间**：8–12 分钟。

**前提**：GitHub Secrets 已填好（`KEEL_API_KEY`、`DEEPSEEK_API_KEY`）✅

---

## 逐步操作（跟着点就行）

### 1. 打开 Railway 并登录

在浏览器地址栏粘贴并回车：

**https://railway.app**

- 若未注册：点 **Login** → 选 **Login with GitHub**（用 `mosesdai` 账号授权）
- 若已注册：直接 GitHub 登录

---

### 2. 新建项目并连 GitHub 仓库

1. 点右上角或首页 **New Project**
2. 选 **Deploy from GitHub repo**
3. 若首次使用，点 **Configure GitHub App** 授权 Railway 读你的仓库
4. 在列表里选 **`mosesdai/keel`**
5. 等 Railway 自动创建 Service（约 10–30 秒）

---

### 3. 设置 Root Directory（最关键！）

1. 点进刚创建的 **Service**（通常叫 `keel` 或仓库名）
2. 上方点 **Settings**
3. 找到 **Root Directory**
4. 填：**`track-a`**（不是仓库根目录，不是 `/`，就是这四个字母）
5. 点 **Save** 或等自动保存

> ⚠️ 若漏填或填错，部署会失败或找不到 Dockerfile。

---

### 4. 填环境变量（Variables）

1. 上方点 **Variables**
2. 点 **New Variable**，逐个添加：

| 变量名 | 值 |
|--------|-----|
| `KEEL_API_KEY` | 与 GitHub Secret 相同（从 `track-a/server/.env` 复制） |
| `DEEPSEEK_API_KEY` | 与 GitHub Secret 相同 |
| `DEFAULT_PROVIDER` | `deepseek` |
| `DEEPSEEK_MODEL_DEFAULT` | `deepseek-chat` |
| `DEEPSEEK_MODEL_DEEP` | `deepseek-reasoner` |

**怎么复制 key：**

- 打开本机 `track-a/server/.env`
- 找到 `KEEL_API_KEY=` 和 `DEEPSEEK_API_KEY=` 行，复制等号后面的值
- **不要**粘贴到 Cursor 聊天，只在 Railway 网页里填

填完后 Railway 会自动重新部署（等 2–5 分钟）。

---

### 5. 生成公网域名

1. 回到 **Settings**
2. 找到 **Networking** 区域
3. 点 **Generate Domain**
4. 记下生成的地址，形如：`https://keel-production-xxxx.up.railway.app`

---

### 6. 验证部署成功

在浏览器地址栏打开（把域名换成你的）：

**https://你的域名.up.railway.app/health**

应看到类似 `{"status":"ok"}` 或页面显示 **ok**。

若打不开或报错：点 **Deployments** → **View Logs** 看红色报错；常见原因是 Root Directory 没填 `track-a` 或 Variables 漏填。

---

### 7. 把 URL 告诉 Agent（二选一）

做完后任选一种方式，**不要发 API key**：

- 在 Cursor 对话里发：`Railway URL: https://你的域名.up.railway.app`
- 或编辑 [`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md)，在「Staging URL」一行填域名

---

### 8. （建议）回填 GitHub Variable

Railway 域名生成后，回到 GitHub：

**https://github.com/mosesdai/keel/settings/variables/actions**

点 **New repository variable**：

| 名称 | 值 |
|------|-----|
| `KEEL_STAGING_URL` | `https://你的域名.up.railway.app`（**无**尾斜杠） |

---

## 做完即可关机

自检清单：

- [ ] Root Directory = `track-a`
- [ ] Variables 已填 5 项
- [ ] `/health` 浏览器可访问
- [ ] URL 已告诉 Agent 或写入 `DEPLOYMENT_STATUS.md`

**全部打勾 → 可以关电脑。** Agent 会在云上继续开发。

---

## 常见问题

| 现象 | 处理 |
|------|------|
| 部署失败 / 502 | 检查 Root Directory 是否为 `track-a`；看 Deployments 日志 |
| `/health` 打不开 | 等部署完成（绿勾）；确认已 Generate Domain |
| 401 错误 | `KEEL_API_KEY` 与快捷指令不一致 |
| 模型报错 | 检查 `DEEPSEEK_API_KEY` 和 `DEFAULT_PROVIDER=deepseek` |

---

## 相关文档

- 详细手把手：[`track-a/deploy/RAILWAY_WALKTHROUGH.md`](./track-a/deploy/RAILWAY_WALKTHROUGH.md)
- 部署后验收 curl：[`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`](./track-a/deploy/RAILWAY_STAGING_CHECKLIST.md)
- 关机前总清单：[`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md)
