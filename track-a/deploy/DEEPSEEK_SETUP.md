# DeepSeek 模型与费用设置（Track A）

## 路由策略（成本优先）

- 默认走 `DEEPSEEK_MODEL_DEFAULT`（建议 `deepseek-chat`，便宜够用）。
- 仅在以下任一条件触发时走 `DEEPSEEK_MODEL_DEEP`（建议 `deepseek-reasoner`）：
  - 用户消息包含 `/max`
  - entry 显式标记 `depth: deep`
  - topic 配置 `depth_mode=true`（或命中 `DEEP_TOPIC_SLUGS`）
- 若 DeepSeek 不可用，服务会退到 Qwen 后备模型；再不可用则用本地 mock 兜底。

## 环境变量（推荐）

```env
DEEPSEEK_MODEL_DEFAULT=deepseek-chat
DEEPSEEK_MODEL_DEEP=deepseek-reasoner
```

> 规则：默认便宜模型常开，`/max` 才升档，避免日常对话误用高价模型。

## 单人月费估算（两种用法）

估算假设（可按你实际量替换）：
- 每天 30 次请求
- 每次约 1.3K tokens（输入+输出）
- 月总量约 1.17M tokens

记：
- 便宜模型单价 = `C`
- 深度模型单价 = `R`（通常显著高于 `C`）

场景 A（便宜为主，`/max` <= 10%）：
- 月费约 `1.17M * (0.9*C + 0.1*R)`
- 常见在“低个位数到十几元人民币”区间（取决于官方当日单价）。

场景 B（频繁 `/max`，约 50%）：
- 月费约 `1.17M * (0.5*C + 0.5*R)`
- 常见会上升到“数十元人民币”区间。

建议：
- 把 `/max` 作为“关键判断时再开”的开关，默认便宜模型即可把月费压在低区间。
