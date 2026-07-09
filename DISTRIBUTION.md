# 主见 / Keel · iPhone 分发手册

> 日期：2026-07-09  
> 读者：Moses、九叔、AI agents  
> 依据：`ROADMAP.md`、`PLAYBOOK.md`、`GITHUB_SETUP.md`、`research/04-M0-快速路径.md`  
> 一句话：**7/15 用 Bridge Track 过渡；原生 app 出来后，Moses 可接受用 AirDrop 发 Ad Hoc IPA 给九叔真机安装。**

---

## 0. 诚实时间线（先说清楚）

| 路径 | 首次交付耗时 | 一次性决策 | 更新节奏 |
|---|---|---|---|
| **Bridge Track**（快捷指令 + 主屏图标）| **48–72 小时**，7/15 可交付 | 无 Apple 账号要求 | Moses 改快捷指令 / 后端热更新 |
| **Ad Hoc + AirDrop** | UDID 注册后 **当天可装**；首次搭签名通常 **1–2 天** | Apple Developer **$99/年**、九叔 UDID、Bundle ID | 每次出新 build，Moses AirDrop 新 IPA |
| **Development build** | 同 Ad Hoc，但证书 7 天 | 同上，且仅限开发机 | 不适合给九叔长期用 |
| **TestFlight** | 原生 app 做完后 **+1–3 天 beta review**；整体 **2–4 周** | 同上 + 隐私文案 + Beta 审核信息 | 上传新 build 后九叔在 TestFlight 内更新；可微信发 public link |
| **App Store** | **数周**，审核不可控 | 上架元数据、截图、隐私政策 | 九叔 App Store 更新 |
| **PWA** | 数小时可做 demo | 无 | 仅过渡，**不作主路径** |

**Ad Hoc 比 TestFlight 快多少？**  
- 跳过 Apple Beta App Review（首个外测 build 通常 **24–48 小时**，有时更长）。  
- UDID 已在 Developer Portal 注册、签名配好后，**Archive → Export Ad Hoc → AirDrop** 可在 **30 分钟内** 让九叔装上。  
- 代价：每次更新需 Moses 手动 AirDrop；设备数有上限；证书/描述文件要维护。

**Moses 须拍板的一次性决策：**
1. 是否开通/续费 **Apple Developer Program**（$99/年）。
2. **Bundle ID**（建议 `com.eliam.keel` 或公司域名反写）。
3. 收集 **九叔 iPhone UDID** 并注册到 Developer Portal。
4. 7/15 前走 Bridge Track；原生出来后 **Ad Hoc AirDrop** 还是等 **TestFlight**（可并行：先 AirDrop Alpha，后切 TestFlight）。

---

## 1. 主推荐路径：九叔 iPhone「像 app 一样用」对比

### 1.1 分阶段推荐（2026-07-09 修订）

| 阶段 | 日期 | 主路径 | 交付物 | 九叔体验 |
|---|---|---|---|---|
| **过渡** | 07-15 | **Bridge Track** | 快捷指令 + 云端 API + 主屏图标 | 像装了一个入口，本质是快捷指令；**不需 Cursor** |
| **原生 Alpha** | 07-18–07-24 | **Ad Hoc + AirDrop**（Moses 明确接受）| 签过名的 `.ipa` | **真·原生 app**，主屏有图标，点开即用 |
| **原生 Beta** | 08-02 前后 | **TestFlight public link** | 微信可转的测试链接 | 先装 TestFlight，再装「主见/Keel」；更新自动提示 |
| **稳定** | 08 月+ | TestFlight 长期 / App Store | 视审核策略 | 最像正式产品 |

### 1.2 全方案对比表

| 方案 | 传输方式 | 像真 app？ | 微信能发？ | 首次耗时 | 适合阶段 |
|---|---|---:|---|---:|---|
| Bridge Track | 当面/微信发安装说明 | 半像（主屏图标）| ✅ 说明/链接 | 1–3 天 | **7/15 主路径** |
| **Ad Hoc + AirDrop** | **AirDrop `.ipa`** 或安装页 | **✅ 真原生** | ❌（AirDrop 需近场）；可用邮件/网盘备选 | UDID 后当天 | **原生 Alpha 主路径之一** |
| TestFlight | 微信 public link | ✅ 真原生 | ✅ | +1–3 天 review | **原生 Beta 主路径** |
| Development | Xcode 直连 / AirDrop | ✅ 真原生 | ❌ | 当天 | 仅 Moses 自测，不给九叔 |
| Enterprise | 内网链接 / MDM | ✅ | 视内网 | 需企业账号 | **不推荐**（违规风险）|
| PWA | URL | ❌ 弱 | URL 可发 | 数小时 | **仅 demo，不作主入口** |
| App Store | 商店链接 | ✅ 最正式 | ✅ | 数周 | M1 稳定化 |

