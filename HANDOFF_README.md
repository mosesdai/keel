# 主见 / Keel（军师）· 项目交接文档

> **快照日期**：2026-07-14  
> **交接人**：Moses  
> **主用户**：九叔（NBA China 商业侧 CEO）  
> **GitHub**：https://github.com/mosesdai/keel  
> **线上 API**：https://keel-production-be1c.up.railway.app

本文档是**外部同事接手开发的主入口**，可单独阅读。更细的决策与操作见文末索引表。

---

## 1. 一句话是什么

**军师 / 主见（Keel）** = 给高管用的**私人战略思考 OS**：树洞（敢说）+ 诤友（敢顶）+ 镜子（帮你看清自己）。外显名 **主见 / Keel**，对内人格仍叫 **军师**。

---

## 2. 谁、为什么

| 角色 | 说明 |
|------|------|
| **Moses** | 产品/技术负责人 + 终审；版权续约（腾讯/阿里）、李宁 pitch、白酒等战略案子的幕僚需求来源之一 |
| **九叔** | 第一用户 + co-designer；NBA China 商业侧 CEO，不是工程师，**必须脱离 Cursor** |
| **AI agents** | 写代码、文档、prompt、CI；关键决策须 Moses 拍板 |

**商业背景**：九叔手上有腾讯/阿里版权续约、李宁 Curry 合作、白酒双签等高压决策。军师要让他敢说真心话，并给出**有力度、不迎合、带 disruptive 创意、不冒犯**的建议。

**为什么不是 Cursor 引导包**：`PASTE_TO_JIUSHU_CURSOR.md` 是九叔战略工作台的临时手段；**独立 app 才是终点**（见 `DECISIONS.md` 决策 1）。

---

## 3. 当前状态快照（2026-07-14）

### 已通 ✅

| 项 | 状态 |
|----|------|
| GitHub 仓库 | `mosesdai/keel`，`main` 分支，CI workflow 已配 |
| Railway 部署 | Root Directory = `track-a`；URL 见上 |
| `GET /health` | HTTP 200，`deepseek_configured: true` |
| `POST /v1/entry` | HTTP 200，**`used_mock: false`**（2026-07-11 验收） |
| DeepSeek 大脑 | `system.txt` 注入人格；矛盾检测；质量闸门；生长逻辑（近 8 条 + 立场书） |
| 品质升级 | 固定输出块【看见】【主见】【硬反对】【disruptive】【镜子/盲点】【下一步】 |
| Track A 全栈 | FastAPI 后端 + demo + 快捷指令文档 + 三 topic seed |
| iOS 占位 | `ios/Keel/` SwiftUI 骨架（无 `.xcodeproj`） |
| 文档体系 | PLAYBOOK / ACCEPTANCE / ROADMAP / SESSION_LOG 等 |

### 未完成 ⏳

| 项 | 说明 |
|----|------|
| **九叔真机装机** | P0；文档已就绪，差 Moses 当面 5–15 分钟 |
| **7/15 Bridge 验收** | 九叔主屏能用「主见」，敢说腾讯/阿里真话（见 `ACCEPTANCE.md` A0） |
| **本地 DeepSeek key** | 本地 `.env` key 已失效（401）；staging 正常，本地需轮换 key |
| **GitHub Variable** | `KEEL_STAGING_URL` 可选回填 |
| **原生 SwiftUI app** | Track B，7/16 后起 |

### 时间线：Bridge Track vs 原生 app

```
07-04 ──► Track A 实现（快捷指令 + 轻后端 + iCloud 落盘）
07-09 ──► 修订：7/15 = Bridge Track，不承诺 TestFlight
07-10 ──► Railway staging 上线
07-11 ──► 大脑接通 + 品质打到最高
07-15 ──► 【目标】九叔 Bridge Track 验收（A0）
07-16~24 ──► SwiftUI 原生 Alpha（Ad Hoc + AirDrop）
07-25~08-02 ──► TestFlight 外测
08-03+ ──► 稳定化 / App Store 评估
```

