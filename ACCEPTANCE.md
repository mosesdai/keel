# 主见 / Keel 验收手册

> 日期：2026-07-09  
> 使用者：Moses、九叔、AI agents  
> 验收原则：真实帮助优先于功能打勾。功能存在但九叔不敢说真话，验收失败。

---

## 0. 验收分层

| 层级 | 日期目标 | 验收对象 | 结论口径 |
|---|---:|---|---|
| A0 Bridge | 2026-07-15 | Track A 快捷指令 + 云端 API | 九叔像装 app 一样从 iPhone 主屏使用，不碰 Cursor |
| A1 Native Alpha | 2026-07-24 | 原生 SwiftUI iPhone app | 核心闭环真机跑通，可 Ad Hoc 或本地安装 |
| A2 TestFlight | 2026-08-02 | TestFlight 外测版本 | 微信发 TestFlight 链接，九叔可安装更新 |
| A3 Stable | 2026-08-09 起 | 连续使用版本 | 连续 7 天稳定，有日志、有同步、有质量回归 |

---

## 1. 两句话最终验收

九叔能真心说出下面两句话，才算 M0 有价值：

1. **信任 DoD**：我敢在这里说腾讯/阿里续约的真实想法。
2. **诤友 DoD**：它顶了我一次，但我没觉得被冒犯。

如果功能都完成，但这两句不成立，产品方向要回炉。

---

## 2. A0 Bridge 验收（7/15）

### Moses 验收清单

- [ ] 九叔 iPhone 主屏出现入口，显示名为“主见”或 Moses 终审名，不显示“军师/反昏君/商业真心话”等敏感词。
- [ ] 九叔不需要 Cursor、命令行、GitHub、Railway、API key。
- [ ] 点击入口后能完成一次输入：说话或文字 -> 确认 -> 提交 -> 军师回复。
- [ ] 回复能体现 `PERSONALITY_CHARTER.md`：接住情绪、给判断、至少一条反对意见或脆弱假设、一个 disruptive 备选。
- [ ] 当天记录落盘到 `track-a/data/` 或九叔 iCloud 对应目录，后续能导入原生 app。
- [ ] 后端 `GET /health` 返回 ok。
- [ ] 三条质量用例按 `track-a/server/QUALITY_TESTS.md` 跑过。
- [ ] DeepSeek/Qwen key 已轮换，密钥只在 Railway/GitHub Secrets/本地 `.env`，不进 repo。

### 九叔现场验收脚本

让九叔现场试三条，不解释技术：

1. “我对腾讯/阿里续约现在真实担心的是……”
2. “我可能错在哪，你别顺着我。”
3. “常规打法之外，给一个更激进但能落地的打法。”

通过标准：
- 他愿意说具体人、具体判断、具体担心，而不是只说表面话。
- 军师有力度但不羞辱、不爹味。
- 九叔看得懂下一步该做什么。

失败信号：
- 九叔问“这个会不会被别人看到？”且解释后仍不愿说。
- 军师只复述和鼓励，没有反对意见。
- 军师用词冒犯，让九叔防御。
- 快捷指令步骤太多，他不愿再点第二次。

---

## 3. A1 Native Alpha 验收（7/24）

### 必须功能

- [ ] 原生 SwiftUI iPhone app 可在真机安装。
- [ ] 语音输入：按住说话或点击录音，生成可编辑草稿。
- [ ] 提交前确认：专有名词、金额、人名可手改后再入库。
- [ ] topic：可创建、选择、切换战略项目。
- [ ] 立场：每个 topic 有当前立场卡片。
- [ ] 日志：可查看历史 entries。
- [ ] 力谏 slider：1 只听、2 轻扶、3 常态、4 直谏、5 最高诚意。
- [ ] `/max` 或最高诚意入口可触发深度回复。
- [ ] 反昏君结构位不可关闭：重大决策必须出现“你若错，最可能错在哪”。
- [ ] 草稿不丢：录音/提交失败时可恢复。

### 暂不要求

- [ ] App Store 正式上架。
- [ ] 完整 Mac 版。
- [ ] PPT 深度解析。
- [ ] 矛盾图谱可视化。
- [ ] 多用户协作。

---

## 4. A2 TestFlight 验收（8/2）

- [ ] Apple Developer Program 可用。
- [ ] Bundle ID、签名、Capabilities 配好。
- [ ] TestFlight first external build 已通过 Beta App Review。
- [ ] public link 可复制到微信。
- [ ] 九叔点击微信链接后：安装 TestFlight -> 接受测试 -> 安装“主见/Keel”。
- [ ] build 90 天有效期已记录在 `ROADMAP.md`。
- [ ] beta 描述和截图保持 discreet，不暴露敏感商业话题。

注意：TestFlight 外部测试第一版需要 Apple 审核，不能承诺 7/15 前一定通过。

---

## 5. A3 稳定使用验收

连续 7 天：

- [ ] 每天至少 3 次有效输入。
- [ ] 每个活跃 topic 有 daily snapshot。
- [ ] iPhone 与 Mac/CloudKit 同步目标 <10 秒；Bridge Track 阶段可用 iCloud 文件替代。
- [ ] 关键词能搜到最近 30 天记录。
- [ ] 重大决策 Challenge Rate >= 70%。
- [ ] 明显矛盾 Contradiction Catch Rate >= 85%。
- [ ] 可查事实 Evidence Citation / 待核实标记 >= 90%。
- [ ] 月成本预估在 ¥150–700，超过 ¥800 触发 Moses 决策。

---

## 6. 隐私与安全验收

- [ ] 客户端不硬编码模型 API key。
- [ ] GitHub repo 不含 `.env`、证书、provisioning profile 私钥、Apple 密码。
- [ ] 服务端日志不记录原始高敏正文。
- [ ] UI 或设置页能说明当前模型供应商和保留策略。
- [ ] topic 级利益冲突屏蔽生效：谈腾讯不用腾讯托管通道，谈阿里不用阿里托管通道，除非 Moses 明确拍板。
- [ ] 删除/导出路径有文档，哪怕 M0 先手工执行。

---

## 7. 验收记录格式

每次 release PR 必须在 PR 描述里追加：

```markdown
## Acceptance
- Target: A0 / A1 / A2 / A3
- Device:
- Build:
- Passed:
- Failed:
- User quote:
- Decision needed from Moses:
```

如果没有真实设备测试，必须写明“未完成真机验收”，不能用 simulator 结果冒充交付。
