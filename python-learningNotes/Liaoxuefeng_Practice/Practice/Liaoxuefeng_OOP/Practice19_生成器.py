import math

'''
    生成器集合
'''
# 01 自定义的生成器 用yield实现
'''
yield语句作为一个循环暂停点，yield 可以返回一个值，也可以什么都不做

'''


# 此函数可以生产一个斐波那契数列

def fib_yield():
    a, b = 0, 1
    while 1:
        a, b = b, a + b
        yield a  # a = f(n) = f(n-1) + f(n-2)


def test_fib_yield(fib_yield):
    a = []
    for i in fib_yield:
        if i < 1000:
            a.append(i)
        else:
            break
    if a == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]:
        print('生成器生成了正确的序列！')


def primes_yield(m, n):
    def is_prime(n):
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    for i in range(m, n + 1):
        if is_prime(i):
            yield i


def test_primes_yield():
    a = []
    p = primes_yield(5000000000, 5000000090)
    for i in p:
        a.append(i)
    if a == [5000000029, 5000000039, 5000000059, 5000000063]:
        print('素数序列生成器产生了正确的序列！')


# 02 反向迭代器
'''
反向迭代器 reverse 是一个内置函数
如果一个可迭代对象实现了__reversed_()方法，则可以使用reversed()函数获得其反向可迭代对象
'''


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 生成一个递减序列
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
def test_reversed():
    a = []
    b= []
    c=[]
    for i in Countdown(10):
        a.append(i)
    for i in reversed(Countdown(10)):
        b.append(i)
    for i in range(len(a)):
        if a[i]==b[-(i+1)]:
            c.append(1)
        else:
            c.append(0)
    if 0 in c:
        print('测试失败')
    else:
        print('测试成功！')