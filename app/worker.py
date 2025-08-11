# app/worker.py
import os
import logging
from typing import Optional

import requests

HEALTH_URL = os.getenv("HEALTH_URL", "http://127.0.0.1:8099/healthz")
REQ_TIMEOUT = float(os.getenv("WORKER_TIMEOUT", "3"))

log = logging.getLogger("APP")

def run_once(context: Optional[dict] = None) -> None:
    """
    Одна итерация воркера: проверка healthz.
    Никаких исключений наружу — сервис не валим.
    """
    try:
        r = requests.get(HEALTH_URL, timeout=REQ_TIMEOUT)
        ok = r.status_code == 200 and '"ok":true' in r.text
        log.info("WORKER: health %s -> %s", r.status_code, "OK" if ok else "FAIL")
    except Exception as e:
        log.warning("WORKER: error %s", e)
