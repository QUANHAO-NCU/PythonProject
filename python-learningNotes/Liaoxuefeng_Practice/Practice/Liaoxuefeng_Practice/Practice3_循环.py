# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,' + name)

# 生成顺序数列
# 并求和
sum = 0
for i in range(101):
    sum = sum + i
    if i > 90:
        break
print(sum)
# range 生成一个顺序，range()括号里面的数是停止的数，默认生成的数列小于这个数，默认从0 开始，所以range（101）即为 0-100
# break 语句，当条件达成时终止循环
# range从指定开始位置，以指定步长生成顺序数列
sum2 = 0
for i in range(11, 202, 3):
    if i % 2 == 0:
        continue
    sum2 += i
print(sum2)

# range（start,stop,step）
# continue 语句：配合if，当条件达成时直接进入下一次的循环

# while 循环
n = 100
sum3 = 0
while n > 0:
    sum3 += n
print(sum3)

# 死循环，用Ctrl+C退出
n1 = 2
while n < 1:
    n += 1
