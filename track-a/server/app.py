from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import httpx
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).with_name(".env"))
except Exception:  # noqa: BLE001
    # 没有 python-dotenv 也可运行，环境变量可由部署平台注入
    pass


# Track A 目录约定：server/ 与 data/ 同级，便于直接落 iCloud 兼容文件结构
APP_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP_ROOT.parent
DATA_DIR = Path(os.getenv("TRACK_A_DATA_DIR", APP_ROOT / "data"))
TOPICS_DIR = DATA_DIR / "topics"
SYSTEM_PROMPT_PATH = Path(
    os.getenv("SYSTEM_PROMPT_PATH", Path(__file__).with_name("prompts") / "system.txt")
)
CHARTER_PATH = Path(
    os.getenv("PERSONALITY_CHARTER_PATH", PROJECT_ROOT / "PERSONALITY_CHARTER.md")
)

TOPIC_SEEDS = [
    ("tencent-ali-renewal", "腾讯阿里版权续约"),
    ("lining-pitch", "李宁提案"),
    ("baijiu-wly-lzlj", "白酒（五粮液 & 泸州老窖）"),
]

FALLBACK_CHARTER = """
你是军师（外显名主见 / Keel）的内部人格，目标是帮助主人形成有脊梁的判断。
必须执行：
1) 树洞：接住情绪，不评判，不泄露；
2) 诤友：反昏君，不迎合，重大判断必须给至少1条反对意见；
3) 镜子：指出与过往立场的张力，解释为何转变。
若输入含 /max、entry 标记 depth: deep，或主题已开启深度模式，请升级为最高诚意模式：更强推理、更完整反证、更大胆 disruptive 创意。
语气规则：就事论事，不羞辱，不冒犯。
"""

POSITIVE_HINTS = ["支持", "看好", "继续", "推进", "增持", "买入", "续约", "乐观", "加码"]
NEGATIVE_HINTS = ["反对", "担心", "停止", "退出", "减持", "卖出", "不续约", "悲观", "撤出"]
ENTITY_HINTS = ["腾讯", "阿里", "版权", "续约", "李宁", "白酒", "NBA"]


class FileMeta(BaseModel):
    filename: Optional[str] = None
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None
    note: Optional[str] = None


class EntryRequest(BaseModel):
    topic_slug: str = Field(..., description="话题 slug，如 tencent-ali-renewal")
    raw_text: str = Field(..., min_length=1, description="语音转写并人工确认后的文本")
    files: Optional[list[FileMeta]] = Field(default=None, description="可选文件元数据")
    topic_mark: Optional[str] = Field(default=None, description="可选标签，例如 深度")
    depth: Optional[str] = Field(default=None, description="可选深度标记，例如 deep")
    advice_intensity: Optional[int] = Field(
        default=3, ge=1, le=5, description="力谏强度 1（平和）~ 5（呛人）"
    )


class EntryResponse(BaseModel):
    topic_slug: str
    reply: str
    living_position_summary: str
    daily_snapshot_snippet: str
    contradiction_detected: bool
    model_provider: str
    model_name: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    used_mock: bool
    timestamp: str


class TopicResponse(BaseModel):
    topic_slug: str
    display_name: str
    living_position: str
    snapshots: list[dict[str, Any]]
    entries: list[dict[str, Any]]
    entries_count: int


