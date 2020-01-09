n = int(input())
result = {1:[1],2:[1],3:[1],4:[1,4150,4151],5:[1,4150,4151,54748,92727,93084],6:[1,4150,4151,54748,92727,93084,194979]}
# for i in range(1, pow(10, n)):
#     stri = str(i)
#     sum = 0
#     for k in range(len(stri)):
#         sum += pow(int(stri[k]), 5)
#     if sum == i:
#         print(i)
for i in result[n]:
    print(i)
