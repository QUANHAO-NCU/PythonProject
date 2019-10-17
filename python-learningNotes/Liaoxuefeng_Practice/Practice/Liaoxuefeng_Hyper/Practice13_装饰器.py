import functools
import time
from time import strftime, localtime


# 装饰器：在代码运行期间动态的增加功能

# 示例：装饰器log将打印在运行中的函数的名字


def log(func):
    def wrapper(*args, **kwargs):
        print("The function %s is executed :" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print(time.time())


now()
print("你可以自行修改log装饰器里面的参数，使在调用函数now时打印的提示信息动态变化")


# 使用了装饰器之后，每次调用now函数等于调用now = log(now)

# 示例2：

# 由于装饰器本身也是一个特殊的函数，所以可以设计一个可以接受参数的装饰器

# 示例2的装饰器的提示信息将由用户自行定义

def log2(tips):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s : %s" % (tips, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log2("这是装饰器2，现在执行的函数是")
def now2():
    print("2019-09-07,this is decorator 2!")


now2()

# 注意装饰器成功作用的关键是正确的逐步返回对应的函数

print("这时候出现了一个小问题，now2的name已经变成", now2.__name__)


# 使用python内建的函数functools.wraps()解决

def log3(tips):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s : %s" % (tips, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log3("这是装饰器3，现在运行的函数是")
def now3():
    print("2019-09-07,这是装饰器3！")


now3()


# 练习：设计一个decorator，使之能够作用于任意一个函数，并打印执行该函数所用的时间

def time_counter(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        re_func = func(*args,**kwargs)
        print("%s excuied in %s ms"%(func.__name__,time.time()-t1))
        return re_func
    return wrapper

@time_counter
def test():
    print("测试算式：")
    for i in range(1,20):
        n = pow(i,3)
        print(n)

test()
