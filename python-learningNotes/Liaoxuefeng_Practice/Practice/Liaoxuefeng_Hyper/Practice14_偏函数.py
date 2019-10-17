# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# 示例：
# int()函数：int(x,base = 10)
# 前一部分是传入的字符串，后一部分设置转换的进制
# 则可以有如下调用方式
import functools

print(int('12345', base=10))
print(int('12345', base=8))


# 为了固定int(x,base = 10)中base参数的值为2
# 由以下两种形式
def int2_0(x):
    return int(x, base=2)


# 或者采取偏函数的形式
int2_1 = functools.partial(int, base=2)

print("二者的作用是等效的\n", int2_0('10010011'), "\n偏函数的形式是：\n", int2_1('10010011'))
