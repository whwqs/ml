#特别注意 __getattribute__ 用法
import types
class People(object):
    TypeName = "灵长类"
    def __init__(self, *args, **kwargs):  
        print("3 : 调用'__init__'不走__getattribute__")#构造函数的调用不走__getattribute__
        self.性别 = ""
        self.姓名 = ""
        self.生日 = ""
        if len(args)>0:
            self.姓名 = args[0]
        if len(args)>1:
            self.生日 = args[1]        

    def 报名(self):
        print("3 : 真正调用'报名'")#真正的方法这个是第三个调用
        print(self.姓名)
        return self

    def 报生日(self):
        print(self.生日)
        return self

    def __getattribute__(self, name):
        print("2：找属性："+name)#父类的这个是第二个调用
        return super().__getattribute__(name)#千万不能忘记 return
    

class Man(People):
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.性别 = "男"

    def __getattribute__(self, name):
        print("1：找属性："+name)#这个是第一个调用
        attr = super().__getattribute__(name)
        print(type(attr))
        return attr #千万不能忘记 return

Man("张三").报名()

print("用__getattribute__实现代理")
#代理的目的通常是为了AOP
class c1:
    def 打印工作(self,text):
        print(text)

class c1proxy:
    def __init__(self, *args, **kwargs):        
        self.obj = args[0]#c1的实例

    def __getattribute__(self, name):
        #method = getattr(self.obj,name)#不能这样取得属性，会导致无出口的递归：RecursionError: maximum recursion depth exceeded
        target = object.__getattribute__(self,"obj")
        method = object.__getattribute__(target,name)        
        if type(method) != types.MethodType:
            raise NotImplementedError
        def 闭包函数(*args,**kwargs):
            print("调用'"+name+"'开始：")
            method(*args,**kwargs)
            print("调用结束")
        return 闭包函数

c1proxy(c1()).打印工作("hello world")

print("设计模式：代理模式")

class parent:    
    def 打印工作(self,text):#抽象方法
        raise NotImplementedError

class son(parent):
    def 打印工作(self,text):
        print(text)

class sonproxy(parent):
    def __init__(self, obj):
        self.obj = obj

    def 打印工作(self,text):
        print("开始：")
        self.obj.打印工作(text)
        print("结束")

sonproxy(son()).打印工作("hello")