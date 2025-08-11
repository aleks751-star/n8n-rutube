# CODEx Contract — n8n-rutube

## Цель
Кодекс (агент) сам пишет код, прогоняет тесты, деплоит на сервер и проверяет, что сервис жив.

## Важное
- Язык: Python 3.11
- Вирт. окружение: сервер создаёт/обновляет сам (pip install -r requirements.txt)
- Сервис: systemd unit `n8n-rutube.service`
- Порт/health: `GET http://127.0.0.1:8099/healthz` → `{"ok":true}`
- Логи: `journalctl -u n8n-rutube -n 60 --no-pager | grep -E "APP: heartbeat|WORKER:"`
- Интервал цикла: переменная `APP_INTERVAL` (сек), дефолт 7
- Воркёр: включение флагом `WORKER_ENABLED=1`, точка входа `app/worker.py:run_once(context)`

## Структура репозитория
- `.github/workflows/ci.yml` — CI GitHub Actions (checkout → python 3.11 → pip → smoke/pytest).
- `.ops/deploy.sh` — репо-хук: тянет `main`, устанавливает зависимости, рестартует сервис.
- `app/main.py` — цикл приложения: печатает `APP: heartbeat`, условно вызывает `app.worker.run_once()`.
- `app/worker.py` — **сюда добавлять рабочую логику** (сейчас заглушка `run_once()`).
- `tests/` — pytest-тесты (минимум smoke: импорт модулей). Добавляй тесты к изменениям.
- `requirements.txt` — зависимости.

## Как работает конвейер
1. Любой коммит в `main` → запускается CI (`.github/workflows/ci.yml`).
2. CI ставит зависимости и гоняет smoke/pytest.
3. Успешный push → GitHub Webhook дергает сервер → `/opt/ops_webhook_free/hooks/deploy.sh`.
4. Деплой-хук вызывает `.ops/deploy.sh` из репо, который:
   - `git fetch --all --quiet && git reset --hard origin/main`
   - `pip install -r requirements.txt`
   - `systemctl restart n8n-rutube`
5. Проверка: healthz + логи.

## Что можно менять
- Код в `app/` и `tests/`, зависимости в `requirements.txt`, CI шаги в `.github/workflows/ci.yml`.
- Логику воркера в `app/worker.py:run_once()` (держи её быстрой и устойчивой к временным ошибкам).

## Что нельзя ломать
- Файлы в `.ops/` и имя systemd-юнита `n8n-rutube.service`.
- Порт и эндпоинт `/healthz`.

## Локальные критерии «готово»
- CI зелёный.
- `curl -fsS http://127.0.0.1:8099/healthz` → `{"ok":true}`
- В логах каждые ~APP_INTERVAL сек две строки:
  - `APP: heartbeat ...`
  - `WORKER: ...` (когда WORKER_ENABLED=1)

## Подсказки
- Логи сервера быстро:  
  `journalctl -u n8n-rutube -n 60 --no-pager | grep -E "APP: heartbeat|WORKER:" || true`
- Безопасный рестарт + статус (на сервере уже установлено):  
  `n8n-restart` и `n8n-status`
- Если изменил зависимости — не забудь `requirements.txt` и тесты.

## Дальнейшее
Поддерживай этот файл актуальным: дополняй при добавлении фич, тестов, переменных окружения и т.д.
