# 练习1 定义一个函数，要求传入两个参数，求从参数a（头）到参数b（尾）的自然数列和
import sys
import math


def sum_a_b(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    sum += b  # 注意range生成的数列最大值是b-1，所以要加上b
    return sum


print(sum_a_b(1, 100))

# 知识点 def 函数名 （参数列表）：
# 执行语句
# return返回对象（这个对象可以是各种内容：值，字符串，列表，字典，函数等等）

# 练习2 定义一个函数，给定一个圆的半径，计算圆的面积，并按照“半径为r的圆的面积是s”的格式输出，保留两位小数
r = int(input('请输入圆的半径r：'))


def round(r):
    s = math.pi * (r ** 2)  # math.pi获取圆周率的数值
    return s


print('半径为{:.1f}的圆的面积是{:.2f}'.format(r, round(r)))

#   练习3 python内置函数的使用
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
dec = int(input('请输入一个十进制整数'))
print(str(hex(dec)))


# python内置函数有很多，每个库（模块）也有自己定义的内置函数，不必要去拿不死记硬背，学会查看函数的文档然后正确使用之才是关键


# 练习4
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程
# ax ^ 2 + bx + c = 0 的两个解。
#
# 提示：
#
# 用一元二次方程的求根公式求解
# 计算平方根可以调用math.sqrt()函数：
def quadratic(a, b, c):
    # 检查是否有解
    deta = b ** 2 - 4 * a * c
    if deta < 0:
        return '无实数解'
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
# 知识点：
# python中常常有人这么写
x1, x2 = quadratic(2, 3, 1)
print('x1', x1, 'x2', x2)


# 实际上，x1，x2不是两个独立的变量，他们是省略了括号的元组
# 同理，函数返回值中看起来是返回了多个值，实质上是返回了一个元组

# -----------------------知识点：函数的参数-----------------------#

# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# -----------------------知识点：函数的参数-----------------------#
def fun1(x, y):
    return x + y


# 常规参数设置，x，y都是必选参数，函数调用时都需要传入
print('fun1(2,3) is ', fun1(2, 3))


# 调用实例
def fun2(x, y, string='the sum is'):
    return string + ' ' + str(x + y)


# ---------------------默认参数---------------------
# 默认参数已赋值，调用时不需要给默认参数进行赋值，但是，特别的，在需要的时候也可以给默认参数重新赋值
print('fun2(2,3) is ', fun2(2, 3))
print('这次调用将改变默认参数 fun2(2,3,\'hello\') is ', fun2(2, 3, 'hello'))


# 调用实例
# ---------------------可变参数---------------------
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
def fun3(*nums):
    sum = 0
    for i in nums:
        sum += i * i
    return sum


# 调用实例
print('fun3(1,2,3,4) is ', fun3(1, 2, 3, 4))
# 另外的，把一个列表/元组的所有元素当成可变参数传入可以采用这种方法
list2 = [1, 2, 3, 4]
print('fun3(*list2) is ', fun3(*list2))
# 结果是一样的

#---------------------关键字参数---------------------
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def fun4 (name,city,**kwargs):
    print('hello,my name is ',name,'I am from ',city,end='')
    if kwargs !=None:
        for i in kwargs:
            print(i,kwargs[i])

fun4('michal','Beijing',job = 'Programer')

#也可以使用字典进行批量传参，用法类似于可变参数
dit = {'job':'Programer','Universe':'NCU'}
fun4('michal','Beijing',**dit)
#---------------------命名关键字参数---------------------
#实质就是对关键字参数进行限制，限制其传入的关键字参数的名字
#命名关键字参数必须传入参数名，这和位置参数不同。
def fun5 (name,city,*,job, Universe):
    print('hello,my name is ',name,'I am from ',city,job,Universe)
fun5('michal','NanChang',job='Programer',Universe='NCU')

# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y
def product(x,*args):
    sum = 1
    sum = sum *x
    if args :
        for i in args:
            sum =sum *i
    return sum

print(product(1,2,3,4,5,6,7,8,9,10))
quit(0)
