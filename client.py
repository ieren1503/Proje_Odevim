"""
#!/usr/bin/env python3

import socket
import sys
from struct import unpack

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '192.168.0.8', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

while True:
    # Wait for message
    message, address = sock.recvfrom(4096)

    print(f'Received {len(message)} bytes:')
    x, y, z = unpack('3f', message)
    print(f'X: {x}, Y: {y}, Z: {z}')
    
"""

#client code
import socket
import time

clientsocket = socket.socket()
host = '192.168.1.38'
port = 2613
clientsocket.connect((host,port))
i = 0
while True:
    try:
        start_time = time()
        clientsocket.recv(1024)
        # clientsocket.connect((host,port))
        print(clientsocket.recv(1024))
        # print(clientsocket.recv(1024) - int(round(time.time() * 1000)))
        # print("normal time = " ,int(round(time.time() * 1000)))
        print("Trial {}, delay: {} seconds ".format(i,time() - start_time))
        print("***************\n")
        # clientsocket.recv(1024)
        # clientsocket.close()
        # time.sleep(0.5)
        # i = i+ 1
    except:
        print("failed")
        time.sleep(1)
        break


clientsocket.close()