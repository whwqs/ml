import types

class People(object):
    TypeName = "灵长类"
    def __init__(self, *args, **kwargs):
        self.姓名 = args[0]
        self.性别 = ""
        self.生日 = ""
        if len(args)>1:
            self.生日 = args[1]

    def 报名(self):
        print(self.姓名)
        return self

    def 报生日(self):
        print(self.生日)
        return self

class Man(People):
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.性别 = "男"

Man("张三").报名().报生日()
Man("李四","1990-01-01").报名().报生日()
类名 = "Man"
方法名 = "报名"
dic = globals()
print(type(dic))
print(dic)
Man2 = dic[类名]
print(Man==Man2)
print(type(Man.__dict__))
Man的方法名称数组1 = [key for key,v in Man2.__dict__.items() if type(v)==types.FunctionType]
print(Man的方法名称数组1)

#反射
man1 = dic[类名]("我是谁")#实例
method1 = getattr(man1,方法名)#实例方法
method1()#方法调用
method2 = getattr(Man,方法名)#类方法
method2(man1)

