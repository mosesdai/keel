# GitHub Issues 草稿索引 · Keel

> 在 GitHub **New Issue** 中粘贴对应 `.md` 正文（含标题行）。  
> 仓库：https://github.com/mosesdai/keel/issues

---

| 文件 | 建议标题 | Labels | 何时开 |
|------|----------|--------|--------|
| [`001-S0-railway-bridge.md`](./001-S0-railway-bridge.md) | S0 · Railway 部署 + Bridge Track 7/15 | `agent`, `S0` | Railway 初配；**大部分已收口** |
| [`002-S1-bridge-jiushu.md`](./002-S1-bridge-jiushu.md) | S1 · Bridge Track — 九叔可用手势 / 快捷指令 | `agent`, `S1` | **staging ok 后优先** · 7/15 关键 |
| [`003-ios-scaffold.md`](./003-ios-scaffold.md) | S2 prep · SwiftUI 项目脚手架（ios/） | `agent`, `S2` | 7/16 起原生 Alpha |
| [`004-demo-from-research05.md`](./004-demo-from-research05.md) | Demo · 按 research/05 改进 UI/UX | `agent`, `S1` | demo 体验迭代；可并行 |

---

## 粘贴步骤

1. GitHub → **Issues** → **New issue**
2. 复制对应文件 **全文**（含 `#` 标题）
3. 标题用文件内 `GitHub Issue 标题` 一行
4. Labels：`agent` + `S0`/`S1`/`S2`
5. 勿粘贴任何 API key

---

## 自动 issue

- **每周一**：`.github/workflows/agent-backlog.yml` 开「S0/S1 进度检查」（无 LLM）
- 模板：`.github/ISSUE_TEMPLATE/agent-task.md`

---

## 当前推荐（2026-07-10）

1. **002** — 九叔 Bridge（文档已就绪，差九叔真机）
2. **004** — demo P1/P2（部分已在 main）
3. **003** — iOS 脚手架（`ios/Keel/` 已占位）
