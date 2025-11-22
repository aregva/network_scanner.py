# Network Scanner

This is a simple Python program that scans a target IP address for open ports.  
It checks ports from 1 to 1024 and shows which ones are open.  
The program also tries to read a small banner from the open ports.

This project is good for learning basic network programming in Python.

---

## Features

- Scans ports 1–1024  
- Shows open ports  
- Reads service banner (if available)  
- Single Python file  
- Easy to run and understand  

---

## How to Run

1. Make sure you have Python 3 installed.
2. Save the file as:
3. Run the program:

```bash
python3 advanced_network_scanner.py
[OPEN] Port 80
[OPEN] Port 22
Scan complete
Open ports: [80, 22]
Possible OS: Linux

