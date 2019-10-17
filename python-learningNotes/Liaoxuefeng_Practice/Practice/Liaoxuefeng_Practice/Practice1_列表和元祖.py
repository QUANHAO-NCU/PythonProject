# #练习1：
# 请用索引取出下面list的指定元素：
#
# # -*- coding: utf-8 -*-
#
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印apple
print(L[0][0])
#打印python
print(L[1][1])
#打印Lisa
print(L[2][2])

#“可变”元祖

t = (1,2,[3,4])
print(t)
t[2][1] = 6
t[2][0] = 9
#这个元祖应该改为t = (1,2,[9,6])
print(t)

#只有一个元素的元祖
t2 = (1,)
#必须要使用一个,号来定义只有一个元素的数组

#----------------------------------列表的方法----------------------------------
# 以列表L为例

#1获取列表的某个元素

print(L[0][1])#应该是Google

# 2 .append 方法：在列表尾追加元素
    # list.append(要增加的元素)
L.append('javascript')#L中最后应该多了一个javascript的字符串
print(L)
# 3 .insert 方法：在指定位置插入指定元素
    # list.insert(位置，要插入的元素)
L.insert(1,'Oracle')#则列表L中的第二个元素应该是‘Oracle’
print(L)
# 4 .pop 方法：弹出/删除指定位置的元素
    # list.pop(位置)
L.pop(1)#刚刚添加的字符‘Oracle‘会被删除
print(L)