**诚实边界**：7/15 交付的是「像装 app 一样用」的**快捷指令 + 云端 API**，不是原生 TestFlight app。

---

## 4. 仓库地图

```
/
├── HANDOFF_README.md      ← 本文档（交接主入口）
├── README.md              ← 简短入口，指向本文档
├── DECISIONS.md           ← 9 条项目宪法（改设计不改决策）
├── PERSONALITY_CHARTER.md ← 军师人格规范书（system prompt 地基）
├── NAMING.md              ← 外显名 主见/Keel + discreet 规范
├── TEAM.md                ← 角色分工与人类审批点
├── SESSION_LOG.md         ← 每轮进度日志（唤醒时先读最新一轮）
├── RESUME.md              ← 开发恢复入口 + demo 命令
├── MOSES_STATUS.md        ← Moses 一页纸状态
├── PLAYBOOK.md            ← 云上自主开发阶段与门禁
├── ACCEPTANCE.md          ← 验收手册（A0–A3）
├── ROADMAP.md             ← 日期里程碑
├── DISTRIBUTION.md        ← iPhone 分发（Bridge / Ad Hoc / TestFlight）
├── AUTONOMOUS_DEV.md      ← Agent 关机后可持续工作 SOP
├── CLOUD_DEV.md           ← 云开发环境说明
├── GITHUB_SETUP.md        ← GitHub/Railway/Apple 一次性设置
├── GITHUB_SECRETS.md      ← Secrets 清单
├── RAILWAY_傻瓜版.md       ← Railway 零基础部署
├── PASTE_TO_JIUSHU_CURSOR.md  ← 九叔 Cursor 引导包（非 Track A 本体）
│
├── research/              ← 调研报告（01–06）
│   ├── 01-市场案例研究.md
│   ├── 02-军师特质与产品化.md
│   ├── 03-技术架构与项目组.md
│   ├── 04-M0-快速路径.md
│   ├── 05-UI-UX与开源参考.md
│   └── 06-品质拉升记录.md
│
├── track-a/               ← 7/15 Bridge Track 实现
│   ├── server/            ← FastAPI 后端（app.py, prompts/, Dockerfile）
│   ├── data/              ← topic 活文档（JSONL + Markdown，gitignore 活数据）
│   ├── demo/              ← 浏览器 mockup（力谏滑块、Live 联调）
│   ├── shortcuts/         ← iPhone 快捷指令搭建（JIUSHU_5MIN.md）
│   ├── deploy/            ← 部署手册 + DEPLOYMENT_STATUS.md
│   ├── mac/               ← Mac companion 脚本
│   ├── scripts/           ← iCloud 同步
│   ├── JIUSHU_ONBOARDING.md
│   ├── DELIVERY_PLAN.md
│   └── MOSES_CHECKLIST.md
│
├── ios/Keel/              ← SwiftUI 占位（Track B）
├── issues/                ← GitHub issue 草稿（001–004）
└── .github/workflows/     ← server-ci, deploy-server, docs-check, agent-backlog
```

---

## 5. 已完成清单

### 调研与决策
- [x] `research/01–04` 市场、人格、架构、M0 路径
- [x] `DECISIONS.md` v1.0 九条宪法
- [x] `PERSONALITY_CHARTER.md` 五档力谏 + 反昏君/disruptive 常驻
- [x] `NAMING.md` Top 1：**主见 / Keel**

### Track A 实现
- [x] FastAPI：`/health`、`/v1/entry`、`X-API-Key` 鉴权
- [x] 三 topic seed：`tencent-ali-renewal`、`lining-pitch`、`baijiu-wly-lzlj`
- [x] JSONL + Markdown 落盘（`track-a/data/`）
- [x] 浏览器 demo（四 tab + 力谏滑块 1–5）
- [x] 快捷指令模板 + 九叔 onboarding 文档

### 部署
- [x] Railway staging：`keel-production-be1c.up.railway.app`
- [x] GitHub Actions：server-ci、deploy-server、docs-check
- [x] Docker + `railway.toml`（Root = `track-a`）

