# app/worker.py
def run_once(context=None):
    # специально через print, чтобы гарантированно оказаться в логе systemd
    print("WORKER: stub run_once executed")
