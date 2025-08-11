# app/main.py
import os
import time
import datetime
import logging

# Настройки из окружения
INTERVAL = int(os.environ.get("APP_INTERVAL", "7"))
WORKER_ENABLED = os.environ.get("WORKER_ENABLED", "0").lower() in ("1", "true", "yes")

# Пишем в stdout (systemd подхватит)
logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("APP")

def _load_worker():
    if not WORKER_ENABLED:
        return None
    try:
        from .worker import run_once
        log.info("APP: worker enabled")
        return run_once
    except Exception as e:
        log.exception("APP: failed to import worker: %s", e)
        return None

def main():
    run_worker_once = _load_worker()
    log.info("APP: started")
    while True:
        log.info("APP: heartbeat %s", datetime.datetime.now().isoformat())
        if run_worker_once is not None:
            try:
                run_worker_once({})
            except Exception as e:
                log.exception("WORKER: error: %s", e)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
