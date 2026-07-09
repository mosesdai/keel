# SESSION LOG · 军师 app / 主见 Keel

> 每轮结束由 `/liq` 自动追加。唤醒词：`军师` `主见` `Keel` `Track A`  
> 唤醒时先读 `RESUME.md`，再读本文件最新一轮的「下次从这里继续」。

---

## 模板（复制以新增一轮）

```
## [YYYY-MM-DD] 第 N 轮
- 本轮目标：
- 本轮结论（钉死的）：
- 新证据（含来源级别 A–E）：
- 仍未决 / 需九叔拍板：
- 下次从这里继续：<打开哪个文件、先干哪件事>
```

---

## [2026-07-04] 第 1 轮 · 从零到 Track A 可演示

- **本轮目标**：完成军师 app 调研与拍板，落地 7/15 前过渡方案（Track A），让 Moses 能本地跑通并「看见」产品体验。

- **本轮做了什么**：
  - **调研三份 + M0 路径**：`research/01-市场案例研究.md`（竞品与差异化）、`02-军师特质与产品化.md`（树洞×诤友×镜子、人格规范书地基）、`03-技术架构与项目组.md`（CloudKit、隐私-算力分层、模型路由、1人+AI 团队）；`04-M0-快速路径.md` 定义双轨 Track A/B。
  - **决策宪法**：`DECISIONS.md` v1.0，9 条拍板（九叔第一用户、智能优先、iPhone+Mac、Qwen/DeepSeek 日常路由、力谏可调但反昏君常驻、7/15 交付日、co-designer 等）。
  - **人格与命名**：`PERSONALITY_CHARTER.md`（5 档力谏 + 不可关底线）；`NAMING.md` 外显名 **主见 / Keel**，对内仍叫军师。
  - **Track A 实现**：`track-a/server/` FastAPI 轻后端（`/health`、`/v1/entry`、`X-API-Key`、三 topic seed、JSONL+Markdown 落盘）；`track-a/data/` 活文档结构；部署文档 `deploy/DEPLOY.md`、`RAILWAY_WALKTHROUGH.md`、`DEEPSEEK_SETUP.md`；快捷指令模板与 `JIUSHU_ONBOARDING.md`。
  - **DeepSeek 本地跑通**：`server/.env` 配置 `DEEPSEEK_API_KEY` + `KEEL_API_KEY`，`uvicorn app:app --port 8787` 可真实调用。
  - **浏览器 demo**：`track-a/demo/index.html` 单页 mockup（说 / 立场 / **历史** / 日志四 tab）；**力谏强度滑块** 1–5，绿→红实时变色；Live 模式联调 API，`POST /v1/entry` 携带 `advice_intensity`。
  - **交付排程**：`track-a/DELIVERY_PLAN.md`（07-04→07-15 每日清单）；`MOSES_CHECKLIST.md`（Moses 人工步骤）。

- **本轮结论（钉死的）**：
  - 对外名 **主见 / Keel**，对内人格 **军师**；discreet 通知不暴露敏感内容。
  - **7/15** 为 Track A 验收日；成功标准 = 九叔感到真实帮助（敢说腾讯/阿里续约真心话 + 有力度不冒犯建议），非功能打勾。
  - **模型路由**：日常默认便宜档（`deepseek-chat`）；深度场景（`/max`、`depth: deep`）才升档；利益冲突 topic 屏蔽对应云通道。
  - **力谏 slider**：1 平和 → 5 呛人；**绿（低）→ 红（高）** 语义；反昏君 + disruptive 创意**任何档位不可关**。
  - Track A 形态 = iOS 快捷指令 + 轻后端 + iCloud 落盘；原生 SwiftUI app 为 Track B（2–4 周）。

- **新证据（含来源级别）**：
  - A：Moses 拍板 `DECISIONS.md` 9 条（项目内一手）。
  - B：research 01–03 竞品与架构研究（公开资料 + 项目内综合）。
  - C：本机 DeepSeek API 调用成功、`tencent-ali-renewal` 已有首条 snapshot（`track-a/data/topics/tencent-ali-renewal/snapshots/20260704.md`）。

