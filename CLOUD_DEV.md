# 云上自主开发运行手册

> 日期：2026-07-09  
> 目标：Moses 的电脑不必常开；GitHub、CI、云部署和 agent 工作流在云上推进。Moses 只在决策门禁出现时介入。

---

## 1. 目标架构

```text
GitHub Issues
  -> Agent works in cloud/dev environment
  -> Pull Request
  -> GitHub Actions
       - server CI
       - iOS simulator CI on macOS runner
       - docs checks
  -> Preview / staging deploy
  -> Moses only reviews decision gates
  -> merge to main
  -> production deploy
```

Cursor 是开发环境，不是最终 chatbot。九叔日常入口是 iPhone app；Moses 日常入口是 GitHub issue/PR 和少量审批。

---

## 2. 推荐 repo 结构

短期保守方案：保留现有 `track-a/`，新增原生与云开发目录。

```text
/
  ios/                    # SwiftUI app，7/16 后建立
  server/                 # 长期 BFF / model router，后续从 track-a/server 迁移
  track-a/                # Bridge Track：7/15 过渡交付
  docs/                   # 以后可迁移 PLAYBOOK/ACCEPTANCE 等手册
  research/               # 已有研究，不重复造轮子
  .github/
    workflows/
    ISSUE_TEMPLATE/
  PLAYBOOK.md
  ACCEPTANCE.md
  CLOUD_DEV.md
  ROADMAP.md
  GITHUB_SETUP.md
  SESSION_LOG.md
  DECISIONS.md
```

7/15 前不要重构 `track-a/` 到 `server/`，避免破坏已跑通的 FastAPI + Railway 路径。7/16 后再做迁移 PR。

---

## 3. GitHub Actions 设计

### server-ci.yml

触发：
- PR 到 `main`
- push 到 `main`

做：
- 安装 Python。
- `pip install -r track-a/server/requirements.txt`
- 运行基本 import/test。
- 启动 FastAPI，打 `/health` smoke。
- 若配置 staging URL，跑 `track-a/server/QUALITY_TESTS.md` 对应脚本。

### deploy-server.yml

触发：
- `main` 合并。
- 手动 `workflow_dispatch`。

做：
- Railway：用 `RAILWAY_TOKEN` 部署。
- Fly.io 备选：用 `FLY_API_TOKEN` 部署。
- 部署后打 `/health`。

### ios-ci.yml

触发：
- `ios/**` 变更。
- PR 到 `main`。

做：
- 使用 GitHub-hosted macOS runner。
- `xcodebuild -scheme Keel -destination 'platform=iOS Simulator,name=iPhone 16' test`
- 无签名阶段只跑 simulator。
- 真机/TestFlight 阶段再引入 Apple signing。

### ios-release.yml

触发：
- 手动 `workflow_dispatch`。
- tag，如 `ios-v0.1.0-beta1`。

做：
- 读取 App Store Connect API key。
- archive。
- 上传 TestFlight。
- 生成 release notes 草稿。

注意：iOS 真机构建需要 macOS runner。GitHub-hosted macOS 足够起步；若排队慢或签名复杂，再迁到 Codemagic/Bitrise。

### docs-check.yml

触发：
- PR 到 `main`。

做：
- 检查 `PLAYBOOK.md`、`ACCEPTANCE.md`、`CLOUD_DEV.md`、`ROADMAP.md`、`GITHUB_SETUP.md` 存在。
- 检查 PR 描述包含 Acceptance block。
- 提醒 agent 更新 `SESSION_LOG.md`。

---

## 4. Secrets 管理

绝不进 repo：

- `KEEL_API_KEY`
- `DEEPSEEK_API_KEY`
- `DASHSCOPE_API_KEY`
- `RAILWAY_TOKEN`
- `FLY_API_TOKEN`
- `APP_STORE_CONNECT_API_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`
- `APP_STORE_CONNECT_PRIVATE_KEY`
- Apple signing certificates / provisioning profiles

建议分层：

| 场景 | 放哪里 |
|---|---|
| 本地开发 | `.env`，已被 `.gitignore` 忽略 |
| GitHub CI | GitHub Actions Secrets |
| Railway/Fly runtime | 平台 Variables / Secrets |
| Apple 上传 | App Store Connect API key + GitHub Secrets |
| 九叔手机 | 不放模型 key，只放后端短 API key；长期应改 token/登录 |

密钥轮换：
- 7/15 前上线必须轮换 DeepSeek key。
- 每次外发给九叔前确认 `git status` 无 `.env`、证书、profile。
- 泄漏疑似发生时先撤销 key，再排查。

---

## 5. Agent 工作流

### Issue -> PR

每个 issue 必须包含：
- 目标阶段：S0/S1/S2/S3/S4。
- 用户价值：九叔/Moses/agent。
- DoD：引用 `ACCEPTANCE.md`。
- 是否触发 Moses 门禁。

Agent 自主做：
- 切分任务。
- 写代码。
- 写测试。
- 更新文档。
- 跑 CI。
- 修复非决策型失败。

Moses 只做：
- 看 PR 摘要。
- 批决策门禁。
- 合并 go/no-go。

### PR 模板

