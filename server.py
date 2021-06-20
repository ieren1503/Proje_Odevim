import socket
import geocoder
import time 
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.38'
port = 2613


serversocket.bind((host, port))
serversocket.listen(5)
while True:
  try:
    g = geocoder.ip('me')
    string_1 = str(g.city)
    string_2 = str(datetime.datetime.now())
    (clientsocket, address) = serversocket.accept()
    data_total = string_1 + string_2
    clientsocket.send(data_total.encode())
  except:
    print("failed")
    time.sleep(1)
    break
