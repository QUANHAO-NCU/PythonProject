# 练习 统计一个列表中相同的元素的个数，最终结果以字典的方式给出
# list = ['a', 'b', 'a', 'c', 'd', 'b', 'c', 'c']
# 结果应该表现为
# dit = {'a':2,'b':2,'c':3,'d':1}
list = ['a', 'b', 'a', 'c', 'd', 'b', 'c', 'c']
dit = {}
for i in list:
    dit[i] = list.count(i)
print(dit)

# 其他知识点
# ---------------字典---------------#
# 字典数据存储方式是键值对，键：值
dit1 = {'python': 1, 'java': 2, 'php': 3}
# 字典通过     "键"      进行数据操作
# 取数据
print(dit1['python'])
# 改值
dit1['java'] = 3
dit1['php'] = 2
print(dit1)

#键：值     这个关联中每一个键必须对应唯一的值
dit1['python']=2
print(dit1)
dit1['python']=1
print(dit1)
#观察发现python这个键指挥对应一个值

#一个键如何对应“多个”值？
#让值是一个列表!
dit1['编程语言'] = ['c','c++','ruby','lua']
print(dit1)
#事实上这改变了字典的初衷，不建议使用
#（学过汇编的应该知道，字典的键实质上是一个索引表，即汇编中的地址表）
#判断键是否在字典中
#in方法
print('hello' in dit1)
#get 方法
print(dit1.get('world',-1))

#建议使用调试模式学习此笔记