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

## [2026-07-10] 第 8 轮 · Moses 关机前全量 handoff

- **本轮目标**：Moses 离开前把文档、九叔 Bridge、demo/iOS、issues 索引与 curl 验收落盘并 push GitHub。

- **本轮做了什么**：
  - curl：`GET /health` → **200**，`api_key_configured: **true**`；`POST /v1/entry`（有效 Key）→ **200**（曾 mock 兜底，建议查 Railway `DEEPSEEK_API_KEY`）。
  - 新建 `DEEPSEEK_余额与预算.md`、`JIUSHU_BRIDGE_READY.md`、`track-a/shortcuts/JIUSHU_5MIN.md`、`issues/README.md`。
  - 完善 `JIUSHU_ONBOARDING.md`、`shortcuts/SETUP.md`（真实 Railway URL + Key 引用方式）。
  - demo：确认卡、prompt chips、三段回复结构、Mac 状态条 mock、低置信度错误态（research/05 §5）。
  - `ios/Keel/` SwiftUI 占位（`KeelApp.swift`、`ContentView.swift`、README）。
  - 更新 `MOSES_STATUS.md`、`DEPLOYMENT_STATUS.md`、本日志。

- **本轮结论**：
  - **GitHub = 唯一 handoff**；关机后 Cursor 不能继续，回来读 `MOSES_STATUS.md` 或说「继续军师 app」。
  - **7/15 阻塞**转为九叔真机装机（Moses decision-gate）。

- **下次从这里继续**：
  1. Moses：[`JIUSHU_BRIDGE_READY.md`](./JIUSHU_BRIDGE_READY.md) → 九叔 5 分钟装 [`track-a/shortcuts/JIUSHU_5MIN.md`](./track-a/shortcuts/JIUSHU_5MIN.md)。
  2. 可选：GitHub Variable `KEEL_STAGING_URL`；Railway 确认 DeepSeek 非 mock。
  3. Agent：粘贴 GitHub issue **002**；推进 `ios/` CI（`003`）。

---

## [2026-07-10] 第 7 轮 · Railway staging 上线验收

- **本轮目标**：Moses Railway 部署成功后公网 curl 验收，更新部署/状态文档并 push。

- **本轮做了什么**：
  - curl `GET /health` → **200**，`status":"ok"`；`api_key_configured":false`。
  - curl `POST /v1/entry`（topic `tencent-ali-renewal`）→ **503**，`服务端未配置 KEEL_API_KEY`。
  - 更新 `track-a/deploy/DEPLOYMENT_STATUS.md`、`MOSES_STATUS.md`、`RESUME.md`；新增 `track-a/shortcuts/KEEL_URL.txt`；`SETUP.md` 写入 staging entry URL。
  - 说明 GitHub Variable **`KEEL_STAGING_URL`** = `https://keel-production-be1c.up.railway.app`（无尾斜杠）。

- **本轮结论**：
  - **Railway ✅**：API 进程与域名可达；Moses 可关机，push `main` 继续自动部署。
  - **P0 余留**：Railway Variables 补 **`KEEL_API_KEY`**（+ 确认 `DEEPSEEK_API_KEY`、`DEFAULT_PROVIDER=deepseek`）→ Redeploy → 再验 entry。

- **下次从这里继续**：
  1. Moses（可选 2 分钟）：Railway 补 `KEEL_API_KEY` + Redeploy；GitHub Variable `KEEL_STAGING_URL`。
  2. Agent：entry smoke 通过后更新 `DEPLOYMENT_STATUS.md`；推进 `issues/002` 九叔 Bridge。
  3. 九叔：`track-a/shortcuts/SETUP.md` + `KEEL_URL.txt` 装快捷指令真机试。


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


---

## [2026-07-09] 第 4 轮 · Moses GitHub push 成功

- **本轮目标**：确认 `mosesdai/keel` 远程可用，更新状态文档，落 S0 issue 草稿与 Secrets 清单。

- **本轮做了什么**：
  - Moses 执行 `git push -u origin main` 成功：`main -> main`，`origin/main` 跟踪已建立。
  - 更新 `GITHUB_STATUS.md`（push ✅）、`RESUME.md`（remote URL）、本日志。
  - 新增 `issues/001-S0-railway-bridge.md`、`GITHUB_SECRETS.md`。

- **本轮结论**：
  - S0 代码底座已在 GitHub；CI workflow 骨架随 push 生效（`server-ci`、`docs-check`、`deploy-server` 占位）。
  - 阻塞转为：GitHub Actions Secrets、Railway 部署、Bridge Track 7/15 验收。

