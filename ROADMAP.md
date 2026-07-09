# 主见 / Keel Roadmap

> 日期：2026-07-09  
> 原目标：2026-07-15 九叔可用  
> 修订结论：**7/15 可交付“像装 app 一样用”的 Bridge Track；7/15 不应承诺原生 TestFlight app。原生 TestFlight 合理目标为 2026-08-02 前后。**

---

## 1. 核心结论

`research/04-M0-快速路径.md` 已经判断：48–72 小时做不出完整原生 TestFlight app，能做的是快捷指令 + 轻后端 + iCloud/文件落盘的过渡方案；可用 TestFlight 原生 app 需要 2–4 周。

本轮新要求把“过渡方案”重新定义为 **Bridge Track**：
- 不是最终产品。
- 不是废案。
- 是 7/15 前唯一诚实可交付路径。
- 数据必须能迁移到 SwiftUI app。

---

## 2. iPhone app 怎么发给九叔

> 完整手册：**`DISTRIBUTION.md`**。Moses 已接受 **Ad Hoc IPA + AirDrop** 作原生 Alpha 主路径之一。

### 方案对比（2026 中国场景）

| 方案 | 微信能不能发 | 九叔安装体验 | 时间线 | 限制 | 结论 |
|---|---|---|---:|---|---|
| Track A 快捷指令 + 主屏图标 | 可以发说明/链接/二维码 | 像装了一个“主见”入口，但本质是快捷指令 | 07-15 可行 | 无原生 UI；步骤需指导；密钥/URL 配置要小心 | **7/15 主路径** |
| TestFlight | 可以把 public link 发微信 | 先装 TestFlight，再装 app | 07-25 至 08-02 较现实 | 外部测试最多 10,000 人；build 90 天；首个外测 build 需 Apple beta review；大陆可用但审核不可控 | **原生主路径** |
| Ad Hoc + AirDrop | AirDrop `.ipa`（近场）| 真·原生 app，主屏图标 | UDID 后当天；首配 1–2 天 | 每年 100 台/类；更新需再 AirDrop | **原生 Alpha 主路径之一**（Moses 已接受）|
| Enterprise | 可以内部分发 | 安装较直接 | 不建议 | Apple Enterprise 只给组织内部员工，不能给外部个人滥用；账号风险高 | 不作为路径 |
| PWA | 可以发 URL | 需在 Safari 手动添加到主屏；微信内不是真安装 | 07-12 可做 demo | iOS 无自动安装提示；微信内置浏览器不能完整 Add to Home Screen；语音/通知/后台弱 | 只做 demo/备选，不做军师主入口 |
| App Store 正式上架 | 可以发 App Store 链接 | 最像正式 app | 08 月以后 | 审核、隐私、截图、元数据周期不可控；敏感定位要谨慎 | M1 稳定化目标 |

来源要点：
- Apple TestFlight 支持 public link/email 外部测试，最多 10,000 外部测试员，build 最多测试 90 天，首个外部测试 build 需 App Review；Apple 中文 TestFlight 页面显示该路径在中国大陆可用。
- Apple Ad Hoc 需 UDID；跳过 TestFlight beta review，**比 TestFlight 快 1–3 天**；AirDrop 是传 IPA 最稳方式。
- iOS PWA 没有自动安装提示，需 Safari 分享菜单“添加到主屏幕”；微信内置浏览器不是可靠安装入口。

### 推荐路径

主路径：
1. **07-15：微信发 Bridge Track 安装说明给九叔**。Moses 或助理按 15 分钟脚本帮他把“主见”放到 iPhone 主屏。
2. **07-18–07-24：Ad Hoc + AirDrop** — Moses/CI 产 IPA → AirDrop 九叔 → 信任描述文件。见 `DISTRIBUTION.md`。
3. **08-02：TestFlight public link**。通过微信发给九叔，九叔装 TestFlight 后安装“主见/Keel”。
4. **08 月以后：App Store 或长期 TestFlight/私有分发**。看隐私、品牌、审核策略。

不推荐：
- 7/15 承诺 TestFlight。
- 用 Enterprise 证书给九叔分发。
- 把 PWA 当最终 app。

---

## 3. 日期里程碑

### 07-09（今天）

