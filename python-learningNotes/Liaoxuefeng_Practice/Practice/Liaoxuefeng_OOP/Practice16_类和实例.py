# 面向对象最重要的概念就是类（Class）和实例（Instance）
# 必须牢记类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 标准的class应这样定义
class Class_name(object):
    pass


# class 后面加类名，类名的首字母一般大写，(object)里面的object表示这个类所继承的类。如果确定了父类的名字就写父类的名字。
# 如果没有合适的继承类就写object，object是所有类最终都要继承的类
# 与C++不同，Python的类只有操作方法，没有成员对象(属性)
# --------------与C++不同，Python的类里面属性(即成员对象)应该全部绑定到类的初始方法__init__-----------------

# 示例

class Student(object):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_detail(self):
        print("Student name: %s\nStudent age: %d\nStudent grade:%d" % (self.name, self.age, self.grade))


class Student1(object):
    def Attributes(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_detail_1(self):
        print("Student name: %s\nStudent age: %d\nStudent grade:%d" % (self.name, self.age, self.grade))
    def print_name(self):
        print(self.name)
        return self.name
    def print_age(self):
        print(self.age)
        return self.age
    def print_grade(self):
        print(self.grade)
        return self.grade


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
# 但self不需要传，Python解释器自己会把实例变量传进去：
# 实例化类有两种方法
Tom = Student('Tom', 20, 97)
jason = Student('jason', 18, 77)

# 第二种赋值方法适用于没有init方法
jack_ma = Student1()
jack_ma.name = 'jack_ma'
jack_ma.age = 19
jack_ma.grade = 85

# 两个实例化的对象的赋值方式不同，但是可以使用相同的方法

Tom.print_detail()
jason.print_detail()
jack_ma.print_detail_1()

# 数据封装：在访问一个实例的属性/数据时，并不直接访问实例的属性/数据，而是直接调用实例里的对应的成员方法

jack_ma.print_age()
print(jack_ma.print_age())
# 二者的作用相同

# Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

jason.country = 'America'
simpson = Student('simpson',18,78)
simpson.University = '杭州师范'

# 二者同属于Student类的一个实例，