### 1.3 为什么 AirDrop 对军师项目合理

- Moses 与九叔**可当面或同城**，AirDrop 零摩擦，**不依赖微信传大文件**。
- 微信传 `.ipa` 常被限制或体验差；AirDrop 是 Apple 生态内最稳的「把 app 塞到对方手机」方式。
- 仅 **1 台设备**（九叔 iPhone），远低于 Ad Hoc **每类设备每年 100 台**上限。
- 在 TestFlight beta review 等待期，Ad Hoc 让九叔**提前 1–3 天**用上原生 build。

---

## 2. AirDrop 路径详解（Ad Hoc IPA）

### 2.1 技术实质：三种 build 怎么选

| 类型 | 签名目的 | 设备限制 | 有效期 | 能否 AirDrop 给九叔 | 结论 |
|---|---|---|---|---:|---|
| **Development** | 开发调试 | 注册的开发设备 | 证书约 **7 天** | 能装，但常过期 | **不给九叔** |
| **Ad Hoc** | 限定设备分发 | 最多 **100 台/类/年** | 分发证书 **1 年**；描述文件随证书 | **✅ 推荐** | **Moses → 九叔主路径** |
| **App Store / TestFlight** | 商店或 TestFlight | 外部测试最多 1 万人 | build **90 天**（TestFlight）| 走 TestFlight，不走 AirDrop IPA | Beta 主路径 |

**Ad Hoc 是什么？**  
用 Apple Developer 账号签名、且 **Provisioning Profile 里写明允许安装的 UDID 列表** 的 IPA。只有列表里的 iPhone 能装。装好后图标在主屏，体验与 App Store 版一致（无 TestFlight 壳）。

**不是**「破解安装」；是 Apple 官方支持的小规模分发，适合内部测试、客户预览、家人朋友——正好符合 Moses → 九叔 n=1 场景。

### 2.2 前置条件（一次性 + 每设备）

#### A. Apple Developer Program

