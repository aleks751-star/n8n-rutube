#!/usr/bin/env bash
set -Eeuo pipefail
echo "[repo] custom deploy hook running"

PY=python3
[ -x ./.venv/bin/python ] && PY=./.venv/bin/python

# Запускаем модуль (если модульный запуск не сработает — файл напрямую)
$PY -m app || $PY app/main.py
