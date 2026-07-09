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

- [ ] Topic pill 切换 + 当前 topic 高亮
- [ ] 通知预览：普通 vs 隐身（discreet）两态
- [ ] 力谏：三档 segmented + 绿→红语义（或保留 slider，文档说明）

### P1 — 本 issue 重点

- [ ] **历史 tab**：空状态文案 + 首条记录后的时间线样式（参考 Voicenotes / Day One 时间线）
- [ ] **立场 tab**：当前立场卡片结构（结论 / 开放问题 / 上次更新）
- [ ] **说 tab**：打开即录/即输入的 primary CTA 层级（一键说话视觉权重）

### P2 — 可选

- [ ] 深色金色视觉微调（对比度、字号层级）
- [ ] Live 模式错误态（API 失败友好提示，不泄露 key）

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
