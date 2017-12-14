import socket


# echo服务器　将收到的所有的客户端数据　原封不动回传客户端
# 1 创建套接字　                       data gram   数据报
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2 绑定端口
udp_socket.bind(('', 8888))

while True:
    # 3 使用套接字接收客户端的请求数据
    recv_data ,remote_address = udp_socket.recvfrom(4096)
    print("接收到来自%s 的数据：%s" % (str(remote_address), recv_data.decode()))

    # 4 回传数据
    udp_socket.sendto(recv_data, remote_address)

# 5 关闭套接字
udp_socket.close()
