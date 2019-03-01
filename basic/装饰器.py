from datetime import *


def 通用装饰(被装饰函数):
    def 闭包函数(*args, **kwargs):
        print("begin at "+str(time()))
        print()
        被装饰函数(*args, **kwargs)
        print()
        print("end at "+str(time()))
    return 闭包函数


class c1(object):
    def __init__(self):
        self.name = "my name is c1obj"

    @通用装饰
    def 报名(self):
        print(self.name)


@通用装饰
def f1(name):
    print(name)


f1("全局函数")

c1().报名()

