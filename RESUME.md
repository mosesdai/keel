# 下次入口指南 · 军师 app / 主见 Keel

> 工作区：`/Users/Eliam-Code/20260701 军师 app/`  
> 最后更新：2026-07-09

---

## 一句话

给 NBA China 商业侧 CEO **九叔**的私人 AI 幕僚——外显名 **主见 / Keel**，对内人格 **军师**；7/15 前用 Track A（快捷指令 + 轻后端）过渡，目标是让他脱离 Cursor、敢说真话、得到有力度且不冒犯的建议。

---

## 打开演示（复制即用）

**只看体验（内置 mock，无需服务）：**

```bash
open "/Users/Eliam-Code/20260701 军师 app/track-a/demo/index.html"
```

**Live 联调 API（另开终端）：**

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a/server"
source .venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8787 --reload
```

然后在 demo 页 ⚙ 填入与 `server/.env` 相同的 `KEEL_API_KEY`。详细步骤见 `track-a/demo/README.md`。

---

## 继续开发 · 先读这些文件

| 优先级 | 文件 | 用途 |
|--------|------|------|
| ★ | `SESSION_LOG.md` | 最新一轮做了什么、未决、下次从哪继续 |
| ★ | `DECISIONS.md` | 9 条项目宪法，改设计不改决策 |
| ★ | `track-a/MOSES_CHECKLIST.md` | Moses 人工步骤（部署、快捷指令、验收） |
| ★ | `track-a/DELIVERY_PLAN.md` | 07-04→07-15 每日清单与 DoD |
| | `PERSONALITY_CHARTER.md` | 军师人格与 5 档力谏规范 |
| | `NAMING.md` | 外显名 主见/Keel 与 discreet 规范 |
| | `TEAM.md` | 角色分工与沉淀机制 |
| | `track-a/README.md` | Track A 目录地图 |
| | `track-a/deploy/RAILWAY_WALKTHROUGH.md` | Railway 逐步部署（当前阻塞项） |
| | `track-a/deploy/DEEPSEEK_SETUP.md` | DeepSeek key 配置 |
| | `track-a/server/README.md` | 后端接口与本地启动 |
| | `track-a/shortcuts/SETUP.md` | iPhone 快捷指令搭建 |
| | `track-a/server/QUALITY_TESTS.md` | 验收质量用例 |
| ★ | `DISTRIBUTION.md` | **iPhone 分发**：Bridge Track、Ad Hoc AirDrop、TestFlight 对比与操作 |
| ★ | `PLAYBOOK.md` | 云上自主开发阶段与门禁 |
| ★ | `GITHUB_SETUP.md` | GitHub/Railway/Apple 一次性设置 |
| ★ | `ROADMAP.md` | 日期里程碑与分发路径 |

---

## 在 Cursor 里如何唤醒本话题

**建议唤醒词**（任选其一）：`军师` · `主见` · `Keel` · `Track A`

**示例唤醒语（复制粘贴）：**

> 继续军师 app Track A 开发。请先读 `RESUME.md` 和 `SESSION_LOG.md` 最新一轮，然后按 `MOSES_CHECKLIST.md` 帮我推进 Railway 部署。

Agent 应先读 `RESUME.md` + `SESSION_LOG.md`，再读任务相关的 checklist / plan，不要凭记忆续写。

---

## 给九叔的路径（Moses 转交时）

| 文件 | 说明 |
|------|------|
| `track-a/JIUSHU_ONBOARDING.md` | 15 分钟当面 onboarding 脚本（腾讯阿里版权三段真话） |
| `track-a/shortcuts/SETUP.md` | 手机快捷指令安装步骤 |
| `PASTE_TO_JIUSHU_CURSOR.md` | 九叔 Cursor 引导包（战略项目工作台，非 Track A 本体） |

Track A 本体 = 快捷指令 + 云端 API + iCloud 文件，**不需要 Cursor**。

---

## 分发路径（给九叔装 app）

| 阶段 | 路径 | Moses | 文档 |
|------|------|-------|------|
| 7/15 过渡 | Bridge Track | 微信说明或当面装主屏入口 | `JIUSHU_ONBOARDING.md` |
| 7/24 原生 | **Ad Hoc + AirDrop** | 收 UDID → 产 IPA → **AirDrop 九叔** | **`DISTRIBUTION.md`** |
| 8/02 Beta | TestFlight link | 微信发 public link | `DISTRIBUTION.md` §3.1 |

须先办 Apple Developer（$99/年）并注册九叔 UDID。7/15 前不需 Apple 账号。

---

## 7/15 前待办 Top 3

1. **Railway 部署上线** — `railway login` → 填 Variables（`KEEL_API_KEY`、`DEEPSEEK_API_KEY`、`DEFAULT_PROVIDER=deepseek`）→ `railway up` → 公网 `/health` 返回 ok。文档：`track-a/deploy/RAILWAY_WALKTHROUGH.md`
2. **九叔手机装快捷指令 + 首测** — 替换 `{{KEEL_API_URL}}` / `{{KEEL_API_KEY}}`，按 `JIUSHU_ONBOARDING.md` 完成腾讯阿里版权三段输入。文档：`track-a/shortcuts/SETUP.md`
3. **DeepSeek key 轮换 + 质量验收** — 上线前换新 key；跑通 `QUALITY_TESTS.md` 三条用例，确认「反对意见 + disruptive 备选」且不冒犯

---

## 快速路径图

```
Moses 演示          →  open track-a/demo/index.html
本地开发            →  track-a/server/ + uvicorn :8787
上线（阻塞中）      →  track-a/deploy/RAILWAY_WALKTHROUGH.md
九叔上手（未开始）  →  track-a/JIUSHU_ONBOARDING.md
验收日              →  2026-07-15（见 DELIVERY_PLAN.md）
```
