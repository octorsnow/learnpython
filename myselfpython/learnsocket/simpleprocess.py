#1.	编写一个程序，实现创建一个子进程，子进程每一秒打印一次：
# 这是子进程，循环的第n次，打印 的次数是由主进程传递给子进程。


import multiprocessing
import time


def process1(num):
    for i in range(num):
        time.sleep(1)
        print("这是子进程,循环的第%d次" % (i + 1))


def main():
    num = int(input("请输入要循环的次数："))
    process = multiprocessing.Process(target=process1, args=(num,))
    process.start()

if __name__ == '__main__':
    main()