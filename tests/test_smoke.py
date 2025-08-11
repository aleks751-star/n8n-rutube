import importlib

def test_app_imports():
    m = importlib.import_module("app.main")
    assert hasattr(m, "main"), "app.main must expose main()"

def test_worker_stub_imports():
    m = importlib.import_module("app.worker")
    assert hasattr(m, "run_once"), "app.worker must expose run_once()"

