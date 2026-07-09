# Cursor Cloud Agent 绑定 GitHub Issue 设置指南

> 日期：2026-07-10  
> 仓库：https://github.com/mosesdai/keel  
> 目标：Moses 关机后，Cursor Cloud Agent 可从 GitHub issue 启动，开分支、写代码、跑测试、发 PR；Moses 只 review PR 和决策门禁。

---

## 结论

**值得现在弄。** 先用最小路径跑通一次 `@cursor` issue 启动，今晚 15 分钟够；真正 24/7 自动响应 `agent` label，再多花 20-40 分钟配置 Cursor Automation。

复杂度：

- 手动 issue comment `@cursor`：**2/5 星**
- 自动监听 issue label `agent`：**3/5 星**

---

## 1. 前提条件

### Cursor 账号 / 订阅

Cursor 官方文档口径：

- Cloud Agents 需要 **paid Cursor plan**。
- Cloud Agents 使用 Max Mode 模型，按所选模型的 API pricing 计费。
- 第一次使用 Cloud Agent 时，Dashboard 会要求设置 spend limit。

Moses 需要确认：

- 若是个人 repo `mosesdai/keel`：通常 **Pro 或更高付费档**即可开始。
- 若放在团队/组织下：可能需要 Cursor team admin 连接 source control；团队自动化可用 team-owned automation。
- **费用关系【待核实】**：2026 文档与社区反馈显示，Cloud Agent 会消耗可用 usage / API usage，并可能在 included usage 用完后走 on-demand billing；最终以 Moses 的 Cursor Dashboard 为准。

### GitHub 权限

Moses 需要：

- 对 `mosesdai/keel` 有 GitHub repo admin 或 write 权限。
- 在 Cursor Dashboard 连接 GitHub，并授权 Cursor GitHub App 访问 `mosesdai/keel`。
- 允许 Cursor Cloud Agent clone repo、push branch、open PR。

注意：

- Cloud Agent 会在云 VM clone repo，不依赖 Moses 电脑在线。
- 它不能替 Moses 登录 Railway / Apple / GitHub Dashboard 填敏感 secrets。
- GitHub issue 读取权限在部分账号上可能遇到 `Resource not accessible by integration`。若发生，最稳妥做法是把 issue 正文直接粘进 agent prompt；进阶 workaround 是在 Cursor Cloud Agent environment 里配置 `GH_TOKEN`，但这会增加凭据管理复杂度。

---

## 2. 最小路径：从 GitHub Issue 手动启动

适合今晚先跑通。

1. 打开 Cursor Dashboard：`https://cursor.com/dashboard`
2. 进入 Cloud Agents / Agents / Integrations，连接 GitHub。
3. 授权 repo：选择 `mosesdai/keel`。
4. 在 Dashboard 首次启动 Cloud Agent 时设置 spend limit。建议先设小额上限，例如只够试跑 1-3 次。
5. 打开 GitHub issue，确保有 `agent` label。
6. 在 issue 下评论：

```markdown
@cursor 请按本 issue 完成任务：

1. 先读 AUTONOMOUS_DEV.md、CLOUD_DEV.md、PLAYBOOK.md。
2. 只做 issue 范围内的代码/文档修改。
3. 不读取或提交 secrets、.env、证书、profile。
4. 若触发 PLAYBOOK.md §5 决策门禁，停止并在 PR/issue 说明需要 Moses。
5. 完成后开 PR，PR 必须包含 Summary、Acceptance、Risks。
```

7. 等 Cloud Agent 开分支和 PR。
8. Moses review PR：看 diff、看 CI、看是否触发门禁；无门禁且 CI 绿再 merge。

---

## 3. 24/7 路径：Automation 监听 `agent` label

适合今晚或明天补上，实现“给 issue 打 label 后自动开跑”。

1. 打开 `https://cursor.com/automations`，或 Cursor Agents Window 里新建 automation。
2. Trigger 选 GitHub source control：
   - 类型：**Issue label changed**
   - Repo：`mosesdai/keel`
   - Label：`agent`
3. Repository 选择：
   - Single repository：`mosesdai/keel`
   - Branch：`main`
4. Tool / permission：
   - 保持 Pull request creation 开启。
   - 如需要评论 PR，可开启 Comment on pull request。
   - 不要给 Railway / Apple secrets，除非 Moses 明确知道用途。
5. Prompt 粘贴：

```markdown
你是 keel 仓库的 Cursor Cloud Agent。

每次 GitHub issue 被打上 agent label 后：

1. 读取 issue 标题、正文、labels 和引用文件。
2. 先读 AUTONOMOUS_DEV.md、CLOUD_DEV.md、PLAYBOOK.md、RESUME.md、SESSION_LOG.md。
3. 判断目标阶段 S0/S1/S2/S3/S4 和是否触发 PLAYBOOK.md §5 决策门禁。
4. 只做 issue 范围内的最小修改；优先保持 CI 绿。
5. 禁止提交 .env、API key、证书、provisioning profile、Railway/Apple secrets。
6. 不调用付费模型 API；CI 和 smoke 只能用 mock 或已有 staging URL。
7. 若触发 Moses 决策门禁，停止对应 PR，在 PR/issue 写清“需要 Moses 决策：...”，不要擅自 merge。
8. 完成后开 PR，PR 包含 Summary、Acceptance、Risks、Docs updated；同步更新 SESSION_LOG.md。
```

6. Save and activate。
7. 测试：给一个低风险 issue 加 `agent` label，观察是否创建 Cloud Agent run 和 PR。

