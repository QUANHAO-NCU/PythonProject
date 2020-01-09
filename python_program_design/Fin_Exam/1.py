n = int(input())
s= []
s = input().split()
score = []
for i in s:
    score.append(int(i))
max = score[0]
index = 0
for i in range(len(score)):
    if max < score[i]:
        max = score[i]
        index = i
score.pop(index)
max = score[0]
index = 0
for i in range(len(score)):
    if max < score[i]:
        max = score[i]
        index = i
score.pop(index)
max = score[0]
index = 0
for i in range(len(score)):
    if max > score[i]:
        max = score[i]
        index = i
score.pop(index)
max = score[0]
index = 0
for i in range(len(score)):
    if max > score[i]:
        max = score[i]
        index = i
score.pop(index)
sum = 0
for i in score:
    sum += i
aver = sum / len(score)
print('aver=%.2f'%aver,end='')