### 大脑与品质
- [x] DeepSeek 调用链 + `used_mock` 显式标记
- [x] `system.txt` 人格硬注入
- [x] 矛盾检测 + 立场书演变体
- [x] 模型路由：日常 chat；`/max`/intensity≥4/矛盾 → reasoner
- [x] 质量闸门：缺硬反对/disruptive → 自动补轮
- [x] `research/06-品质拉升记录.md`

### 文档与工程底座
- [x] PLAYBOOK / ACCEPTANCE / ROADMAP / DISTRIBUTION
- [x] AUTONOMOUS_DEV + issues 001–004 草稿
- [x] `ios/Keel/` SwiftUI 占位
- [x] `SESSION_LOG.md` 8 轮记录

---

## 6. 产品设计要点

| 要点 | 说明 |
|------|------|
| **生长性** | 断续输入 → 立场书演变 → 跨轮串起【看见】；不是一次性聊天 |
| **矛盾处理** | 关键词 + 模型对照 `living_position`；解释转变不裁决 |
| **力谏滑块** | 1 平和 → 5 呛人；绿→红语义；**反昏君 + disruptive 任何档位不可关** |
| **反昏君** | 主人逻辑跳跃/证据不足/过度乐观时必须直言；对应 `/ifalsify` |
| **discreet 命名** | 锁屏/通知/主屏显示「主见」，不暴露「军师/反昏君/商业真心话」 |
| **验收标准** | 不是功能打勾，是九叔敢说真话 + 被顶了但没被冒犯 |

---

## 7. 技术架构

```
┌─────────────────────────────────────────────────────────┐
│  iPhone（九叔）                                          │
│  ┌──────────────┐    ┌──────────────┐                   │
│  │ 快捷指令      │    │ SwiftUI app  │  ← Track B 7/16+  │
│  │ (Track A)    │    │ (ios/Keel)   │                   │
│  └──────┬───────┘    └──────┬───────┘                   │
└─────────┼───────────────────┼───────────────────────────┘
          │ POST /v1/entry    │
          ▼                   ▼
┌─────────────────────────────────────────────────────────┐
│  Railway · FastAPI (track-a/server)                     │
│  · 人格注入 (system.txt + PERSONALITY_CHARTER)          │
│  · 模型路由 (DeepSeek chat / reasoner, Qwen 后备)       │
│  · 矛盾检测 + 质量闸门                                   │
│  · 不落盘高敏明文到云端（落盘在 data/ 或 iCloud）        │
└─────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────┐
│  数据层                                                  │
│  · track-a/data/topics/<slug>/entries.jsonl             │
│  · living_position.md + snapshots/                      │
│  · 规划：CloudKit 私有库（Track B）                      │
└─────────────────────────────────────────────────────────┘

Mac companion：track-a/mac/（看快照、打字补充）
```

**模型路由**（`DECISIONS.md` 决策 4）：
- 日常：`deepseek-chat`（便宜档）
- 深度：`/max`、intensity≥4、矛盾 → `deepseek-reasoner`
- 利益冲突：谈腾讯不用腾讯云通道（topic 级 blocklist）

**平台**：仅 iPhone + Mac（决策 3）；不做 Android/Web 正式版。

---

## 8. 本地如何跑

### 8.1 只看体验（无需服务）

```bash
open "track-a/demo/index.html"
```

内置 mock，有力谏滑块、四 tab、通知预览。

### 8.2 本地 API + Live 联调

```bash
cd track-a/server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env：填入 KEEL_API_KEY 和 DEEPSEEK_API_KEY（勿 commit）
uvicorn app:app --host 0.0.0.0 --port 8787 --reload
```

另开终端验证：

```bash
curl -sS "http://127.0.0.1:8787/health"
curl -sS -X POST "http://127.0.0.1:8787/v1/entry" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEEL_API_KEY" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"本地联调","advice_intensity":3}'
```

