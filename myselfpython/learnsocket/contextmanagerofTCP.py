from contextlib import contextmanager
import socket

@contextmanager

def my_recv(client_socket):
    data = client_socket.recv(4096)
    yield data
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 8080))
server_socket.listen(128)

client_socket, client_addr = server_socket.accept()

with my_recv(client_socket) as data:

    if data:
        print("收到数据", data.decode())
        client_socket.send(data)

    else:
        print(data, '客户端的TCP连接已经断开')