- **仍未决 / 需 Moses 或九叔**：
  - **Railway 未上线**：CLI 已装，需 Moses 本机 `railway login` → Variables → `railway up`（见 `track-a/deploy/RAILWAY_WALKTHROUGH.md`）。
  - **九叔快捷指令未装**：`shortcuts/SETUP.md` + `JIUSHU_ONBOARDING.md` 待当面 15 分钟 onboarding。
  - **DeepSeek API key 需轮换**：当前 key 已在开发环境使用，上线前应在 DeepSeek 控制台换新 key 并更新 Railway Variables（勿 commit `.env`）。
  - 外显名 Top 1「主见 / Keel」待 Moses 终审签字（`NAMING.md`）。

- **有价值的 know-how**：
  - **模型路由降本**：高频日常走 DeepSeek/Qwen 便宜档；反昏君/disruptive 场景保留升档资格，不因省钱降级——见 `server/app.py` 路由逻辑 + `DECISIONS.md` 决策 4。
  - **隐私与算力分层**：正文落九叔 iCloud（`track-a/data/`），后端只做 prompt 注入与模型调用、不长期存明文；高敏靠「不训练 + 路径可见 + 利益冲突屏蔽」，不靠阉割模型能力——见 research 03 §3.2 + 决策 2。
  - **Track A 过渡策略**：先让九叔「今天就能用」建立信任，数据格式（Markdown + JSONL）从第一天按 Track B 可导入设计——见 `04-M0-快速路径.md` §2.3 诚实妥协清单。
  - **demo 不等于产品**：`track-a/demo/` 是 Moses 对齐体验的预览；真实路径是快捷指令 → `/v1/entry` → iCloud 文件。

- **下次从这里继续**：
  1. 读 `RESUME.md`（入口指南）和本文件。
  2. Moses 优先：`track-a/MOSES_CHECKLIST.md` 步骤 3–7（Railway 部署 → 快捷指令填 URL/Key → 九叔首测）。
  3. 本地演示：`open "track-a/demo/index.html"`；Live 联调见 `track-a/demo/README.md`。
  4. 7/15 排程对照 `track-a/DELIVERY_PLAN.md` 07-05 起每日任务。

---

## [2026-07-09] 第 2 轮 · 方向调整为云上自主开发 + iPhone app

- **本轮目标**：按 Moses 新要求重定军师 app 交付路径：像 ipitch 一样由 agent/CI 在云上推进，Cursor 只做开发环境，最终让九叔在 iPhone app 里使用“主见 / Keel”。

- **本轮做了什么**：
  - 读取 `RESUME.md`、`SESSION_LOG.md`、`DECISIONS.md`、`track-a/`、`research/`、`PERSONALITY_CHARTER.md`、`TEAM.md`。
  - 研究 `~/.cursor/skills/ipitch/SKILL.md`：可借鉴的是固定轮次、固定门禁、固定产物、handoff，而不是某个单一云平台。
  - 核对 2026 iPhone 分发路径：TestFlight 可 public link/微信分享但首个外测 build 需 Apple beta review；Ad Hoc 需 UDID 且每类设备每年 100 台；PWA 在 iOS/微信内安装摩擦大；App Store 正式上架周期不可控。
  - 新增五份根目录手册：`PLAYBOOK.md`、`ACCEPTANCE.md`、`CLOUD_DEV.md`、`ROADMAP.md`、`GITHUB_SETUP.md`。
  - **Moses 补充分发约束**：若微信等传输困难，可用 **AirDrop** 把原生 app 给九叔——他能装上能用即可。
  - 新增 **`DISTRIBUTION.md`**（Ad Hoc AirDrop 完整手册）；更新 `ROADMAP.md`、`PLAYBOOK.md`、`GITHUB_SETUP.md`、`RESUME.md` 分发章节。

- **本轮结论（钉死的）**：
  - **7/15 不承诺原生 TestFlight app**。7/15 主路径修订为 Bridge Track：Track A 快捷指令 + 云端 API + iPhone 主屏入口，让九叔“像装 app 一样用”，且不需要 Cursor。
  - 原生 SwiftUI app 进入 7/16 后 Track B：07-24 真机 Alpha，08-02 前后 TestFlight public link 是更诚实目标。
  - **Moses 接受 AirDrop 分发**：原生 app 用 **Ad Hoc IPA + AirDrop** 给九叔（见 `DISTRIBUTION.md`）。
  - Track A 不废弃，改为 Bridge Track；它的数据和体验反馈必须迁移/反哺原生 app。
  - GitHub repo + Actions + Railway/Fly + Apple/TestFlight 签名流水线是新的工程底座；Moses 只在决策门禁介入。

