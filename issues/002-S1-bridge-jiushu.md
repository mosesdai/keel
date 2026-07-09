# S1 · Bridge Track — 九叔可用手势 / 快捷指令

> **GitHub Issue 标题**：`S1 · Bridge Track — 九叔可用手势 / 快捷指令`  
> **Labels**：`agent`, `S1`  
> **仓库**：https://github.com/mosesdai/keel

---

## 背景

7/15 前主交付为 **Bridge Track**（`track-a/`）：九叔通过 iPhone **快捷指令 + 主屏图标**使用军师，**不需要 Cursor**。本 issue 收口九叔侧「像 app 一样用」的安装与手势路径。

---

## 任务清单

### A. 快捷指令与 URL Scheme（agent）

- [x] 核对 `track-a/shortcuts/SETUP.md` 与 staging URL（`https://keel-production-be1c.up.railway.app/v1/entry`）
- [ ] 更新 `track-a/shortcuts/keel-entry.shortcut.json` 与 payload 模板（若 API 路径有变）
- [ ] 文档化 **Back Tap / 辅助触控** 触发快捷指令（可选增强，见 Apple 文档链接）
- [ ] `track-a/shortcuts/URL_SCHEME.md` 与 demo Live 模式对齐

### B. 九叔 onboarding（agent 写文档；Moses 执行）

- [x] `track-a/JIUSHU_ONBOARDING.md`：15 分钟脚本 + 真实 URL / Key 引用
- [x] `track-a/shortcuts/JIUSHU_5MIN.md` + 根目录 `JIUSHU_BRIDGE_READY.md`
- [x] 微信可转发版「安装到主屏」短说明（见 onboarding 文末）
- [ ] Moses：九叔手机完成一次安装 + 首测（**decision-gate**：交给九叔前 go/no-go）

### C. 验收

- [x] staging `/health` ok（`api_key_configured: true`，2026-07-10）
- [ ] 端到端：文字/语音 → 军师回复 → iCloud/落盘路径可见（待九叔真机）
- [ ] 军师至少一次给出**反对意见**或 disruptive 备选，语气不冒犯
- [ ] `ACCEPTANCE.md` A0 Bridge 项勾选

---

## Definition of Done

1. 九叔 iPhone 主屏有「主见/Keel」入口（快捷指令图标）。
2. 不打开 Cursor 即可完成一次真实 topic 输入。
3. 文档 handoff 写入 `SESSION_LOG.md`（不写 key 明文）。

---

## Agent 可自主完成

- 快捷指令 JSON/文档、onboarding 文案、PR + CI
- staging 可用时跑 `QUALITY_TESTS.md` 脚本草稿

## Moses 必须做

- 九叔手机安装与首测（或远程指导）
- 确认 staging URL / API key 与 Railway Variables 一致

---

## 参考

- `PLAYBOOK.md` § S1
- `ACCEPTANCE.md` A0
- `DISTRIBUTION.md` § Bridge Track
- `issues/001-S0-railway-bridge.md`（依赖 staging 上线）
