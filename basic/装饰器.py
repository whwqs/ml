def 通用装饰(被装饰函数):
    def 闭包函数(*args,**dicargs):
        print("begin")
        被装饰函数(*args,**dicargs)
        print("end")
    return 闭包函数

class c1(object):
    def __init__(self):
        self.x = 9
    
    def func1(self,name):
        print(name)



@通用装饰 
def f1(arr,a=900):
    print(arr[1])
    print(a)

f1("345",a=390)

def x1(*args,**dicargs):
    print(args[0],dicargs["x"])

x1("100",x=345)