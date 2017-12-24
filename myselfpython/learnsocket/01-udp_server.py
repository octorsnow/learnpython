import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = input("请输入要发送的IP地址：")
port = int(input("请输入端口号："))
msg = input("请输入要发送的内容：")
udp_socket.sendto(msg.encode(), (IP, port))

udp_socket.close()