# Moses 一页纸状态 · Keel / 军师

> 更新：**2026-07-10**（Moses 回归 · 主线 = GitHub 自主开发）  
> 仓库：https://github.com/mosesdai/keel

---

## 你现在还要做什么？

| 优先级 | 事项 | 状态 | 怎么做 |
|--------|------|------|--------|
| **P0** | Railway API 24/7 | ⏳ **待做** | 见下方 **2 步** |
| P1 | `KEEL_STAGING_URL` | ⏳ Railway 有域名后 | GitHub → Settings → Variables → 填 `https://….up.railway.app`（无尾斜杠） |
| P2 | 创建 agent issues | 可选 | 从 `issues/002`–`004` 粘贴到 GitHub New Issue |
| — | GitHub Secrets | ✅ 已完成 | `KEEL_API_KEY`、`DEEPSEEK_API_KEY` |

### Railway 若仍未成功：只需 2 步（约 10 分钟）

这是 **API 24/7 在线** 的前提；做完可关机，push `main` 会自动部署。

1. **Root Directory** — Railway → 你的 Service → **Settings** → **Root Directory** 填：**`track-a`** → Save  
2. **Redeploy** — 同一页或 **Deployments** → **Redeploy**（或 push 任意 `track-a/` 变更到 `main`）

然后确认 Variables 已有 `KEEL_API_KEY`、`DEEPSEEK_API_KEY`、`DEFAULT_PROVIDER=deepseek`，并 **Generate Domain**，浏览器打开 `https://你的域名/health` 应返回 ok。

详细图文：[`RAILWAY_傻瓜版.md`](./RAILWAY_傻瓜版.md) · 验收：[`track-a/deploy/RAILWAY_STAGING_CHECKLIST.md`](./track-a/deploy/RAILWAY_STAGING_CHECKLIST.md)

---

## 什么已经可无人值守？

| 能力 | 说明 |
|------|------|
| **Server CI** | push `main`（`track-a/server` 变更）→ 测试 import + `/health` smoke |
| **Docs check** | 关键文档存在性检查 |
| **每周 backlog issue** | `agent-backlog.yml` 周一自动开「S0/S1 进度检查」（无 LLM） |
| **Railway 自动部署** | GitHub 集成 + Root `track-a` 后，**Moses 关机** push 仍部署 API |
| **Agent 文档** | [`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md) 规定读序、可做/不可做、决策门禁 |
| **Issue 草稿** | `issues/001`–`004` 可粘贴创建任务 |

### 仍需要你或 Cloud Agent 的

- **写 Swift / 复杂 PR** — 标准 GitHub Actions 不会自动写代码  
- **Cursor Cloud Agent** 或你偶尔开机 5 分钟 merge PR  
- **九叔装快捷指令、真机验收** — 决策门禁  
- **Apple 签名 / TestFlight** — 7/16 后再说  

---

## 如何验证「GitHub 在帮我开发」？

三个检查点（约 1 分钟）：

1. **Actions 绿** — https://github.com/mosesdai/keel/actions  
   - `Server CI`、`Docs check` 最近 run 为 success  
2. **Issues / 每周检查** — https://github.com/mosesdai/keel/issues  
   - label `agent`；或每周一自动的「S0/S1 进度检查」  
3. **Commit 历史** — https://github.com/mosesdai/keel/commits/main  
   - 文档、workflow、demo 持续更新；`SESSION_LOG.md` 有 handoff  

Railway 配好后第 4 点：`/health` 公网 ok + `track-a/deploy/DEPLOYMENT_STATUS.md` 有 URL。

---

## fix/railway 分支

`fix/railway-track-a-deploy` 已与 **`main` 同 commit**（`ea77bb1` Docker build + root fallback）。无需再 merge；本地可执行：

```bash
git branch -u origin/main main
```

---

## 下一步建议（粘贴 issue）

| 若… | 建议粘贴 |
|-----|----------|
| Railway 刚配好 | `issues/002-S1-bridge-jiushu.md` — 九叔 Bridge Track |
| 想先改 demo 体验 | `issues/004-demo-from-research05.md` |
| Railway 仍阻塞 | 先完成上方 2 步，再开 `002` |

---

## 相关入口

- 关机清单：[`MOSES_BEFORE_SHUTDOWN.md`](./MOSES_BEFORE_SHUTDOWN.md)  
- Agent SOP：[`AUTONOMOUS_DEV.md`](./AUTONOMOUS_DEV.md)  
- 恢复开发：[`RESUME.md`](./RESUME.md) → [`SESSION_LOG.md`](./SESSION_LOG.md)  
