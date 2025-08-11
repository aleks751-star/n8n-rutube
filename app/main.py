# app/main.py
import time, datetime

def main():
    print("APP: started")
    while True:
        print("APP: heartbeat", datetime.datetime.now().isoformat())
        time.sleep(7)
