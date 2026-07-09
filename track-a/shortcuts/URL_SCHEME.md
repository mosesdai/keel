# 快捷指令 URL Scheme（含 keel:// 深链草案）

---

## 1) 直接触发快捷指令

- `shortcuts://run-shortcut?name=主见`
- `shortcuts://run-shortcut?name=Keel`

带文本输入：

- `shortcuts://run-shortcut?name=主见&input=text&text=%2Fmax%20腾讯阿里版权续约我有个反直觉判断`

---

## 2) keel:// topic 深链（建议）

Track A 推荐在外部文档里统一写：

- `keel://topic/tencent-ali-renewal`
- `keel://topic/lining-pitch`
- `keel://topic/baijiu-wly-lzlj`

可带参数：

- `keel://topic/tencent-ali-renewal?input=%2Fmax%20请帮我先证伪再给建议`

---

## 3) 当前落地方式（过渡版）

目前 iOS 不会直接识别 `keel://`，建议这样映射：

1. 在备忘录/日历里使用 `keel://topic/...` 作为统一书写规范
2. 实际可点击链接使用 `shortcuts://run-shortcut?...`
3. 在快捷指令内部根据传入文本或菜单选择 topic

> 等原生 app 具备 URL Scheme Handler 后，`keel://topic/{slug}` 可直接落到对应 topic 页面。