```markdown
## Summary

## Acceptance
- Target:
- Device:
- Passed:
- Failed:
- Decision needed from Moses:

## Risks

## Docs updated
- [ ] SESSION_LOG.md
- [ ] ROADMAP.md if milestone changed
- [ ] ACCEPTANCE.md if criteria changed
```

---

## 6. 云上 agent 推进节奏

每日无人值守循环：

1. 读取 open issues。
2. 优先处理 CI red、release blockers、7/15 Bridge Track。
3. 生成 PR。
4. 修 CI。
5. 如果没有门禁，继续下一个 issue。
6. 如果触发门禁，暂停该 PR 并 ping Moses，其他非阻塞 issue 继续。

每轮结束自动更新：
- `SESSION_LOG.md`：做了什么、证据、未决、下次从哪继续。
- `ROADMAP.md`：如果日期或里程碑变化。
- PR Acceptance block。

---

---

## 6b. Moses 关机后 agent 自主推进 SOP

Moses 按 [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md) 完成 GitHub Secrets + Railway 后即可关机。此后 agent 在本仓库与 GitHub 上按本 SOP 循环，**不**为普通工程事项打断 Moses。

### 每轮启动（读序）

1. [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md) — 确认 Railway / URL 是否已就绪
2. [`SESSION_LOG.md`](./SESSION_LOG.md) + [`RESUME.md`](./RESUME.md)
3. GitHub open issues（优先 `issues/001-S0-railway-bridge.md` 或线上 #1）
4. [`GITHUB_STATUS.md`](./GITHUB_STATUS.md) — CI / Remote 状态

### 自主循环

1. **读 issue** — 对齐阶段 S0/S1、DoD、是否触发 [`PLAYBOOK.md`](./PLAYBOOK.md) 决策门禁
2. **开分支 → 改代码/文档 → PR** — PR 模板含 Acceptance；同步 `SESSION_LOG.md`
3. **Push / 合并** — 仅当 CI 绿且无未决门禁；Moses 未在线时 agent 可在无门禁 PR 上合并（若仓库策略允许）或留 PR 待合并，**继续**非阻塞 issue
4. **部署**
   - **Railway 已连 GitHub**（Root `track-a`）：`main` 合并 → Railway **自动**构建部署；无需 Moses 本机
   - **仅有** `RAILWAY_TOKEN`：`deploy-server.yml` 在 `main` 上触发 CLI 部署
   - **两者皆无**：只 push 代码；在 PR/issue 注明「待 Moses 完成 Railway 步骤 2」，**不**假装 staging 已上线
5. **验证** — 若存在 `KEEL_STAGING_URL` 或 [`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md) 中的 URL：打 `/health`，并推进 `QUALITY_TESTS.md` 对 staging 的自动化草稿
6. **门禁** — 命中 PLAYBOOK §5 时：暂停该 PR，在 issue/PR 写清「需要 Moses 决策：…」，**其他** issue 继续

### 明确不做（需 Moses 或 Railway Dashboard）

- 登录 Railway / GitHub 替 Moses 创建 Secrets 的值
- 替九叔手机安装快捷指令或首次真机验收（除非 Moses 事后授权远程指导流程）

### 产物

每轮至少更新：`SESSION_LOG.md`；里程碑变化时更新 `ROADMAP.md` / `GITHUB_STATUS.md`；部署变化时更新 `track-a/deploy/DEPLOYMENT_STATUS.md`（不写 key）。

---

## 7. 后端部署策略

7/15 前：
- Railway 主路径，Fly.io 备选。
- 保留 `track-a/railway.toml`。
- `main` 合并后自动部署 staging；生产可先手动批准。

7/16 后：
- 把模型路由器整理为长期 `server/`。
- API 从快捷指令输入扩展为原生 app BFF。
- 长期可选 Cloudflare Workers / Railway / Fly；中国可触达性优先实测。

后端原则：
- 不长期存高敏明文。
- 日志脱敏。
- key 只在后端。
- topic 级 provider blocklist。

---

## 8. iOS 构建策略

7/15 前：
- 不把 TestFlight 当硬承诺。
- Track A 用快捷指令主屏图标完成“像装 app 一样用”。

7/16 至 7/24：
- SwiftUI app 真机 Alpha。
- 无 Apple 审核路径可用 Ad Hoc，但需要九叔 UDID。

7/25 至 8/02：
- TestFlight 外部测试。
- 微信转发 public link。
- 记住 build 90 天有效期。

正式上架：
- 隐私政策、截图、App Review 文案需要 Moses 审。
- 周期不可控，作为 M1 稳定化而不是 7/15 目标。

---

## 9. 什么时候打断 Moses

只在 `PLAYBOOK.md` 决策门禁清单内打断。典型例子：

- “请支付 Apple Developer 年费。”
- “TestFlight vs Ad Hoc 选哪个给九叔。”
- “隐私政策是否可以写 DeepSeek/Qwen 会处理输入。”
- “谈腾讯时是否允许用腾讯云通道。”
- “本月模型成本预计超过 ¥800。”
- “今晚是否把这个 build 发给九叔。”

不要为以下事情打断：

- CI 失败但能修。
- 文档需要更新。
- 代码风格。
- issue 拆分。
- Railway/Fly 普通部署重试。
- 非敏感依赖升级。
