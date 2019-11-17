n = int(input())
a = input().split(' ')
b = input().split(' ')
for i in range(n):
    for j in range(n):
        print('%2d' % (int(a[i * n + j]) + int(b[i * n + j])), end=' ')
    print('')