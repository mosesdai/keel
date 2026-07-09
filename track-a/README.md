# Track A（7/15 前过渡可交付版）

这个目录是军师 app 的 10 天过渡可运行实现，目标不是堆功能，而是让九叔马上获得真实帮助。

## 子目录

- `server/`：FastAPI 轻后端（模型路由 + 人格注入 + 本地落盘）
- `data/`：本地数据目录（JSONL + Markdown，兼容 iCloud 同步）
- `shortcuts/`：iPhone 快捷指令搭建说明
- `mac/`：Mac companion 使用说明
- `deploy/`：Railway/Fly.io 部署手册
- `scripts/`：iCloud 同步脚本
- `JIUSHU_ONBOARDING.md`：九叔 15 分钟上手脚本
- `DELIVERY_PLAN.md`：07-04 到 07-15 执行计划
- `MOSES_CHECKLIST.md`：Moses 最后人工执行清单

## 快速入口

1. 先看 `server/README.md` 跑起后端  
2. 按 `deploy/DEPLOY.md` 上线服务  
3. 再按 `shortcuts/SETUP.md` 做 iPhone 快捷指令  
4. 按 `MOSES_CHECKLIST.md` 完成人工步骤并验收
