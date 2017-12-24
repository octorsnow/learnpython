#nnnnnnnnnnn
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = input('IP')
add = (IP, 2425)
msg = input("请输入内容：")

a = "1:525:wow:None:32"

a = a + msg
s.sendto(a.encode("gbk"), add)

s.close()