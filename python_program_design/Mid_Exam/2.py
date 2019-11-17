q = 1
result = 0
def cal(get_list,q):
    global result
    for i in get_list:
        if (type(i)==list):
            q = q+1
            cal(i,q)
        if(type(i)==list):
            q = q-1
            continue
        result = q * i + result
    return result
test = eval(input())
cal(test,q)
print(result)