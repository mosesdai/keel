# 主见 · Keel — SwiftUI 多平台客户端

> **状态**：`ios/Keel/` 源码占位已就绪 · 7/16 起 S2 Alpha  
> 交互研究：[`research/05-UI-UX与开源参考.md`](../research/05-UI-UX与开源参考.md)

Track A 当前以 **API + 快捷指令** 交付（7/15）；本目录规划 **iOS / iPadOS / macOS** 原生壳，与 `/v1/*` 后端对齐。

---

## 快速开始

1. 读 [`Keel/README.md`](./Keel/README.md) — Xcode 新建 App 并导入现有 Swift 文件  
2. Staging API：`https://keel-production-be1c.up.railway.app`  
3. Issue 任务：[`issues/003-ios-scaffold.md`](../issues/003-ios-scaffold.md)

---

## 产品定位（与 demo 一致）

- **说**：语音/文字 → 转写确认 → 请教军师（力谏 1–5）
- **立场**：话题级 `living_position`
- **日志**：每日快照，discreet 通知
- **历史**：时间线 + 状态标签（待验证 / 已验证 / 推翻）

浏览器预览：[`track-a/demo/index.html`](../track-a/demo/index.html)

---

## 目标平台

| 平台 | 优先级 | 说明 |
|------|--------|------|
| iOS | P0 | 主战场；与快捷指令互补 |
| iPadOS | P1 | 立场 + 历史分栏 |
| macOS | P2 | 菜单栏；衔接 [`track-a/mac/`](../track-a/mac/) |

---

## Tab 结构（SwiftUI `TabView`）

```
说 (Speak)     → 麦克风 / 转写 / 提交
立场 (Position) → living_position + 张力横幅
历史 (History)  → 时间线
日志 (Log)      → 快照 + 搜索
```

---

## 架构（一句话）

**SwiftUI** + **KeelAPIClient**（`URLSession`，Keychain 存 API Key）+ **CloudKit 私有库缓存**（S2 后期）。

```
┌─────────────┐     HTTPS      ┌──────────────────┐
│  SwiftUI    │ ──────────────▶│  Track A API     │
│  Views      │                │  /v1/entry …     │
└─────────────┘                └──────────────────┘
```

---

## 目录

```
ios/
├── README.md          ← 本文件
└── Keel/
    ├── KeelApp.swift
    ├── ContentView.swift
    └── README.md      ← Xcode 打开步骤
```

---

## 相关文档

- Track A API：[`track-a/server/README.md`](../track-a/server/README.md)
- 分发：[`DISTRIBUTION.md`](../DISTRIBUTION.md)
- 路线图：[`ROADMAP.md`](../ROADMAP.md)
