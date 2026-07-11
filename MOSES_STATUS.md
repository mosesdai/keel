# Moses 一页纸状态 · Keel / 军师

> 更新：**2026-07-11 品质升级——输出打到最高（staging 已验收 used_mock:false）**

---

## 诚实边界

**Cursor 对话在你关机后不能继续。** 本次 agent 任务是把成果 **落盘并 push 到 GitHub**。  
你回来：开 Cursor 说 **「继续军师 app」**，或先读 **本文件** + [`SESSION_LOG.md`](./SESSION_LOG.md) 最新一轮。

---

## 2026-07-11 · 品质升级（打到最高）

> 标准：Moses 自己用也要被输出不断积累、有启发、甚至害怕。详见 [`research/06-品质拉升记录.md`](./research/06-品质拉升记录.md)。

| 项 | 状态 |
|----|------|
| 人格硬注入（`system.txt` 重写）| ✅ 反昏君配额+disruptive常驻+力谏五档+解释转变不裁决+禁鸡汤/空洞平衡/复读；固定硬核块【看见】【主见】【硬反对】【disruptive】【镜子/盲点】【下一步】 |
| 生长逻辑（`app.py`）| ✅ 每轮喂近8条 entry+立场书；立场书改「演变体」（保留未决张力/军师留着的盲点/关键字）；去过短字数限 |
| 模型路由 | ✅ 日常 chat；`/max`、intensity≥4、矛盾 → **reasoner** |
| 质量闸门 | ✅ 缺硬反对/disruptive/过短 → 自动补一轮追问；仍缺标 `metadata.quality_gap` |
| Staging 实测 3 条 | ✅ **`used_mock:false`**（含 1 条自动升 reasoner）；三条都命中「顶穿/害怕」标准；【看见】能跨轮串起 3 条输入 = 积累生效 |
| ⚠️ 本地真模型 | 本地 `.env` DeepSeek key 已失效（401）→ 本地只出 mock；**需轮换本地 key** 才能本地复现 |

**Moses 下一步**：① 轮换本地 DeepSeek key（本地测真模型）；② 连续多天真实输入让立场书/盲点长出个人化深度；③ 九叔 iPhone 按 [`track-a/shortcuts/JIUSHU_5MIN.md`](track-a/shortcuts/JIUSHU_5MIN.md) 装机。

---

## 2026-07-11 · 大脑已接通

| 项 | 状态 |
|----|------|
| DeepSeek 调用链 | ✅ 端点/错误处理/显式 `used_mock` 标记 |
| `prompts/system.txt` | ✅ 注入 PERSONALITY_CHARTER 核心人格 |
| 矛盾检测 | ✅ 关键词辅助 + 模型对照立场书 |
| Railway `POST /v1/entry` | ✅ **`used_mock: false`**（2026-07-11 10:17 JST 双用例验收）；下一步九叔装机 |

**Moses 下一步**：九叔 iPhone 按 [`track-a/shortcuts/JIUSHU_5MIN.md`](track-a/shortcuts/JIUSHU_5MIN.md) 装机。

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
| P1 | Railway DeepSeek 非 mock（`used_mock: false`） | ⚠️ **换 DeepSeek key**（当前 401） |
| P2 | GitHub 粘贴 issue **002** | 可选 |

---

## 相关入口

- 5 分钟教装：[`track-a/shortcuts/JIUSHU_5MIN.md`](./track-a/shortcuts/JIUSHU_5MIN.md)  
- 预算：[`DEEPSEEK_余额与预算.md`](./DEEPSEEK_余额与预算.md)  
- Agent SOP：[`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md)  
- 恢复开发：[`RESUME.md`](./RESUME.md)