app = FastAPI(title="Keel Track A Server", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8765",
        "http://localhost:8765",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "null",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def ensure_storage() -> None:
    # 启动即保证 seed topic 存在，做到“开箱可用”
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    for slug, display_name in TOPIC_SEEDS:
        ensure_topic(slug, display_name)


def ensure_topic(topic_slug: str, display_name: Optional[str] = None) -> dict[str, Any]:
    topic_dir = TOPICS_DIR / topic_slug
    snapshots_dir = topic_dir / "snapshots"
    topic_dir.mkdir(parents=True, exist_ok=True)
    snapshots_dir.mkdir(parents=True, exist_ok=True)

    topic_json = topic_dir / "topic.json"
    living_path = topic_dir / "living_position.md"
    entries_path = topic_dir / "entries.jsonl"

    if not topic_json.exists():
        topic_payload = {
            "slug": topic_slug,
            "display_name": display_name or topic_slug,
            "depth_mode": False,
            "created_at": utc_now(),
        }
        topic_json.write_text(
            json.dumps(topic_payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    if not living_path.exists():
        living_path.write_text("待主人首次输入后生长。", encoding="utf-8")

    if not entries_path.exists():
        entries_path.write_text("", encoding="utf-8")

    return json.loads(topic_json.read_text(encoding="utf-8"))


def utc_now() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def today_compact() -> str:
    return datetime.now().strftime("%Y%m%d")


def load_charter_text() -> str:
    if CHARTER_PATH.exists():
        return CHARTER_PATH.read_text(encoding="utf-8")
    return FALLBACK_CHARTER


def load_system_prompt_base() -> str:
    if SYSTEM_PROMPT_PATH.exists():
        return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()
    return load_charter_text()


def strip_fences(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
        cleaned = re.sub(r"```$", "", cleaned).strip()
    return cleaned


def extract_json_payload(text: str) -> Optional[dict[str, Any]]:
    candidate = strip_fences(text)
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    snippet = candidate[start : end + 1]
    try:
        return json.loads(snippet)
    except json.JSONDecodeError:
        return None


def polarity_score(text: str) -> int:
    pos = sum(text.count(word) for word in POSITIVE_HINTS)
    neg = sum(text.count(word) for word in NEGATIVE_HINTS)
    return pos - neg


def shared_entity(text_a: str, text_b: str) -> bool:
    for token in ENTITY_HINTS:
        if token in text_a and token in text_b:
            return True
    return False


def detect_contradiction_hint(new_text: str, living_position: str) -> bool:
    # 关键词辅助检测：同实体 + 情绪极性反转（支持<->反对）；最终张力由模型对照立场书判断
    if not living_position or living_position.strip() == "待主人首次输入后生长。":
        return False

    old_score = polarity_score(living_position)
    new_score = polarity_score(new_text)
    opposite_polarity = old_score * new_score < 0 and abs(old_score) >= 1 and abs(new_score) >= 1
    if opposite_polarity and shared_entity(new_text, living_position):
        return True

    hard_pairs = [
        ("支持", "反对"),
        ("继续", "停止"),
        ("续约", "不续约"),
        ("增持", "减持"),
        ("买入", "卖出"),
    ]
    for left, right in hard_pairs:
        if (
            (left in living_position and right in new_text)
            or (right in living_position and left in new_text)
        ) and shared_entity(new_text, living_position):
            return True
    return False


def route_model(
    raw_text: str, topic: dict[str, Any], topic_mark: Optional[str], entry_depth: Optional[str]
) -> tuple[str, str, bool]:
    # 路由原则：默认走最便宜可用 DeepSeek；仅深度请求才升档
    has_deepseek = bool(os.getenv("DEEPSEEK_API_KEY"))
    has_qwen = bool(os.getenv("DASHSCOPE_API_KEY"))

    deep_topics = {
        item.strip()
        for item in os.getenv("DEEP_TOPIC_SLUGS", "deep,strategic,重大").split(",")
        if item.strip()
    }
    deepseek_default_model = os.getenv("DEEPSEEK_MODEL_DEFAULT", "deepseek-chat")
    deepseek_deep_model = os.getenv("DEEPSEEK_MODEL_DEEP") or os.getenv(
        "DEEPSEEK_MODEL_MAX", "deepseek-reasoner"
    )

    depth_by_text = "/max" in raw_text.lower()
    depth_by_mark = (topic_mark or "").strip().lower() in {"深度", "deep"}
    depth_by_entry = (entry_depth or "").strip().lower() == "deep"
    depth_by_topic = bool(topic.get("depth_mode")) or topic["slug"] in deep_topics
    is_depth = depth_by_text or depth_by_mark or depth_by_entry or depth_by_topic

    if is_depth:
        if has_deepseek:
            return "deepseek", deepseek_deep_model, True
        if has_qwen:
            return "qwen", os.getenv("QWEN_MODEL_MAX", "qwen-max"), True
        return "mock", "mock-max", True

    if has_deepseek:
        return "deepseek", deepseek_default_model, False
    if has_qwen:
        return "qwen", os.getenv("QWEN_MODEL_DEFAULT", "qwen-plus"), False
    return "mock", "mock-default", False


INTENSITY_HINTS: dict[int, str] = {
    1: "力谏强度 1/5（平和）：以倾听和澄清为主，少反驳，语气柔软。",
    2: "力谏强度 2/5（轻扶）：温和提醒风险，不强行对抗。",
    3: "力谏强度 3/5（常态）：平衡树洞与诤友，常规反对意见。",
    4: "力谏强度 4/5（直谏）：直言风险与反对，不回避冲突。",
    5: "力谏强度 5/5（呛人）：最高诚意、最强反对，措辞可更尖锐但仍不冒犯。",
}


def compose_system_prompt(
    charter_text: str, contradiction_hint: bool, advice_intensity: int = 3
) -> str:
    hint_rule = (
        "关键词辅助检测到新旧立场可能有张力——请在 reason_for_shift 中认真解释转变或延续，"
        "对照旧立场书逐点说明哪些假设变了、哪些证据变了、哪些只是情绪态。"
        if contradiction_hint
        else "请主动对照旧立场书与新输入，判断是延续还是转变，并在 reason_for_shift 中说明理由。"
    )
    intensity_rule = INTENSITY_HINTS.get(advice_intensity, INTENSITY_HINTS[3])
    return (
        f"{charter_text}\n\n"
        f"{intensity_rule}\n"
        f"{hint_rule}\n"
        "回复要有力度、不迎合；允许较长、结构化推演。仅返回 JSON，不要多余文本。"
    )


def require_api_key(x_api_key: Optional[str] = Header(default=None, alias="X-API-Key")) -> None:
    expected = os.getenv("KEEL_API_KEY", "").strip()
    if not expected:
        raise HTTPException(status_code=503, detail="服务端未配置 KEEL_API_KEY")
    if not x_api_key or x_api_key != expected:
        raise HTTPException(status_code=401, detail="X-API-Key 无效")


def compose_user_prompt(
    topic: dict[str, Any], raw_text: str, living_position: str, contradiction_hint: bool
) -> str:
    hint_note = (
        "关键词辅助：可能检测到立场张力（仅供参考，以你的对照分析为准）。"
        if contradiction_hint
        else "关键词辅助：未检测到明显极性反转（仍须你独立对照旧立场书判断）。"
    )
    return f"""
当前主题：
- slug: {topic["slug"]}
- 展示名: {topic.get("display_name", topic["slug"])}

当前立场书（旧）：
{living_position}

新输入（已人工确认）：
{raw_text}

{hint_note}

【镜子任务】把「当前立场书（旧）」和「新输入」一起读，判断是延续还是转变。
在 reason_for_shift 中解释：哪些证据/假设变了？是情绪态反转还是理性修正？仍有哪些不确定性？

请输出 JSON，字段必须完整：
{{
  "reply": "给主人的结构化回复（Markdown，200~600字，含主见/反对意见/disruptive备选/下一步）",
  "living_position_update": "更新后的当前立场书（Markdown，150~400字）",
  "daily_snapshot": "今日快照追加片段（Markdown，100~250字）",
  "reason_for_shift": "对照旧立场书解释：延续还是转变，为什么（80~200字）",
  "tension_detected": true或false
}}
"""


class ModelCallError(Exception):
    def __init__(
        self,
        message: str,
        *,
        provider: str,
        status_code: Optional[int] = None,
        error_code: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.provider = provider
        self.status_code = status_code
        self.error_code = error_code


def parse_provider_error(response: httpx.Response, provider: str) -> ModelCallError:
    status = response.status_code
    body: dict[str, Any] = {}
    try:
        body = response.json()
    except Exception:  # noqa: BLE001
        body = {}

    err = body.get("error", body)
    message = str(err.get("message") or response.text[:240] or f"{provider} HTTP {status}")
    error_code = err.get("code") or err.get("type")
    return ModelCallError(
        message,
        provider=provider,
        status_code=status,
        error_code=str(error_code) if error_code else None,
    )


def deepseek_chat(messages: list[dict[str, str]], model: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ModelCallError("DEEPSEEK_API_KEY 未配置", provider="deepseek")

    payload = {"model": model, "messages": messages, "temperature": 0.6}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/chat/completions")

    with httpx.Client(timeout=40.0) as client:
        response = client.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise parse_provider_error(response, "deepseek")
        data = response.json()
    return data["choices"][0]["message"]["content"]


def qwen_chat(messages: list[dict[str, str]], model: str) -> str:
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise ModelCallError("DASHSCOPE_API_KEY 未配置", provider="qwen")

    payload = {"model": model, "messages": messages, "temperature": 0.6}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    url = os.getenv(
        "QWEN_BASE_URL",
        "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
    )

    with httpx.Client(timeout=40.0) as client:
        response = client.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise parse_provider_error(response, "qwen")
        data = response.json()
    return data["choices"][0]["message"]["content"]


def mock_output(raw_text: str, contradiction_hint: bool) -> dict[str, str]:
    head = raw_text.strip().replace("\n", " ")
    if len(head) > 80:
        head = head[:80] + "..."

    if contradiction_hint:
        reply = (
            "⚠️ **本地兜底（非 DeepSeek）**\n\n"
            "**主见**：我先不裁决对错——你这次判断和旧立场出现了张力。\n"
            "**反对意见**：若把情绪反转当成证据更新，可能误判谈判窗口。\n"
            "**disruptive备选**：先冻结立场 48 小时，用三条独立证据复核后再定档。\n"
            "**下一步**：列出触发变化的三条证据，做续约分层（必须谈/可谈/坚决不谈）。"
        )
        reason = "关键词辅助检测到张力；本地兜底无法做真推演，待 DeepSeek 恢复后重跑。"
    else:
        reply = (
            "⚠️ **本地兜底（非 DeepSeek）**\n\n"
            f"**主见**：我先接住你的核心判断——{head}\n"
            "**反对意见**：若只盯支持证据，可能错过替代合作窗口。\n"
            "**disruptive备选**：并行试探第二谈判路径，不把筹码押在单一路径。\n"
            "**下一步**：48 小时内补齐关键反证与价格区间证据。"
        )
        reason = "本地兜底延续旧立场框架；待 DeepSeek 恢复后做真推演。"

    living_update = (
        "## 当前立场\n"
        "- 主张：围绕当前主题，优先把可验证条件讲清，再谈情绪判断。\n"
        "- 本轮新增："
        + head
        + "\n- 反对意见：若过度押注单一路径，可能错失替代窗口。\n"
        "- 下一步：48 小时内补齐关键反证与价格区间证据。"
    )
    daily_snapshot = (
        f"### {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 片段：{head}\n"
        "- 军师动作：本地兜底——给出稳妥路径 + disruptive 备选，并提示最脆弱假设。"
    )
    return {
        "reply": reply,
        "living_position_update": living_update,
        "daily_snapshot": daily_snapshot,
        "reason_for_shift": reason,
        "tension_detected": contradiction_hint,
    }


def call_model(
    provider: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    raw_text: str,
    contradiction_hint: bool,
) -> tuple[dict[str, Any], bool, str, str, dict[str, Any]]:
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
    error_meta: dict[str, Any] = {}

    if provider == "mock":
        error_meta = {
            "fallback_reason": "no_provider_key",
            "message": "未配置 DEEPSEEK_API_KEY 或 DASHSCOPE_API_KEY",
        }
        return mock_output(raw_text, contradiction_hint), True, "mock", model, error_meta

    try:
        if provider == "deepseek":
            content = deepseek_chat(messages, model)
        elif provider == "qwen":
            content = qwen_chat(messages, model)
        else:
            raise ModelCallError(f"未知 provider: {provider}", provider=provider)

        parsed = extract_json_payload(content)
        if not parsed:
            error_meta = {
                "fallback_reason": "invalid_json",
                "message": "模型返回非 JSON，已降级",
                "raw_preview": content[:300],
            }
            parsed = mock_output(raw_text, contradiction_hint)
            parsed["reply"] = (
                "⚠️ 模型输出格式异常，已降级为本地兜底（非真军师推理）：\n\n" + parsed["reply"]
            )
            return parsed, True, "mock", "mock-fallback", error_meta
        return parsed, False, provider, model, error_meta
    except ModelCallError as exc:
        error_meta = {
            "fallback_reason": "provider_error",
            "provider": exc.provider,
            "status_code": exc.status_code,
            "error_code": exc.error_code,
            "message": exc.message,
        }
        fallback = mock_output(raw_text, contradiction_hint)
        status = exc.status_code or "n/a"
        code = exc.error_code or "unknown"
        fallback["reply"] = (
            f"⚠️ {exc.provider} 调用失败（HTTP {status} / {code}）：{exc.message}\n"
            "以下为本地兜底，**不是真军师推理**。请检查 API Key 与余额后重试。\n\n"
            + fallback["reply"]
        )
        return fallback, True, "mock", "mock-fallback", error_meta
    except Exception as exc:  # noqa: BLE001
        error_meta = {
            "fallback_reason": "unexpected_error",
            "message": str(exc),
            "error_type": exc.__class__.__name__,
        }
        fallback = mock_output(raw_text, contradiction_hint)
        fallback["reply"] = (
            f"⚠️ 模型调用异常（{exc.__class__.__name__}）：{exc}\n"
            "以下为本地兜底，**不是真军师推理**。\n\n"
            + fallback["reply"]
        )
        return fallback, True, "mock", "mock-fallback", error_meta


def append_entry(topic_slug: str, record: dict[str, Any]) -> None:
    entries_path = TOPICS_DIR / topic_slug / "entries.jsonl"
    with entries_path.open("a", encoding="utf-8") as fp:
        fp.write(json.dumps(record, ensure_ascii=False) + "\n")


def update_living_position(topic_slug: str, content: str) -> str:
    living_path = TOPICS_DIR / topic_slug / "living_position.md"
    text = content.strip() if content else "待主人首次输入后生长。"
    living_path.write_text(text, encoding="utf-8")
    return text


def append_snapshot(topic_slug: str, snapshot_content: str) -> str:
    snapshot_path = TOPICS_DIR / topic_slug / "snapshots" / f"{today_compact()}.md"
    if snapshot_path.exists():
        existing = snapshot_path.read_text(encoding="utf-8").rstrip()
        merged = f"{existing}\n\n---\n\n{snapshot_content.strip()}\n"
    else:
        merged = f"# {today_compact()} 快照\n\n{snapshot_content.strip()}\n"
    snapshot_path.write_text(merged, encoding="utf-8")
    return snapshot_content.strip()


def load_recent_entries(topic_slug: str, limit: int = 20) -> list[dict[str, Any]]:
    entries_path = TOPICS_DIR / topic_slug / "entries.jsonl"
    if not entries_path.exists():
        return []
    lines = [line for line in entries_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    records: list[dict[str, Any]] = []
    for line in lines[-limit:]:
        records.append(json.loads(line))
    records.reverse()
    return records


def load_recent_snapshots(topic_slug: str, limit: int = 7) -> list[dict[str, Any]]:
    snapshots_dir = TOPICS_DIR / topic_slug / "snapshots"
    snapshot_files = sorted(snapshots_dir.glob("*.md"), reverse=True)
    results: list[dict[str, Any]] = []
    for path in snapshot_files[:limit]:
        content = path.read_text(encoding="utf-8")
        results.append(
            {
                "date": path.stem,
                "path": str(path.relative_to(DATA_DIR)),
                "preview": content[:280],
            }
        )
    return results


def entries_count(topic_slug: str) -> int:
    entries_path = TOPICS_DIR / topic_slug / "entries.jsonl"
    if not entries_path.exists():
        return 0
    lines = entries_path.read_text(encoding="utf-8").splitlines()
    return len([line for line in lines if line.strip()])


@app.on_event("startup")
def startup() -> None:
    ensure_storage()


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "timestamp": utc_now(),
        "data_dir": str(DATA_DIR),
        "seed_topics": [seed[0] for seed in TOPIC_SEEDS],
        "api_key_configured": bool(os.getenv("KEEL_API_KEY", "").strip()),
        "deepseek_configured": bool(os.getenv("DEEPSEEK_API_KEY", "").strip()),
        "qwen_configured": bool(os.getenv("DASHSCOPE_API_KEY", "").strip()),
    }


@app.get("/healthz")
def healthz() -> dict[str, Any]:
    return health()


@app.post("/v1/entry", response_model=EntryResponse)
def post_entry(payload: EntryRequest, _: None = Depends(require_api_key)) -> EntryResponse:
    topic = ensure_topic(payload.topic_slug)
    topic_slug = topic["slug"]

    living_path = TOPICS_DIR / topic_slug / "living_position.md"
    living_before = living_path.read_text(encoding="utf-8")
    contradiction_hint = detect_contradiction_hint(payload.raw_text, living_before)

    provider, model, routed_deep = route_model(payload.raw_text, topic, payload.topic_mark, payload.depth)
    intensity = payload.advice_intensity if payload.advice_intensity is not None else 3
    system_prompt = compose_system_prompt(load_system_prompt_base(), contradiction_hint, intensity)
    user_prompt = compose_user_prompt(topic, payload.raw_text, living_before, contradiction_hint)
    model_payload, used_mock, model_provider_used, model_name_used, error_meta = call_model(
        provider,
        model,
        system_prompt,
        user_prompt,
        payload.raw_text,
        contradiction_hint,
    )

    reply = str(model_payload.get("reply", "")).strip()
    living_update = str(model_payload.get("living_position_update", "")).strip()
    daily_snapshot = str(model_payload.get("daily_snapshot", "")).strip()
    reason_for_shift = str(model_payload.get("reason_for_shift", "")).strip()
    tension_detected = bool(model_payload.get("tension_detected", contradiction_hint))

    if not reply:
        raise HTTPException(status_code=500, detail="模型返回为空")

    living_text = update_living_position(topic_slug, living_update)
    snapshot_snippet = append_snapshot(topic_slug, daily_snapshot or "（本次无快照内容）")

    now = utc_now()
    append_entry(
        topic_slug,
        {
            "timestamp": now,
            "topic_slug": topic_slug,
            "raw_text": payload.raw_text,
            "files": [item.model_dump() for item in payload.files] if payload.files else [],
            "reply": reply,
            "reason_for_shift": reason_for_shift,
            "contradiction_detected": tension_detected,
            "contradiction_hint": contradiction_hint,
            "provider": model_provider_used,
            "model": model_name_used,
            "provider_routed": provider,
            "model_routed": model,
            "advice_intensity": intensity,
            "metadata": {
                "model_used": f"{model_provider_used}:{model_name_used}",
                "routing_mode": "deep" if routed_deep else "default",
                **({"error": error_meta} if error_meta else {}),
            },
            "used_mock": used_mock,
        },
    )

    response_metadata: dict[str, Any] = {
        "model_used": f"{model_provider_used}:{model_name_used}",
        "model_routed": f"{provider}:{model}",
        "routing_mode": "deep" if routed_deep else "default",
        "contradiction_hint": contradiction_hint,
    }
    if error_meta:
        response_metadata["error"] = error_meta

    return EntryResponse(
        topic_slug=topic_slug,
        reply=reply,
        living_position_summary=living_text[:400],
        daily_snapshot_snippet=snapshot_snippet[:320],
        contradiction_detected=tension_detected,
        model_provider=model_provider_used,
        model_name=model_name_used,
        metadata=response_metadata,
        used_mock=used_mock,
        timestamp=now,
    )


@app.get("/v1/topic/{slug}", response_model=TopicResponse)
def get_topic(slug: str, _: None = Depends(require_api_key)) -> TopicResponse:
    topic_dir = TOPICS_DIR / slug
    if not topic_dir.exists():
        raise HTTPException(status_code=404, detail=f"topic 不存在: {slug}")

    topic_meta = json.loads((topic_dir / "topic.json").read_text(encoding="utf-8"))
    living = (topic_dir / "living_position.md").read_text(encoding="utf-8")

    return TopicResponse(
        topic_slug=slug,
        display_name=topic_meta.get("display_name", slug),
        living_position=living,
        snapshots=load_recent_snapshots(slug),
        entries=load_recent_entries(slug),
        entries_count=entries_count(slug),
    )
