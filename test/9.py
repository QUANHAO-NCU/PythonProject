import operator, functools


def fact_r(n):
    try:
        if type(n) != int:
            raise TypeError
        elif n < 0:
            raise AssertionError
    except TypeError:
        print('传入的参数格式错误')
    except AssertionError:
        print('传入的参数值域错误')
    else:
        if n == 1:
            return 1
        return n * fact(n - 1)


def fact(n):
    try:
        if type(n) != int:
            raise TypeError
        elif n < 0:
            raise AssertionError
    except TypeError:
        print('传入的参数格式错误')
    except AssertionError:
        print('传入的参数值域错误')
    else:
        return functools.reduce(operator.mul, range(1, n + 1))


fact(-2)
fact_r('a')
print(fact(10))
