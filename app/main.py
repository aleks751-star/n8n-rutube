# app/main.py
import os
import time
import datetime
import logging

def _as_bool(name: str, default: bool = False) -> bool:
    v = os.environ.get(name)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "on")

def main():
    logging.basicConfig(level=logging.INFO)
    print("APP: started")

    # Интервал тиков (сек). По умолчанию 7 — как мы уже обкатывали.
    interval = int(os.environ.get("APP_INTERVAL", "7"))

    # Воркер выключен по умолчанию. Включается WORKER_ENABLED=1
    worker_enabled = _as_bool("WORKER_ENABLED", False)
    run_once = None

    if worker_enabled:
        try:
            from app.worker import run_once as _run_once
            run_once = _run_once
            print("WORKER: enabled")
        except Exception as e:
            print(f"WORKER: failed to import: {e}")
            worker_enabled = False

    while True:
        print("APP: heartbeat", datetime.datetime.now().isoformat())
        if worker_enabled and run_once:
            try:
                run_once({})
            except Exception as e:
                logging.getLogger("APP").warning("WORKER error: %s", e)
        time.sleep(interval)

if __name__ == "__main__":
    main()
