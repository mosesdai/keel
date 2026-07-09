#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${ROOT_DIR}/data/topics"
TARGET_DIR="${1:-$HOME/Library/Mobile Documents/com~apple~CloudDocs/Keel/topics}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "源目录不存在：${SOURCE_DIR}"
  exit 1
fi

mkdir -p "${TARGET_DIR}"

echo "同步中..."
echo "FROM: ${SOURCE_DIR}"
echo "TO  : ${TARGET_DIR}"

rsync -av --delete "${SOURCE_DIR}/" "${TARGET_DIR}/"

echo "完成：已同步到 iCloud Keel/topics。"
