class Animal(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("-----a-----")


dog = Animal("Tom")

print("---1---")
dog1 = dog
print("----1----")
del dog
del dog1
print("---2---")
#虽然没有调用__del__方法，那是谁调用的？
#Python解释器 如果检测到一个对象没有任何用处了 那么就会把这个对象kill掉