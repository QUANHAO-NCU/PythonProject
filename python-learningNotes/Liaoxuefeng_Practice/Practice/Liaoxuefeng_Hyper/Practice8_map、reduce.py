from functools import reduce

# map (Function,Iterable)
# map 的作用是将后面的Iterable数据序列的每个元素作为参数让Function作用，然后得到一个处理后的Iterator
# 得到的这个Iterator是一个迭代器类型,获取处理后的数据需要遵循迭代器的调用方法

list0 = [1, 2, 3, 4, 5]


def fc_plus(x):
    return x + 1


print('第一个map\n将列表中各个数据加一:\n' + str(list(map(fc_plus, list0))))


# Reduce(Function_R,Iterable)
# Reduce 的作用是将后面的Iterable数据序列的每个元素依次传入Function，并将结果相加，然后得到一个处理后的结果
# Reduce 只会得到一个结果，而Reduce需要的Function需要传入两个参数

def fc_sum(x, y):
    return x + y


print('第一个reduce\n得到列表中各个数据的和:\n' + str(reduce(fc_sum, list0)))

# 练习1： 利用map函数将列表中不规则的用户名变成规范的用户名（首字母大写，其他字母小写）
list_name = ['adam', 'LISA', 'barT']


def pra_format_name(name):
    return name[0].upper() + name[1:].lower()


print('第一个练习，map\n将列表中的用户名格式化:\n' + str(list(map(pra_format_name, list_name))))

# 练习2： 利用reduce函数设计一个函数使之能接受一个列表并求列表里面各元素的积
list_prod = [3, 5, 7, 9]


def pra_prod(x,y):
    return x*y


print('第二个练习，reduce\n求列表中各元素的积:\n' + str(reduce(pra_prod, list_prod)))


# 练习3： 利用map 和 reduce 写一个函数，将字符串‘123.456’转换成浮点数123.456
str_test = '123.456'



def str2float(_str):
    def char2num(char):
        ditc = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return ditc[char]
    def str2int(x,y):
        return x*10+y
    list = _str.split('.')
    int_part = reduce(str2int,map(char2num,list[0]))
    float_part = reduce(str2int,map(char2num,list[1]))*pow(0.1,len(list[1]))
    return int_part+float_part



print('第三个练习，map和reduce\n将传入的字符串转换成对应的浮点数:\n%.3f' % str2float(str_test)+' type is '+str(type(str2float(str_test))))

# 练习三参考了回答中的方法