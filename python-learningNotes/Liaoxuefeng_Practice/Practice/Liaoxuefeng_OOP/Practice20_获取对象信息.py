"""
使用type()确定类的类型
"""


class myclass(object):
    pass


test = myclass()

print(type(test))  # type 查看test这个对象的类型是一个type类型？
print(type(123))

"""
使用isinstance()函数确定一个类的父子关系

isinstance (一个对象的实例, 一个由 具体的数据类型 组成的tuple )
    isinstance 所确定的不只是直接父子关系，对于祖父类和子孙类同样判定为True
isinstance 判断的是两个类之间，前一个类是否是后一个类派生的子类
"""


#
class Animal():
    age = 0

    def __init__(self):
        pass

    def action(self):
        print('this is an action!')


class dog(Animal):
    def action(self):
        print('I am a dog,I can hunt!')


class Husky(dog):
    def kind(self):
        print('I am a Husky!')


a = Animal()
d = dog()
h = Husky()
print(isinstance(h, Animal))
print(isinstance(h, dog))

"""
获取一个对象的所有属性和方法
dir()函数
dir()将返回一个包含字符串的列表，每一个字符串就是这个对象的所有属性和方法

对一个对象的属性和方法进行操作
getattr() :获取一个对象的属性,成功返回0,没有则直接触发 AttributeError 错误
setattr() :给对象设置一个新的属性
hasattr() :检查这个对象是否有某一个属性
"""
print(dir(h))
print(getattr(h,'age'))
print(getattr(h,'name'))
if not hasattr(h,'sex') :
    setattr(h,'sex','female')
    print(getattr(h,'sex'),end='')
quit(0)