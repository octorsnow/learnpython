"""
1.	什么是网络？ 使用网络的目的是什么？
一种沟通共享的工具（网络是一种辅助双方或者多方能够连接在一起的工具） 
信息的传递和数据的共享.
2.	IP地址的作用？
标记网络中的一台主机的
3.	IP地址有什么组成？ 
网络号和主机号
4.	IP地址分类有哪些？（了解）
A B C D E F类  私有IP
5.	127.0.0.1这个IP的作用是什么？
代表本机系统的IP地址  用于回路测试
6.	在linux下怎么查看网卡的信息
ifconfig
7.	Ping命令的作用是什么？
检测网络是否通畅 
8.	什么是端口？ 端口的作用是什么？
port设备与外界通讯交流的出口 
用来标识主机中的一个应用程序
9.	在Linux系统中端口有多少个？
65536  2的16次方
10.	端口号的分类？范围是什么？
知名端口 动态端口  分别是0-1023    1024-65535
11.	IP地址和端口号的作用分别是什么？
IP地址标识网络上的一个主机，端口号标识是这台电脑上的一个应用程序（进程）
12.	什么是进程？（先了解，后续还会讲），进程见通信指的是什么？
正在运行的程序以及运行时用到的资源 ，这个整体称为进程。  
运行的程序间的实现数据共享和传递
13.	什么是socket？
套接字
14.	使用socket通信的前提是什么？
需要有一对套接字 网络通信的一端为一个套接字
15.	socket的本质是什么？
对底层网络协议TCP/IP的封装并且提供了一套应用程序接口（API）
16.	怎么去创建一个udp的socket？(说明函数中的两个参数分别代表的是什么)
import socket  协议地址 套接字类型
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.close()
17.	怎么实现str类型的编码与bytes类型进行互转
str.encode()
bytes.decode()

18.	socket怎么接受数据？参数代表是什么？接受到的数据是什么格式的？
Socket.recvfrom(字节数)  
参数代表的是本次接收的最大字节数，一般是1024的整倍数。
接收到的数据是元组形式（数据， （发送方的IP，端口号））
19.	怎么去绑定一个端口？
Socket.bind(‘’,port)函数         
 注意：参数数元组形式的，ip一般不用写，表示本机的任何一个ip
"""
# 20.	编写一个程序，实现udp的客户端
# 发送的消息来自用户的输入
# 发送的ip和端口号来自用户的输入。
# #创建socket
# #获取要发送的内容和发送的IP以及端口号
# #关闭socket

# import socket
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send_ip = input("请输入要发送的ip：")
# send_port = int(input("请输入端口号："))
# send_msg = input("请输入内容：")
# udp_socket.sendto(send_msg.encode(), (send_ip, send_port))
# udp_socket.close()

# 21.	编写一个程序，实现udp的服务端，实现收发消息。
# 绑定固定的端口--> 10086
# 打印接收到的消息，格式： 接收到来自xx的消息：XXX
# 回复消息，回复的消息来自自己的输入。
# 改良程序：实现循环的接收、发送消息。
# #创建socket对象
# #绑定固定端口
# #接收消息
# #关闭socket
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(('', 10087))
while True:
    data, ip_port = udp_socket.recvfrom(1024)
    print(ip_port)
    print("接收到来自%s的消息:%s" % (str(ip_port), data.decode()))
    msg = input("请输入要回复的消息：")
    udp_socket.sendto(msg.encode(), ip_port)

udp_socket.close()