# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线_
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
class Student(object):
    def __init__(self,name, score):
        self.__name = name
        self.__score = score
    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score
    def set_name(self,in_name):
        self.__name = in_name
    def set_score(self,in_score):
        self.__score = in_score

jason  = Student('jason',77)
try:
    print(jason.name)
except:
    print('出现这句提示时表明已经不能直接访问jason.name属性')

print('真正访问jason.name的方法是调用内部方法jason.getName()：')
print(jason.getName())

# 设置访问限制的作用有：
# 防止对象的属性被错误修改
# 在定义内置方法时可以检查参数的有效性，减少非法调用的风险


# 设置私有变量的本质
print('参见两种访问私有变量的方法：\njason.getName() = '+jason.getName()+'\njason._Student__name:'+jason._Student__name)

# 设置好私有变量后，Python编译器自动将私有变量设置为   '_className__Attributes'
# 如果你直接设置 instance.__newAttributes 并不能正确的设置为对应的实例的私有属性
