# 输入本金，年利率和年数，计算复利

principal = float(input("请输入本金："))
Annual_interest_rate = float(input('请输入年利率：'))
years = int(input('请输入年数：'))
for i in range(5):
    principal = principal*(1+0.01*Annual_interest_rate)
print('本金利率和为：{:.2f}'.format(principal))