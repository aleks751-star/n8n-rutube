# app/main.py
import os
import time
import datetime

APP_INTERVAL = int(os.getenv("APP_INTERVAL", "7"))
WORKER_ENABLED = os.getenv("WORKER_ENABLED", "0") == "1"

def _run_worker_once():
    if not WORKER_ENABLED:
        return
    try:
        from app.worker import run_once
        run_once({})
    except Exception as e:
        # Не валим сервис из-за воркера: просто лог
        print(f"WORKER: error: {e}")

def main():
    print("APP: started")
    while True:
        print("APP: heartbeat", datetime.datetime.now().isoformat())
        _run_worker_once()
        time.sleep(APP_INTERVAL)

if __name__ == "__main__":
    main()
