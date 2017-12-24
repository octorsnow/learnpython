# 创建套接字
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定固定端口
udp_socket.bind(('', 10086))
#实现udp的服务端，实现循环的收发消息
while True:
    data, ip_port = udp_socket.recvfrom(2048)
    print("接收到来自%s 的消息：%s" % (str(ip_port), data.decode("gbk")))
    msg = input("请输入要回复的消息：")
    udp_socket.sendto(msg.encode('gbk'), ip_port)
    udp_socket.close()
# 打印接收到的消息
# 回复消息，回复的消息来自自己的输入
