import socket

HOST = '192.168.1.7'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((s.gethostbyname(), PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))