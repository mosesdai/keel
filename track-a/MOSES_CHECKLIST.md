# Moses 一键执行清单（Track A）

先看部署新手教程：`deploy/DEEPSEEK_SETUP.md`  
**Railway 逐步操作**：`deploy/RAILWAY_WALKTHROUGH.md`（CLI 未登录时需你本机 `railway login` 后执行）

目标状态：只差你填 key + 点部署 + 九叔手机安装快捷指令。

---

1. **[已完成]** 拉起本地服务结构与 seed topic（3 分钟）  
   - 已含 `tencent-ali-renewal`、`lining-pitch`、`baijiu-wly-lzlj`

2. **[已完成]** 接口安全与探活（3 分钟）  
   - 已加 `GET /health`、`GET /healthz`、`X-API-Key` 鉴权

3. **[进行中 · 你来做]** 生成并填写密钥（5 分钟）  
   - 本地 `server/.env` 已有 key（勿 commit）  
   - 在 Railway Variables 填：`KEEL_API_KEY`、`DEEPSEEK_API_KEY`（Dashboard 粘贴）、`DEFAULT_PROVIDER=deepseek`

4. **[进行中 · 你来做]** 部署上线（8 分钟）  
   - 主路径：按 `deploy/RAILWAY_WALKTHROUGH.md`（`railway login` → `railway init` → Variables → `railway up` → Generate Domain）  
   - 备选 GitHub：`deploy/RAILWAY_WALKTHROUGH.md` 路径 B  
   - 备选平台：`deploy/DEPLOY.md` Fly.io

5. **[你来做]** 把 `{{KEEL_API_URL}}` + `{{KEEL_API_KEY}}` 写进快捷指令（8 分钟）  
   - 文档：`shortcuts/SETUP.md`  
   - URL 形如：`https://xxx.up.railway.app/v1/entry`

6. **[你来做]** 九叔手机安装并首测（10 分钟）  
   - 脚本：`JIUSHU_ONBOARDING.md`

7. **[你来做]** 验证部署是否成功（3 分钟）  
   - 健康检查：
     ```bash
     curl -sS "https://你的域名/health"
     ```
   - 业务检查：
     ```bash
     curl -sS "https://你的域名/v1/entry" \
       -H "Content-Type: application/json" \
       -H "X-API-Key: 你的KEEL_API_KEY" \
       -d '{"topic_slug":"tencent-ali-renewal","raw_text":"上线验收：请给我1条反对意见+1条disruptive方案"}'
     ```

8. **[已完成]** 质量回归用例准备（3 分钟）  
   - 文档：`server/QUALITY_TESTS.md`

---

**Agent 侧已完成（2026-07-04）**：`track-a/` Git 已 init；根目录 `.gitignore` 忽略 `.env`/`.venv`；本机已装 `@railway/cli`（需你 `railway login` 后代为部署）。