- **下次从这里继续**：
  1. Moses：按 `RAILWAY_傻瓜版.md` 完成 Railway 部署 → 发 `Railway URL: https://…`。
  2. Agent：用 `RAILWAY_STAGING_CHECKLIST.md` 跑 staging 验收；更新 `DEPLOYMENT_STATUS.md`。
  3. Moses（可选）：回填 `KEEL_STAGING_URL` GitHub Variable；创建 issue #1。
  4. S1 Bridge Track 按 `ACCEPTANCE.md` A0 推进。

---

## [2026-07-09] 第 5 轮 · Secrets 完成 + Railway 傻瓜版

- **本轮目标**：Moses 确认 GitHub Secrets 已填；产出 Railway 零基础部署文档；agent 自主推进 demo / 验收清单。

- **本轮做了什么**：
  - Moses 回复「secrets 填好了」→ GitHub `KEEL_API_KEY`、`DEEPSEEK_API_KEY` 视为 ✅。
  - 新增 [`RAILWAY_傻瓜版.md`](./RAILWAY_傻瓜版.md)（中文逐步：GitHub 登录 Railway → Root `track-a` → Variables → Generate Domain → `/health`）。
  - 新增 [`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`](./track-a/deploy/RAILWAY_STAGING_CHECKLIST.md)（agent 部署后 curl 验收）。
  - 更新 [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md)：Secrets ✅，Railway ⏳ 下一步。
  - demo 轻量改进（`research/05-UI-UX与开源参考.md` §5）：topic pill 切换、通知普通/隐身预览、力谏三档 segmented、历史状态标签。

- **本轮结论**：
  - **阻塞转为 Railway 人工部署**（约 8–12 分钟）；Moses 做完即可关机。
  - Agent 无法在 Moses 浏览器代填 Railway Variables；staging 验收待 URL 到位后执行。

- **下次从这里继续**：
  1. Moses：`RAILWAY_傻瓜版.md` 步骤 1–7 → 回复 `Railway URL: https://….up.railway.app`。
  2. Agent：`RAILWAY_STAGING_CHECKLIST.md` 验收 + 更新 `DEPLOYMENT_STATUS.md`。
  3. 可选：GitHub Variable `KEEL_STAGING_URL`；issue #1。

---

## [2026-07-10] 第 6 轮 · Moses 回归 · GitHub 自主开发机制

- **本轮目标**：审计 repo 状态；建立 Moses 关机后 agent 可持续工作的文档 + Actions + issue 草稿；诚实说明 Actions 不能替 Agent 写代码。

- **本轮做了什么**：
  - 审计：`main` 与 `origin/main`、`fix/railway-track-a-deploy` 同 commit `ea77bb1`（Railway Docker fix 已在 main，无需再 merge）。
  - 新增 [`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md)（触发器、读序、可做/不可做、ipitch 映射、现实约束）。
  - 新增 [`MOSES_STATUS.md`](./MOSES_STATUS.md)（Railway 2 步、3 检查点、下一 issue 建议）。
  - 新增 `.github/ISSUE_TEMPLATE/agent-task.md`；`.github/workflows/agent-backlog.yml`（每周 S0/S1 进度 issue，无 LLM）。
  - 增强 `deploy-server.yml` 注释（Railway GitHub 集成不必 `RAILWAY_TOKEN`）；`server-ci` / `docs-check` 路径更新。
  - 新增 `issues/002-S1-bridge-jiushu.md`、`003-ios-scaffold.md`、`004-demo-from-research05.md`。
  - 更新 `RESUME.md`、本日志。

- **本轮结论**：
  - **无人值守**：CI、Railway 自动 deploy（配好后）、每周 backlog issue、文档/issue 管理。
  - **仍需 Moses 或 Cloud Agent**：Swift/复杂 PR、九叔装机、Apple 签名、Secrets 填值。
  - **P0 阻塞仍为 Railway**：Moses 只需 Root Directory `track-a` + Redeploy（见 `MOSES_STATUS.md`）。

- **下次从这里继续**：
  1. Moses：`RAILWAY_傻瓜版.md` 或 `MOSES_STATUS.md` 2 步 → 发 `Railway URL: https://…`（勿发 key）。
  2. Agent：staging 验收 `RAILWAY_STAGING_CHECKLIST.md`；更新 `DEPLOYMENT_STATUS.md`。
  3. Moses 粘贴 issue：Railway 好后 → `issues/002`；否则可先 `issues/004` demo。
  4. 可选：Cursor Cloud Agent 处理 label `agent` 的 issues。
