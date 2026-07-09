# 军师 app 云上自主开发 Playbook

> 日期：2026-07-09  
> 外显名：主见 / Keel  
> 内部人格：军师  
> 目标：让九叔在 iPhone app 里日常和军师对话；Cursor 只作为开发环境，不作为最终产品入口。  
> 依据：`DECISIONS.md`、`PERSONALITY_CHARTER.md`、`TEAM.md`、`research/03-技术架构与项目组.md`、`research/04-M0-快速路径.md`、`track-a/`。

---

## 0. 本轮问题重定义

用户表面要的是“像 ipitch 一样云上自主开发”。实际要解的是：**Moses 不再盯着本机 Cursor 推进工程，而是把军师变成一个 GitHub/CI/云部署可持续推进的 iPhone 产品项目；只有真人判断点才打断 Moses。**

本 playbook 能保证：
- 阶段、产物、DoD、门禁清晰，agent 可以按 issue/PR 推进。
- 7/15 前交付路径诚实：保住九叔“像装 app 一样用”的可用体验，原生 app 不做虚假承诺。
- 文档体系由 agent 自动维护，不需要 Moses 手工写 playbook、验收手册、日志。

本 playbook 不能保证：
- Apple 审核、TestFlight beta review、App Store 正式审核一定在 7/15 前通过。
- Moses 不做任何账号/付费/隐私措辞决策。
- 第三方模型、Railway、Apple、国内网络长期稳定。

---

## 1. 借鉴 ipitch 的模式

`~/.cursor/skills/ipitch/SKILL.md` 的核心不是某个云平台，而是“**固定轮次 + 固定门禁 + 固定产物 + 可 grill 的内核**”：

- R0/R1/R2/R3 每轮都有输入、产出、门禁。
- 研究材料沉入 `research/`，对外交付保持短而锋利。
- bespoke 产物和货架产物分轨，避免把临时定制误当标准产品。
- 每轮结束都能留下 handoff，让下一轮 agent 接着干。

军师项目借鉴：
- 把开发拆成 `M0 Track A`、`M0 Native Alpha`、`M0 TestFlight`、`M1 App Store/长期运营` 四个阶段。
- 每阶段必须产出代码、验收记录、决策日志、下一步 issue。
- 每个阶段设置 go/no-go，没过门禁不能假装进入下一阶段。
- 文档由 agent 在 PR 中自动更新：`SESSION_LOG.md`、`ROADMAP.md`、`ACCEPTANCE.md`、`CLOUD_DEV.md`。

军师项目要改：
- ipitch 是内容/销售工作流，军师是有账号、密钥、CI、iOS 签名、隐私风险的软件产品。
- ipitch 的“云上”可以是 agent 持续产出；军师必须落成 GitHub Actions、iOS 构建、后端部署、secrets 管理。
- ipitch 产物可 markdown/html 交付；军师最终必须是九叔 iPhone 上的可安装入口。

---

## 2. 阶段总览

| 阶段 | 日期目标 | 主产物 | DoD | 谁做 |
|---|---:|---|---|---|
| S0 云上底座 | 07-09 至 07-10 | GitHub repo、Actions、Railway/Fly、issue 模板 | 云端 CI 能跑；后端可从 GitHub 自动部署 | agent 执行，Moses 建账号/填 secrets |
| S1 7/15 过渡交付 | 07-10 至 07-15 | Track A 快捷指令 + 云端 API + iPhone 主屏图标 | 九叔可通过微信收到安装说明，装到主屏像 app 一样用；不需要 Cursor | agent 完成文档/后端，Moses 装机/首测 |
| S2 原生 Alpha | 07-16 至 07-24 | SwiftUI iPhone app **Ad Hoc + AirDrop** 可装 | 语音、topic、立场、日志、力谏 slider、历史最小闭环跑通 | agent 写代码 + CI 产 IPA，Moses AirDrop |
| S3 TestFlight Beta | 07-25 至 08-02 | TestFlight 外测链接 | 外部测试审核通过；微信分享链接可安装 | agent 准备包，Moses 审核提交/隐私措辞 |
| S4 稳定化 | 08-03 起 | App Store 或长期 TestFlight/Ad Hoc 策略 | 连续 7 天稳定使用，质量验收通过 | agent 迭代，Moses 只批门禁 |

---

## 3. 每阶段操作 playbook

### S0 云上底座

Agent 做：
- 初始化 GitHub monorepo 结构：`ios/`、`server/`、`docs/`、`track-a/`、`research/`。
- 迁移 `track-a/server` 到 `server/` 或保留 `track-a/server` 并在 Actions 明确 working directory；短期建议保留，避免 7/15 前重构风险。
- 写 GitHub Actions：
  - `server-ci.yml`：Python lint/test/health smoke。
  - `ios-ci.yml`：macOS runner 执行 `xcodebuild test`，无签名先跑 simulator。
  - `docs.yml`：检查关键文档存在并自动生成 session 摘要草稿。
- 配置 Dependabot 或等价依赖更新。
- 建 issue 模板：`decision-gate`、`feature`、`bug`、`release-check`。