1. 访问 [developer.apple.com](https://developer.apple.com/programs/) 注册/续费（**$99/年**）。
2. 确认 **Team**（个人或公司）与后续证书一致。
3. 在 **Certificates, Identifiers & Profiles** 创建：
   - **App ID** / Bundle ID：`com.eliam.keel`（示例，Moses 终审）。
   - **iOS Distribution Certificate**（Apple Distribution）。
   - **Ad Hoc Provisioning Profile**：类型选 **Ad Hoc**，勾选九叔设备 UDID，关联上述 App ID。

#### B. 九叔设备 UDID

九叔只需配合 **30 秒**；Moses 操作：

**方法 1：九叔用 Mac 连 iPhone（推荐）**
1. iPhone 连 Mac，打开 **Finder**（或旧版 iTunes）。
2. 选中设备 → 点序列号区域直至显示 **UDID** → 右键复制。

**方法 2：九叔 iPhone 本机（iOS 16+）**
1. 设置 → 通用 → 关于本机。
2. 连点「序列号」切换显示 **UDID**（部分机型/版本需借助 Apple Configurator 或 Xcode Devices 窗口）。

**方法 3：临时配置文件**
1. Moses 发一个 `.mobileconfig` 或通过 Apple Configurator 读取（适合远程；当面用方法 1 最快）。

拿到 UDID 后：
1. Developer Portal → **Devices** → Register Device（名称填 `Jiushu-iPhone`）。
2. 编辑 **Ad Hoc Provisioning Profile** → 勾选该设备 → **Download** 新 profile。
3. 若用 Xcode Automatic Signing，在 Xcode 中 Refresh Profiles。

#### C. 本地或 CI 签名材料

| 材料 | 存放位置 | 禁止 |
|---|---|---|
| `.p12` 分发证书 + 密码 | Moses 钥匙串 / CI Secrets | **不得 commit 到 GitHub** |
| `.mobileprovision` Ad Hoc 描述文件 | Xcode / CI 临时目录 | **不得 commit** |
| `ExportOptions.plist` | repo 可放**无密钥**模板 | 不含 team ID 敏感备份 |

---

### 2.3 Moses 操作：本地 Xcode Archive → AirDrop

**首次约 1–2 小时**（含证书）；之后每次发版 **约 30 分钟**。

#### Step 1：工程签名

1. 打开 `ios/Keel.xcodeproj`（Track B  scaffold 完成后）。
2. **Signing & Capabilities**：
   - Team：Moses 的 Developer Team。
   - Bundle Identifier：与 Portal 一致。
   - Release 配置使用 **Ad Hoc** profile（Manual 或 Automatic 均可，以能 Export Ad Hoc 为准）。

#### Step 2：Archive

1. 选真机目标 **Any iOS Device (arm64)**（不要选 Simulator）。
2. 菜单 **Product → Archive**。
3. Organizer 打开后选中 archive → **Distribute App**。

#### Step 3：Export Ad Hoc

1. 选 **Ad Hoc** → Next。
2. 勾选正确 profile（含九叔 UDID）→ Next。
3. 导出文件夹内得到 **`Keel.ipa`**（名称随 scheme）。

可选：同目录常有 **`manifest.plist` + IPA** 组合，可挂 HTTPS 做 OTA；军师 n=1 场景 **AirDrop 更简单**，OTA 作远程备选。

#### Step 4：AirDrop 给九叔

1. Moses Mac 上 Finder 选中 `Keel.ipa`。
2. 右键 → **共享 → AirDrop** → 选九叔 iPhone（须蓝牙/Wi-Fi 近场、双方 Apple ID 可互发现）。
3. 九叔 iPhone 点 **接受**。

**备选传输**（非近场时）：
- **Apple Mail** 发附件（小团队可行；IPA 约 20–80 MB）。
- **iCloud Drive 链接** + 九叔 Safari 打开（需配合 OTA manifest 或安装工具；不如 AirDrop 稳）。
- **当面用 Apple Configurator 2** 装到已连接设备。

---

### 2.4 九叔操作：安装与首次打开

1. **接受 AirDrop** 后，iPhone 提示安装「主见/Keel」→ 点 **安装**。
2. 若提示未受信任企业级开发者：
   - **设置 → 通用 → VPN 与设备管理**（或「设备管理」/「描述文件」）。
   - 点 **Moses 的开发者名称** → **信任**。
3. 回主屏点开 **主见**：
   - 首次启动允许 **麦克风**（语音）、**网络**。
   - 登录/填 API 由 onboarding 引导（**不应让九叔自己填模型 key**）。
4. 试一条真实输入，确认能收到军师回复。

**九叔不需要**：Xcode、TestFlight、Cursor、GitHub、UDID 自填。

---

### 2.5 限制与维护

| 项目 | 说明 | Moses 应对 |
|---|---|---|
| **设备数上限** | 每 **product family** 每 **membership year** 最多 **100 台** | 军师仅 1–2 台，充裕 |
| **UDID 变更** | 九叔换机 → 新 UDID 须重新注册 + **重签 IPA** | 收新 UDID，重 Export Ad Hoc，再 AirDrop |
| **分发证书** | Apple Distribution 有效期 **1 年** | 到期前续签、重签所有 Ad Hoc build |
| **描述文件** | Profile 过期或增删设备后失效 | Portal 更新 profile → 重新 Archive Export |
| **更新分发** | **无自动更新** | 每个新版本：CI 或 Xcode 产出新 IPA → Moses AirDrop → 九叔覆盖安装 |
| **有效期体验** | Ad Hoc IPA 本身无 90 天限制（不同于 TestFlight build）| 证书/profile 有效期内可一直用 |
| **隐私** | 真 app 仍连 Moses 后端；数据策略见 `DECISIONS.md` | discreet 图标与通知文案 |

**更新 SOP（简版）**  
1. Agent 合并 PR → CI 产出 `Keel-<version>-adhoc.ipa` artifact。  
2. Moses 下载 → AirDrop 九叔。  
3. 九叔安装（覆盖旧版）→ 点开确认版本号。  
4. 在 `SESSION_LOG.md` 记一笔交付记录。

---

## 3. 备选路径

### 3.1 TestFlight（微信可发，原生 Beta 主路径）

**何时用**：原生 app 功能闭环后（目标 **08-02 前后**），需要 **可远程、可自动更新** 的分发。

**Moses 操作概要**：
1. App Store Connect 创建 app、填 Beta 审核信息（隐私 URL、测试说明）。
2. Xcode Archive → **Distribute → App Store Connect**（或 CI 上传）。
3. 等 **Beta App Review**（首个外测 build **通常 24–48h+**）。
4. 外部测试 → 开启 **Public Link** → 复制链接 **微信发给九叔**。

**九叔操作**：
1. 微信点链接 → 安装 **TestFlight**（若未有）。
2. 接受测试 → 安装「主见/Keel」。
3. 以后更新在 TestFlight 里点 **更新**。

**相对 Ad Hoc 的优点**：远程、可微信、更新省心、不需每次收 UDID（已加入测试后）。  
**缺点**：首个 build 要等审核；build **90 天**过期需上传新版；多一步 TestFlight 壳。

**建议策略**：**07-24 前后 Ad Hoc AirDrop 给九叔先用 Alpha** → **08-02 切 TestFlight** 作长期 Beta，九叔可卸载 Ad Hoc 版改装 TestFlight 版（数据走 CloudKit/导入器衔接）。

### 3.2 Enterprise（不推荐）

- Apple Developer **Enterprise Program** 面向 **组织内部员工**，不得给外部个人（九叔）routine 分发。
- 违规可导致 **账号封禁**。
- **不作为军师项目路径**。

### 3.3 Development build（仅 Moses 自测）

- Moses 本机 Xcode **Run to Device** 或 Export Development IPA。
- 证书 **7 天**、设备须注册，**不适合**给九叔长期使用。

---

## 4. 不推荐：PWA 作主路径

| 问题 | 影响 |
|---|---|
| iOS 无自动「安装 app」提示 | 须 Safari **添加到主屏幕**，步骤多 |
| 微信内置浏览器 | **不能**完整 Add to Home Screen；语音/能力受限 |
| 后台、通知、麦克风 | 弱于原生；不符合「随时按住说话」 |
| 决策 3 | 长期形态是 **iPhone + Mac 原生**，非 Web |

**允许用途**：Moses 桌面 `track-a/demo/index.html` 预览体验；**不给九叔作主入口**。

---

## 5. 与 GitHub CI 集成：自动产出可 AirDrop 的 IPA

目标：**agent 合并 PR 后，Moses 从 CI 下载 artifact，AirDrop 给九叔**——无需本机 Archive。

### 5.1 方案对比

| CI | macOS 构建 | 签名 | Artifact | 推荐场景 |
|---|---|---|---|---|
| **GitHub Actions** | `macos-latest` runner | fastlane match 或 manual secrets | `actions/upload-artifact` | 已有 GitHub 底座，**首选** |
| **Codemagic** | 原生 macOS | 内置 iOS 签名向导 | IPA 下载 + 邮件通知 | 签名嫌麻烦时 |
| **Bitrise** | 同上 | 同上 | 同上 | 备选 |

### 5.2 GitHub Actions：`ios-adhoc.yml`（示意）

触发：手动 `workflow_dispatch` 或 tag `ios-v*`。

```yaml
# .github/workflows/ios-adhoc.yml（agent 实现时写入 repo）
name: iOS Ad Hoc IPA
on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Marketing version'
        required: true
jobs:
  adhoc:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install signing cert
        env:
          BUILD_CERTIFICATE_BASE64: ${{ secrets.IOS_DIST_CERT_BASE64 }}
          P12_PASSWORD: ${{ secrets.IOS_DIST_CERT_PASSWORD }}
          BUILD_PROVISION_PROFILE_BASE64: ${{ secrets.IOS_ADHOC_PROFILE_BASE64 }}
        run: |
          # 解码证书与 profile 到 temp keychain（脚本由 agent 补全）
          echo "import cert and profile"
      - name: Build and archive
        run: |
          xcodebuild -scheme Keel -configuration Release \
            -archivePath $RUNNER_TEMP/Keel.xcarchive archive
      - name: Export Ad Hoc IPA
        run: |
          xcodebuild -exportArchive \
            -archivePath $RUNNER_TEMP/Keel.xcarchive \
            -exportPath $RUNNER_TEMP/export \
            -exportOptionsPlist ios/ExportOptionsAdHoc.plist
      - name: Upload IPA artifact
        uses: actions/upload-artifact@v4
        with:
          name: Keel-adhoc-ipa
          path: ${{ runner.temp }}/export/*.ipa
```

**Moses 事后操作**：
1. GitHub → Actions → 选成功 run → **Artifacts** → 下载 `Keel-adhoc-ipa`。
2. 解压得到 `.ipa` → **AirDrop 九叔**。

### 5.3 需在 GitHub Secrets 配置的项（7/16 后）

| Secret | 用途 |
|---|---|
| `IOS_DIST_CERT_BASE64` | 分发证书 `.p12` Base64 |
| `IOS_DIST_CERT_PASSWORD` | `.p12` 密码 |
| `IOS_ADHOC_PROFILE_BASE64` | Ad Hoc `.mobileprovision` Base64 |
| `KEYCHAIN_PASSWORD` | CI 临时钥匙串密码（随机字符串即可）|
| `APP_STORE_CONNECT_*` | TestFlight 上传用（Ad Hoc 不强制）|

生成 Base64（Moses 本机一次性）：

```bash
base64 -i Certificates.p12 | pbcopy
base64 -i AdHoc_com.eliam.keel.mobileprovision | pbcopy
```

**安全**：证书/profile **只进 Secrets**；`.gitignore` 排除 `*.p12`、`*.mobileprovision`。

### 5.4 Codemagic 简版

1. 连接 GitHub repo → 选 `ios/` 工程。
2. **Code signing identities** 上传同一套 Distribution cert + Ad Hoc profile。
3. Workflow 增加 **Ad Hoc** publishing → **IPA artifact**。
4. Build 完成 → Codemagic 面板下载 IPA → Moses AirDrop。

### 5.5 `ExportOptionsAdHoc.plist` 模板（可入库，无密钥）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>method</key>
  <string>ad-hoc</string>
  <key>teamID</key>
  <string>YOUR_TEAM_ID</string>
  <key>compileBitcode</key>
  <false/>
  <key>thinning</key>
  <string>&lt;none&gt;</string>
</dict>
</plist>
```

`YOUR_TEAM_ID` 可入库（非密钥）；或由 CI 环境变量注入。

---

## 6. 分阶段分发决策树

```text
7/15 前
  └─ Bridge Track（快捷指令 + 主屏）── 微信发说明，不需 Apple 账号

7/16 起有 ios/ 工程
  ├─ 九叔在身边、要快？ ── Ad Hoc + AirDrop（Moses 已接受）✅
  ├─ 要远程、要自动更新？ ── 等 TestFlight public link
  └─ Moses 本机调试 ── Development（不给九叔）

8/02 前后
  └─ TestFlight 作长期 Beta；Ad Hoc 可退役或并行救急

M1
  └─ App Store 或长期 TestFlight
```

---

## 7. 相关文档

| 文件 | 内容 |
|---|---|
| `ROADMAP.md` | 日期里程碑与路径选择 |
| `PLAYBOOK.md` | S2 Ad Hoc / S3 TestFlight 阶段 DoD |
| `GITHUB_SETUP.md` | Secrets、CI PR 批次 |
| `CLOUD_DEV.md` | `ios-adhoc.yml` / `ios-release.yml` 位置 |
| `ACCEPTANCE.md` | A0 Bridge / A1 Alpha / A2 TestFlight 验收 |
| `track-a/JIUSHU_ONBOARDING.md` | Bridge Track 九叔上手 |
| `track-a/shortcuts/SETUP.md` | 快捷指令安装 |

---

## 8. Moses 检查清单（分发前）

- [ ] Apple Developer 有效；Team 与 Bundle ID 已定。
- [ ] 九叔 UDID 已注册；Ad Hoc profile 含该设备。
- [ ] `git status` 无 `.p12`、`.mobileprovision`、`.env`。
- [ ] IPA 为 **Release + Ad Hoc**，非 Development/Simulator。
- [ ] 后端 `/health` 正常；九叔端不需填模型 key。
- [ ] 主屏图标与名称 **discreet**（「主见」，非「军师」）。
- [ ] AirDrop 或 TestFlight 交付后，在 `SESSION_LOG.md` 记录版本与日期。
