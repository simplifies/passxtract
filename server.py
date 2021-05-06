import socket
s = socket.socket()
#######################REPLACE PORT WITH PORT YOU ARE FORWARDING
port = 55555
#######################REPLACE PORT WITH PORT YOU ARE FORWARDING
s.bind(('', port))
s.listen(5)
print("Waiting For Connections...")
c, addr = s.accept()
print("connection from",addr)
while True:
    rcvdData = c.recv(1024).decode()
    print(rcvdData)
c.close()