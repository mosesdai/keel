# Mac Companion（查看 iCloud 话题与快照）

这个目录用于 Moses 在 Mac 端快速复核九叔当天输入与军师输出。

---

## 1) iCloud 路径（统一约定）

默认路径：

`~/Library/Mobile Documents/com~apple~CloudDocs/Keel/topics/`

目录结构：

- `Keel/topics/{slug}/YYYYMMDD.md`：当天记录（快捷指令写入）
- `Keel/topics/{slug}/living_position.md`：当前立场书
- `Keel/topics/{slug}/snapshots/`：每日快照（后端追加）

---

## 2) 先看什么

建议顺序：

1. `tencent-ali-renewal/living_position.md`
2. 当天 `YYYYMMDD.md`
3. `snapshots/` 最近 3 天

---

## 3) 一键打开今日记录

```bash
cd "track-a/mac"
chmod +x open_today_snapshot.sh
./open_today_snapshot.sh tencent-ali-renewal
```

如果你 iCloud 目录不同，可传第二个参数：

```bash
./open_today_snapshot.sh tencent-ali-renewal "/你的/Keel/topics路径"
```

---

## 4) Mac 侧联调命令（可选）

```bash
curl -sS "{{KEEL_API_URL}}" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: {{KEEL_API_KEY}}" \
  -d '{"topic_slug":"tencent-ali-renewal","raw_text":"Mac 侧连通性验证"}'
```
