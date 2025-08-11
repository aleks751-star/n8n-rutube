# app/main.py
import time, datetime
print("APP: started")
while True:
    print("APP: heartbeat", datetime.datetime.now().isoformat())
    time.sleep(30)
