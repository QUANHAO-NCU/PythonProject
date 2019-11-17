n = int(input())
assert n >= 1
Matrix1 = list(map(int, input().split()))
Matrix2 = list(map(int, input().split()))
Matrix3 = []
for i in range(0, len(Matrix1)):
    Matrix3.append(Matrix1[i] + Matrix2[i])
for i in range(0, len(Matrix3)):
    t = Matrix3[i]
    print('{: >2}'.format(t), end='')
    print(' ',end='')
    if ((i + 1) % n == 0 and (i + 1) // n != n):
        print('')
    else:
        continue
quit(0)
