# 主见 · Keel — SwiftUI 多平台客户端

> **状态**：规划骨架 · 待 `research/05`（iOS 原生路径）定稿后细化

Track A 当前以 **API + 快捷指令** 交付；本目录规划 **iOS / iPadOS / macOS** 原生壳，与现有 `/v1/*` 后端对齐，面向高管 discreet 使用场景。

---

## 产品定位（与 demo 一致）

- **说**：语音/文字输入 → 转写确认 → 请教军师（力谏强度 1–5）
- **立场**：话题级 `living_position` 活文档，随输入生长
- **日志**：每日快照，锁屏/通知仅中性文案
- **历史**：按话题时间线回顾原始输入与军师回复

详细交互与 discreet 约束见 `track-a/demo/index.html` 与 `research/05`（待发布）。

---

## 目标平台

| 平台 | 优先级 | 说明 |
|------|--------|------|
| iOS | P0 | 主战场：快捷指令互补、通知、锁屏 discreet |
| iPadOS | P1 | 分栏：立场 + 历史并排 |
| macOS | P2 | 菜单栏/快照只读，与 `track-a/mac/` 脚本衔接 |

---

## Tab 结构（SwiftUI `TabView`）

```
说 (Speak)     → 麦克风 / 转写确认 / 提交
立场 (Position) → living_position 渲染 + 张力横幅
日志 (Log)      → 快照列表 + 搜索
历史 (History)  → 时间线 + 可展开详情
```

全局：**话题切换**、**力谏滑块**、**Live/Mock 连接状态**（Settings）。

---

## 架构（一句话）

**SwiftUI 视图层** + **CloudKit 私有库同步话题元数据/快照缓存** + **KeelAPIClient**（`URLSession` 调用 Track A `GET/POST /v1/*`，`X-API-Key` 存 Keychain）— 离线可读缓存，在线提交与拉取活文档。

```
┌─────────────┐     HTTPS      ┌──────────────────┐
│  SwiftUI    │ ──────────────▶│  Track A API     │
│  Views      │                │  /v1/entry …     │
└──────┬──────┘                └──────────────────┘
       │
       ▼
┌─────────────┐
│ CloudKit    │  话题列表、快照缓存、设备间 discreet 同步
│ (private)   │
└─────────────┘
```

---

## 目录规划（待创建 Xcode 工程）

```
ios/
├── README.md          ← 本文件
├── Keel/              ← SwiftUI App target
│   ├── App/
│   ├── Features/      Speak · Position · Log · History
│   ├── Services/      KeelAPIClient · CloudKitSync
│   └── Models/        Topic · Entry · Snapshot
└── KeelTests/
```

---

## 依赖 research/05

以下项在 `research/05-iOS原生路径.md`（工作标题）定稿后回填：

- [ ] 是否 CloudKit 为主、API 为辅，或 API-only MVP
- [ ] 快捷指令 vs App 内语音的分工
- [ ] 通知与 Widget 的 discreet 文案规范
- [ ] TestFlight / 分发路径（见 `DISTRIBUTION.md`）

---

## 相关文档

- 浏览器体验预览：`track-a/demo/`
- Track A API：`track-a/server/README.md`
- 技术架构总览：`research/03-技术架构与项目组.md`
- 产品特质：`research/02-军师特质与产品化.md`
