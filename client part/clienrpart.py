import socket
socket1 = socket.socket()
socket1.connect(('localhost', 9022))
a = input()
socket1.send(a.encode())
data = socket1.recv(1024)
socket1.close()
print (str(data))