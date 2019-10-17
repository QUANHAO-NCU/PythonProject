# 定义一个Animal 类
class Animal (object):
    def __init__(self,name,action):
        self.name = name
        self.action = action
    def getName(self):
        return self.name
    def getAction(self):
        return self.action
    def run(self):
        print ('hello, i`m '+self.name+' ,i can '+self.action)
        return 0
#     cat 类继承自Animal类，子类继承父类的所有属性和方法
class cat(Animal):
    pass
# miaomiao 为cat类的一个实例
miaomiao = cat('cat','catching mice')

miaomiao.run()
print (miaomiao.name)
print (miaomiao.action)

# 以上为继承

class dog(Animal):
    def run(self):
        print ('Attention! this is  Dog`s function.Hello, i`m ' + self.name + ' ,i can ' + self.action)
# dog类继承自Animal类，但是这里重了run()方法
# 子类重写父类的方法，会把父类的方法覆盖掉，在这个方法被调用时，会使用子类的方法，从而实现 多态：同一方法的不同实现

wangwang = dog('Dog','watch the door')

wangwang.run()


# 多态的高效应用
# 在写API时，我们不必指明参数的具体类，而可以用类的父类指定参数类型


# 定义函数，参数为Animal 类或其子类的实例
def runTwice(Animal):
    Animal.run()
    Animal.run()
# 运行中，我们传入了Animal的子类cat的一个实例miaomiao，它可以正确运行
runTwice(miaomiao)

class dogSon(dog):
    def run(self):
        print ('my name is '+self.name+' I am dog son')

# 子类的子类同样归属于父类的类型，尽管run函数的操作有所不同（多态），但是runtwice函数都能接受并成功运行

print ('子孙类的调用：')
dog_son = dogSon('dogson','son of dog')
runTwice(dog_son)