然后在 demo 页 ⚙ 填入相同 `KEEL_API_KEY` 切 Live 模式。详见 `track-a/demo/README.md`。

> **注意**：截至 2026-07-11，本地 DeepSeek key 可能已失效（401），staging 正常。本地测真模型需轮换 key。

### 8.3 环境变量（`.env`）

| 变量 | 必填 | 说明 |
|------|------|------|
| `KEEL_API_KEY` | ✅ | 快捷指令 `X-API-Key` |
| `DEEPSEEK_API_KEY` | ✅* | 至少配一个模型 key |
| `DASHSCOPE_API_KEY` | 可选 | Qwen 后备 |

完整列表见 `track-a/server/.env.example`。

---

## 9. 线上如何维护

### 9.1 Railway Variables（在 Dashboard 填，不进 repo）

| 变量 | 说明 |
|------|------|
| `KEEL_API_KEY` | 服务鉴权 |
| `DEEPSEEK_API_KEY` | DeepSeek 调用 |
| `DEFAULT_PROVIDER` | `deepseek` |

傻瓜版步骤：`RAILWAY_傻瓜版.md`、`track-a/server/RAILWAY_VARIABLES_傻瓜版.md`

### 9.2 部署与 Redeploy

- Railway 已连 GitHub：`push main` → 自动部署
- Root Directory 必须是 **`track-a`**
- 改 Variables 后须 **Redeploy**

### 9.3 Health 验收（不含 key）

```bash
curl -sS "https://keel-production-be1c.up.railway.app/health"
```

期望：`status: ok`，`deepseek_configured: true`

Entry 验收见 `track-a/deploy/DEPLOYMENT_STATUS.md`（需 `X-API-Key`，勿把 key 写进文档）。

### 9.4 GitHub Secrets（CI 用）

`KEEL_API_KEY`、`DEEPSEEK_API_KEY` 等 — 见 `GITHUB_SECRETS.md`

---

## 10. 打算做但未完成

| 优先级 | 事项 | 文档 |
|--------|------|------|
| **P0** | 九叔 iPhone 装快捷指令 + 首测三条真话 | `track-a/shortcuts/JIUSHU_5MIN.md` |
| **P0** | 7/15 Bridge Track 验收（A0） | `ACCEPTANCE.md` |
| P1 | 本地 DeepSeek key 轮换 | `DEEPSEEK_余额与预算.md` |
| P1 | GitHub Variable `KEEL_STAGING_URL` | `GITHUB_SETUP.md` |
| S2 | SwiftUI 真机 Alpha（语音、topic、力谏、CloudKit） | `issues/003-ios-scaffold.md` |
| S2 | Ad Hoc IPA + AirDrop 给九叔 | `DISTRIBUTION.md` |
| S3 | TestFlight public link（~08-02） | `DISTRIBUTION.md` |
| 未来 | Cloud Agent 自动化处理 `agent` label issues | `AUTONOMOUS_DEV.md` |
| 未来 | 思维画像自动提醒、矛盾图谱可视化 | `ROADMAP.md` §4 暂缓项 |

---

## 11. 决策门禁（只有 Moses / 产品主需要拍板）

以下事项 **agent 不可自行决定**，须开 `decision-gate` issue 或当面确认：

1. **架构变更**（如后端从 FastAPI 迁 Workers、数据层从文件迁 CloudKit schema）
2. **隐私策略变更**（数据留存、供应商、训练承诺）
3. **模型供应商变更**（日常主力从 DeepSeek 换 Qwen 等）
4. **上线交给九叔**（go/no-go）
5. **外显名终审**（当前 Top 1：主见/Keel，待 Moses 签字）
6. **Apple Developer / Bundle ID / UDID 收集**
7. **涉及腾讯/阿里的模型路由与利益冲突屏蔽最终口径**
8. **人格底线条款变更**（反昏君/disruptive 不可关 — 原则上永不改）

---

## 12. 安全红线

