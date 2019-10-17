def GetValue(b, r, n):
    for i in range(n):
        b = b * (1 + 0.01 * r)
    return round(b,2)


if (GetValue(2000, 5.6, 5) == 2626.33): print('Right!')
principal = float(input('请输入本金：'))
rate = float(input('请输入年利率：'))
years = int(input('请输入年数：'))
print(GetValue(principal,rate,years))