Moses 做：
- 建 GitHub repo。
- 填 GitHub Secrets：模型 key、Railway token、Apple 相关凭据只填在 GitHub/App Store Connect，不进 repo。
- 授权 Railway/Fly 从 GitHub 部署。

DoD：
- PR 打开后 CI 自动跑。
- `main` 合并后后端自动部署到云。
- 任何文档变更和代码变更同 PR 交付。

### S1 7/15 过渡交付

Agent 做：
- 继续使用 `track-a/`：FastAPI + DeepSeek/Qwen 路由 + 快捷指令。
- 把快捷指令包装成九叔视角的“安装到主屏”流程：微信发链接/说明，九叔点开后按步骤添加。
- 更新 `ACCEPTANCE.md` 中 7/15 验收清单。
- 后端上线后自动跑 `track-a/server/QUALITY_TESTS.md` 三条质量用例。

Moses 做：
- 只在手机上替九叔完成一次安装或远程指导。
- 首测“腾讯阿里续约”真实输入。

DoD：
- 九叔不打开 Cursor。
- iPhone 主屏有“主见”入口。
- 一次输入能完成：语音/文字 -> 确认 -> 军师回复 -> 记录落盘。
- 军师至少一次给出反对意见或 disruptive 备选，且语气不冒犯。

### S2 原生 Alpha

Agent 做：
- 建 `ios/Keel.xcodeproj` 或 Swift Package + Xcode project。
- MVP 功能：
  - 语音输入与提交前编辑。
  - topic 创建/选择。
  - 当前立场卡片。
  - entries 日志与历史。
  - 力谏 slider 1–5。
  - `/max` 或深度模式。
  - 本地持久化，CloudKit schema 预留。
- 先用 simulator 和 Moses 设备跑通，不等待 TestFlight。

Moses 做：
- 批准 App 名、图标方向、Bundle ID、Apple Developer 账号（$99/年）。
- 收集九叔 iPhone **UDID**，注册到 Developer Portal。
- 从 Xcode 或 CI artifact 取 **Ad Hoc IPA** → **AirDrop 给九叔**（Moses 已接受此路径；见 `DISTRIBUTION.md` §2–§5）。

DoD：
- 九叔真机可安装（AirDrop 后信任描述文件即可打开）。
- 断网时不丢草稿。
- 每条重大决策回复都有反对意见结构位。

### S3 TestFlight Beta

Agent 做：
- 配好签名、版本号、隐私说明、Beta App Review 信息。
- GitHub Actions 或 Codemagic/Bitrise 产出 archive。
- 提交 TestFlight 外部测试审核。
- 生成微信可转发的 TestFlight 安装说明。

Moses 做：
- Apple Developer/App Store Connect 账号审批。
- 审隐私政策、测试说明、截图是否 discreet。
- 审核通过后把 TestFlight public link 发给九叔。

DoD：
- TestFlight public link 可打开。
- 九叔安装 TestFlight app 后能装“主见/Keel”。
- 90 天 beta 有更新节奏，不靠本机 Cursor。

### S4 稳定化

Agent 做：
- 质量回归、崩溃收集、成本监控、模型路由评测周报。
- 准备 App Store 正式上架或长期私发策略。

Moses 做：
- 只批隐私、品牌、正式上架与模型路由变更。

DoD：
- 连续 7 天稳定使用。
- 同步、检索、历史、反昏君质量达 `ACCEPTANCE.md` 标准。

---

## 4. Track A 与原生 app 的关系

不废弃 Track A。它改名为 **Bridge Track**：

- 7/15 前：主交付路径，保住“九叔立刻能用”。
- 7/16 后：原生 app 的数据种子和验收对照组。
- 原生 app 上线后：写一次性导入器，把 `track-a/data/topics/**` 导入 CloudKit/本地库。

不得做的事：
- 不在 7/15 前把 Track A 全面重构成原生 app。
- 不承诺 App Store/TestFlight 一定在 7/15 前通过。
- 不让九叔回到 Cursor。

---

## 5. 决策门禁

只有以下情况打断 Moses：

1. Apple Developer 账号、年费、团队角色、Bundle ID、证书签名。
2. TestFlight / Ad Hoc / App Store / Enterprise 分发路径选择（**Ad Hoc AirDrop 已为 Moses 可接受主路径之一**，见 `DISTRIBUTION.md`）。
3. 隐私政策、Beta Review 文案、App Store 文案中涉及数据保留、模型供应商、敏感内容的措辞。
4. 模型供应商变更，尤其涉及腾讯、阿里、字节、DeepSeek/Qwen 的路由与利益冲突屏蔽。
5. 费用超过预算告警：单人月费预计超过 ¥800，或云平台/CI 出现持续收费。
6. 架构级变更：CloudKit vs 自建云 Hub、端侧存储策略、日志保留策略。
7. 交给九叔前的 go/no-go。
8. 涉及九叔真实商业敏感内容的外部分享、截图、演示。

其他事情 agent 自主推进：代码、测试、文档、issue 分解、PR、CI 修复、部署脚本、验收记录。