- [x] 完成方向调整研究。
- [x] 新增 `PLAYBOOK.md`、`ACCEPTANCE.md`、`CLOUD_DEV.md`、`ROADMAP.md`、`GITHUB_SETUP.md`。
- [x] 更新 `SESSION_LOG.md`。

### 07-10

- [ ] Moses 建 GitHub repo。
- [ ] agent 建 `.github/workflows` 与 issue/PR 模板。
- [ ] Railway/Fly 从 GitHub 接入部署。
- [ ] secrets 填入 GitHub/Railway，不进 repo。

### 07-11

- [ ] 云端部署 Track A server。
- [ ] `/health` 和 `/v1/entry` 云上通过。
- [ ] 三条质量测试跑通。
- [ ] 快捷指令安装说明更新为九叔视角。

### 07-12 至 07-13

- [ ] Moses 自己手机完整走一遍：主屏入口 -> 输入 -> 回复 -> 落盘。
- [ ] 修正 prompt 分寸。
- [ ] DeepSeek/Qwen key 轮换。
- [ ] 准备给九叔的微信短说明。

### 07-14

- [ ] 九叔设备预装或远程安装演练。
- [ ] 首测三条真实问题。
- [ ] 验收结果写入 PR/`SESSION_LOG.md`。

### 07-15

- [ ] Bridge Track 对九叔交付。
- [ ] 成功口径：九叔 iPhone 主屏能用“主见”，不需要 Cursor。
- [ ] 不把 7/15 称为原生 app 发布日。

### 07-16 至 07-24

- [ ] 建 `ios/` SwiftUI app。
- [ ] 真机 Alpha：语音、topic、立场、日志、力谏 slider、历史。
- [ ] CloudKit schema 初版。
- [ ] Track A 数据导入器草案。
- [ ] 收九叔 UDID → Ad Hoc 签名 → Moses AirDrop IPA（见 `DISTRIBUTION.md`）。

### 07-25 至 08-02

- [ ] App Store Connect 配置。
- [ ] TestFlight 外部测试信息。
- [ ] 上传 build。
- [ ] 等 Apple beta review。
- [ ] 审核通过后微信发 public link 给九叔。

### 08-03 至 08-09

- [ ] 连续 7 天稳定性验收。
- [ ] 成本监控与模型路由周报。
- [ ] 决定是否准备 App Store 正式上架。

---

## 4. MVP 原生 app 范围

必须做：
- 语音输入与提交前编辑。
- topic。
- 当前立场。
- 日志与历史。
- 力谏 slider 1–5。
- `/max` 或最高诚意入口。
- 每日快照。
- CloudKit 私有同步。
- 关键词检索。
- 模型路由状态可见。

暂缓：
- Mac 版完整体验。
- PPT 深度解析。
- 矛盾图谱可视化。
- 思维画像自动提醒。
- 多用户/共享。
- 企业级审计。

---

## 5. 后端路线

7/15 前：
- 继续 FastAPI + DeepSeek/Qwen，沿用 `track-a/server`。
- Railway 主路径，Fly 备选。
- 服务只做 prompt 注入、模型路由、结构化返回，不长期存高敏明文。

7/16 后：
- 整理为长期 BFF / model router。
- 原生 app 直接调用 BFF。
- CloudKit 做同步主干，BFF 做策略、短期令牌、模型调用。

未来可评估：
- Cloudflare Workers：低运维、边缘部署，但需实测大陆可达性。
- 国内云：可达性好，但涉及腾讯/阿里等利益冲突时必须路由屏蔽。

---

## 6. 7/15 风险与备选

最大风险：
- Railway/GitHub 接入被账号或网络卡住。
- 快捷指令安装太繁琐，九叔不愿用。
- 模型回复太软或太刺，没过信任/诤友 DoD。

备选：
- Railway 不通 -> Fly.io。
- 快捷指令太繁琐 -> Moses 当面预装，九叔只点主屏图标。
- 语音问题多 -> 先文字输入，保留提交前确认。
- 模型质量不够 -> `/max` 场景切 Qwen Max/DeepSeek reasoner 或国际通道。

不可用备选：
- PWA 代替 app。
- Cursor 引导包代替 app。
- 7/15 假装 TestFlight 已是承诺交付。
