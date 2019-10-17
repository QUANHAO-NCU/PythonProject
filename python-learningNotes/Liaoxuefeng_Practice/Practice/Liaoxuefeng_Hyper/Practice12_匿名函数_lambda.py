# 匿名函数，即不需要显式的定义一个函数，省去了定义函数的麻烦过程

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。

# 示例：设计一个求平方函数f(x) = x^2

def power2(x):
    return x * x


# 匿名函数形式：

f = lambda x: x * x
# 注意，匿名函数可以像正常的函数一样进行赋值

# 二者的使用形式和效果是相同的

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print ("由正常定义的函数power2作用的情况为：", list(map(power2, list_)))

print ("由匿名函数作用的情况为：", list(map(f, list_)))

print ("直接将lambda函数写成map里需要的Function：", list(map(lambda x: x * x, list_)))


# 练习：利用匿名函数改造一下代码

def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print ("原代码的结果为：", L)

L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print ("经lambda改造的filter如：\nL2 = list(filter(lambda x:  n%2==1,range(1,20)))。\n结果为：", L2)
