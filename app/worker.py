import logging
from typing import Optional

def run_once(context: Optional[dict] = None) -> None:
    """
    Одна итерация работы воркера (заглушка).
    Реальную логику подставим, когда дашь задачу воркеру.
    """
    logging.getLogger("APP").info("WORKER: stub run_once executed")
