
#!/usr/bin/env python3

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
        print(clientsocket.recv(1024))
        print("Trial {}, delay: {} seconds ".format(i,time() - start_time))
        print("***************\n")
        time.sleep(0.5)
        i = i+ 1
    except:
        print("failed")
        time.sleep(1)
        break


clientsocket.close()