---

## 4. Keel 项目建议

### Label

保留现有 label：

- `agent`：允许 Cloud Agent 自主处理。
- `S0` / `S1` / `S2` / `S3` / `S4`：阶段。
- `decision-gate`：需要 Moses review 后才可 merge。

### Issue 模板

现有 `.github/ISSUE_TEMPLATE/agent-task.md` 已够用。每个 agent issue 必须写清：

- 目标阶段
- 用户价值
- 任务清单
- Definition of Done
- 是否触发 Moses 决策门禁
- 参考文件

不要在 issue 里贴：

- API key
- `.env`
- Railway / Apple / GitHub token
- 九叔真实商业敏感内容截图

### 首个测试 issue

建议第一个 Cloud Agent run 用低风险前端任务：

- 草稿：`issues/004-demo-from-research05.md`
- GitHub issue 标题：`Demo · 按 research/05 改进 UI/UX`
- Labels：`agent`, `S1`

如果这个 issue 已经完成，可新建一个更小测试 issue：

```markdown
标题：Agent smoke · 检查 demo 文档和 SESSION_LOG
Labels：agent, S1

目标：
确认 Cursor Cloud Agent 能 clone keel、读文档、做小修改、开 PR。

任务：
- [ ] 读 AUTONOMOUS_DEV.md、CLOUD_DEV.md、PLAYBOOK.md
- [ ] 检查 track-a/demo/README.md 是否说明 demo 如何打开
- [ ] 如有必要，只补 1-3 行文档
- [ ] 更新 SESSION_LOG.md handoff

Definition of Done：
- PR 创建成功
- docs-check 通过
- 不改 server API，不碰 secrets
```

---

## 5. 时间估算

首次 setup：

- Cursor 连接 GitHub：5-10 分钟
- 授权 repo + 设置 spend limit：5-10 分钟
- 从 issue 评论 `@cursor` 跑通一次：5 分钟启动，等待 PR 另算
- Automation 监听 `agent` label：20-40 分钟
- 若 GitHub org / 权限 / billing 卡住：额外 15-30 分钟

每个 agent run：

- 纯文档小改：5-15 分钟
- demo / 前端小任务：20-45 分钟
- server 测试 + CI 修复：30-90 分钟
- iOS scaffold / 签名前准备：45-120 分钟
- 触发门禁或 CI 红：可能需要多轮，Moses 只处理决策与 merge。

---

## 6. Moses 必须亲手做 vs 可自动化

Moses 必须亲手做：

- Cursor 付费订阅 / spend limit。
- GitHub 授权 Cursor App 访问 `mosesdai/keel`。
- Railway Variables / Secrets 的真实值。
- Apple Developer、证书、Bundle ID、TestFlight、UDID、签名策略。
- PR 最终 review / merge，尤其是 `decision-gate`。

可自动化：

- 读取 GitHub issue。
- 开 branch、改代码、补文档。
- 跑 repo 内测试和 lint。
- 修复非决策型 CI 失败。
- 开 PR、更新 `SESSION_LOG.md`。
- 无 secrets 的 Railway 文档和 smoke 脚本。

---

## 7. 费用与风险

费用：

- Cloud Agents 使用 Max Mode 模型，按模型 API pricing 计费。
- 首次使用会要求 spend limit。
- 是否先消耗 included usage、何时进入 on-demand billing，以 Cursor Dashboard 为准。
- 建议 Moses 先设低 spend limit，跑 1-2 个小 issue 后看 Usage。

风险：

- Issue 写得太大，agent run 会变长、变贵、PR 难 review。
- Automation 如果监听太宽，可能对错误 label 或评论开跑。
- Cloud VM 没有 Moses 本机 `.env`，需要的 secrets 必须显式配置，但 keel 初期不建议给 Cloud Agent 高敏 secrets。
- Cloud Agent 可以写代码，但不能替代 Moses 的产品判断、商业敏感判断、Apple 签名和真实用户验收。

---

## 8. 今晚 15 分钟最小路径

如果 Moses 只有 15 分钟：

1. 确认 Cursor 是 paid plan，并在 Dashboard 打开 Cloud Agents。
2. 连接 GitHub，授权 `mosesdai/keel`。
3. 设置一个低 spend limit。
4. 在 GitHub 新建或打开低风险 issue，打 `agent` label。
5. 评论 `@cursor`，把 issue 正文和上面的规则粘进去。
6. 关机；明天看 PR、CI 和 Cursor Dashboard usage。

今晚先不做：

- Automation 监听 label。
- 给 Cloud Agent 配 Railway secrets。
- Apple signing / TestFlight。

---

## 9. 验收标准

Cloud Agent setup 视为跑通，当满足：

1. Cursor Dashboard 能看到 keel repo 的 Cloud Agent run。
2. Agent 能 clone `mosesdai/keel`。
3. Agent 创建了非 `main` 分支。
4. Agent 打开 PR。
5. PR 没有 secrets。
6. PR 描述包含 Summary / Acceptance / Risks。
7. GitHub Actions 能在 PR 上运行。

---

## 10. 相关文档

- [`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md)
- [`CLOUD_DEV.md`](./CLOUD_DEV.md)
- [`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md)
- [`PLAYBOOK.md`](./PLAYBOOK.md)
- [`SESSION_LOG.md`](./SESSION_LOG.md)
- Cursor Cloud Agents: https://cursor.com/docs/cloud-agent
- Cursor Automations: https://cursor.com/docs/cloud-agent/automations
