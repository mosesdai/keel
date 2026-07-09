#!/usr/bin/env bash
set -euo pipefail

TOPIC_SLUG="${1:-tencent-ali-renewal}"
ICLOUD_TOPICS_DIR="${2:-$HOME/Library/Mobile Documents/com~apple~CloudDocs/Keel/topics}"
TODAY="$(date +%Y%m%d)"
TARGET_FILE="${ICLOUD_TOPICS_DIR}/${TOPIC_SLUG}/${TODAY}.md"

if [[ -f "${TARGET_FILE}" ]]; then
  echo "Opening: ${TARGET_FILE}"
  open "${TARGET_FILE}"
else
  echo "未找到今日文件：${TARGET_FILE}"
  echo "请先在 iPhone 快捷指令里执行一次「主见」。"
  exit 1
fi
