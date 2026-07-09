# ios/Keel · SwiftUI 占位工程

> **状态**：源码骨架 · 无 `.xcodeproj`（避免无签名 CI 复杂度）  
> **父文档**：[`../README.md`](../README.md) · Issue：[`issues/003-ios-scaffold.md`](../../issues/003-ios-scaffold.md)

---

## 在 Xcode 中打开（推荐）

1. 安装 **Xcode 15+**（macOS）
2. **File → New → Project → iOS → App**
3. Product Name：**Keel**，Interface：**SwiftUI**，Language：**Swift**
4. 保存到本目录 **`ios/Keel/`**（与现有 `KeelApp.swift`、`ContentView.swift` 合并或替换默认文件）
5. **Minimum Deployments**：iOS **17.0**（可调）
6. Scheme **Keel** → 选 **iPhone 16 Simulator** → **Run**

---

## 用 Swift Package 预览（可选）

本目录暂无 `Package.swift`；SwiftUI App 需 App target，**Xcode 新建工程**最快。

---

## 文件说明

| 文件 | 作用 |
|------|------|
| `KeelApp.swift` | `@main` 入口 |
| `ContentView.swift` | 四 tab 占位：说 / 立场 / 历史 / 日志 |
| `README.md` | 本说明 |

---

## 下一步（S2）

- `KeelAPIClient`：`URLSession` + Keychain 存 `KEEL_API_KEY`
- 对接 staging：`https://keel-production-be1c.up.railway.app`
- CI：`.github/workflows/ios-ci.yml`（simulator build，无签名）

---

## Bundle ID（待 Moses 拍板）

占位：`com.mosesdai.keel` — 见 [`DISTRIBUTION.md`](../../DISTRIBUTION.md) Ad Hoc 路径。
