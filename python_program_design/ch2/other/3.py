import math
radius = float(input('请输入球的半径：'))
print('球的表面积为：{:.2f},球的体积为：{:.2f}'.format(4*math.pi*pow(radius,2),4/3*(math.pi*pow(radius,3))))