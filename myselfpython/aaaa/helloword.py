# coding = utf-8
def my_func(a, b, func):
    result = func(a, b)
    print(result)

new_func = input("请输入一个匿名函数：")
new_func = eval(new_func)
my_func(100, 200, new_func)