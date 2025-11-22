import socket
import threading
import time
from queue import Queue

target = input("Enter target IP: ")

q = Queue()
open_ports = []
lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"[OPEN] Port {port}")
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    Banner: {banner}")
            except:
                pass
        s.close()
    except:
        pass

def worker():
    while not q.empty():
        port = q.get()
        scan_port(port)
        q.task_done()

def detect_os():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        start = time.time()
        s.connect((target, 80))
        end = time.time()
        latency = (end - start) * 1000
        if latency < 3:
            print("Possible OS: Linux")
        elif latency < 10:
            print("Possible OS: Windows")
        else:
            print("OS detection uncertain")
    except:
        print("Could not detect OS")

def main():
    for port in range(1, 1025):
        q.put(port)
    for _ in range(100):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
    q.join()
    print("\nScan complete")
    print("Open ports:", open_ports)
    detect_os()

if __name__ == "__main__":
    main()
