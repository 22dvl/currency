import socket
socket1 = socket.socket()
socket1.bind(('', 9022))
socket1.listen(1)
connect1, address = socket1.accept()
print('connection success: ', address)
while True:
    data = connect1.recv(1024)
    if not data:
        continue
    connect1.send(data.upper())
connect1.close()