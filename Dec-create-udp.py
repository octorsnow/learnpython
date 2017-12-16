#创建套接字
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('', 8888))
#使用套接字进行数据收发
data = input("请输入你想对服务器说的话：")
udp_socket.sendto(data.encode(), ('192.168.115.81', 8080))
recv_data, remo_address = udp_socket.recvfrom(4096)

print("接收到来自%s 的数据" % (str(remo_address), recv_data.decode()))
#关闭套接字
udp_socket.close()