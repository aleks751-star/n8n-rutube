#!/usr/bin/env bash
set -Eeuo pipefail

echo "[repo] custom deploy hook running"
date

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$APP_DIR/.venv/bin/python"
[[ -x "$PY" ]] || PY="$(command -v python3)"

# Лёгкая пост-проверка, что код загружается
"$PY" - <<'PY'
import importlib
import app
print("post-deploy: import app OK")
PY

echo "[repo] done."
