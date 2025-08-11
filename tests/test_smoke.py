import importlib

def test_app_imports():
    m = importlib.import_module("app.main")
    assert hasattr(m, "main")

