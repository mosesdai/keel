import SwiftUI

/// 首屏占位 · 对齐 `track-a/demo/index.html` 四 tab 与 research/05 状态机
struct ContentView: View {
    @State private var selectedTab = 0
    @State private var topicSlug = "tencent-ali-renewal"
    @State private var transcript = ""
    @State private var adviceIntensity = 3

    private let topics: [(slug: String, name: String)] = [
        ("tencent-ali-renewal", "腾讯阿里版权续约"),
        ("lining-pitch", "李宁提案"),
        ("baijiu-wly-lzlj", "白酒")
    ]

    var body: some View {
        TabView(selection: $selectedTab) {
            speakTab
                .tabItem { Label("说", systemImage: "mic.fill") }
                .tag(0)
            placeholderTab(title: "立场", icon: "square.stack.3d.up", hint: "living_position 活文档")
                .tabItem { Label("立场", systemImage: "square.stack.3d.up") }
                .tag(1)
            placeholderTab(title: "历史", icon: "clock", hint: "按话题时间线")
                .tabItem { Label("历史", systemImage: "clock") }
                .tag(2)
            placeholderTab(title: "日志", icon: "doc.text", hint: "每日快照")
                .tabItem { Label("日志", systemImage: "doc.text") }
                .tag(3)
        }
        .tint(Color(red: 0.77, green: 0.65, blue: 0.45))
        .preferredColorScheme(.dark)
    }

    private var speakTab: some View {
        NavigationStack {
            VStack(spacing: 20) {
                topicPills
                Text("说一句正在卡住你的事。")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                promptChips
                TextEditor(text: $transcript)
                    .frame(minHeight: 100)
                    .padding(8)
                    .background(Color(white: 0.12))
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                Button {
                    // TODO: KeelAPIClient POST /v1/entry
                } label: {
                    Label("确认并请教军师", systemImage: "sparkles")
                        .frame(maxWidth: .infinity)
                }
                .buttonStyle(.borderedProminent)
                .tint(Color(red: 0.77, green: 0.65, blue: 0.45))
                Spacer()
            }
            .padding()
            .navigationTitle("主见")
            .toolbar {
                ToolbarItem(placement: .principal) {
                    Text("Keel").font(.caption).foregroundStyle(.secondary)
                }
            }
        }
    }

    private var topicPills: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                ForEach(topics, id: \.slug) { t in
                    Button(t.name) { topicSlug = t.slug }
                        .font(.caption)
                        .padding(.horizontal, 12)
                        .padding(.vertical, 6)
                        .background(topicSlug == t.slug ? Color.white.opacity(0.12) : Color.clear)
                        .overlay(Capsule().stroke(Color.white.opacity(0.15)))
                        .clipShape(Capsule())
                }
            }
        }
    }

    private var promptChips: some View {
        HStack {
            ForEach(["该不该推进？", "怎么开口？", "我哪里想错了？"], id: \.self) { chip in
                Button(chip) { transcript = chip }
                    .font(.caption2)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(Color.white.opacity(0.06))
                    .clipShape(Capsule())
            }
        }
    }

    private func placeholderTab(title: String, icon: String, hint: String) -> some View {
        ContentUnavailableView(
            title,
            systemImage: icon,
            description: Text(hint)
        )
    }
}

#Preview {
    ContentView()
}
