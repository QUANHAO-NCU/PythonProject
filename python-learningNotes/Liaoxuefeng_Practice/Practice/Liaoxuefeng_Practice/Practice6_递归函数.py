# -----------递归函数—----------
# 自身调用自身
# 计算阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))


# 注意，递归函数一定要设置终止条件
# 尾递归优化
# 在递归调用时不应该再出现直接的表达式，而应该直接调用递归函数
def fact2(n, result=1):
    result = result * n
    if n == 1:
        return result
    return fact2(n - 1, result)


print(fact2(10))


# 练习 汉诺塔 问题描述见网络
# 思路 简化问题
# 第一步：其他盘子移动到第二根柱子上
# 第二步：最大的盘子移动到第三根柱子上
# 第三步：第二根柱子上的盘子移动到第三根柱子上

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a,c )


print(hanoi(3, 'A', 'B', 'C'))

# 注意参数的代换关系
# 0次调用      3 A B C
# Hanoi1      2 A C B
# Hanoi1      1 A B C
# Print1         A-> C
# 回退
# Hanoi1      1 A C B   ###记各参数为 a1=A   b1=C    c1=B
# Print2         A-> B
# Hanoi2      1 C C B   ###转换关系示例：a2=b1=C b2=a1=A c2=C1=B
# Print3       a2 --> c2  即 C --> B
#
quit(0)
