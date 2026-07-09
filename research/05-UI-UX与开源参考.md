# 军师 / 主见（Keel）UI/UX 与开源参考研究

日期：2026-07-09  
对象：私人 AI 战略顾问，语音优先，discreet 高管风；外显名「主见」/ Keel  
参考现状：`track-a/demo/index.html` 已有「说 / 立场 / 日志 / 历史」、topic 选择、通知预览、力谏 slider（绿到红）和深色金色视觉基调。

## 0. 研究结论摘要

Keel 不应做成「更会聊天的日记」或「更可爱的 AI companion」，而应是一个能在 10 秒内承接一句话、确认立场、给出不谄媚回应、并把判断沉淀为可回看的战略记忆的原生工具。最值得借鉴的方向有三类：

1. 语音优先产品的「一键说话 + 实时转写 + 结束后结构化」路径，来自 Voicenotes、Rosebud、ChatGPT / Claude voice mode 与多个开源 voice diary。
2. 日记 / 笔记产品的「时间线、标签、无压力空状态、轻量检索」模式，来自 Day One、Bear、Voicenotes 与 Echo 类项目。
3. AI companion / executive coach 项目的「本地记忆、明确人格边界、推送要克制」思路，来自 DailyVox、AICoven Local、PikoChan、Alfred、The Praeceptor 等开源项目。

Keel 的差异化：不是情绪陪伴，不是通用助理，不是会议记录，而是「高管的私人逆耳顾问」。视觉上要像一只收在口袋里的罗盘：安静、可信、少说废话、必要时敢变红。

---

## 1. GitHub 开源案例研究

> 搜索关键词覆盖：`voice journal`、`AI diary`、`executive coach app`、`SwiftUI chat memory`、`private AI companion`、`voice diary`、`local AI journal`。Star 数以 2026-07-09 GitHub API / 搜索结果为量级参考，低 star 不代表无借鉴价值，很多项目是 2026 年新项目。

