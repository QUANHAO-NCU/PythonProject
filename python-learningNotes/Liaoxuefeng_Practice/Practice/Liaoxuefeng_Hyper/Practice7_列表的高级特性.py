# ----------------切片-------------------#
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#     0          1        2        3      4
#     -5         -4       -3      -2       -1
# 切片可以快速方便的取出列表中的某一部分元素
l1 = L[0:2]
l2 = L[-3:-1]
# 可以设置取样的步长
l3 = L[::2]


# 通式list[起点：终点：步长]
# ---------练习---------#
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
# 字符串本身就是一个列表
def trim(s):
    while len(s) > 1 and s[0] == ' ':
        s = s[1:]
    while s and s[-1] == ' ':
        s = s[0:-1]
    return s


print(trim('   hello  world  '))
print(type(trim('             ')))

# 迭代：迭代是一种抽象思想，在python中，可迭代对象都可以进行迭代操作，简单的说，就可以for i in iterable：
# 字符串，列表，元组等，python中可迭代对象很多
# 判断方法 isinstance(object,iterable)
from collections import Iterable

l = [231, 534, 76, 435, 578, 5, 6, 8, 43, 2, 66, 64, 65]


def list_min_max(list):
    if isinstance(l, Iterable):
        max_num = 0
        min_num = l[0]
        for i in l:
            if i > max_num:
                max_num = i
            if i < min_num:
                min_num = i
    return min_num, max_num


print(list_min_max(l))

# 列表生成式/列表解析
# list = [表达式/循环/过滤函数]
# list = [ 变量 变量的表达式/循环/过滤函数]
list1 = [x for x in range(1, 24, 2) if x % 3 == 0]

list2 = [m + n for m in 'ABC' for n in 'XYZ']

# 练习
# 把列表中的字符串元素首字母小写 其他类型元素不做处理
L2 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L2 if isinstance(x, str)]
print(L2)


# 生成器-generator

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 实际上yield类似于一个指令标记每次到yield时就用这里的指令地址覆写函数的指令地址。

# 练习：用生成器输出杨辉三角
def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[x] + p[x + 1] for x in range(len(p) - 1)] + [1]


n = 10
for t in triangles():
    print(t)
    n -= 1
    if n == 0:
        break
# 这个代码非原创，转自回复中 @学习了 的代码
# 结合了生成器yield ，列表生成式等方法，简洁高效
quit(0)
