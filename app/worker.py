# app/worker.py
import logging
from typing import Optional

def run_once(context: Optional[dict] = None) -> None:
    """
    Один такт работы воркера (заглушка).
    Реальную логику добавим позже.
    """
    logging.getLogger("APP").info("WORKER: stub run_once executed")