- **新证据（含来源级别）**：
  - A：Moses 本轮新要求（项目一手约束）。
  - A：`DECISIONS.md` 决策 1/3/4/5/6/9：九叔脱离 Cursor、iPhone+Mac、Qwen/DeepSeek、反昏君、7/15 真实帮助优先。
  - A：`research/04-M0-快速路径.md` 已明确 48–72h 做不出完整 TestFlight，原生 TestFlight 需 2–4 周。
  - B：Apple TestFlight 文档：外部测试 public link/email，最多 10,000 外部测试员，build 90 天，首个外测 build 需 review。
  - B：Apple Developer 设备文档：Ad Hoc 每类设备每 membership year 最多 100 台，需注册设备。
  - C：PWA/iOS 资料：iOS 无自动安装提示，需 Safari 手动添加到主屏；微信内置浏览器不是可靠安装入口。

- **仍未决 / 需 Moses 拍板**：
  - GitHub repo 名与 owner。
  - Apple Developer Program 是否已有、是否支付年费（$99）、Team/Bundle ID。
  - 九叔 UDID 收集（Ad Hoc AirDrop 必需；Moses 已接受此路径）。
  - 隐私政策与 TestFlight beta review 文案。
  - 涉及腾讯/阿里时的模型路由与利益冲突屏蔽最终口径。

- **下次从这里继续**：
  1. 先读 `DISTRIBUTION.md`、`PLAYBOOK.md`、`GITHUB_SETUP.md`、`ROADMAP.md`。
  2. Moses 一次性执行 `GITHUB_SETUP.md` 第 1–4 步：建 repo、push、填 secrets、连 Railway。
  3. Moses 拍板 Apple Developer + 收九叔 UDID（原生 Alpha 前，见 `DISTRIBUTION.md` §2.2）。
  4. Agent 在云上开 PR 1：CI scaffold；PR 2：Railway deploy；PR 3：Bridge Track + `ios-adhoc.yml`。
  5. 7/15 前所有工作以 `ACCEPTANCE.md` A0 Bridge 验收为准。

---

## [2026-07-09] 第 3 轮 · 按 GITHUB_SETUP 初始化 Git + Actions 骨架

- **本轮目标**：根目录 monorepo、`git init`、安全 `.gitignore`、GitHub Actions 脚手架、本地初始 commit；能则 `gh repo create` + push + issue #1。

- **本轮做了什么**：
  - 完整对齐 `GITHUB_SETUP.md`、`PLAYBOOK.md`、`CLOUD_DEV.md`、`RESUME.md`。
  - 新增根 `.gitignore`（含 `track-a/server/.env`、活数据 `entries.jsonl`/snapshots 等）。
  - 删除 `track-a/.git` 嵌套空仓库，避免 submodule 冲突。
  - 新增 `.github/workflows/server-ci.yml`、`docs-check.yml`、`deploy-server.yml`（Railway 占位）；PR 模板与 issue 模板。
  - `git init` + `main` 分支 + 初始 commit；新增 `GITHUB_STATUS.md` 记录 Moses 待办。

- **本轮结论**：
  - 本机**未安装 `gh`**，remote / push / issue #1 **未创建**；见 `GITHUB_STATUS.md` 逐步命令。
  - 推送前门禁：`track-a/server/.env`、`.venv` 未纳入版本库；敏感 topic 活数据由 `.gitignore` 排除。

- **下次从这里继续**：
  1. Moses：`brew install gh` → `gh auth login` → `gh repo create keel --private --source=. --remote=origin --push`（见 `GITHUB_STATUS.md`）。
  2. Moses：GitHub Secrets（`KEEL_API_KEY`、`DEEPSEEK_API_KEY`、`RAILWAY_TOKEN` 等）。
  3. Agent（repo 存在后）：issue #1 + PR 完善 Railway deploy workflow；Railway Dashboard 连 GitHub `track-a` root。
