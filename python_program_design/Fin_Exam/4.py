poll = input().split(',')
poll = list(set(poll))
result = []
for i in range(6, 11):
    if str(i) not in poll:
        result.append(i)
for i in range(len(result)):
    print(result[i], end='')
    if (i != len(result) - 1):
        print(' ', end='')
