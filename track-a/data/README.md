# Track A 数据与 iCloud 同步说明

Track A 的本地数据统一在：

- `track-a/data/topics/{slug}/`

推荐 iCloud 目标目录（与快捷指令一致）：

- `iCloud Drive/Keel/topics/{slug}/`

---

## 每个 topic 目录结构

```
Keel/topics/{slug}/
├── topic.json
├── living_position.md
├── entries.jsonl
└── snapshots/
    └── YYYYMMDD.md
```

说明：

- `topic.json`：主题元信息（slug、展示名、深度标记）
- `living_position.md`：当前立场书（持续覆盖更新）
- `entries.jsonl`：每次输入与回复记录（追加）
- `snapshots/YYYYMMDD.md`：按天快照（追加）

---

## 本地到 iCloud 的同步方式

### 方式 A（推荐）：脚本同步

```bash
cd "track-a"
chmod +x scripts/sync_to_icloud.sh
./scripts/sync_to_icloud.sh
```

默认会同步到：

- `~/Library/Mobile Documents/com~apple~CloudDocs/Keel/topics`

### 方式 B：Finder 手动复制

把 `track-a/data/topics/` 全量复制到：

- `iCloud Drive/Keel/topics/`

---

## 注意事项

- iCloud 有延迟是正常现象，建议同步后等待 10~60 秒再在另一端查看。
- 不要在两端同时手改同一文件，优先通过 API/快捷指令写入，避免冲突。
