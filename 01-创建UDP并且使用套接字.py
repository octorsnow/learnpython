import socket   # 导入模块


# 1 创建ＵＤＰ套接字　参数１表示地址协议－IPv4 IPv6　　参数２表示套接字类型 ---> 返回值就是套接字对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind函数就可以让程序使用固定端口
# 参数是一个 本地地址元组(IP,端口) IP如果为空表示绑定本地所有的IP地址
# 告诉操作系统不要给我分配随机端口 我要使用固定的
udp_socket.bind(('', 8888))

# 2 使用套接字进行数据的收发
# 发送数据使用ｓｅｎｄto方法　参数１表示需要发的数据<bytes类型>
# 参数２　收件人地址元组　(IP 字符串，端口port　整数)－－套接字地址
data = input("请输入你想要对服务器说的话:")
udp_socket.sendto(data.encode(), ('192.168.115.81', 8080))

# 3 接收数据　recvfrom　会阻塞等待对方发送数据----参数表示本次接收数据的最大长度
# 返回值就是接收数据的相关信息  (b'hehehe', ('192.168.115.81', 8080))
# 是一个元组　　(ｂｙｔｅｓ类型的数据，　发件人的地址信息元组)
recv_data, remote_address = udp_socket.recvfrom(4096)



print("接收到来自%s 的数据：%s" % (str(remote_address), recv_data.decode()))
# 4　关闭套接字
udp_socket.close()