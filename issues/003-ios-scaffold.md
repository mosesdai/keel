# S2 prep · SwiftUI 项目脚手架

> **GitHub Issue 标题**：`S2 prep · SwiftUI 项目脚手架（ios/）`  
> **Labels**：`agent`, `S2`  
> **仓库**：https://github.com/mosesdai/keel

---

## 背景

7/16 起进入 **S2 原生 Alpha**（`PLAYBOOK.md`）。本 issue 在 **不触发 Apple 签名** 的前提下，建立 `ios/` 目录与 simulator CI 骨架，供后续 Ad Hoc AirDrop 路径使用。

---

## 任务清单

### A. 项目结构（agent）

- [x] 创建 `ios/Keel/` SwiftUI app 骨架 + [`ios/Keel/README.md`](../ios/Keel/README.md)（Xcode 打开步骤）
- [x] 更新 `ios/README.md`：staging URL、目录、Tab 结构
- [x] 首屏占位：说 tab（topic pills、prompt chips、提交按钮）；立场/历史/日志 `ContentUnavailableView`
- [ ] 本地持久化预留（SwiftData / Core Data 二选一，文档说明）

### B. CI（agent）

- [ ] 新增 `.github/workflows/ios-ci.yml`：macOS runner，`xcodebuild -scheme Keel -destination 'platform=iOS Simulator,name=iPhone 16' build`（无签名）
- [ ] PR 触发路径 `ios/**`

### C. 文档

- [ ] 链接 `DISTRIBUTION.md` Ad Hoc 路径
- [ ] `ROADMAP.md` S2 里程碑勾选「脚手架」子项
- [ ] `SESSION_LOG.md` handoff

---

## Definition of Done

1. `ios/` 存在且 README 可让 Moses/Xcode 打开项目。
2. Simulator build 在 CI 或通过文档逐步可复现（CI 绿优先）。
3. **不包含** TestFlight、证书、九叔 UDID（属 decision-gate）。

---

## 决策门禁

- [ ] Apple Developer $99、Bundle ID 最终值 — **需 Moses**
- [ ] 九叔 UDID、Ad Hoc profile — **需 Moses**（S2 后期）

---

## 参考

- `PLAYBOOK.md` § S2
- `research/05-UI-UX与开源参考.md`
- `ios/README.md`（已有 skeleton 说明）
- `CLOUD_DEV.md` § ios-ci.yml
