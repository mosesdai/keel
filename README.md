# 20260701 jiushu bootstrap

给 **九叔（NBA China 商业侧 CEO）** 的一次性引导包。

## 这是什么

`PASTE_TO_JIUSHU_CURSOR.md` 是**唯一交付物**：一整块可全选粘贴的文本。九叔在一个全新的 Cursor 对话里 select-all + paste，他的 Cursor Agent 读到后会**执行指令并创建 19 个文件**——把我们这套工作方式（斜杠指令 + 反昏君 + 深度研究 + 项目唤醒/自动沉淀）装到他电脑上，并建好三个战略项目工作台。

## 全局 vs 项目 的取舍

- **全局（`~/.cursor/`）**：斜杠指令与技能（`/max /cheap /grill /3rounds /ifalsify /liq /deep /resume /pitchsop`）+ 一条常驻规则。放全局，因为这些是**跨项目**的工作方式，任何项目都要用；且唤醒/自动沉淀机制写在常驻规则里，才能在任意对话生效。
- **项目（工作区根目录）**：`lining pitch/`、`baijiu wly lzlj/`、`tencent ali renewal/`。每个含 `_charter.md`（宪法+开场审讯）、`SESSION_LOG.md`（进度）、`research/`（证据）。放项目里，因为这些是**这几个案子专属**的上下文，需要可暂停、可唤醒、可持续深挖。

## 每次聊完出报告 + 同话题滚动讨论

- **当天结论报告**：每次聊完（暂停/结束、触发自动沉淀时），Agent 会在对应项目的 `reports/` 目录里生成一份**当天 HTML 报告**（自包含、可打印成 PDF），文件名与页头都标**日期**与话题，内容含：日期 / 话题 / 本轮结论 / 关键新证据（带来源级别）/ 未决问题 / 下次从哪继续。`reports/` 目录在首次出报告时于运行时创建，不在引导阶段预建。
- **滚动讨论**：同一个话题不是一次性的。用唤醒词 + 话题回到同一话题时，Agent 会读取该话题此前的报告、接着往下聊，并为本次再出一份新的当天报告——于是每个话题积累成一条**按日期排序的报告序列**，越聊越深，而非每次从头开始。

## 自包含保证

九叔的机器**没有** `/Users/Eliam-Code/...`。所以粘贴文本里每个技能都**内联了完整正文**，零外部依赖。唯一出现的绝对路径是 `~/.cursor/...`（全局技能）和工作区相对路径（项目文件夹）。

## 关键事实来源（写进 charter 的，均来自 Moses 的任务简报）

- 李宁：签了 Curry；NBA 用 NBA×NBA 品牌合作帮 Curry×李宁 落地；约 $5M（权益费 $1.5–2M + 激活），**$5M 是李宁增量预算，不从 Curry 激活预算切**。
- 白酒：五粮液 + 泸州老窖都要签；两家有竞争过节、五粮液曾截胡、NBA 先接触泸州老窖；marketing vs licensing 待定；烈酒球员肖像限制 + 球队 logo 需单独签 + 轩尼诗式先例。
- 腾讯/阿里版权：占位 TBD。

三个 charter 里嵌的“开场问题”是 **Moses 没有、九叔可能有** 的信息——Agent 必须主动问，不能假设。

## Track A 入口

Track A 交付入口请直接看：`track-a/README.md`  
部署步骤见：`track-a/deploy/DEPLOY.md`  
Moses 执行清单见：`track-a/MOSES_CHECKLIST.md`

## 续接开发

暂停后下次接着干 → 先读 **[RESUME.md](RESUME.md)**（入口指南 + demo 命令 + 唤醒语）  
本轮进度与决策 → **[SESSION_LOG.md](SESSION_LOG.md)**
