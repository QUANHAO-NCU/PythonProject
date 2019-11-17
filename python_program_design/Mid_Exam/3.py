Iuput_num = int(input())
all_dic = []
for i in range(0, Iuput_num):
    all_dic.append(eval(input()))
Node_num = Iuput_num
Side_num = 0
sum_length = 0
for dic in all_dic:
    for v in dic:
        dic1 = dic[v]
        for k in dic1:
            Side_num +=1
            sum_length += dic1[k]
print(Node_num,Side_num,sum_length)
quit(0)
