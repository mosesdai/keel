# iPhone 快捷指令搭建（主见 / Keel）

目标链路：`录音/听写 -> 人工改错 -> 选 topic -> POST -> 展示回复 -> 写 iCloud`

**5 分钟当面教九叔**：[`JIUSHU_5MIN.md`](./JIUSHU_5MIN.md) · **15 分钟脚本**：[`../JIUSHU_ONBOARDING.md`](../JIUSHU_ONBOARDING.md)

---

## 0) 先准备两个值（Moses 填，勿 commit）

| 占位符 | 填什么 |
|--------|--------|
| **`{{KEEL_API_URL}}`** | `https://keel-production-be1c.up.railway.app/v1/entry` |
| **`{{KEEL_API_KEY}}`** | 与 `track-a/server/.env` 里 `KEEL_API_KEY=` **相同**（亦与 Railway Variables、GitHub Secret 一致） |

复制 URL 见 [`KEEL_URL.txt`](./KEEL_URL.txt)。

**先验云端**（浏览器或快捷指令「获取 URL 内容」GET）：

```
https://keel-production-be1c.up.railway.app/health
```

应返回 JSON，含 `"status":"ok"` 且 `"api_key_configured":true`。

---

## 1) 新建快捷指令（建议命名：主见）

1. iPhone 打开 **「快捷指令」** App  
2. 右下角 **「+」** 新建  
3. 点顶部名称，改为 **`主见`**（或 `Keel`）  
4. 点图标 → 选中性符号（避免业务相关图案）  
5. **添加到主屏幕**：快捷指令内 **⋯** → **添加到主屏幕** → 名称 **`主见`**

---

## 2) 按顺序添加动作（逐步）

> 每步：搜索框输入动作名 → 点选 → 按下面填参数。

### 动作 1：听写文本

- 搜索：**听写文本**
- 语言：**中文（普通话）**
- 提示语：`说给主见`
- （可选）完成后 **设定变量** → 名称 `raw_text`

### 动作 2：显示结果（可编辑）

- 搜索：**显示结果**
- 输入：选变量 **`raw_text`**
- 打开 **「可编辑」**
- 用户改完后 **设定变量** → 名称 `confirmed_text`

### 动作 3：从菜单中选取（topic）

- 搜索：**从菜单中选取**
- 提示：`选话题`
- 菜单项（每项一行，**返回值写 slug**）：

| 显示给九叔 | 实际值（slug） |
|------------|----------------|
| 腾讯阿里版权续约 | `tencent-ali-renewal` |
| 李宁提案 | `lining-pitch` |
| 白酒（五粮液/泸州老窖） | `baijiu-wly-lzlj` |

- 菜单结果 **设定变量** → `topic_slug`
- （可选）加 **如果** 选「手动」→ **询问输入** → 写入 `topic_slug`

### 动作 4：字典（组装 JSON）

- 搜索：**字典**
- 键值对：

| 键 | 值 |
|----|-----|
| `topic_slug` | 变量 `topic_slug` |
| `raw_text` | 变量 `confirmed_text` |
| `advice_intensity` | 数字 `3`（或后续加菜单 1–5） |

### 动作 5：获取 URL 内容（POST）⭐

- 搜索：**获取 URL 的内容**
- **URL**：`https://keel-production-be1c.up.railway.app/v1/entry`
- **方法**：`POST`
- **请求正文**：`JSON`
- **请求体**：上一步 **字典**
- **Headers**（点「显示更多」）：

| 键 | 值 |
|----|-----|
| `Content-Type` | `application/json` |
| `X-API-Key` | 粘贴 Moses 给的 key（与 `.env` 一致） |

### 动作 6：从输入获取词典值

- 对返回 JSON 取：
  - `reply`
  - `living_position_summary`
  - `daily_snapshot_snippet`

（或用 **获取词典值** 三次。）

### 动作 7：显示结果（给九叔看）

- 搜索：**显示结果**
- 文本：

```text
军师回复：
{{reply}}

立场摘要：
{{living_position_summary}}

今日快照：
{{daily_snapshot_snippet}}
```

### 动作 8：写入 iCloud（可选，推荐）

1. **获取当前日期** → **格式化日期** → 格式 `yyyyMMdd`  
2. **文本** 动作，内容：

```text
## {{当前时间}}
原话：{{confirmed_text}}

军师：
{{reply}}

立场摘要：
{{living_position_summary}}
```

3. **存储文件**：
   - 位置：**iCloud Drive**
   - 路径：`Keel/topics/{{topic_slug}}/{{yyyyMMdd}}.md`
   - 若文件已存在：**追加**

---

## 3) discreet 建议

1. 名称只用 **`主见`** 或 **`Keel`**
2. 通知文案仅写：**`主见：记录已完成`**
3. iPhone **设置 → 通知 → 快捷指令** → 关闭预览（可选）

---

## 4) 联调顺序（Moses 做一遍再给九叔）

| 步 | 做什么 | 期望 |
|----|--------|------|
| 1 | GET `/health` | 200，`api_key_configured: true` |
| 2 | 完整跑一遍，topic 选 **腾讯阿里版权续约** | 有军师回复 |
| 3 | 看 iCloud | `Keel/topics/tencent-ali-renewal/今天.md` |
| 4 | Mac | 见 [`../mac/README.md`](../mac/README.md) 能否打开 |

**常见错误**：

| HTTP | 原因 |
|------|------|
| 401 | `X-API-Key` 与 Railway 不一致 |
| 503 | Railway 未设 `KEEL_API_KEY` |
| 500 | 查 Railway `DEEPSEEK_API_KEY` |

---

## 5) 参考文件

- JSON 模板：[`keel-entry.shortcut.json`](./keel-entry.shortcut.json)、[`shortcut-payload-template.json`](./shortcut-payload-template.json)
- URL Scheme：[`URL_SCHEME.md`](./URL_SCHEME.md)