| 红线 | 说明 |
|------|------|
| **勿 commit `.env`** | 已在 `.gitignore`；含 `KEEL_API_KEY`、`DEEPSEEK_API_KEY` |
| **勿泄露 API key** | 不进 issue/PR/文档/chat；轮换后旧 key 作废 |
| **勿 commit 活数据** | `entries.jsonl`、`living_position.md`、snapshots 已 gitignore |
| **商业机密** | 腾讯/阿里续约、李宁金额、白酒策略等 topic 正文不进公开 repo |
| **zip 交接** | 本包已排除 `.env`、`.venv`、`.git`；密钥在 Moses 处单独交接 |

---

## 13. 建议同事从哪里开工

按你手上的权限和时间，三选一：

### 选项 A · 推进 7/15 验收（推荐，若你能接触九叔或 Moses）

1. 读 `ACCEPTANCE.md` A0 + `track-a/shortcuts/JIUSHU_5MIN.md`
2. 协助 Moses 完成九叔真机装机
3. 现场跑三条验收脚本（腾讯/阿里真话、别顺着我、disruptive 打法）
4. 结果写入 `SESSION_LOG.md`

### 选项 B · 后端与品质（推荐，若你偏工程）

1. `git clone https://github.com/mosesdai/keel.git`
2. 本地跑 `track-a/server`（Moses 提供 key 或你用 staging curl）
3. 跑 `track-a/server/QUALITY_TESTS.md` 三条用例
4. 修 `used_mock`、质量闸门、prompt 分寸；开 PR

### 选项 C · 原生 iOS（7/16 起）

1. 读 `issues/003-ios-scaffold.md` + `DISTRIBUTION.md`
2. Xcode 新建 Keel 工程合并 `ios/Keel/` 源码
3. 实现 `KeelAPIClient` 对接 staging
4. Moses 拍板 Bundle ID + 收九叔 UDID → Ad Hoc

---

## 14. 关键文档索引

| 文档 | 路径 | 用途 |
|------|------|------|
| 项目宪法 | `DECISIONS.md` | 9 条拍板，改设计不改决策 |
| 人格规范 | `PERSONALITY_CHARTER.md` | system prompt 地基 |
| 验收手册 | `ACCEPTANCE.md` | A0–A3 分层验收 |
| 开发 Playbook | `PLAYBOOK.md` | S0–S4 阶段与门禁 |
| 路线图 | `ROADMAP.md` | 日期里程碑 |
| 分发手册 | `DISTRIBUTION.md` | Bridge / Ad Hoc / TestFlight |
| 恢复开发 | `RESUME.md` | demo 命令 + 唤醒语 |
| 进度日志 | `SESSION_LOG.md` | 每轮 handoff |
| Moses 状态 | `MOSES_STATUS.md` | 一页纸当前状态 |
| Track A 入口 | `track-a/README.md` | 子目录地图 |
| 部署状态 | `track-a/deploy/DEPLOYMENT_STATUS.md` | staging URL + curl 记录 |
| 九叔 5 分钟装机 | `track-a/shortcuts/JIUSHU_5MIN.md` | P0 阻塞项 |
| 品质记录 | `research/06-品质拉升记录.md` | 打到最高的标准 |
| M0 路径 | `research/04-M0-快速路径.md` | Track A/B 双轨 |
| 架构研究 | `research/03-技术架构与项目组.md` | CloudKit、隐私分层 |
| Agent SOP | `AUTONOMOUS_DEV.md` | 无人值守机制 |
| Issue 草稿 | `issues/README.md` | 001–004 粘贴指南 |

---

## 15. 获取最新代码

本 zip 是 **2026-07-14 快照**，不含 `.git`。持续开发请：

```bash
git clone https://github.com/mosesdai/keel.git
cd keel
# 读本文档 → RESUME.md → SESSION_LOG.md 最新一轮
```

**唤醒词**（Cursor）：`军师` · `主见` · `Keel` · `Track A`

---

*交接包生成：2026-07-14 · Moses · 有问题先读 `SESSION_LOG.md` 最新一轮「下次从这里继续」*