| 项目 | star 量级 | 简介 | 可借鉴 UI/UX 点 | 不适合军师的点 |
|---|---:|---|---|---|
| [intrepidkarthi/dailyvox](https://github.com/intrepidkarthi/dailyvox) | 11 | SwiftUI iPhone/iPad voice journal，Apple Speech + NaturalLanguage，本地 AI，强调「private constellation」 | 一键语音记录、离线优先、每条记录成为可视化记忆点；ActivityKit / WidgetKit 可启发锁屏与 Dynamic Island 的 discreet 状态 | 星座/情绪可视化偏温柔疗愈，Keel 更应偏决策与立场，不宜过度诗化 |
| [chenjy16/EchoDiary](https://github.com/chenjy16/EchoDiary) | 4 | SwiftUI 智能语音日记，MLX + SwiftWhisper，本地 AI 推理 | 「语音转文字 -> AI 扩展追问 -> 情绪/主题洞察」链路适合 Keel 的「说完后确认意图」 | 日记语境偏生活反思，容易进入陪伴/心理咨询语气；Keel 要避免柔性共情过多 |
| [SANABI-LL/Voice-Diary](https://github.com/SANABI-LL/Voice-Diary) | 1 | PWA「碎碎念」，Gemini 实时语音对话、自动转写、日总结、插画回忆 | 实时会话 + 自动保存有意义片段；每日摘要和日历回看适合 Keel 的「战略日志」 | 水彩插画、朋友式角色「念念」太亲密；Keel 不应拟人化成可爱伙伴 |
| [Lalitmukesh69/aurea-voice-journal](https://github.com/Lalitmukesh69/aurea-voice-journal) | 1 | E2EE AI voice journal，Supabase + Gemini，life chapters 与情绪分析 | 端到端加密、生命周期章节、情绪/主题元数据，对 Keel 的隐私和长期脉络很有启发 | 「Operating System for the Soul」叙事过重，Keel 应少宣称人生系统，多给决策帮助 |
| [Prabodh-dev/voice-diary](https://github.com/Prabodh-dev/voice-diary) | 0 | Next.js + Ollama + faster-whisper 的本地 voice diary | 全本地 pipeline、录音后自动转写/改写/保存；「原文 vs 优化稿」切换可借鉴为「原话 vs 军师理解」 | 电影感全屏 story view 和情绪渐变偏消费化；Keel 应减少表演感 |
| [29sayantanc/Echo](https://github.com/29sayantanc/Echo) | 16 | Privacy-first offline AI journal + conversational assistant，Whisper/Ollama/Piper，语义搜索 | 「把语音/文本变成可检索记忆，并能与自己的历史对话」非常贴近 Keel 的历史脉络 | 桌面/自托管工具感较重；Keel iPhone 端需要更少设置、更强默认路径 |
| [neur0map/PikoChan](https://github.com/neur0map/PikoChan) | 14 | SwiftUI macOS notch AI companion，本地 LLM、semantic memory、activity feed | Mac 上「notch / menu-bar resident companion」启发 Keel Mac 端做低打扰状态入口；activity feed 可借鉴为历史轨迹 | Buddy/personality-first 过强，不适合高管顾问；Keel 不应在桌面上频繁“活着”打扰 |
| [inthepond/Ba-Chan](https://github.com/inthepond/Ba-Chan) | 1 | SwiftUI iOS/macOS on-device companion，程序化表情、长期记忆、视觉 | 「conversation journal + time-aware memory」适合回答“上次我们怎么判断的”；本地记忆衰减也值得参考 | 可爱脸、眨眼、lip-sync 与 Keel 的 discreet 高管风相冲突 |
| [lepapillonterrible/aicoven-local-opensource](https://github.com/lepapillonterrible/aicoven-local-opensource) | 7 | Swift iOS/macOS 本地优先 AI assistant，GRDB/SQLite，加密 chats/memories/settings，BYOK | 本地加密存储、Keychain、provider-agnostic 模型路由、context sandwich 是 Keel 原生架构强参考 | 偏通用 AI assistant 和多 agent，界面容易复杂；Keel 首屏必须比它更窄、更快 |
| [mitensampat/alfred](https://github.com/mitensampat/alfred) | 28 | macOS Swift executive coach，Claude + Calendar + Notion，关注 consequential work | 「Not a dashboard. Not an assistant. A coach.」定位贴近 Keel；嵌入日程/承诺/笔记后给逆向推动 | 依赖工作系统集成，初版 Keel 不应一开始承担太多连接器和后台观察 |

补充关注但不列入主表的项目：

- [orteug/the-praeceptor](https://github.com/orteug/the-praeceptor)：SwiftUI iOS voice mentor，公开搜索显示约 12 stars；「按住说话，导师回应，整个界面就这样」非常接近 Keel 的极简语音路径，但其名人导师复合人格不适合直接复制。
- [sozercan/ayna](https://github.com/sozercan/ayna)：SwiftUI macOS/iOS/watchOS ChatGPT client，公开搜索显示约 23 stars；多 provider、watchOS 快速入口、memory 与加密聊天可参考，但它是通用聊天客户端。
- [oguzkopan/simon-ai-coach](https://github.com/oguzkopan/simon-ai-coach)：Swift iOS coaching app，重点是创建/浏览不同 coach；Keel 不应让用户管理一堆 coach，而应只有一个稳定顾问人格。

### 对 Keel 的开源案例启示

1. **优先借 DailyVox / EchoDiary 的原生语音与本地隐私，不借它们的疗愈化视觉。**
2. **借 Echo / AICoven 的记忆架构，但把“记忆管理”藏在系统后面，不让高管维护数据库。**
3. **借 Alfred / The Praeceptor 的 coach 定位和克制交互，但 Keel 要更适合 iPhone 口袋场景。**
4. **谨慎对待 companion 项目的拟人化。** Keel 可以有语气和人格边界，但不应有表情、宠物、过度情绪动画。
5. **许多新项目 star 少，但提供了 2026 年 AI app 的真实默认：SwiftUI、本地优先、语音、长期记忆、BYOK/本地模型。**

---

## 2. 美观 UI 参考：语音优先与高质感笔记产品

### 2.1 Voicenotes

来源：[Voicenotes 官网](https://voicenotes.com/)、[App Store 页面](https://apps.apple.com/us/app/voicenotes-ai-notes-meetings/id6483293628)、[Tags help](https://help.voicenotes.com/en/articles/10393499-how-to-organize-your-notes-in-voicenotes-using-tags)

可提炼 pattern：

- **打开即录。** 首页第一动作是 record，而不是先选模板。
- **录音、转写、摘要、行动项在同一条 note 内。** 用户不需要理解 pipeline，只看到一个可回看的记录容器。
- **Tags 横向过滤。** 标签在搜索/Ask AI 附近出现，轻量过滤，不像文件夹那么重。
- **Ask AI 有来源。** 对历史记忆回答时要显示来自哪几条记录，减少 AI 断言感。
- **多端快捷入口。** iOS、macOS、Watch、Action Button 都强调「捕捉瞬间」。

对 Keel 的启发：首屏应把「说一句」放在视觉中心；回答要能回溯到原话、历史立场和相关 topic。

### 2.2 Rosebud

来源：[Rosebud 官网](https://www.rosebud.app/new-home)、[Rosebud voice journaling help](https://help.rosebud.app/tools-for-growth/voice-journaling)、[App Store 页面](https://apps.apple.com/kz/app/rosebud-ai-journal-diary/id6451135127)

可提炼 pattern：

- **Hands-free voice journaling。** 适合走路、车里、睡前的自然表达。
- **Auto-stop sensitivity。** 用户可以调低/中/高灵敏度，适应安静办公室、车内、户外。
- **Glossary。** 可指定人名/公司名/术语，提高转写正确率。
- **Weekly insights。** 把碎片反思变成可回看的周期性洞察。
- **安全感。** 强调加密、Face ID / Touch ID / PIN。

对 Keel 的启发：Keel 需要「名词本」而不是通用 glossary，保存人名、公司、项目、对手、董事会成员；同时需要 Face ID 保护和极简隐私承诺。

### 2.3 ChatGPT iOS

来源：[OpenAI Voice help](https://help.openai.com/en/articles/20001274)、[PhoneArena 关于 voice in chat 的报道](https://www.phonearena.com/news/chatgpt-voice-mode-is-accessible-in-chat_id176082)、[VentureBeat Action Button 教程](https://venturebeat.com/business/how-to-map-openais-chatgpt-advanced-voice-mode-to-your-iPhone-action-button)

可提炼 pattern：

- **语音入口贴近输入框。** 用户不必进入一个全新产品区。
- **voice in chat。** 语音对话和文字历史共存，便于回看。
- **Start with Voice / Action Button。** 高频用户可以直接进入语音状态。
- **可中断、可静音、可退出。** 语音对话必须有清晰控制权。
- **字幕/转写可见。** 用户可确认 AI 听到的是什么。

对 Keel 的启发：Keel 的语音不是“炫技模式”，而是默认输入方式；必须实时展示「我听到的是……」，否则战略建议会失去可信度。

### 2.4 Claude iOS

来源：[Claude voice mode help](https://support.claude.com/en/articles/11101966-use-voice-mode)、[Claude Artifacts blog](https://claude.com/blog/artifacts)

可提炼 pattern：

- **hands-free 与 push-to-talk 双模式。** 嘈杂环境切到按住说。
- **同一会话内切换文字/语音。** 前后文不丢。
- **voice settings 可调声音和语速。** 顾问语气应允许慢一点、稳一点。
- **Artifacts / dedicated workspace。** 长内容不塞在聊天气泡里，给独立承载空间。

对 Keel 的启发：重大建议可从语音对话中“升格”为一张「立场卡」或「决策备忘」，而不是永远留在聊天流。

### 2.5 Day One

来源：[Day One UI Breakdown](https://screensdesign.com/showcase/day-one-journal-private-diary)、[MacStories Review](https://www.macstories.net/reviews/review-the-new-day-one/)

可提炼 pattern：

- **Prominent plus / quick capture。** 启动记录不能有阻力。
- **Timeline / Calendar / Gallery / Map 多种回看。** 历史不是单一列表。
- **上下文元数据。** 地点、天气、活动、照片等自动补足记忆。
- **空白页提示。** Journaling Suggestions 解决不知道写什么。
- **媒体工具栏分层。** 常用动作外露，次级动作收到 More。

对 Keel 的启发：Keel 的历史可以有「时间线 / topic / 立场 / 决策后果」四种回看，不必做花哨媒体。

### 2.6 Bear

来源：[Bear UI Breakdown](https://screensdesign.com/showcase/bear-markdown-notes)、[Bear Typography-First Writing](https://blakecrosley.com/guides/design/bear)

可提炼 pattern：

- **Typography-first。** 长文字可读性决定高级感。
- **Tags replace folders。** 组织发生在写作/记录过程中，不要先建文件夹。
- **Focus mode。** 需要深入看一条建议时，界面退后。
- **零加载感。** 本地缓存让内容随时可见。
- **主题整体切换，而不是乱调色。**

对 Keel 的启发：Keel 的建议卡需要非常好的中文排版；topic 应像标签一样自然附着在记录上，而不是让用户管理层级。

### 2.7 Things

来源：[Things 3: The Art of Focused Simplicity](https://blakecrosley.com/guides/design/things)

可提炼 pattern：

- **颜色只表达意义。** Things 绝大多数界面中性，黄色/红色等只在需要传达状态时出现。
- **把“什么时候做”和“什么时候截止”分开。** 复杂概念被拆成清晰模型。
- **快捷但不强迫。** 键盘/手势高级功能可发现，但不阻碍初学者。
- **非常克制的动效。**

对 Keel 的启发：demo 里的绿 -> 红力谏 slider 是好方向，但红色只能用于“风险/强谏/必须面对”，不能全屏铺满。

---

## 3. UX 最佳实践

### 3.1 语音 -> 确认 -> 回复流程

推荐主流程：

1. **一键开始说。** 首屏大按钮文案：`按住说一句` / `点按开始，停顿自动收尾`。支持 Action Button / Widget / Menu Bar。
2. **实时转写。** 显示 1-3 行大字号转写，不要整屏滚动字幕；重点是确认，不是直播字幕。
3. **自动识别 topic。** 识别为 `融资`、`组织`、`客户`、`家庭边界`、`战略判断` 等，允许一滑切换。
4. **确认卡。** 结束后出现短卡：`你要我判断的是：是否该继续押注 A 客户？`，附 `改一句`、`直接答`、`补充 10 秒`。
5. **生成回复。** 回复分三层：`一句话立场`、`理由 3 点`、`下一步动作`。
6. **可追问。** 用户可继续语音补充，但默认不要诱导长聊。
7. **沉淀。** 用户可把回复保存为 `立场卡`、`日志`、`待复盘`，也可自动保存但低调提示。

关键原则：AI 先证明“听懂了用户要判断什么”，再给意见。战略顾问不是听写员。

### 3.2 Discreet 通知

适合 Keel 的通知不应像社交 app。建议：

- 通知标题默认只显示 `主见`，正文使用隐晦但有用的短句：`有一条立场需要复盘`、`上周的判断到了验证点`。
- 锁屏默认不暴露敏感人名、公司名、金额、情绪词。
- 通知类型分三档：`轻提醒`、`复盘点`、`强风险`。
- 强风险也要克制：红色只在 app 内显示，系统通知不使用戏剧化语言。
- 支持「隐身模式」：通知只显示 `有新提醒`。
- 支持「工作日/深夜免打扰」，避免私人顾问变成焦虑源。

### 3.3 力谏强度控件

demo 的力谏 slider 很有辨识度，应保留但改成更语义化：

- 三档默认：`留余地`、`直说`、`力谏`，而不是 0-100。
- 高级用户可长按展开五档：`温和澄清`、`平衡分析`、`直给判断`、`挑战假设`、`强行拦截`。
- 颜色从中性金 -> 警示琥珀 -> 克制红，不要绿红交通灯过强。
- 每档配一句示例：`我会指出你可能不想听的部分`。
- 强度应影响语气和结构，不应影响事实严谨度。
- 对高风险议题可自动建议提高强度，但必须让用户确认。

### 3.4 历史时间线

Keel 历史不是聊天记录，而是战略记忆。建议使用三层：

- **Today / 本周**：按时间显示原话、立场、下一步。
- **Topic 视图**：同一个客户、项目、组织议题下的连续判断。
- **立场卡视图**：只看已沉淀的关键判断，像私人投资备忘录。

每条历史卡的结构：

- 标题：AI 自动生成，但可编辑。
- 原话：保留 1-2 句关键转写。
- 主见：一句立场。
- 依据：最多 3 点。
- 后续：`待观察`、`已验证`、`推翻`、`过期`。
- 来源：关联历史记录和 topic。

### 3.5 Topic 切换

Topic 不应是复杂文件夹。建议：

- 首屏顶部显示当前 topic pill：`公司战略`、`销售机会`、`组织人事`、`家庭/精力`、`未分类`。
- 语音结束后自动建议 topic，用户左右滑确认。
- 支持一个记录多个 topic，但主 topic 只有一个。
- Mac 端可提供侧栏管理，iPhone 端只提供搜索和横向 pills。
- 允许固定 3 个常用 topic，其余折叠。

### 3.6 空状态

Keel 的空状态应该像顾问坐在旁边，而不是营销页。建议文案：

- 主标题：`说一句正在卡住你的事。`
- 副文案：`10 秒也够。我会先确认问题，再给立场。`
- 三个 prompt chip：`这事该不该推进？`、`我是不是在自欺？`、`怎么跟他开口？`
- 隐私提示：`默认只在本机保存；可随时删除。`
- 不建议用：`今天感觉如何？`、`我一直都在哦`、`让我们一起成长`。

### 3.7 加载态

加载不是 spinner，而是判断过程可见：

- 转写中：小波形 + `正在听`。
- 理解中：`正在确认你真正要判断的问题`。
- 回复中：分阶段显示 `立场` -> `理由` -> `下一步`。
- 如果超过 4 秒，显示一行可取消文案：`还在想，先给你一句初判？`
- 对 Mac 端可使用 menu bar 小状态，不抢焦点。

### 3.8 错误态

错误态要像可靠助手，不要像 API 报错：

- 麦克风权限缺失：`我还不能听你说话。打开麦克风权限后再试。`
- 转写置信度低：`这句我没听准。你可以重说，或直接改这 12 个字。`
- 网络/模型失败：`这次没能给出完整判断。原话已保存，稍后可继续。`
- 敏感内容保存失败：`记录没有写入本地库。你可以复制文本或重试。`
- 不确定回答：明确说 `我没有足够信息下结论`，并给 1 个最关键追问。

---

## 4. 军师专属设计原则

1. **先承接，再判断。** 每次回复先用一句话确认“你真正问的是……”，再给立场。否则再聪明也像冒进。
2. **树洞感来自安静，不来自撒娇。** 深色、低亮度、少动效、短句、Face ID，让用户敢说难听话和真实恐惧。
3. **不谄媚的视觉语气。** 成功不是烟花，风险不是咆哮；颜色和文案都服务判断，不服务情绪奖励。
4. **高管 10 秒路径。** 打开、说一句、确认、得到立场，核心路径不能超过 2 次显性选择。
5. **立场要可追溯。** 每个建议都能回到原话、历史判断和关键依据；不要给无来源的“神谕”。
6. **默认私密，显式外发。** 任何分享、导出、推送细节、云同步都要用户主动打开。
7. **少聊天，多沉淀。** Keel 可以对话，但产品价值在立场卡、复盘点、topic 脉络，而不是消息数量。
8. **力谏是权力，不是皮肤。** “强谏”只在用户授权或风险明确时出现；它应该让人清醒，不让人被冒犯。

---

## 5. 对 `track-a/demo` 的具体改进建议（可实施）

1. **把首屏 CTA 从多 tab 感改为「单一语音入口」。** 当前有「说 / 立场 / 日志 / 历史」的 demo 信息完整，但首屏焦点可以更强：默认展示大号圆形/胶囊按钮 `按住说一句`，tab 降到下方。
2. **加入「确认卡」状态。** 录音结束后先显示 `我理解你要判断的是……`，按钮为 `对，直接答`、`改一下`、`再补 10 秒`。
3. **力谏 slider 改为三档 segmented control + 可展开 slider。** 默认显示 `留余地 / 直说 / 力谏`，避免用户一开始被绿红渐变暗示成情绪强度。
4. **顶部 topic select 改成 pill。** `战略`、`组织`、`客户`、`融资` 横向 pill 更像移动端原生模式；select 在 iOS 上会显得网页化。
5. **通知预览增加隐私版本切换。** 同一张卡展示 `普通：A 客户该复盘了` 与 `隐身：有一条立场需要复盘`，帮助定义 discreet 规则。
6. **回复卡固定三段结构。** 每次 demo 回复使用 `主见`、`为什么`、`下一步`，培养产品记忆点。
7. **历史卡增加状态标签。** `待验证`、`已验证`、`推翻`、`过期` 比单纯时间线更像战略顾问。
8. **减少全局金色面积。** 金色保留给 brand、primary CTA 和关键立场；普通边框/背景继续用低对比灰，提升高管风。
9. **加入错误/低置信度 demo。** 展示 `这句我没听准` 的编辑体验，语音产品的可信度来自失败时也优雅。
10. **加入 Mac 状态入口 mock。** 在 demo 旁边放一个小 menu bar / notch 入口示意：`主见 · 待复盘 1`，连接未来 iPhone+Mac 方向。

---

## 6. `ios/` 原生 app 界面架构建议

当前仓库未见 `ios/` 文件，因此以下按新建 SwiftUI iPhone+Mac 方案建议。

### 6.1 产品信息架构

建议 iPhone 使用 4 个底部 tab：

1. **说**：默认主屏，语音输入、确认卡、即时回复。
2. **立场**：沉淀后的关键判断卡，不等同于聊天历史。
3. **日志**：按时间线看原话、转写、回复、topic。
4. **我**：隐私、模型、名词本、通知、力谏默认强度。

Mac 使用三栏或两栏：

- 左侧：Topic / 立场 / 搜索。
- 中间：时间线或立场列表。
- 右侧：选中记录详情 / 语音输入浮层。
- Menu bar extra：快速说一句、最近待复盘、隐身模式开关。

### 6.2 主屏默认态

默认态结构：

1. 顶部：`主见` + 隐私状态小字 `本机记录` + topic pill。
2. 中央：大按钮 `按住说一句`，下方小字 `10 秒也够`。
3. 按钮下：三个 prompt chips：`该不该推进？`、`怎么开口？`、`我哪里想错了？`
4. 下方：最近一条未复盘立场，小卡片即可，不要抢主 CTA。
5. 底部：tab bar。

### 6.3 主屏状态机

建议 SwiftUI 先按状态机实现，而不是边写边堆 view：

- `idle`：空闲 / 默认态。
- `recording`：正在录音，显示波形、实时转写、取消。
- `confirming`：确认 AI 理解的问题，允许改写。
- `responding`：生成主见，分段流式显示。
- `result`：立场卡，可保存/追问/标记待复盘。
- `error`：权限、转写、网络、模型失败。

### 6.4 关键界面组件

- `VoiceCaptureButton`：支持 tap-to-start、press-and-hold、Action Button shortcut。
- `TranscriptPreview`：1-3 行实时转写，可点开全文。
- `IntentConfirmCard`：确认问题和 topic。
- `CounselResponseCard`：`主见 / 为什么 / 下一步`。
- `AdmonitionControl`：力谏强度三档控件。
- `StanceCard`：可复盘判断卡。
- `TimelineCard`：日志中的轻量记录。
- `TopicPillBar`：横向 topic 筛选。
- `PrivacyBanner`：仅在首次和设置页出现，不要常驻制造焦虑。

### 6.5 iPhone 与 Mac 差异

- iPhone：为 10 秒输入优化，尽量少管理。
- Mac：为复盘、搜索、编辑立场卡优化。
- iPhone 默认语音；Mac 默认键盘 + menu bar 快速语音。
- iPhone 的 history 是卡片流；Mac 的 history 是可筛选列表。
- iPhone 不显示复杂 memory；Mac 可以显示「相关历史」和「引用来源」。

### 6.6 首版不建议做的界面

- 不做 AI 头像、表情、宠物、眨眼。
- 不做复杂 dashboard 和情绪图谱。
- 不做公开社区 prompt。
- 不做多 coach 市场。
- 不把所有模型/provider 设置放在首屏。
- 不默认展示公司名/人名在通知里。

---

## 7. 最值得借鉴的 3 个 UI pattern

1. **Voice-in-Context：语音不脱离历史。** 像 ChatGPT / Claude 新 voice mode，把语音、转写、回复留在同一会话/记录上下文里；Keel 应进一步把它沉淀为立场卡。
2. **Source-backed Memory：历史回答必须可追溯。** 像 Voicenotes 的 Ask AI sources、Echo 的语义搜索、AICoven 的本地 memories；Keel 的每个判断都应能显示「来自哪几条原话/历史立场」。
3. **Semantic Restraint：颜色和动效只表达判断。** 像 Things 的克制配色、Bear 的 typography-first、Day One 的轻量 capture；Keel 的金色用于信任，红色只用于强风险，动画只用于录音/生成状态。

---

## 8. 来源链接索引

开源项目：

- DailyVox: https://github.com/intrepidkarthi/dailyvox
- EchoDiary: https://github.com/chenjy16/EchoDiary
- Voice-Diary / 碎碎念: https://github.com/SANABI-LL/Voice-Diary
- Aurea Voice Journal: https://github.com/Lalitmukesh69/aurea-voice-journal
- Local voice-diary: https://github.com/Prabodh-dev/voice-diary
- Echo: https://github.com/29sayantanc/Echo
- PikoChan: https://github.com/neur0map/PikoChan
- Ba-Chan: https://github.com/inthepond/Ba-Chan
- AICoven Local: https://github.com/lepapillonterrible/aicoven-local-opensource
- Alfred: https://github.com/mitensampat/alfred
- The Praeceptor: https://github.com/orteug/the-praeceptor
- Ayna: https://github.com/sozercan/ayna
- Simon AI Coach: https://github.com/oguzkopan/simon-ai-coach

产品 / UI 参考：

- Voicenotes: https://voicenotes.com/
- Voicenotes App Store: https://apps.apple.com/us/app/voicenotes-ai-notes-meetings/id6483293628
- Voicenotes tags help: https://help.voicenotes.com/en/articles/10393499-how-to-organize-your-notes-in-voicenotes-using-tags
- Rosebud: https://www.rosebud.app/new-home
- Rosebud voice journaling: https://help.rosebud.app/tools-for-growth/voice-journaling
- Rosebud App Store: https://apps.apple.com/kz/app/rosebud-ai-journal-diary/id6451135127
- ChatGPT Voice help: https://help.openai.com/en/articles/20001274
- ChatGPT voice-in-chat coverage: https://www.phonearena.com/news/chatgpt-voice-mode-is-accessible-in-chat_id176082
- ChatGPT Action Button reference: https://venturebeat.com/business/how-to-map-openais-chatgpt-advanced-voice-mode-to-your-iPhone-action-button
- Claude voice mode: https://support.claude.com/en/articles/11101966-use-voice-mode
- Claude Artifacts: https://claude.com/blog/artifacts
- Day One UI breakdown: https://screensdesign.com/showcase/day-one-journal-private-diary
- Day One review: https://www.macstories.net/reviews/review-the-new-day-one/
- Bear UI breakdown: https://screensdesign.com/showcase/bear-markdown-notes
- Bear typography-first guide: https://blakecrosley.com/guides/design/bear
- Things focused simplicity guide: https://blakecrosley.com/guides/design/things
