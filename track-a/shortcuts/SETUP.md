# iPhone 快捷指令搭建（主见 / Keel）

目标链路：`录音/听写 -> 人工改错 -> 选 topic -> POST -> 展示回复 -> 写 iCloud`

---

## 0) 先准备两个占位符

- `{{KEEL_API_URL}}`：**Staging（Railway）** → `https://keel-production-be1c.up.railway.app/v1/entry`（亦见同目录 [`KEEL_URL.txt`](./KEEL_URL.txt)）
- `{{KEEL_API_KEY}}`：和后端 `KEEL_API_KEY` 完全一致（勿写进 repo）

---

## 1) 新建快捷指令（建议命名：主见）

1. iPhone 打开「快捷指令」App
2. 右上角 `+` 新建
3. 名称改为 `主见`（或 `Keel`）
4. 图标用中性符号（避免泄露业务信息）

---

## 2) 按顺序添加动作（截图级说明）

### 动作 1：听写文本

- 搜索动作：`听写文本`
- 语言：中文（普通话）
- 提示语：`说给主见`
- 输出命名变量：`raw_text`

### 动作 2：显示结果（可编辑）

- 搜索动作：`显示结果`
- 输入内容：选择变量 `raw_text`
- 打开选项：`可编辑`
- 用户修改错字后，把结果命名为 `confirmed_text`

### 动作 3：从菜单中选取（topic）

菜单项与值（建议）：

1. `腾讯阿里版权续约` -> `tencent-ali-renewal`
2. `李宁提案` -> `lining-pitch`
3. `白酒（五粮液/泸州老窖）` -> `baijiu-wly-lzlj`
4. `手动输入` -> 增加一个「询问输入」，结果写入 `topic_slug`

### 动作 4：字典（组装 JSON）

键值：

- `topic_slug`: 上一步选择结果
- `raw_text`: `confirmed_text`
- `topic_mark`: 空字符串（需要深度时可填 `深度`）

### 动作 5：获取 URL 内容（POST）

- URL：`{{KEEL_API_URL}}`
- 方法：`POST`
- 请求正文：`JSON`
- 请求体：使用上一步字典
- Header 1：`Content-Type` = `application/json`
- Header 2：`X-API-Key` = `{{KEEL_API_KEY}}`

### 动作 6：提取返回字段

从返回 JSON 读取：

- `reply`
- `living_position_summary`
- `daily_snapshot_snippet`

### 动作 7：显示结果（给九叔看）

文本建议：

```text
军师回复：
{{reply}}

立场摘要：
{{living_position_summary}}

今日快照：
{{daily_snapshot_snippet}}
```

### 动作 8：写入 iCloud

1. 加 `获取当前日期` + `格式化日期`（`yyyyMMdd`）
2. 加 `文本` 动作，内容示例：

```text
## {{当前时间}}
原话：{{confirmed_text}}

军师：
{{reply}}

立场摘要：
{{living_position_summary}}
```

3. 加 `存储文件`：
   - 位置：iCloud Drive
   - 路径：`Keel/topics/{{topic_slug}}/{{yyyyMMdd}}.md`
   - 若存在：`追加`

---

## 3) discreet 建议

1. 名称只用 `主见` 或 `Keel`
2. 通知文案仅写：`主见：记录已完成`
3. iPhone 设置 -> 通知 -> 快捷指令 -> 关闭预览（可选）

---

## 4) 联调顺序（建议）

1. 先测健康检查：把 `{{KEEL_API_URL}}` 末尾 `/v1/entry` 改成 `/health` 后访问
2. 再跑一次完整流程（topic 选 `tencent-ali-renewal`）
3. 确认 iCloud 出现：`Keel/topics/tencent-ali-renewal/今天日期.md`
4. Mac 端按 `../mac/README.md` 验证可见
