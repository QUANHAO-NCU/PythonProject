n = int(input())
result = 0
for i in range(1, n + 1):
    if '1' in list(str(i))or '2' in list(str(i)) or '0' in list(str(i)) or '9' in list(str(i)):
        result += i
print(result)
