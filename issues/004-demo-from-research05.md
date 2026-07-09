# Demo · 按 research/05 改进 track-a/demo

> **GitHub Issue 标题**：`Demo · 按 research/05 改进 UI/UX`  
> **Labels**：`agent`, `S1`  
> **仓库**：https://github.com/mosesdai/keel

---

## 背景

[`research/05-UI-UX与开源参考.md`](../research/05-UI-UX与开源参考.md) 已研究语音优先、discreet 高管风、历史/立场/力谏 pattern。`track-a/demo/index.html` 是 Moses 对齐体验的 mock；本 issue 把 research §5 建议落地到 demo（**不影响** server API 契约）。

---

## 任务清单（来自 research/05 §5 优先级）

### P0 — 已部分完成，核对并补全

- [x] Topic pill 切换 + 当前 topic 高亮
- [x] 通知预览：普通 vs 隐身（discreet）两态
- [x] 力谏：三档 segmented + 可展开 1–5 slider

### P1 — 本 issue 重点

- [x] **历史 tab**：空状态 + 时间线 + 状态标签（待验证/已验证/推翻）
- [x] **立场 tab**：活文档卡片 + 空状态
- [x] **说 tab**：按住说话 CTA + prompt chips + **确认卡**（提交前）

### P2 — 可选

- [x] 回复卡 **主见 / 为什么 / 下一步** 三段结构
- [x] Mac menu bar 状态 mock（demo 舞台旁）
- [x] 低置信度 / API 失败友好错误态 demo
- [ ] 深色金色视觉进一步微调（对比度、字号层级）

---

## Definition of Done

1. `open track-a/demo/index.html` 可演示 P1 项，无需 server 亦可 mock。
2. Live 模式仍联调 `POST /v1/entry`（见 `track-a/demo/README.md`）。
3. `SESSION_LOG.md` 记录改了哪些 tab；**不**改 `ACCEPTANCE.md` 除非 Moses 要求。

---

## Agent 可自主完成

- 纯前端 HTML/CSS/JS、截图说明、PR、docs-check 通过

## 不做

- 不调用付费模型 API
- 不替九叔验收真机快捷指令

---

## 参考

- `research/05-UI-UX与开源参考.md` §5「对 demo 的具体建议」
- `track-a/demo/README.md`
- `PERSONALITY_CHARTER.md`（力谏档位语义）
