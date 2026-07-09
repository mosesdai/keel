# 主见 · Keel — 浏览器演示

Track A 目前是 **API + iOS 快捷指令**，没有原生 UI。本目录提供一个**自包含单页**，让 Moses 立刻「看见」产品体验。

---

## 最快打开（30 秒）

在项目根目录执行：

```bash
open "/Users/Eliam-Code/20260701 军师 app/track-a/demo/index.html"
```

或在浏览器地址栏直接打开该文件。

> 直接打开 `file://` 即可完整体验**内置演示数据**（三个话题、军师回复、立场、日志）。无需启动任何服务。

---

## 用本地 HTTP 打开（推荐）

部分浏览器对 `file://` 下的 fetch 有限制；若需 **Live 模式**联调 API，建议用 HTTP 提供 demo：

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a/demo"
python3 -m http.server 8765
```

浏览器访问：<http://127.0.0.1:8765/>

---

## Live 模式（可选）

演示页会尝试连接 `http://127.0.0.1:8787/health`。若 API 在线且已配置 Key，提交输入时会真实调用 `POST /v1/entry`。

### 1. 启动 Track A 后端

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a/server"
source .venv/bin/activate   # 若尚未创建 venv，见 server/README.md
uvicorn app:app --host 0.0.0.0 --port 8787 --reload
```

确保 `server/.env` 中已配置：

- `KEEL_API_KEY=...`
- `DEEPSEEK_API_KEY=...` 或 `DASHSCOPE_API_KEY=...`

### 2. 启动 demo HTTP 服务（另开终端）

```bash
cd "/Users/Eliam-Code/20260701 军师 app/track-a/demo"
python3 -m http.server 8765
```

### 3. 在演示页配置 Key

1. 打开 <http://127.0.0.1:8765/>
2. 点右上角 ⚙
3. 填入与 `server/.env` 相同的 `KEEL_API_KEY`
4. 保存后角标应显示 **Live**

若 Live 请求失败（如 CORS），页面会自动回退到内置 mock 回复，不影响演示。

---

## 页面上有什么

| 区块 | 说明 |
|------|------|
| **说** | 模拟快捷指令：按住说 → 转写确认 → 军师回复（含力谏 / 反对意见） |
| **立场** | 当前话题 `living_position` 活文档 |
| **历史** | 过往讨论列表，点开可看原始输入、军师回复、时间、话题、力谏强度 |
| **日志** | 每日快照列表，支持关键字搜索 |

顶部还有：**话题切换**（腾讯阿里版权 / 李宁 / 白酒）、**力谏强度滑块**（1 平和 → 5 呛人，绿→红实时变色）、**锁屏通知 preview**（discreet，不显示敏感内容）。

Live 模式下切换话题时会尝试 `GET /v1/topic/{slug}` 拉取 entries 填充历史；提交时 `POST /v1/entry` 会携带 `advice_intensity`（1–5）。

底部标注：**过渡版 · 7/15 交付**。

---

## 与真实 Track A 的差异

| 演示 | 真实 Track A |
|------|----------------|
| 浏览器里的手机框 mockup | iOS 快捷指令 + 语音输入，无独立 App |
| 内置 mock 或可选 Live API | 始终走 `/v1/entry` 落盘到 `data/topics/` |
| 三 tab 可视化 | 文件系统（Markdown + JSONL）+ 通知仅中性文案 |

本 demo **不是**最终产品 UI，而是 7/15 前的**体验预览**，帮助对齐「主见 / Keel 用起来是什么感觉」。
