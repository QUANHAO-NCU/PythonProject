# 返回函数

# 1.将函数作为返回值返回

# 示例：函数lazy_sum 将返回一个求和的函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)

print("f = lazy_sum(1,3,5,7,9)\n,现在的f是：", f)

print("现在再次调用函数f", f())


# **返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 利用函数里面的函数绑定一个循环变量使之不受外部函数的调用影响

def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print("f1 是：", f1(), "\nf2 是：", f2(), "\nf3是：", f3())


# 练习：用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    def generator_plus():
        n = 0
        while True:
            n = n+1
            yield n

    a = generator_plus()

    def counter():
        return next(a)

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
