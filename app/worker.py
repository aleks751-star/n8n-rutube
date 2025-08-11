# app/worker.py
from typing import Optional

def run_once(context: Optional[dict] = None) -> None:
    """Один такт работы воркера (пока заглушка)."""
    print("WORKER: stub run_once executed")
