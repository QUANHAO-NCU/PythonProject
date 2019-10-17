# filter (Function,Iterable)
# filter 的作用类似与map类似。同样是将后面的Iterable数据依次传入Function，由Function作用于每个元素
# 与map不同的是，filter的Function在每次作用于一个元素后得到一个True或False的值，并以此决定元素的取舍
# 即 filter的Function会将元素进行取舍而不改变元素的值
# filter 返回的是一个Iterator，需要list或逐步调用才能得到完整的结果

# 例子： 利用埃氏筛法写一个可以计算一定范围内的素数

# 首先从3开始构造一个奇数列（偶数必然不是素数）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 设计一个排除函数，返回不能整除n的数（即可能的素数）
def _not_divisible(n):
    return lambda x: x % n > 0


# 设计另一个生成器，不断返回下一个素数
def primes():
    yield 2
    # 获取奇数列生成器
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # 返回生成器的第一个数，3，也是素数
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 练习：利用filter来筛选回数（12321,909）,可以设定范围

# 设置过滤函数
def filter_palindrome(start, stop):
    def is_palindrome(n):
        return n == int(str(n)[::-1])

    return filter(is_palindrome, range(start, stop))


print('1~1000:', list(filter_palindrome(1, 1000)))

# ps：纯过滤函数应为：
def is_palindrome(n):
    return n == int(str(n)[::-1])

# 参考回答中的最优方法