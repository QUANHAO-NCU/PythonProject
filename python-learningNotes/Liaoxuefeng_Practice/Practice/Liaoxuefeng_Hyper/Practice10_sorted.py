# sorted 是Python内建的一个高阶函数，可以对list和tunple进行排序
# sorted 也可以添加用户选定的key函数

# 例子：对列表中的名字按照字母顺序排序（默认排序会按照首字母的ASCII码进行排序）
list_name = ['bob', 'about', 'Zoo', 'Credit']

def key_default(s):
    return s[0]
print("默认排序情况下是",sorted(list_name,key=key_default))

print("按首字母顺序排序是：",sorted(list_name,key=str.upper))

# 给出一组学生的名字和成绩数据，设计key函数，分别按照名字首字母和成绩进行排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sorted_byName(temple):
    name = temple[0]
    return str(name[0]).lower()

def sorted_byGrades(temple):
    return temple[1]


print("按照名字首字母顺序排序是：",sorted(L,key=sorted_byName))
print("按照成绩高低进行排序是：",sorted(L,key=sorted_byGrades))