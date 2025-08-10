from datetime import datetime
import socket

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[app] started at {now} on {socket.gethostname()}")

if __name__ == "__main__":
    main()
