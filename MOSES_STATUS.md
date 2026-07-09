# Moses 一页纸状态 · Keel / 军师

> 更新：**2026-07-10 关机前快照**  
> 仓库：https://github.com/mosesdai/keel

---

## 诚实边界

**Cursor 对话在你关机后不能继续。** 本次 agent 任务是把成果 **落盘并 push 到 GitHub**。  
你回来：开 Cursor 说 **「继续军师 app」**，或先读 **本文件** + [`SESSION_LOG.md`](./SESSION_LOG.md) 最新一轮。

---

## 2026-07-10 离开前 · 已完成

| 项 | 状态 |
|----|------|
| Railway `/health` | ✅ `api_key_configured: true` |
| Railway `POST /v1/entry` | ✅ 200（有效 Key）；DeepSeek 若 mock 需查 Railway `DEEPSEEK_API_KEY` |
| `DEEPSEEK_余额与预算.md` | ✅ 新建 |
| 九叔 Bridge 文档 | ✅ `JIUSHU_ONBOARDING` / `SETUP` / `JIUSHU_5MIN` / `JIUSHU_BRIDGE_READY` |
| Demo research/05 增量 | ✅ 确认卡、prompt chips、三段回复、Mac 状态条、错误态 |
| `ios/Keel/` SwiftUI 占位 | ✅ 源码骨架 + README |
| `issues/README.md` + 002–004 | ✅ 索引与正文就绪 |
| `DEPLOYMENT_STATUS.md` | ✅ curl 验收记录 |

---

## 回来第一眼看什么？

1. **[`JIUSHU_BRIDGE_READY.md`](./JIUSHU_BRIDGE_READY.md)** — 九叔装机还差哪几项  
2. **[`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md)** — 线上 API 最后验收  
3. **https://github.com/mosesdai/keel/actions** — CI 是否绿  

---

## 下一里程碑

| 日期 | 目标 |
|------|------|
| **7/15** | 九叔 Bridge Track 验收（快捷指令 + 真实帮助，见 [`ACCEPTANCE.md`](./ACCEPTANCE.md) A0） |
| **7/16+** | iOS SwiftUI Alpha（[`issues/003`](./issues/003-ios-scaffold.md)） |
| **可选 2 分钟** | GitHub Variable `KEEL_STAGING_URL` = `https://keel-production-be1c.up.railway.app` |

---

## P0 / P1 待办（你或九叔）

| 优先级 | 事项 | 状态 |
|--------|------|------|
| P0 | 九叔 iPhone 装快捷指令 + 首测 | ⏳ Moses 当面 |
| P1 | `KEEL_STAGING_URL` GitHub Variable | ⏳ 可选 |
| P1 | Railway DeepSeek 非 mock（回复无「本地兜底」） | ⏳ 查 Variables |
| P2 | GitHub 粘贴 issue **002** | 可选 |

---

## 相关入口

- 5 分钟教装：[`track-a/shortcuts/JIUSHU_5MIN.md`](./track-a/shortcuts/JIUSHU_5MIN.md)  
- 预算：[`DEEPSEEK_余额与预算.md`](./DEEPSEEK_余额与预算.md)  
- Agent SOP：[`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md)  
- 恢复开发：[`RESUME.md`](./RESUME.md)
