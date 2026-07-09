# 九叔 Bridge Track · 装机检查清单

> **目标日期**：2026-07-15 · **当前 staging**：`https://keel-production-be1c.up.railway.app`  
> 完整 issue：[`issues/002-S1-bridge-jiushu.md`](./issues/002-S1-bridge-jiushu.md)

---

## A. 云端（Moses / agent 已完成项打 ✅）

| # | 检查项 | 状态 | 怎么验 |
|---|--------|------|--------|
| A1 | `/health` 200，`api_key_configured: true` | ✅ 2026-07-10 | [打开 health](https://keel-production-be1c.up.railway.app/health) |
| A2 | `POST /v1/entry` + 有效 `X-API-Key` → 200 | ✅ 2026-07-10 | 见 [`DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md) |
| A3 | DeepSeek 真模型（非 mock 兜底） | ⏳ | 回复不含「本地兜底」；查 Railway `DEEPSEEK_API_KEY` |
| A4 | GitHub `KEEL_STAGING_URL` Variable | ⏳ | `https://keel-production-be1c.up.railway.app`（无尾斜杠） |
| A5 | 文档：SETUP / ONBOARDING / 5MIN | ✅ | 本 repo `track-a/shortcuts/` |

---

## B. 九叔 iPhone（Moses 当面 · decision-gate）

| # | 检查项 | 说明 |
|---|--------|------|
| B1 | 快捷指令 **「主见」** 已安装 | 见 [`track-a/shortcuts/SETUP.md`](./track-a/shortcuts/SETUP.md) |
| B2 | URL = `…/v1/entry`，Key 与 Moses 一致 | 见 [`KEEL_URL.txt`](./track-a/shortcuts/KEEL_URL.txt) |
| B3 | **主屏幕** 有图标 | 名称 discreet：`主见` 或 `Keel` |
| B4 | 通知预览关闭或仅中性文案 | 「主见：记录已完成」 |
| B5 | 首测 topic = **腾讯阿里版权续约** | 至少 1 次真实输入 + 看到反对意见或 disruptive 备选 |
| B6 | iCloud `Keel/topics/…` 可见（若启用动作 8） | Mac 见 [`track-a/mac/README.md`](./track-a/mac/README.md) |

**5 分钟教装**：[`track-a/shortcuts/JIUSHU_5MIN.md`](./track-a/shortcuts/JIUSHU_5MIN.md)  
**15 分钟 onboarding**：[`track-a/JIUSHU_ONBOARDING.md`](./track-a/JIUSHU_ONBOARDING.md)

---

## C. 验收口径（ACCEPTANCE A0）

- [ ] 九叔 **不打开 Cursor** 完成一次 topic 输入  
- [ ] 军师回复 **有力度、不冒犯**  
- [ ] Moses 确认 go → 7/15 按 Bridge Track 交付  

---

## D. 阻塞与升级

| 现象 | 处理 |
|------|------|
| `/health` 非 200 | [`RAILWAY_故障排查.md`](./RAILWAY_故障排查.md) |
| entry 503 | Railway 补 `KEEL_API_KEY` → Redeploy |
| entry 401 | 快捷指令 Key 与 Railway 不一致 |
| 回复全是 mock | Railway 补/换 `DEEPSEEK_API_KEY` |
| 九叔不愿装 | 延后 decision-gate；不虚假宣称「已交付」 |

---

## E. 相关链接

- 仓库：https://github.com/mosesdai/keel  
- Moses 一页纸：[`MOSES_STATUS.md`](./MOSES_STATUS.md)  
- 部署状态：[`track-a/deploy/DEPLOYMENT_STATUS.md`](./track-a/deploy/DEPLOYMENT_STATUS.md)
